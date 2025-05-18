import sys

import cv2
import numpy as np
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QCloseEvent, QImage, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class VideoThread(QThread):
    update_frame = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.camera_id = 0
        self.running = False

    def run(self):
        self.running = True
        cap = cv2.VideoCapture(self.camera_id)

        if not cap.isOpened():
            print("无法打开摄像头")
            return

        while self.running:
            ret, frame = cap.read()
            if ret:
                self.update_frame.emit(frame)

        cap.release()

    def stop(self):
        self.running = False
        self.wait()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("摄像头视频显示")
        self.resize(800, 600)

        # 创建中央部件和布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # 创建用于显示视频的标签
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        self.setCentralWidget(central_widget)

        # 创建并启动视频线程
        self.video_thread = VideoThread()
        self.video_thread.update_frame.connect(self.update_frame)
        self.video_thread.start()

    def update_frame(self, frame: np.ndarray):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        qt_image = QImage(rgb_frame.data, w, h, ch * w, QImage.Format.Format_RGB888)

        pixmap = QPixmap.fromImage(qt_image)
        self.image_label.setPixmap(
            pixmap.scaled(
                self.image_label.width(),
                self.image_label.height(),
                Qt.AspectRatioMode.KeepAspectRatio,
            )
        )

    def closeEvent(self, event: QCloseEvent) -> None:
        self.video_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
