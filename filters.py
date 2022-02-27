import numpy as np


def apply_film_filter(image: np.ndarray, intensity = 0) -> np.ndarray:
    ''' Limits the range of values allowed in a matrix,
        changing the difference between the max value (255) and min value (0)
        based on intensity. More intensity = less difference.
        Less intensity = more difference.
    '''
    low_limit = 128 - (128 - intensity / 2)
    high_limit = 128 + (128 - intensity / 2) - 1
    
    new_image = image.copy()
    new_image = np.clip(new_image, low_limit, high_limit)
    
    return new_image.astype(np.uint8)

