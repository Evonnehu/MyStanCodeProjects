"""
File: blur.py
Name: Evonne
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image.
    :return: SimpleImage, the image will be blurred by changing the original pixel value to the average value of
             this pixel and its adjacent pixels.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            num = 0

            # To get the data from the pixel and its adjacent pixels.
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    img_x = x + i
                    img_y = y + j

                    # To set the boundary limits of the image.
                    if 0 <= img_x < img.width - 1 and 0 <= img_y < img.height - 1:
                        pixel_o = img.get_pixel(img_x, img_y)
                        r_sum += pixel_o.red
                        g_sum += pixel_o.green
                        b_sum += pixel_o.blue
                        num += 1
            pixel_n = new_img.get_pixel(x, y)
            pixel_n.red = r_sum / num
            pixel_n.green = g_sum / num
            pixel_n.blue = b_sum / num
    return new_img


def main():
    """
    This program can make the image blurred.
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
