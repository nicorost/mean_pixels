# This is my project!
import statistics
from utils import calculate_pixel_brightness

pixels = [
    {'red': 100, 'green': 0, 'blue': 0},
    {'red': 50, 'green': 100, 'blue': 0}
]

pixel_brightness = [calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue']) for pixel in pixels]
mean_brightness = statistics.mean(pixel_brightness)
print(mean_brightness)
