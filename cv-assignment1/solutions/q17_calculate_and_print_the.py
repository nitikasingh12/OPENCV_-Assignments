"""
Q17: Calculate and print the mean intensity of a grayscale image.

APPROACH:
cv2.mean() (or np.mean()) averages all pixel values, giving a single number that summarizes overall image brightness.
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
    gray = cv2.imread(IMG_PATH, cv2.IMREAD_GRAYSCALE)
    mean_cv = cv2.mean(gray)[0]     # cv2.mean returns a 4-tuple
    mean_np = np.mean(gray)
    print(f"Mean intensity (cv2.mean): {mean_cv:.2f}")
    print(f"Mean intensity (np.mean):  {mean_np:.2f}")


if __name__ == "__main__":
    main()
