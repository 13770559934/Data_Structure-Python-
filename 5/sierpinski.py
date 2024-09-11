import turtle;

def sierpinski(degree, points, t):
    colormap = ['blue','red','green','white','yellow','orange','purple']
    drawtriangle(points,colormap[degree],t);
    if degree > 0:
        sierpinski(
            degree-1,
            {
                'left' : points['left'],
                'right': getmid(points['left'],points['right']),
                'top':  getmid(points['top'],points['left'])
            },
            t
        )
        sierpinski(
            degree - 1,
            {
                'top': points['top'],
                'right': getmid(points['top'], points['right']),
                'left' : getmid(points['top'], points['left'])
            },
            t
        )
        sierpinski(
            degree - 1,
            {
                'right': points['right'],
                'top': getmid(points['right'], points['top']),
                'left': getmid(points['right'],points['left'])
            },
            t
        )



def drawtriangle(points, color, t):
    t.fillcolor(color);
    t.penup();
    t.goto(points['top']);
    t.pendown();
    t.begin_fill();
    t.goto(points['left']);
    t.goto(points['right']);
    t.goto(points['top']);
    t.end_fill();

def getmid(point1, point2):
    return ((point1[0] + point2[0])/2, (point1[1]+point2[1])/2);


t = turtle.Turtle();

points = {
    'top': (0,200),
    'left': (-200,-100),
    'right': (200,-100)
}

sierpinski(6,points,t)

turtle.done();