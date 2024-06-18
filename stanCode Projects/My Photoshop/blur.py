"""
File: blur.py
Name: Zoe
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the clear photo
    :return: the blurred photo
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
            # for pixel_x in range(x-1, x+2, 1):
            #     for pixel_y in range(y-1, y+2, 1):
                    if 0 <= pixel_x < img.width and 0 <= pixel_y < img.height:            # 下限包含 上限不包含
                        pixel = img.get_pixel(pixel_x, pixel_y)
                        r_sum += pixel.red
                        g_sum += pixel.green
                        b_sum += pixel.blue
                        count += 1
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = r_sum / count
            new_pixel.green = g_sum / count
            new_pixel.blue = b_sum / count
    return new_img


def main():
    """
    Make a clear image blurred
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
