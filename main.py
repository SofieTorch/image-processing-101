import streamlit as st
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import adjustments as adj
import filters as flt
import grayscale_adjustments as gadj


def get_red_histogram(image, color = 'tomato'):
	red = image[:, :, 0]
	fig, ax = plt.subplots()
	ax.hist(red.ravel(), bins=255, color = color)
	return fig


def get_green_histogram(image, color = 'palegreen'):
	green = image[:, :, 1]
	fig, ax = plt.subplots()
	ax.hist(green.ravel(), bins=255, color = color)
	return fig


def get_blue_histogram(image, color = 'cornflowerblue'):
	blue = image[:, :, 2]
	fig, ax = plt.subplots()
	ax.hist(blue.ravel(), bins=255, color = color)
	return fig

# st.set_page_config(layout="wide")

st.title('Image processing with NumPy 101')
uploaded_file = st.file_uploader(
	'Upload an image to start!',
	type=['png', 'jpg', 'jpeg'],
)

controls, output = st.columns([1, 3])

if uploaded_file is not None:
	image = img.imread(uploaded_file).astype(np.uint16)

	# Sidebar
	st.sidebar.text('Works better on grayscale!')
	enable_grayscale = st.sidebar.checkbox('Turn on grayscale')

	st.sidebar.subheader('General adjustments')
	bright = st.sidebar.slider('Brightness', -255, 255, 0)
	contrast = st.sidebar.slider('Contrast', -127, 128, 0)

	st.sidebar.subheader('Filters')
	film_filter_intensity = st.sidebar.slider('Film', 0, 200, 0)

	# Adjustments
	image = adj.change_brightness(image, bright=bright)
	image = adj.change_contrast(image, contrast=contrast)

	# Filters
	image = flt.apply_film_filter(image, intensity=film_filter_intensity)

	# Gray scale only
	if enable_grayscale:
		image = gadj.to_grayscale(image)
		st.sidebar.header('Grayscale only!')

		enable_thereshold = st.sidebar.checkbox('Thershold')
		st.sidebar.caption('The image will turn to pure black & white')
		if enable_thereshold:
			thershold = st.sidebar.slider('Thershold', 0, 255, 128)
			image = gadj.apply_thershold(image, thereshold=thershold)

		enable_solarization = st.sidebar.checkbox('Solarization')
		st.sidebar.caption('Limit the quantity of tones')
		if enable_solarization:
			solarization = st.sidebar.slider('Solarization (tones quantity)', 2, 32, 6)
			st.sidebar.caption('If you keep seeing only two tones (B&W), please disable the thershold')
			image = gadj.solarize_image(image, solarization=solarization)

	st.image(image)

	show_histogram = st.checkbox('Show histogram')
	if show_histogram:
		red_col, green_col, blue_col = st.columns(3)
		if not enable_grayscale:
			red_col.caption('Histogram on channel Red')
			red_col.pyplot(get_red_histogram(image))
			green_col.caption('Histogram on channel Green')
			green_col.pyplot(get_green_histogram(image))
			blue_col.caption('Histogram on channel Blue')
			blue_col.pyplot(get_blue_histogram(image))
		else:
			green_col.caption('Histogram')
			green_col.pyplot(get_green_histogram(image, color='lightgray'))

