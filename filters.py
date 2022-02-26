import numpy as np

# Limits the range of values allowed in a matrix,
# changing the difference between the max value (255) and min value (0)
# based on intensity. With more intensity, less difference.
# With less intensity, more difference
def apply_film_filter(image, intensity = 0):
    low = 128 - (128 - intensity / 2)
    high = 128 + (128 - intensity / 2) - 1
    new_image = image.copy()
    new_image = np.clip(new_image, low, high)
    new_image = new_image.astype(np.uint8)
    return new_image
