"""
File: my_drawing.py
Name: Zoe
----------------------
TODO: Create a drawing
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GArc, GLine
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage


def main():
    """
    Title: Ferrari F1 car

    This is a Ferrari F1 racing car.
    The number '16' is my favorite driver's racing number.
    Because I am obsessed with F1 racing,
    I applied for a master's degree in the US to learn SCM and to get closer to the racing environment.
    After I was admitted, I realized I should improve my coding skills.
    As you can see, F1 racing is kind of the reason why I am in stanCode.
    So... yes! That's why I drew a Ferrari F1 racing car.
    """
    window = GWindow(width=1200, height=600, title='Ferrari F1 car')

    body1 = GRect(400, 125, x=200, y=300)
    body1.filled = True
    body1.fill_color = 'firebrick'
    body1.color = 'firebrick'
    window.add(body1)

    body2 = GRect(25, 55, x=500, y=195)
    body2.filled = True
    body2.fill_color = 'firebrick'
    body2.color = 'firebrick'
    window.add(body2)

    body3 = GPolygon()
    body3.add_vertex((200, 300))
    body3.add_vertex((200, 220))
    body3.add_vertex((500, 190))
    body3.add_vertex((500, 300))
    body3.filled = True
    body3.fill_color = 'firebrick'
    body3.color = 'firebrick'
    window.add(body3)

    body4 = GArc(2000, 500, 0, 90)
    body4.filled = True
    body4.fill_color = 'firebrick'
    body4.color = 'firebrick'
    window.add(body4, x=100, y=300)

    rear_wing1 = GPolygon()
    rear_wing1.add_vertex((50, 325))
    rear_wing1.add_vertex((175, 400))
    rear_wing1.add_vertex((175, 250))
    rear_wing1.add_vertex((50, 250))
    rear_wing1.filled = True
    rear_wing1.fill_color = 'darkgray'
    rear_wing1.color = 'darkgray'
    window.add(rear_wing1)

    rear_wing2 = GPolygon()
    rear_wing2.add_vertex((50, 255))
    rear_wing2.add_vertex((80, 240))
    rear_wing2.add_vertex((55, 230))
    rear_wing2.filled = True
    rear_wing2.fill_color = 'darkgray'
    rear_wing2.color = 'darkgray'
    window.add(rear_wing2)

    rear_wing3 = GRect(3, 20, x=100, y=230)
    rear_wing3.filled = True
    rear_wing3.fill_color = 'firebrick'
    rear_wing3.color = 'firebrick'
    window.add(rear_wing3)

    rear_wing4 = GRect(65, 3, x=55, y=230)
    rear_wing4.filled = True
    rear_wing4.fill_color = 'firebrick'
    rear_wing4.color = 'firebrick'
    window.add(rear_wing4)

    rear_wing5 = GRect(100, 20, x=75, y=375)
    rear_wing5.filled = True
    rear_wing5.fill_color = 'darkgray'
    rear_wing5.color = 'darkgray'
    window.add(rear_wing5)

    halo1 = GPolygon()
    halo1.add_vertex((730, 305))
    halo1.add_vertex((733, 305))
    halo1.add_vertex((703, 245))
    halo1.add_vertex((700, 245))
    halo1.filled = True
    window.add(halo1)

    halo2 = GPolygon()
    halo2.add_vertex((450, 285))
    halo2.add_vertex((450, 288))
    halo2.add_vertex((715, 243))
    halo2.add_vertex((715, 240))
    halo2.filled = True
    window.add(halo2)

    roll = GRect(12, 20, x=505, y=175)
    roll.filled = True
    window.add(roll)

    front_wing = GArc(500, 520, 0, 80)
    front_wing.filled = True
    front_wing.fill_color = 'darkgray'
    front_wing.color = 'darkgray'
    window.add(front_wing, x=825, y=310)

    floor1 = GArc(750, 200, 80, 100)
    floor1.filled = True
    floor1.fill_color = 'darkgray'
    floor1.color = 'darkgray'
    window.add(floor1, x=500, y=383)

    floor2 = GRect(210, 10, x=300, y=423)
    floor2.filled = True
    floor2.fill_color = 'darkgray'
    floor2.color = 'darkgray'
    window.add(floor2)

    floor3 = GArc(300, 200, 0, 120)
    floor3.filled = True
    floor3.fill_color = 'darkgray'
    floor3.color = 'darkgray'
    window.add(floor3, x=90, y=383)

    mirror1 = GRect(30, 10, x=600, y=280)
    mirror1.filled = True
    mirror1.fill_color = 'firebrick'
    mirror1.color = 'firebrick'
    window.add(mirror1)

    mirror2 = GLine(615, 290, 450, 320)
    mirror2.color = 'firebrick'
    window.add(mirror2)

    mirror3 = GLine(625, 290, 625, 300)
    mirror3.color = 'firebrick'
    window.add(mirror3)

    vent1 = GArc(50, 40, 90, 180)
    vent1.color = 'maroon'
    window.add(vent1, x=320, y=300)

    vent2 = GArc(50, 40, 90, 180)
    vent2.color = 'maroon'
    window.add(vent2, x=350, y=300)

    vent3 = GArc(50, 40, 90, 180)
    vent3.color = 'maroon'
    window.add(vent3, x=380, y=300)

    vent4 = GArc(50, 40, 90, 180)
    vent4.color = 'maroon'
    window.add(vent4, x=410, y=300)

    vent5 = GArc(50, 40, 90, 180)
    vent5.color = 'maroon'
    window.add(vent5, x=440, y=300)

    num = GLabel('16')
    num.font = '-35-bold'
    num.color = 'white'
    window.add(num, x=220, y=285)

    flag1 = GRect(50, 30, x=320, y=230)
    flag1.filled = True
    flag1.fill_color = 'green'
    flag1.color = 'green'
    window.add(flag1)

    flag2 = GRect(50, 30, x=370, y=230)
    flag2.filled = True
    flag2.fill_color = 'white'
    flag2.color = 'white'
    window.add(flag2)

    flag3 = GRect(50, 30, x=420, y=230)
    flag3.filled = True
    flag3.fill_color = 'red'
    flag3.color = 'red'
    window.add(flag3)

    ray = GLabel('Ray·Ban')
    ray.font = 'Verdana-15'
    ray.color = 'white'
    window.add(ray, x=290, y=390)

    ceva = GLabel('CevA')
    ceva.font = '-25'
    ceva.color = 'white'
    window.add(ceva, x=400, y=415)

    zoe = GLabel('Zoe')
    zoe.font = 'Courier-20-bold'
    zoe.color = 'white'
    window.add(zoe, x=690, y=370)

    shell = GImage('SHELL.jpg')
    window.add(shell, x=520, y=325)

    ferrari = GImage('Ferrari.jpg')
    window.add(ferrari, x=640, y=320)

    san = GImage('san.jpg')
    window.add(san, x=990, y=370)

    shell_r = GImage('Shell-R.jpg')
    window.add(shell_r, x=55, y=260)

    shell_t = GLabel('V-Power')
    shell_t.font = 'Verdana-15'
    shell_t.color = 'white'
    window.add(shell_t, x=90, y=285)

    vela = GLabel('▼  VELAS')
    vela.font = 'Verdana-15'
    vela.color = 'white'
    window.add(vela, x=60, y=315)

    snap = GLabel('Snapdragon')
    snap.font = '-15'
    snap.color = 'white'
    window.add(snap, x=610, y=430)

    rear_tyre = GOval(150, 150, x=125, y=300)
    rear_tyre.filled = True
    window.add(rear_tyre)

    rear_y = GOval(125, 125, x=138, y=313)
    rear_y.filled = True
    rear_y.fill_color = 'gold'
    window.add(rear_y)

    rear_b = GOval(100, 100, x=150, y=325)
    rear_b.filled = True
    window.add(rear_b)

    rear_c = GOval(30, 30, x=185, y=360)
    rear_c.filled = True
    rear_c.fill_color = 'gold'
    window.add(rear_c)

    front_tyre = GOval(150, 150, x=775, y=300)
    front_tyre.filled = True
    window.add(front_tyre)

    front_y = GOval(125, 125, x=788, y=313)
    front_y.filled = True
    front_y.fill_color = 'gold'
    window.add(front_y)

    front_b = GOval(100, 100, x=800, y=325)
    front_b.filled = True
    window.add(front_b)

    front_c = GOval(30, 30, x=835, y=360)
    front_c.filled = True
    front_c.fill_color = 'gold'
    window.add(front_c)


if __name__ == '__main__':
    main()
