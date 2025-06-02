import sys

from ultralytics import YOLO


def main():
    if len(sys.argv) < 2:
        print("Usage: python train.py <data_path>")
        sys.exit(1)

    model = YOLO("yolo12m.pt")
    data_path = sys.argv[1]
    results = model.train(
        data=data_path,
        epochs=100,
        imgsz=640,
        verbose=True,
        plots=True,
        # multi gpus
        # device="0,1,2,3",
    )
    print(results)


if __name__ == "__main__":
    main()
