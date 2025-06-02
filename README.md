# YOLO & PySide

使用 PySide6 构建 UI，部署 ONNX YOLO12 模型，可轻量化打包，使用 ONNXRuntime 推理。

## 特征

本项目为 YOLO12 参考项目，提供了 训练、推理、导出和 ONNX 模型的部署示例。

更多：

- [ ] 提供 ONNX 推理示例，包括分类、目标检测、分割、旋转框检测
- [ ] 文档：训练、推理、模型导出

更新：目前已经支持视频推理追帧，后续将继续移除 ONNXRuntime 依赖，转移到 NCNN、TensorRT 等专用平台上。

## 开始

推荐环境：Python 3.12，使用 UV 来管理虚拟环境。

如果没有安装 UV，请先安装：

```bash
pip install uv
```

安装依赖：

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
yolo export model=best.pt format=onnx simplify=True imgsz=640 opset=12
```

## 构建可执行程序

使用 Nuitka 编译 Python 代码：

```bash
just build
```

测试打包：

```bash
just build-test
```

## 协议

[AGPLv3](./LICENSE).
