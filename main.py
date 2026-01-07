from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from scipy.signal import convolve2d

image = load_image("galil.png")
clean_image = median(image, ball(3))
edge_image = edge_detection(clean_image)
img = Image.fromarray(edge_image)
img.save('my_edges.png')
