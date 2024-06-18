"""
File: mirror_lake.py
Name: Zoe
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: the original photo
    :return: photo that had been reflected
    """
    original_mt = SimpleImage(filename)
    reflected_mt = SimpleImage.blank(original_mt.width, original_mt.height*2)
    for x in range(original_mt.width):
        for y in range(original_mt.height):
            # colored
            img_pixel = original_mt.get_pixel(x,y)
            # white1
            blank_pixel = reflected_mt.get_pixel(x,y)
            # white 2
            blank_pixel2 = reflected_mt.get_pixel(x, reflected_mt.height-1-y)

            blank_pixel.red = img_pixel.red
            blank_pixel.green = img_pixel.green
            blank_pixel.blue = img_pixel.blue

            blank_pixel2.red = img_pixel.red
            blank_pixel2.green = img_pixel.green
            blank_pixel2.blue = img_pixel.blue
    return reflected_mt


def main():
    """
    Make a new image that creates a mirror image (reflected)
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
