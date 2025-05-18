import numpy as np
from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import Results

model = YOLO("models/yolo12n.pt")


def predict(img: np.ndarray, conf: float = 0.25) -> tuple[np.ndarray]:
    results: list[Results] = model.predict(img, conf=conf)
    result = results[0]
    img = result.plot()
    return (result.plot(),)
