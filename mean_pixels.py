# This is my project!
import statistics


def calculate_pixel_brightness(red: int, green: int, blue: int) -> float:
    """Calculates the brightness of a pixel from its r,g,b values."""
    return statistics.mean([red, green, blue])


pixels = [
    {'red': 100, 'green': 0, 'blue': 0},
    {'red': 50, 'green': 100, 'blue': 0}
]

pixel_brightness = [calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue']) for pixel in pixels]
pixel_brightness3 = statistics.mean(pixel_brightness)
print(pixel_brightness3)
