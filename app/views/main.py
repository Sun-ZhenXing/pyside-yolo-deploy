import cv2
import numpy as np
from PySide6.QtCore import QTimer, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QWidget

from app.utils.predict import predict
from app.widgets.main_ui import Ui_MainWindow


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
        # 使用 OpenCV 初始化摄像头
        self._video = cv2.VideoCapture(0)

        # 初始化定时器
        self._timer = QTimer()
        self._timer.timeout.connect(self.update_frame)
        # self._timer.start(30)

        self._conf = 0.25
        self._ui.confSlider.setValue(int(self._conf * 100))
        self._ui.confSlider.valueChanged.connect(
            lambda value: self.setConf(value / 100)
        )

    def setConf(self, conf: float) -> None:
        """设置置信度"""
        self._conf = conf
        self._ui.confLabel.setText(f"置信度：{conf:.2f}")

    def update_frame(self):
        """更新帧"""
        ret, frame = self._video.read()
        frame, *_ = predict(frame, conf=self._conf)
        if ret:
            self.display_frame(frame)

    def display_frame(self, frame: np.ndarray):
        """渲染帧"""
        image = QImage(
            frame.data,
            frame.shape[1],
            frame.shape[0],
            frame.strides[0],
            QImage.Format.Format_BGR888,
        )
        self._ui.image_label.setPixmap(QPixmap.fromImage(image))

    def clear_frame(self):
        """清空帧"""
        self._ui.image_label.clear()

    def __del__(self):
        """释放摄像头"""
        self._video.release()

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
            self._video.release()
            self._video = cv2.VideoCapture(file_name)
            self._timer.start(30)

    @Slot()
    def closeVideo(self) -> None:
        """关闭视频"""
        self._timer.stop()
        self._video.release()
        self.clear_frame()
        self._video = cv2.VideoCapture(0)

    @Slot()
    def openCamera(self) -> None:
        """打开摄像头"""
        self._video.release()
        self._video = cv2.VideoCapture(0)
        self._timer.start(30)

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
            "YOLOv11 目标检测",
        )
