# This is my project!


def calculate_pixel_brightness(x, y, z):
    return (x + y + z) / 3


red, green, blue = 100, 0, 0
pixel_brightness = calculate_pixel_brightness(red, green, blue)

red2, green2, blue2 = 50, 100, 0
pixel_brightness2 = calculate_pixel_brightness(red2, green2, blue2)

readiness, readiness = 0, 200

pixel_brightness3 = (pixel_brightness + pixel_brightness2) / 2
print(pixel_brightness3)
