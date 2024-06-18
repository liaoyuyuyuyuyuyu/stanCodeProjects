"""
File: fire.py
Name: Zoe
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage

HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: the original photo
    :return: photo that shows fire places
    """
    highlight_fires_img = SimpleImage(filename)
    for x in range(highlight_fires_img.width):
        for y in range(highlight_fires_img.height):
            pixel = highlight_fires_img.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue) // 3
            if pixel.red > avg * HURDLE_FACTOR:
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.red = avg
                pixel.green = avg
                pixel.blue = avg
    return highlight_fires_img


def main():
    """
    Highlight the fire places
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
