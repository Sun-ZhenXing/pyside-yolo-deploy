import sys

from ultralytics import RTDETR


def main():
    if len(sys.argv) < 2:
        print("Usage: python train.py <data_path>")
        sys.exit(1)

    model = RTDETR("rtdetr-l.pt")
    data_path = sys.argv[1]
    results = model.train(
        data=data_path,
        epochs=300,
        imgsz=640,
        batch=-1,
        verbose=True,
        plots=True,
    )
    print(results)


if __name__ == "__main__":
    main()
