import turtle as t

t.color("yellow")
t.pensize(5)
t.penup()
t.shape("turtle")
t.fillcolor("yellow")
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()
t.done()
