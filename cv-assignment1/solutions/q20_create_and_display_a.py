"""
Q20: Create and display a grayscale intensity ramp whose intensity gradually changes from 0 to 255.

APPROACH:
np.linspace(0, 255, width) generates a smooth 1D gradient; tiling it across rows with np.tile() turns it into a 2D ramp image.
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
    width, height = 256, 100
    ramp_row = np.linspace(0, 255, width, dtype=np.uint8)
    ramp = np.tile(ramp_row, (height, 1))

    cv2.imwrite(os.path.join(OUT_DIR, "q20_intensity_ramp.jpg"), ramp)
    show(ramp, "Q20 - Intensity Ramp (0-255)")
    print("Ramp shape:", ramp.shape, "| min:", ramp.min(), "max:", ramp.max())


if __name__ == "__main__":
    main()
