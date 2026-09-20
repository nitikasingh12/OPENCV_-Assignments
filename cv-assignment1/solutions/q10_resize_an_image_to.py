"""
Q10: Resize an image to 50% of its original width and height.

APPROACH:
cv2.resize(img, (new_w, new_h)) resamples the image; we compute new dimensions as half the original width/height (integer division).
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
    h, w = img.shape[:2]
    resized = cv2.resize(img, (w // 2, h // 2))
    cv2.imwrite(os.path.join(OUT_DIR, "q10_resized_50pct.jpg"), resized)
    print(f"Original size: {w}x{h}  ->  Resized size: {w//2}x{h//2}")


if __name__ == "__main__":
    main()
