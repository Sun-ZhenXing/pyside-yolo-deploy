import sys

import cv2
from PySide6.QtCore import QObject, QSize, QTimer, QUrl, Signal, Slot
from PySide6.QtGui import QGuiApplication, QImage
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import QQuickImageProvider


class OpenCVImageProvider(QQuickImageProvider):
    def __init__(self):
        super().__init__(QQuickImageProvider.ImageType.Image)
        self.img = QImage(1, 1, QImage.Format.Format_RGB888)

    def requestImage(self, id: str, size: QSize, requestedSize: QSize) -> QImage:
        return self.img.copy()

    def updateImage(self, img):
        self.img = img


class CameraController(QObject):
    frameReady = Signal()

    def __init__(self, image_provider: OpenCVImageProvider):
        super().__init__()
        self.image_provider = image_provider
        self.camera = cv2.VideoCapture(0)  # 打开默认摄像头

        # 检查摄像头是否成功打开
        if not self.camera.isOpened():
            print("错误：无法打开摄像头")
            return

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(33)  # ~30fps

    @Slot()
    def updateFrame(self):
        ret, frame = self.camera.read()
        if ret:
            # 转换OpenCV的BGR格式到QImage的RGB格式
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            img = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            self.image_provider.updateImage(img)
            self.frameReady.emit()

    def __del__(self):
        if hasattr(self, "camera"):
            self.camera.release()


def main():
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    # 注册图像提供者
    image_provider = OpenCVImageProvider()
    engine.addImageProvider("camera", image_provider)

    # 创建并注册摄像头控制器
    camera_controller = CameraController(image_provider)
    engine.rootContext().setContextProperty("cameraController", camera_controller)

    # 加载QML
    qml_file = "assets/qml/main.qml"
    engine.load(QUrl.fromLocalFile(qml_file))

    if not engine.rootObjects():
        print("错误：无法加载QML文件")
        return -1

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
