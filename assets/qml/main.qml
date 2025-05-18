import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

Window {
    visible: true
    width: 800
    height: 600
    title: "OpenCV 摄像头查看器"

    Image {
        id: cameraImage
        anchors.fill: parent
        cache: false
        source: "image://camera/frame"
        fillMode: Image.PreserveAspectFit

        // 图像更新时的连接
        Connections {
            target: cameraController
            function onFrameReady() {
                // 通过更改source来强制刷新图像
                cameraImage.source = ""
                cameraImage.source = "image://camera/frame?" + Date.now()
            }
        }
    }
}
