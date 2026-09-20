# Computer Vision â€“ Day 1: 25 Python + OpenCV Coding Questions

Solutions to 25 fundamental Computer Vision practice questions covering
image handling, pixel operations, image representation, sampling,
quantization, and basic geometric operations â€” using Python, OpenCV, and NumPy.

## ðŸ“ Project Structure

```
cv-day1-25-questions/
â”œâ”€â”€ README.md
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ images/
â”‚   â””â”€â”€ sample.jpg          # test image used by every script
â”œâ”€â”€ outputs/                 # generated results land here (gitignored)
â””â”€â”€ solutions/
    â”œâ”€â”€ q01_read_an_image_using.py
    â”œâ”€â”€ q02_check_whether_an_image.py
    â”œâ”€â”€ ...
    â””â”€â”€ q25_rotate_an_image_by.py
```

## ðŸš€ Setup

```bash
git clone <your-repo-url>
cd cv-day1-25-questions
python3 -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## â–¶ï¸ Running a Solution

Each question is a standalone, runnable script. From the project root:

```bash
python3 solutions/q01_read_an_image_using.py
```

Every script:
- Reads `images/sample.jpg` (a synthetic test image included in the repo, so
  everything runs out of the box with no extra downloads).
- Prints its results / observations to the console.
- Saves its output image (where relevant) to `outputs/`.
- Opens a GUI preview window automatically if a display is available (falls
  back gracefully and just saves the file if run headless / on a server).

To use your own image instead, replace `images/sample.jpg` or edit the
`IMG_PATH` variable at the top of any script.

## ðŸ“š Solutions Index

### Q1. Read an image using OpenCV and display it.

**File:** [`solutions/q01_read_an_image_using.py`](solutions/q01_read_an_image_using.py)

**Approach:** cv2.imread() loads the image from disk into a NumPy array (BGR order).
cv2.imshow() opens a window to display it; waitKey(0) pauses until a key
is pressed, and destroyAllWindows() closes the window afterwards.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.imread() reads pixel data as a NumPy array. cv2.imshow()/waitKey()/destroyAllWindows() form the standard display-and-close cycle.

**Observation:** The sample image opens correctly, confirming the file path and OpenCV installation are working.

### Q2. Check whether an image was loaded successfully; print an error if not.

**File:** [`solutions/q02_check_whether_an_image.py`](solutions/q02_check_whether_an_image.py)

**Approach:** cv2.imread() returns None (instead of raising an exception) when the
file path is wrong or the file is unreadable, so we explicitly check for
that with an `is None` test.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.imread() silently returns None on failure rather than throwing an error, so checking `if img is None` is the standard way to validate a load.

**Observation:** The real sample image loads successfully; the deliberately wrong path prints a clean error message instead of crashing.

### Q3. Print the image height, width, and number of channels.

**File:** [`solutions/q03_print_the_image_height.py`](solutions/q03_print_the_image_height.py)

**Approach:** A loaded color image is a NumPy array with shape (height, width, channels). We read these directly from img.shape.

**Key functions used:** see inline comments in the script.

**Explanation:** img.shape returns a tuple (rows, cols, channels) for color images â€” rows = height, cols = width.

**Observation:** For the sample image this prints Height: 400, Width: 600, Channels: 3 (BGR).

### Q4. Calculate and print the total number of pixels in an image.

**File:** [`solutions/q04_calculate_and_print_the.py`](solutions/q04_calculate_and_print_the.py)

**Approach:** Total pixels = height x width (channels are not counted as separate pixels). img.size gives height*width*channels, so we either multiply shape[0]*shape[1] or divide img.size by the channel count.

**Key functions used:** see inline comments in the script.

**Explanation:** height * width gives the true pixel count; img.size (NumPy's total element count) additionally multiplies by the number of channels.

**Observation:** For a 400x600 image, total pixels = 240000, while img.size = 720000 (x3 for BGR).

### Q5. Print the data type (dtype) of the image matrix.

**File:** [`solutions/q05_print_the_data_type.py`](solutions/q05_print_the_data_type.py)

**Approach:** OpenCV stores images as NumPy arrays; every array has a `.dtype` attribute describing the type of each element (typically uint8 for standard images).

**Key functions used:** see inline comments in the script.

**Explanation:** img.dtype reveals the numeric type used per pixel channel â€” uint8 means values range 0-255.

**Observation:** The sample image prints dtype: uint8, the standard format for 8-bit images.

### Q6. Read an image and save it with a different filename using OpenCV.

**File:** [`solutions/q06_read_an_image_and.py`](solutions/q06_read_an_image_and.py)

**Approach:** cv2.imwrite(path, img) writes the in-memory array back to disk under a new filename; the format is inferred from the file extension.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.imwrite() infers the output format (JPEG, PNG, etc.) from the extension you give it, so .jpg -> .png is a one-line conversion.

**Observation:** A new file q06_copy.png appears in outputs/, identical in content to the original but in PNG format.

### Q7. Read an image directly in grayscale mode and display it.

**File:** [`solutions/q07_read_an_image_directly.py`](solutions/q07_read_an_image_directly.py)

**Approach:** cv2.imread() accepts a second flag: cv2.IMREAD_GRAYSCALE (0) loads and converts the image to single-channel grayscale during reading, which is more efficient than reading color then converting.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.IMREAD_GRAYSCALE tells OpenCV's decoder to output a single-channel image directly, so gray.shape has only (height, width), no channel dimension.

**Observation:** The output image is visually gray/black-white; its shape is (400, 600) instead of (400, 600, 3).

### Q8. Convert a color image to grayscale using cv2.cvtColor().

**File:** [`solutions/q08_convert_a_color_image.py`](solutions/q08_convert_a_color_image.py)

**Approach:** cv2.cvtColor(src, code) transforms color spaces. cv2.COLOR_BGR2GRAY applies a weighted sum (0.299R + 0.587G + 0.114B) to collapse 3 channels into 1.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) is the general-purpose color-space converter; COLOR_BGR2GRAY specifically applies luminance weighting to merge B, G, R into one channel.

**Observation:** Result matches Q7's output in appearance but was produced by converting an already-loaded color image rather than reading directly as grayscale.

### Q9. Display an image using Matplotlib and hide the axis.

**File:** [`solutions/q09_display_an_image_using.py`](solutions/q09_display_an_image_using.py)

**Approach:** Matplotlib expects RGB order while OpenCV uses BGR, so we convert with cv2.cvtColor(..., COLOR_BGR2RGB) before plt.imshow(). plt.axis('off') hides the tick marks and axis lines.

**Key functions used:** see inline comments in the script.

**Explanation:** BGR->RGB conversion is required because Matplotlib assumes RGB channel order; plt.axis('off') removes the surrounding axes/ticks for a clean image view.

**Observation:** The saved figure shows the sample image with correct colors and no axis border, confirming the BGR->RGB fix worked.

### Q10. Resize an image to 50% of its original width and height.

**File:** [`solutions/q10_resize_an_image_to.py`](solutions/q10_resize_an_image_to.py)

**Approach:** cv2.resize(img, (new_w, new_h)) resamples the image; we compute new dimensions as half the original width/height (integer division).

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.resize() takes the target size as (width, height) â€” note the order is reversed compared to img.shape (height, width).

**Observation:** For a 600x400 original, the resized output is 300x200, exactly half in each dimension.

### Q11. Access and print the pixel value at a user-provided (x, y) coordinate.

**File:** [`solutions/q11_access_and_print_the.py`](solutions/q11_access_and_print_the.py)

**Approach:** NumPy arrays are indexed [row, col] = [y, x], so a pixel at screen coordinate (x, y) is accessed as img[y, x].

**Key functions used:** see inline comments in the script.

**Explanation:** Image arrays are indexed as [row, column] i.e. [y, x] â€” a common source of bugs is mixing this up with (x, y).

**Observation:** The pixel at (100, 50) returns a 3-element BGR array from inside the green rectangle drawn on the sample image.

### Q12. Modify the intensity/value of a selected pixel and save the modified image.

**File:** [`solutions/q12_modify_the_intensityvalue_of.py`](solutions/q12_modify_the_intensityvalue_of.py)

**Approach:** Assigning a new array (or scalar for grayscale) to img[y, x] overwrites that pixel in place; we then persist the change with cv2.imwrite().

**Key functions used:** see inline comments in the script.

**Explanation:** Direct NumPy indexing (img[y, x] = [B, G, R]) is the fastest way to edit a single pixel; cv2.imwrite() then writes the modified array back to disk.

**Observation:** The single pixel at (100, 50) turns pure red; visually indistinguishable at full-image scale but confirmed by the printed before/after values.

### Q13. Read a color image and print the B, G, and R values of a selected pixel.

**File:** [`solutions/q13_read_a_color_image.py`](solutions/q13_read_a_color_image.py)

**Approach:** OpenCV stores color images in BGR (not RGB) order by default, so img[y, x] returns [B, G, R], which we unpack individually.

**Key functions used:** see inline comments in the script.

**Explanation:** OpenCV's default channel order is BGR, so unpacking img[y, x] as b, g, r (not r, g, b) is essential to avoid swapped colors.

**Observation:** Sampling inside the red circle gives a high R value and low B, G values, confirming BGR ordering.

### Q14. Split a color image into its B, G, and R channels and display each channel.

**File:** [`solutions/q14_split_a_color_image.py`](solutions/q14_split_a_color_image.py)

**Approach:** cv2.split() separates a multi-channel image into a list of single-channel images. Each channel, viewed alone, appears as a grayscale image showing that color's intensity.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.split() returns three single-channel arrays; each is displayed as grayscale because a single channel has no color information of its own, only intensity.

**Observation:** The green channel appears bright where the green rectangle was drawn; the red channel is bright where the red circle was drawn.

### Q15. Merge three separate image channels into a single color image.

**File:** [`solutions/q15_merge_three_separate_image.py`](solutions/q15_merge_three_separate_image.py)

**Approach:** cv2.merge([b, g, r]) is the inverse of cv2.split(): it stacks three single-channel arrays back into one 3-channel BGR image.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.merge() takes a list/tuple of equally-sized single-channel arrays and stacks them along a new axis to reconstruct a multi-channel image.

**Observation:** Merging the previously split B, G, R channels reproduces the original image exactly (pixel-for-pixel equal).

### Q16. Calculate and print the minimum and maximum intensity values of a grayscale image.

**File:** [`solutions/q16_calculate_and_print_the.py`](solutions/q16_calculate_and_print_the.py)

**Approach:** cv2.minMaxLoc() (or simply NumPy's .min()/.max()) scans the array and returns the darkest and brightest pixel values.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.minMaxLoc() returns both the extreme values AND their pixel locations in one call, which is convenient over separate .min()/.max()/np.argmin() calls.

**Observation:** The minimum is near 0 (dark background regions) and the maximum is near 255 (the white text / bright shapes).

### Q17. Calculate and print the mean intensity of a grayscale image.

**File:** [`solutions/q17_calculate_and_print_the.py`](solutions/q17_calculate_and_print_the.py)

**Approach:** cv2.mean() (or np.mean()) averages all pixel values, giving a single number that summarizes overall image brightness.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.mean() returns a 4-element tuple (one value per channel, padded with zeros for grayscale), so we take index [0]; np.mean() gives the same result more directly for a single-channel array.

**Observation:** Both methods agree, giving the same mean brightness value for the sample image (roughly the middle of the 0-255 range given the mixed shapes/background).

### Q18. Calculate and print the mean and standard deviation of a grayscale image using NumPy/OpenCV.

**File:** [`solutions/q18_calculate_and_print_the.py`](solutions/q18_calculate_and_print_the.py)

**Approach:** cv2.meanStdDev() computes both statistics in a single efficient call; np.std() gives the NumPy equivalent for comparison.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.meanStdDev() returns two small arrays (one entry per channel); standard deviation quantifies contrast â€” a higher value means intensities are more spread out.

**Observation:** The sample image has a fairly high standard deviation because it mixes very dark background pixels with bright shapes and white text.

### Q19. Create a 256x256 grayscale image in which every pixel has intensity value 128.

**File:** [`solutions/q19_create_a_256x256_grayscale.py`](solutions/q19_create_a_256x256_grayscale.py)

**Approach:** np.full((h, w), value, dtype=np.uint8) allocates an array pre-filled with a constant value â€” a quick way to build solid-color test images.

**Key functions used:** see inline comments in the script.

**Explanation:** np.full() is the cleanest way to build a constant-value array; np.unique() afterward is used to verify every pixel really is 128.

**Observation:** The saved image is a flat mid-gray square with exactly one unique pixel value: 128.

### Q20. Create and display a grayscale intensity ramp whose intensity gradually changes from 0 to 255.

**File:** [`solutions/q20_create_and_display_a.py`](solutions/q20_create_and_display_a.py)

**Approach:** np.linspace(0, 255, width) generates a smooth 1D gradient; tiling it across rows with np.tile() turns it into a 2D ramp image.

**Key functions used:** see inline comments in the script.

**Explanation:** np.linspace() creates evenly spaced values from 0 to 255 for one row; np.tile() repeats that row vertically to fill the full image height.

**Observation:** The output is a smooth horizontal gradient going from black on the left to white on the right.

### Q21. Convert an 8-bit grayscale image into a 4-bit quantized image and display the result.

**File:** [`solutions/q21_convert_an_8bit_grayscale.py`](solutions/q21_convert_an_8bit_grayscale.py)

**Approach:** 4-bit quantization reduces 256 levels to 16. We divide by 16 (256/16), floor to an integer level, then multiply back by 16 to restore a displayable 0-255 range with only 16 distinct values.

**Key functions used:** see inline comments in the script.

**Explanation:** Integer division by `step` collapses many original values into the same bucket, then multiplying back by `step` maps each bucket to a representative displayable intensity.

**Observation:** The result shows visible 'banding' â€” smooth gradients turn into 16 flat bands instead of 256 smooth shades.

### Q22. Convert an 8-bit grayscale image into a 2-bit quantized image and display the result.

**File:** [`solutions/q22_convert_an_8bit_grayscale.py`](solutions/q22_convert_an_8bit_grayscale.py)

**Approach:** Same technique as Q21 but with only 4 levels (2^2), producing much coarser banding since far fewer intensity steps remain.

**Key functions used:** see inline comments in the script.

**Explanation:** With only 4 possible output levels, the same floor-and-rescale approach as Q21 produces much more visible, blocky banding.

**Observation:** Compared to the 4-bit version, this image looks noticeably more posterized, with large flat regions of identical intensity.

### Q23. Downsample an image by a factor of 2 in both width and height and print the original and new resolutions.

**File:** [`solutions/q23_downsample_an_image_by.py`](solutions/q23_downsample_an_image_by.py)

**Approach:** Downsampling means reducing the sampling rate (fewer pixels), achieved here with cv2.resize() using INTER_AREA interpolation, which is the recommended method for shrinking images.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.INTER_AREA resamples using pixel-area relation, which avoids aliasing artifacts and is OpenCV's recommended interpolation specifically for shrinking images.

**Observation:** The downsampled 300x200 image looks like a clean, slightly softer miniature of the original with no jagged edges.

### Q24. Crop a rectangular Region of Interest (ROI) from an image using user-provided coordinates.

**File:** [`solutions/q24_crop_a_rectangular_region.py`](solutions/q24_crop_a_rectangular_region.py)

**Approach:** Because images are NumPy arrays, cropping is simple slicing: img[y1:y2, x1:x2] extracts the rectangular region between those bounds.

**Key functions used:** see inline comments in the script.

**Explanation:** NumPy slicing img[y1:y2, x1:x2] is all that's needed to crop â€” no dedicated OpenCV function is required since images are just arrays.

**Observation:** The cropped output isolates exactly the green rectangle region drawn on the sample image, at a shape of (150, 200, 3).

### Q25. Rotate an image by 90 degrees, display it, and save the rotated image.

**File:** [`solutions/q25_rotate_an_image_by.py`](solutions/q25_rotate_an_image_by.py)

**Approach:** cv2.rotate() offers fast, fixed-angle rotations without needing a rotation matrix; cv2.ROTATE_90_CLOCKWISE rotates the image 90 degrees.

**Key functions used:** see inline comments in the script.

**Explanation:** cv2.rotate() with ROTATE_90_CLOCKWISE handles the transpose-and-flip needed for a clean 90-degree turn in one call, swapping width and height.

**Observation:** A 600x400 image becomes 400x600 after rotation, with content visibly turned a quarter-turn clockwise.

## ðŸ§° Core Functions Practiced

| Function | Purpose |
|---|---|
| `cv2.imread()` | Load an image from disk |
| `cv2.imshow()` / `waitKey()` / `destroyAllWindows()` | Display an image in a window |
| `cv2.imwrite()` | Save an image to disk |
| `cv2.cvtColor()` | Convert between color spaces (e.g. BGR â†’ Gray, BGR â†’ RGB) |
| `cv2.resize()` | Resize / downsample an image |
| `cv2.split()` / `cv2.merge()` | Separate and recombine color channels |
| `cv2.rotate()` | Rotate an image by a fixed angle |
| `cv2.minMaxLoc()` / `cv2.mean()` / `cv2.meanStdDev()` | Pixel intensity statistics |
| NumPy indexing/slicing | Direct pixel access, cropping, quantization |

## ðŸ“ Notes

- All scripts use OpenCV's default **BGR** channel order unless explicitly
  converted to RGB (Q9) for Matplotlib display.
- Quantization (Q21, Q22) reduces the number of intensity levels via
  integer-division bucketing, which is a simple and common way to
  simulate lower bit-depth images.
- Screenshots of actual output aren't included in this repo since results
  are generated fresh by running the scripts â€” see `outputs/` after running.

## ðŸ‘¤ Author

Nitika Singh ([@nitikasingh12](https://github.com/nitikasingh12))

