"""
File: babygraphics.py
Name: Evonne
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year in the YEARS list,
    returns the x coordinate of the vertical line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    line_interval = int((width - GRAPH_MARGIN_SIZE * 2)/len(YEARS))
    x_coordinate = int(GRAPH_MARGIN_SIZE + year_index * line_interval)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        line_x = get_x_coordinate(CANVAS_WIDTH, i)
        year = YEARS[i]
        canvas.create_line(line_x, 0, line_x, CANVAS_HEIGHT)
        canvas.create_text(line_x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        d_name = name_data[name]

        # Check whether the name has rank in each year in YEARS,
        # If no data, means the rank of the year is out of the MAX_RANK, so add rank data '*' into d_name.
        for year in YEARS:
            if str(year) in d_name:
                pass
            else:
                d_name[str(year)] = '*'

        # Turn the dict into the list of tuple and sorted by year.
        lst = d_name.items()
        new_lst = sorted(lst)

        # Draw the lines and put data of the rank of name in each year.
        line_color = get_line_color(i)

        for j in range(len(YEARS)):
            start_x = get_x_coordinate(CANVAS_WIDTH, j)
            start_y = get_y_coordinate(CANVAS_HEIGHT, new_lst[j][1])
            if j+1 < len(YEARS):
                end_x = get_x_coordinate(CANVAS_WIDTH, j+1)
                end_y = get_y_coordinate(CANVAS_HEIGHT, new_lst[j+1][1])
                canvas.create_line(start_x, start_y, end_x, end_y, width=LINE_WIDTH, fill=line_color)
            canvas.create_text(start_x + TEXT_DX, start_y, text=(name, new_lst[j][1]),
                               anchor=tkinter.SW, fill=line_color)


def get_y_coordinate(height, rank):
    """
        Given the height of the canvas and the rank of the name in specific year of the YEARS list,
        returns the y coordinate of the rank in that year.

        Input:
            height (int): The height of the canvas
            rank (str): The rank of the name in specific year of the YEARS list
        Returns:
            y_coordinate (int): The y coordinate of the rank in that year.
        """
    available_height = int((height - GRAPH_MARGIN_SIZE * 2))
    if rank == '*':
        y_coordinate = int(CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    else:
        y_coordinate = GRAPH_MARGIN_SIZE+int((available_height/MAX_RANK)*int(rank))
    return y_coordinate


def get_line_color(n):
    """
    Input: int, the index number of the searching name.
    Returns: str, the color of the line.
    """
    while True:
        if n < len(COLORS):
            break
        else:
            n -= len(COLORS)
    return COLORS[n]


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
