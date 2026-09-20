"""
Q16: Calculate and print the minimum and maximum intensity values of a grayscale image.

APPROACH:
cv2.minMaxLoc() (or simply NumPy's .min()/.max()) scans the array and returns the darkest and brightest pixel values.
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
    gray = cv2.imread(IMG_PATH, cv2.IMREAD_GRAYSCALE)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
    print(f"Minimum intensity: {min_val} at {min_loc}")
    print(f"Maximum intensity: {max_val} at {max_loc}")


if __name__ == "__main__":
    main()
