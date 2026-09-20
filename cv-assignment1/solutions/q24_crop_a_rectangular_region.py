"""
Q24: Crop a rectangular Region of Interest (ROI) from an image using user-provided coordinates.

APPROACH:
Because images are NumPy arrays, cropping is simple slicing: img[y1:y2, x1:x2] extracts the rectangular region between those bounds.
"""

import os
import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(BASE_DIR, "..", "images", "sample.jpg")
OUT_DIR = os.path.join(BASE_DIR, "..", "outputs")
os.makedirs(OUT_DIR, exist_ok=True)


def _has_display():
    """Detect whether a GUI display is available (Linux/macOS/Windows)."""
    if os.name == "nt":
        return True
    return bool(os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"))


def show(img, window_name="Output"):
    """Show in a GUI window when a display is available; otherwise skip
    safely. The result is always saved to outputs/ regardless, so nothing
    is lost when running headless (e.g. on a server or in CI)."""
    if not _has_display():
        print(f"[{window_name}] No display detected — skipping cv2.imshow "
              f"(image is still saved to the outputs/ folder).")
        return
    try:
        cv2.imshow(window_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except cv2.error:
        pass


def main():
    img = cv2.imread(IMG_PATH)
    x1, y1, x2, y2 = 50, 50, 250, 200  # replace with input() for interactive use
    roi = img[y1:y2, x1:x2]

    cv2.imwrite(os.path.join(OUT_DIR, "q24_cropped_roi.jpg"), roi)
    show(roi, "Q24 - Cropped ROI")
    print(f"Cropped region shape: {roi.shape} (from ({x1},{y1}) to ({x2},{y2}))")


if __name__ == "__main__":
    main()
