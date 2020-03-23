# This is my project!
import statistics


def calculate_pixel_brightness(x, y, z):
    return statistics.mean([x, y, z])


pixel = {'red': 100, 'green': 0, 'blue': 0}
pixel_brightness = calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue'])

pixel2 = {'red': 50, 'green': 100, 'blue': 0}
pixel_brightness2 = calculate_pixel_brightness(pixel2['red'], pixel2['green'], pixel2['blue'])

pixel_brightness3 = statistics.mean([pixel_brightness, pixel_brightness2])
print(pixel_brightness3)
