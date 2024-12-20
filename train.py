import sys

from ultralytics import YOLO


def main():
    if len(sys.argv) < 2:
        print("Usage: python train.py <data_path>")
        sys.exit(1)

    model = YOLO("yolov11m.pt")
    data_path = sys.argv[1]
    results = model.train(
        data=data_path,
        epochs=100,
        imgsz=1280,
        batch=-1,
        verbose=True,
        plots=True,
    )
    print(results)


if __name__ == "__main__":
    main()
