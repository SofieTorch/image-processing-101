import numpy as np

# Performs a matrix addition with a 
# scalar value (bright)
def change_brightness(image, bright = 0):
	new_image = image + bright
	new_image = np.clip(new_image, 0, 255)
	return new_image

# Performs a matrix addition with a scalar value (contrast).
# Increases the lighter tones and decreases the darker ones with a positive contrast,
# decreases the lighter tones and increases the darker ones with a negative contrast.
def change_contrast(image, contrast = 0):
  to_increase = image >= 128
  to_decrease = image < 128
  new_image = image.copy().astype(np.int32)
  new_image[to_increase] = np.clip(new_image[to_increase] + contrast, 128, 255)
  new_image[to_decrease] = np.clip(new_image[to_decrease] - contrast, 0, 127)
  new_image = new_image.astype(np.uint8)
  return new_image
