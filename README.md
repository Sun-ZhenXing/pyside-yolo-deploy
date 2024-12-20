# YOLO & PySide

使用 PySide6 构建 UI，部署 ONNX YOLOv11 模型，可轻量化打包，使用 ONNXRuntime 推理。

## 特征

本项目为 YOLOv11 参考项目，提供了 训练、推理、导出和 ONNX 模型的部署示例。

更多：

- [x] [YOLOv8 OBB：训练旋转框检测](./notebook/obb.ipynb)
- [x] 提供 ONNX 推理示例
- [ ] 提供 OBB 的 ONNX 推理示例
- [x] 支持更多平台，包括 Mac OS 和 Ubuntu
- [ ] 文档：训练、推理、模型导出
- [x] 文档：打包部署

参考了 [X-AnyLabeling: `export_yolov10_onnx.py`](https://github.com/CVHub520/X-AnyLabeling/blob/main/tools/export_yolov10_onnx.py) 的实现。

## 开始

推荐环境：Python 3.11，使用 UV 来管理虚拟环境。

```bash
uv sync
```

下面的操作请在虚拟环境下工作，安装依赖：

```bash
just i
```

运行：

```bash
just dev
```

格式化：

```bash
just lint
```

测试 Git 钩子：

```bash
just test
```

## 导出模型

导出 ONNX 模型：

```bash
yolo export model=/root/runs/detect/train/weights/best.pt format=onnx simplify=True imgsz=1280 opset=12
```

## 构建可执行程序

使用 Nuitka 编译 Python 代码，Windows 打包：

```bash
set UPX_PATH=...
just build
```

测试打包：

```bash
just build-test
```

## 协议

[AGPLv3](./LICENSE).
