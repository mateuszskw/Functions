import turtle

pen = turtle.Turtle()
pen.speed(5)
window = turtle.Screen()
window.bgcolor("lightgreen")

def finish():
  pen.hideturtle()
  window.mainloop()

def goto(x, y):
  pen.penup()
  pen.goto(x, y)
  pen.pendown()

def draw_square(length):
  for i in range(4):
      pen.forward(length)
      pen.right(90)

def draw_rectangle(x, y):
  for i in range(4):
    if i % 2 == 0:
      pen.forward(x)
    else:
      pen.forward(y)
    pen.right(90)

def draw_trangle(length):
    for i in range(3):
      pen.forward(length)
      pen.right(120)
