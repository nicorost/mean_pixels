# This is my project!
import statistics


def calculate_pixel_brightness(x, y, z):
    return statistics.mean([x, y, z])


pixel = {'red': 100, 'green': 0, 'blue': 0}
pixel2 = {'red': 50, 'green': 100, 'blue': 0}
pixels = [pixel, pixel2]

pixel_brightness = [calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue']) for pixel in pixels]

pixel_brightness3 = statistics.mean(pixel_brightness)
print(pixel_brightness3)
