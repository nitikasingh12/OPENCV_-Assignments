"""
Q14: Split a color image into its B, G, and R channels and display each channel.

APPROACH:
cv2.split() separates a multi-channel image into a list of single-channel images. Each channel, viewed alone, appears as a grayscale image showing that color's intensity.
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

    show(b, "Q14 - Blue Channel")
    show(g, "Q14 - Green Channel")
    show(r, "Q14 - Red Channel")

    cv2.imwrite(os.path.join(OUT_DIR, "q14_blue.jpg"), b)
    cv2.imwrite(os.path.join(OUT_DIR, "q14_green.jpg"), g)
    cv2.imwrite(os.path.join(OUT_DIR, "q14_red.jpg"), r)
    print("Saved individual channel images to outputs/")


if __name__ == "__main__":
    main()
