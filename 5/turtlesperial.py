import turtle;
t = turtle.Turtle();

def drawsperial(t, lineLen):
    if lineLen > 0:
        t.forward(lineLen);
        t.right(90);
        drawsperial(t, lineLen - 5);
    t.hideturtle()

drawsperial(t, 200);

turtle.done();