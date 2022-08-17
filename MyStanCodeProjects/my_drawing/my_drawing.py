"""
File: my drawing.py
Name: Evonne
----------------------
創作理念: 我最愛的豆豆龍~ 豆豆龍~ 召喚你我美好的童年回憶
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(width=800, height=500, title='MyDrawing')


def main():
    """
    創作理念: 我最愛的豆豆龍~ 豆豆龍~ 召喚你我美好的童年回憶
    """
    totoro_1()
    totoro_2()
    bus_station()
    grass()
    ground()


def totoro_1():
    body_bottom1 = GOval(202, 150, x=350, y=209)
    body_bottom1.filled = True
    body_bottom1.fill_color = 'silver'
    body_bottom1.color = 'silver'
    window.add(body_bottom1)

    body_top1 = GOval(186, 150, x=358, y=160)
    body_top1.filled = True
    body_top1.fill_color = 'silver'
    body_top1.color = 'silver'
    window.add(body_top1)

    left_b = GArc(150, 250, 190, -90, x=349, y=202)
    left_b.filled = True
    left_b.fill_color = 'silver'
    left_b.color = 'silver'
    window.add(left_b)

    right_b = GArc(90, 270, 0, 110, x=492, y=206)
    right_b.filled = True
    right_b.fill_color = 'silver'
    right_b.color = 'silver'
    window.add(right_b)

    belly = GOval(180, 110, x=360, y=230)
    belly.filled = True
    belly.fill_color = 'whitesmoke'
    belly.color = 'whitesmoke'
    window.add(belly)

    l_ear1 = GOval(50, 90, x=375, y=95)
    l_ear1.filled = True
    l_ear1.fill_color = 'silver'
    l_ear1.color = 'silver'
    window.add(l_ear1)

    r_ear1 = GOval(50, 90, x=475, y=95)
    r_ear1.filled = True
    r_ear1.fill_color = 'silver'
    r_ear1.color = 'silver'
    window.add(r_ear1)

    l_eye1 = GOval(14, 14)
    l_eye1.filled = True
    window.add(l_eye1, x=403, y=198)

    # l_eyeo = GOval(20, 20)
    # window.add(l_eyeo, x=400, y=195)
    #
    # l_eyeo1 = GOval(22, 22)
    # window.add(l_eyeo1, x=399, y=194)

    r_eye1 = GOval(14, 14)
    r_eye1.filled = True
    window.add(r_eye1, x=480, y=198)

    # r_eyeo = GOval(20, 20)
    # window.add(r_eyeo, x=477, y=195)

    # r_eyeo1 = GOval(22, 22)
    # window.add(r_eyeo1, x=476, y=194)

    nose = GPolygon()
    nose.add_vertex((446, 210))
    nose.add_vertex((453, 210))
    nose.add_vertex((449, 213))
    nose.filled = True
    window.add(nose)

    pattern1 = GPolygon()
    pattern1.add_vertex((420, 260))
    pattern1.add_vertex((405, 250))
    pattern1.add_vertex((390, 260))
    pattern1.filled = True
    pattern1.fill_color = 'gray'
    pattern1.color = 'gray'
    window.add(pattern1)

    pattern2 = GPolygon()
    pattern2.add_vertex((465, 260))
    pattern2.add_vertex((450, 250))
    pattern2.add_vertex((435, 260))
    pattern2.filled = True
    pattern2.fill_color = 'gray'
    pattern2.color = 'gray'
    window.add(pattern2)

    pattern3 = GPolygon()
    pattern3.add_vertex((510, 260))
    pattern3.add_vertex((495, 250))
    pattern3.add_vertex((480, 260))
    pattern3.filled = True
    pattern3.fill_color = 'gray'
    pattern3.color = 'gray'
    window.add(pattern3)

    pattern4 = GPolygon()
    pattern4.add_vertex((490, 280))
    pattern4.add_vertex((475, 273))
    pattern4.add_vertex((460, 280))
    pattern4.filled = True
    pattern4.fill_color = 'gray'
    pattern4.color = 'gray'
    window.add(pattern4)

    pattern5 = GPolygon()
    pattern5.add_vertex((440, 280))
    pattern5.add_vertex((425, 273))
    pattern5.add_vertex((410, 280))
    pattern5.filled = True
    pattern5.fill_color = 'gray'
    pattern5.color = 'gray'
    window.add(pattern5)

    line1 = GLine(358, 210, 378, 212)
    window.add(line1)

    line2 = GLine(358, 215, 378, 217)
    window.add(line2)

    line3 = GLine(353, 220, 380, 222)
    window.add(line3)

    line4 = GLine(525, 212, 545, 210)
    window.add(line4)

    line5 = GLine(525, 217, 545, 215)
    window.add(line5)

    line6 = GLine(522, 222, 547, 220)
    window.add(line6)


def totoro_2():
    body_bottom1 = GOval(100, 60, x=560, y=299)
    body_bottom1.filled = True
    body_bottom1.fill_color = 'lightsteelblue'
    body_bottom1.color = 'lightsteelblue'
    window.add(body_bottom1)

    right_b = GArc(105, 270, 115, -120, x=585, y=250)
    right_b.filled = True
    right_b.fill_color = 'lightsteelblue'
    right_b.color = 'lightsteelblue'
    window.add(right_b)

    left_b = GArc(150, 250, 190, -120, x=560, y=245)
    left_b.filled = True
    left_b.fill_color = 'lightsteelblue'
    left_b.color = 'lightsteelblue'
    window.add(left_b)

    belly = GOval(91, 70, x=565, y=288)
    belly.filled = True
    belly.fill_color = 'aliceblue'
    belly.color = 'aliceblue'
    window.add(belly)

    l_ear1 = GOval(20, 50, x=577, y=210)
    l_ear1.filled = True
    l_ear1.fill_color = 'lightsteelblue'
    l_ear1.color = 'lightsteelblue'
    window.add(l_ear1)

    r_ear1 = GOval(20, 50, x=620, y=210)
    r_ear1.filled = True
    r_ear1.fill_color = 'lightsteelblue'
    r_ear1.color = 'lightsteelblue'
    window.add(r_ear1)

    r_eye1 = GOval(7, 12)
    r_eye1.filled = True
    window.add(r_eye1, x=586, y=266)

    l_eye1 = GOval(7, 12)
    l_eye1.filled = True
    window.add(l_eye1, x=627, y=266)

    nose = GPolygon()
    nose.add_vertex((610, 279))
    nose.add_vertex((613, 279))
    nose.add_vertex((611, 280))
    nose.filled = True
    window.add(nose)

    pattern1 = GPolygon()
    pattern1.add_vertex((602, 305))
    pattern1.add_vertex((612, 300))
    pattern1.add_vertex((623, 305))
    pattern1.filled = True
    pattern1.fill_color = 'lightsteelblue'
    pattern1.color = 'lightsteelblue'
    window.add(pattern1)

    pattern2 = GPolygon()
    pattern2.add_vertex((573, 310))
    pattern2.add_vertex((583, 305))
    pattern2.add_vertex((595, 310))
    pattern2.filled = True
    pattern2.fill_color = 'lightsteelblue'
    pattern2.color = 'lightsteelblue'
    window.add(pattern2)

    pattern3 = GPolygon()
    pattern3.add_vertex((630, 310))
    pattern3.add_vertex((642, 305))
    pattern3.add_vertex((650, 310))
    pattern3.filled = True
    pattern3.fill_color = 'lightsteelblue'
    pattern3.color = 'lightsteelblue'
    window.add(pattern3)


def bus_station():
    pole = GRect(8, 70, x=146, y=260)
    pole.filled = True
    pole.fill_color = 'black'
    window.add(pole)

    bottom = GRect(45, 27, x=126, y=331)
    bottom.filled = True
    bottom.fill_color = 'darkgray'
    window.add(bottom)

    board = GOval(103, 103, x=100, y=170)
    board.filled = True
    board.fill_color = 'navy'
    window.add(board)

    s_name = GRect(96, 30, x=103, y=207)
    s_name.filled = True
    s_name.fill_color = 'aliceblue'
    s_name.color = 'whitesmoke'
    window.add(s_name)

    label = GLabel('稻 荷 前')
    label.color = 'midnightblue'
    label.font = '-16-bold'
    window.add(label, x=114, y=234)


def grass():
    grass1 = GPolygon()
    grass1.add_vertex((200, 360))
    grass1.add_vertex((205, 330))
    grass1.add_vertex((210, 345))
    grass1.add_vertex((215, 330))
    grass1.add_vertex((220, 345))
    grass1.add_vertex((225, 325))
    grass1.add_vertex((230, 360))
    grass1.filled = True
    grass1.fill_color = 'darksage'
    grass1.color = 'darksage'
    window.add(grass1)

    grass2 = GPolygon()
    grass2.add_vertex((270, 360))
    grass2.add_vertex((275, 335))
    grass2.add_vertex((280, 350))
    grass2.add_vertex((285, 335))
    grass2.add_vertex((290, 350))
    grass2.add_vertex((295, 335))
    grass2.add_vertex((300, 360))
    grass2.filled = True
    grass2.fill_color = 'olivedrab'
    grass2.color = 'olivedrab'
    window.add(grass2)

    grass3 = GPolygon()
    grass3.add_vertex((690, 360))
    grass3.add_vertex((695, 330))
    grass3.add_vertex((700, 345))
    grass3.add_vertex((705, 330))
    grass3.add_vertex((710, 345))
    grass3.add_vertex((715, 325))
    grass3.add_vertex((720, 360))
    grass3.filled = True
    grass3.fill_color = 'darksage'
    grass3.color = 'darksage'
    window.add(grass3)


def ground():
    g = GRect(650, 8, x=80, y=359)
    g.filled = True
    g.fill_color = 'tan'
    g.color = 'tan'
    window.add(g)


if __name__ == '__main__':
    main()
