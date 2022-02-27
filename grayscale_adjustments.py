import numpy as np


def to_grayscale(image: np.ndarray) -> np.ndarray:
	''' Converts image to grayscale
		using the NTSC formula
	'''
	height, width, _ = image.shape
	red = image[:, :, 0] * 0.299
	green = image[:, :, 1] * 0.587
	blue = image[:, :, 2] * 0.114

	gray = np.ceil(red + green + blue)	
	gray = gray.flatten()
	gray_image = np.array([[p, p, p] for p in gray])
	gray_image = gray_image.reshape(height, width, 3)

	return gray_image.astype(np.uint8)



def apply_thershold(image: np.ndarray, thereshold = 128) -> np.ndarray:
	''' Limits the tones of the image to black and white,
		the amount of each one varies based on thereshold
	'''
	to_white = image > thereshold
	to_black = image <= thereshold

	new_image = image.copy()
	new_image[to_white] = 255
	new_image[to_black] = 0

	return new_image



def solarize_image(image: np.ndarray, solarization = 6) -> np.ndarray:
	''' Limits the quantity of tones on an image based on solarization.
		For example:
		solarization = 2, tones = [0, 255]
		solarization = 5, tones = [0, 64, 128, 192, 255]
	'''
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

	new_image = np.clip(new_image, 0, 255)
	return new_image.astype(np.uint8)

