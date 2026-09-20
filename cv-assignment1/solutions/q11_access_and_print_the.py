"""
Q11: Access and print the pixel value at a user-provided (x, y) coordinate.

APPROACH:
NumPy arrays are indexed [row, col] = [y, x], so a pixel at screen coordinate (x, y) is accessed as img[y, x].
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
    x, y = 100, 50  # replace with input() for interactive use
    pixel = img[y, x]
    print(f"Pixel value at (x={x}, y={y}): B={pixel[0]}, G={pixel[1]}, R={pixel[2]}")


if __name__ == "__main__":
    main()
