import streamlit as st
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import adjustments as adj
import filters as flt
import grayscale_adjustments as gadj
import histogram as hist

# st.set_page_config(layout="wide")

st.title('Image processing with NumPy 101')
uploaded_file = st.file_uploader(
	'Upload an image to start!',
	type=['png', 'jpg', 'jpeg'],
)

if uploaded_file is not None:
	image = img.imread(uploaded_file).astype(np.uint16)

	# Sidebar elements
	st.sidebar.text('Works better on grayscale!')
	enable_grayscale = st.sidebar.checkbox('Turn on grayscale')

	st.sidebar.subheader('General adjustments')
	bright = st.sidebar.slider('Brightness', -255, 255, 0)
	contrast = st.sidebar.slider('Contrast', -127, 128, 0)

	st.sidebar.subheader('Filters')
	film_filter_intensity = st.sidebar.slider('Film', 0, 200, 0)


	# Adjustments applied
	image = adj.change_brightness(image, bright=bright)
	image = adj.change_contrast(image, contrast=contrast)


	# Filters applied
	image = flt.apply_film_filter(image, intensity=film_filter_intensity)


	# Gray scale only
	if enable_grayscale:
		image = gadj.to_grayscale(image)
		st.sidebar.header('Grayscale only!')

		# Thereshold
		enable_thereshold = st.sidebar.checkbox('Thershold')
		st.sidebar.caption('The image will turn to pure black & white')
		if enable_thereshold:
			thershold = st.sidebar.slider('Thershold', 0, 255, 128)
			image = gadj.apply_thershold(image, thereshold=thershold)

		# Solarization
		enable_solarization = st.sidebar.checkbox('Solarization')
		st.sidebar.caption('Limit the quantity of tones')
		if enable_solarization:
			solarization = st.sidebar.slider('Solarization (tones quantity)', 2, 32, 6)
			st.sidebar.caption('If you keep seeing only two tones (B&W), please disable the thershold')
			image = gadj.solarize_image(image, solarization=solarization)

	
	st.image(image)

	# Histograms
	show_histogram = st.checkbox('Show histogram')
	if show_histogram:
		red_col, green_col, blue_col = st.columns(3)

		if not enable_grayscale:
			red_col.caption('Histogram on channel Red')
			red_col.pyplot(hist.red(image))

			green_col.caption('Histogram on channel Green')
			green_col.pyplot(hist.green(image))

			blue_col.caption('Histogram on channel Blue')
			blue_col.pyplot(hist.blue(image))

		else:
			green_col.caption('Histogram')
			# as it is on grayscale, we can choose any channel for histogram
			green_col.pyplot(hist.green(image, color='lightgray'))

