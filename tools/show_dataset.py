import os

import cv2
import numpy as np


def show_dataset(image_path: str, label_path: str):
    for file in os.listdir(image_path):
        ext = os.path.splitext(file)[1]
        if ext not in [".jpg", ".jpeg", ".png"]:
            continue
        img: np.ndarray = cv2.imread(os.path.join(image_path, file))  # type: ignore
        img = (
            cv2.resize(
                img,
                (640, int(640 / img.shape[1] * img.shape[0])),
            )
            if img.shape[1] > 640
            else img
        )
        with open(os.path.join(label_path, file.replace(".jpg", ".txt"))) as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                label = parts.pop(0)
                x, y, w, h = map(float, parts)
                x = int((x - w / 2) * img.shape[1])
                y = int((y - h / 2) * img.shape[0])
                w = int(w * img.shape[1])
                h = int(h * img.shape[0])
                cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (0, 0, 255),
                    1,
                )
                cv2.putText(
                    img,
                    label,
                    (x, y + 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    1,
                    cv2.LINE_AA,
                )
        cv2.imshow("image", img)
        key = cv2.waitKey(0)
        if key == 0x1B:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    show_dataset(
        input("Enter image path: "),
        input("Enter label path: "),
    )
