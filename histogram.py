import matplotlib.pyplot as plt
import numpy as np


def red(image: np.ndarray, color = 'tomato') -> plt.figure:
	red = image[:, :, 0]
	fig, ax = plt.subplots()
	ax.hist(red.ravel(), bins=255, color = color)
	return fig


def green(image: np.ndarray, color = 'palegreen') -> plt.figure:
	green = image[:, :, 1]
	fig, ax = plt.subplots()
	ax.hist(green.ravel(), bins=255, color = color)
	return fig


def blue(image: np.ndarray, color = 'cornflowerblue') -> plt.figure:
	blue = image[:, :, 2]
	fig, ax = plt.subplots()
	ax.hist(blue.ravel(), bins=255, color = color)
	return fig

