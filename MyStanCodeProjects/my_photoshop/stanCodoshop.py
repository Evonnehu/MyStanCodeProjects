"""
File: stanCodoshop.py
Name: Evonne
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # The calculation of the square root = **(0.5)
    color_distance = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    green_total = 0
    red_total = 0
    blue_total = 0
    for pixel in pixels:
        green_total += pixel.green
        red_total += pixel.red
        blue_total += pixel.blue
    avg_rgb_list = [int(red_total/len(pixels)), int(green_total/len(pixels)), int(blue_total/len(pixels))]
    return avg_rgb_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # The list of average red, green, and blue values of the pixels (in order).
    avg_pixel_rgb = get_average(pixels)
    avg_red = avg_pixel_rgb[0]
    avg_green = avg_pixel_rgb[1]
    avg_blue = avg_pixel_rgb[2]

    # Get the "color distance" of each pixel to the average RGB value of the pixels to be compared.
    shortest_dist = 0
    best_pixel = ''
    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel, avg_red, avg_green, avg_blue)
        # Record the 1st data.
        if shortest_dist == 0:
            shortest_dist = pixel_dist
            best_pixel = pixel
        # Compare and get the shortest color distance and the best pixel.
        elif pixel_dist < shortest_dist:
            shortest_dist = pixel_dist
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # Loop over the picture and fill in the best pixels to the result image.
    for x in range(result.width):
        for y in range(result.height):
            result_pixel = result.get_pixel(x, y)
            compared_img_pixel = []
            for img in images:
                img_pixel = img.get_pixel(x, y)
                compared_img_pixel.append(img_pixel)
            best_pixel = get_best_pixel(compared_img_pixel)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
