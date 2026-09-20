"""
Q19: Create a 256x256 grayscale image in which every pixel has intensity value 128.

APPROACH:
np.full((h, w), value, dtype=np.uint8) allocates an array pre-filled with a constant value — a quick way to build solid-color test images.
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


import numpy as np


def main():
    flat_gray = np.full((256, 256), 128, dtype=np.uint8)
    cv2.imwrite(os.path.join(OUT_DIR, "q19_flat_gray_128.jpg"), flat_gray)
    show(flat_gray, "Q19 - Uniform Gray (128)")
    print("Unique pixel values in image:", np.unique(flat_gray))


if __name__ == "__main__":
    main()
