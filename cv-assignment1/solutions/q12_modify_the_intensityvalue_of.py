"""
Q12: Modify the intensity/value of a selected pixel and save the modified image.

APPROACH:
Assigning a new array (or scalar for grayscale) to img[y, x] overwrites that pixel in place; we then persist the change with cv2.imwrite().
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
    x, y = 100, 50
    print("Before:", img[y, x])
    img[y, x] = [0, 0, 255]  # set to pure red (BGR)
    print("After:", img[y, x])
    cv2.imwrite(os.path.join(OUT_DIR, "q12_modified_pixel.jpg"), img)


if __name__ == "__main__":
    main()
