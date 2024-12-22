import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
def draw():
    h = 0;
    n = 98
    for i in range(280):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 1/n
        t.color(c)
        t.pensize(5)
        t.fillcolor('black')
        t.begin_fill()
        t.circle(i,43)
        t.rt(45)
        t.bk(45)
        t.up()
        t.goto(7,56)
        t.down()
        t.circle(i,23)
        t.end_fill()
        t.circle(i,90)
draw()
t.done()

        
