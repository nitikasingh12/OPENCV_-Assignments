"""
Q21: Convert an 8-bit grayscale image into a 4-bit quantized image and display the result.

APPROACH:
4-bit quantization reduces 256 levels to 16. We divide by 16 (256/16), floor to an integer level, then multiply back by 16 to restore a displayable 0-255 range with only 16 distinct values.
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
    levels = 16  # 4-bit = 2^4 = 16 levels
    step = 256 // levels
    quantized = (gray // step) * step
    quantized = quantized.astype(np.uint8)

    cv2.imwrite(os.path.join(OUT_DIR, "q21_quantized_4bit.jpg"), quantized)
    show(quantized, "Q21 - 4-bit Quantized")
    print("Unique intensity levels after quantization:", len(np.unique(quantized)))


if __name__ == "__main__":
    main()
