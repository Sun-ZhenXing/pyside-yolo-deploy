import time

import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtGui import QCloseEvent, QImage, QPixmap
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QWidget

from app.utils.predict import predict
from app.widgets.main_ui import Ui_MainWindow


class VideoProcessor:
    """视频处理类，用于管理视频播放速度和帧率"""

    def __init__(self):
        self.cap = None
        self.frame_rate = 30  # 默认帧率
        self.start_time = 0
        self.frame_count = 0
        self.is_video_file = False

    def open(self, source):
        """打开视频源"""
        self.cap = cv2.VideoCapture(source)
        self.is_video_file = isinstance(source, str)

        if self.is_video_file and self.cap.isOpened():
            self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS)
            if self.frame_rate <= 0:
                self.frame_rate = 30  # 如果获取帧率失败，使用默认值

        self.start_time = time.time()
        self.frame_count = 0
        return self.cap.isOpened()

    def read(self):
        """读取帧，并根据需要跳过帧以保持播放速度"""
        if not self.cap or not self.cap.isOpened():
            return False, None

        if not self.is_video_file:
            # 摄像头模式，不需要跳帧
            return self.cap.read()

        # 计算应该处理的帧
        self.frame_count += 1
        elapsed_time = time.time() - self.start_time
        expected_frame = int(elapsed_time * self.frame_rate)

        # 如果当前处理的帧落后于预期帧，需要跳过中间帧
        if self.frame_count < expected_frame:
            frames_to_skip = expected_frame - self.frame_count
            for _ in range(frames_to_skip):
                self.cap.grab()  # 只获取帧但不解码，以节省时间
                self.frame_count += 1

        return self.cap.read()

    def release(self):
        """释放资源"""
        if self.cap:
            self.cap.release()
            self.cap = None


class VideoThread(QThread):
    update_frame = Signal(np.ndarray)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.source = 0  # 默认摄像头
        self.running = False
        self.conf = 0.25
        self.processor = VideoProcessor()

    def set_source(self, source):
        """设置视频源，可以是摄像头索引或视频文件路径"""
        self.source = source

    def set_conf(self, conf):
        """设置置信度阈值"""
        self.conf = conf

    def run(self):
        self.running = True
        if not self.processor.open(self.source):
            print(f"无法打开视频源: {self.source}")
            return

        while self.running:
            ret, frame = self.processor.read()
            if ret and frame is not None:
                # 在线程中进行推理
                processed_frame, *_ = predict(frame, conf=self.conf)
                self.update_frame.emit(processed_frame)
            else:
                # 视频文件结束
                if self.processor.is_video_file:
                    break

        self.processor.release()

    def stop(self):
        self.running = False
        self.wait()
        self.processor.release()


class MainWindow(QMainWindow):
    def __init__(
        self,
        parent: QWidget | None = None,
        views_map: dict[str, QWidget] | None = None,
    ) -> None:
        super().__init__(parent)
        self._views_map = views_map if views_map is not None else {}

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # 初始化视频线程
        self._video_thread = VideoThread(self)
        self._video_thread.update_frame.connect(self.display_frame)

        self._conf = 0.25
        self._ui.confSlider.setValue(int(self._conf * 100))
        self._ui.confSlider.valueChanged.connect(
            lambda value: self.setConf(value / 100)
        )

    def setConf(self, conf: float) -> None:
        """设置置信度"""
        self._conf = conf
        self._ui.confLabel.setText(f"置信度：{conf:.2f}")
        self._video_thread.set_conf(conf)

    def display_frame(self, frame: np.ndarray):
        """渲染帧"""
        h, w, _ = frame.shape
        if h > 1280 or w > 720:
            ratio = min(1280 / h, 720 / w)
            frame = cv2.resize(frame, (int(w * ratio), int(h * ratio)))
        image = QImage(
            frame.data,
            frame.shape[1],
            frame.shape[0],
            frame.strides[0],
            QImage.Format.Format_BGR888,
        )
        self._ui.imageLabel.setPixmap(QPixmap.fromImage(image))

    def clear_frame(self):
        """清空帧"""
        self._ui.imageLabel.clear()

    def closeEvent(self, event: QCloseEvent) -> None:
        """关闭事件，停止线程"""
        self._video_thread.stop()
        event.accept()
        super().closeEvent(event)

    def __del__(self):
        """析构函数"""
        self._video_thread.stop()

    @Slot()
    def openPicture(self) -> None:
        """打开图片"""
        self.closeVideo()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "打开图片", ".", "图片文件 (*.jpg *.png)"
        )
        if file_name:
            frame = cv2.imread(file_name)
            frame, *_ = predict(frame, conf=self._conf)
            height, width, _ = frame.shape
            if height > 1280 or width > 720:
                ratio = min(1280 / height, 720 / width)
                frame = cv2.resize(frame, (int(width * ratio), int(height * ratio)))
            self.display_frame(frame)

    @Slot()
    def openVideo(self) -> None:
        """打开视频"""
        self.closeVideo()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "打开视频", ".", "视频文件 (*.mp4 *.avi)"
        )
        if file_name:
            self._video_thread.stop()
            self._video_thread.set_source(file_name)
            self._video_thread.start()

    @Slot()
    def closeVideo(self) -> None:
        """关闭视频"""
        self._video_thread.stop()
        self.clear_frame()

    @Slot()
    def openCamera(self) -> None:
        """打开摄像头"""
        self._video_thread.stop()
        self._video_thread.set_source(0)  # 使用默认摄像头
        self._video_thread.start()

    @Slot()
    def aboutQt(self) -> None:
        """显示关于 Qt"""
        QMessageBox.aboutQt(self)

    @Slot()
    def actionSettingClicked(self) -> None:
        """设置"""
        QMessageBox.information(
            self,
            "设置",
            "正在开发中……",
            QMessageBox.StandardButton.Ok,
        )

    @Slot()
    def about(self) -> None:
        """显示关于"""
        QMessageBox.about(
            self,
            "关于",
            "YOLO12 目标检测",
        )
