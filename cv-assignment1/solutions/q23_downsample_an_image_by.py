"""
Q23: Downsample an image by a factor of 2 in both width and height and print the original and new resolutions.

APPROACH:
Downsampling means reducing the sampling rate (fewer pixels), achieved here with cv2.resize() using INTER_AREA interpolation, which is the recommended method for shrinking images.
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
    downsampled = cv2.resize(img, (w // 2, h // 2), interpolation=cv2.INTER_AREA)

    print(f"Original resolution: {w}x{h}")
    print(f"Downsampled resolution: {w//2}x{h//2}")
    cv2.imwrite(os.path.join(OUT_DIR, "q23_downsampled.jpg"), downsampled)


if __name__ == "__main__":
    main()
