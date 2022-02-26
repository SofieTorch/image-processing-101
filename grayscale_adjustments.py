import numpy as np

# Converts image (numpy.ndarray) to grayscale
# using the NTSC formula
def to_grayscale(image):
	height, width, _ = image.shape
	red = image[:, :, 0] * 0.299
	green = image[:, :, 1] * 0.587
	blue = image[:, :, 2] * 0.114
	gray = np.ceil(red + green + blue)	
	gray = gray.flatten()
	gray_image = np.array([[p, p, p] for p in gray])
	gray_image = (gray_image.reshape(height, width, 3)).astype(int)

	return gray_image

# Limits the tone of the image (numpy.ndarray) to black and white,
# the amount of each one varies in base of thereshold
def apply_thershold(image, thereshold = 128):
	to_white = image > thereshold
	to_black = image <= thereshold
	new_image = image.copy()
	new_image[to_white] = 255
	new_image[to_black] = 0
	return new_image

# Limits the quantity of tones on an image (numpy.ndarray)
# minimum tones allowed = 2, which corresponds to black and white
def solarize_image(image, solarization = 6):
	interval = 256 / (solarization - 1)
	valid_tones = np.arange(0, 257, interval).astype(np.uint16)

	previous_tone = 0
	new_image = image.copy().astype(np.uint16)

	for tone in valid_tones:
		inside_tones = np.logical_and(image < tone, image >= previous_tone)
		half_up = np.logical_and(inside_tones, image >= (tone + previous_tone) / 2)
		half_down = np.logical_and(inside_tones, image < (tone + previous_tone) / 2)	
		new_image[half_up] = tone
		new_image[half_down] = previous_tone
		previous_tone = tone

	new_image = np.clip(new_image, 0, 255).astype(np.uint8)
	return new_image
