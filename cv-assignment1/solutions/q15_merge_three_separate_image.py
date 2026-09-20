"""
Q15: Merge three separate image channels into a single color image.

APPROACH:
cv2.merge([b, g, r]) is the inverse of cv2.split(): it stacks three single-channel arrays back into one 3-channel BGR image.
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
    b, g, r = cv2.split(img)
    merged = cv2.merge([b, g, r])

    are_equal = (merged == img).all()
    print("Merged image identical to original:", are_equal)
    cv2.imwrite(os.path.join(OUT_DIR, "q15_merged.jpg"), merged)


if __name__ == "__main__":
    main()
