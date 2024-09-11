import turtle;

def tree(t, branch_len):
    if branch_len > 5:
        t.forward(branch_len);
        t.right(20);
        tree(t, branch_len - 15);
        t.left(40);
        tree(t, branch_len - 15);
        t.right(20);
        t.backward(branch_len);

t = turtle.Turtle();
t.left(90);

t.penup();
t.backward(200);
t.pendown();
t.pencolor('green');
t.pensize(2);
tree(t,75);
t.hideturtle()
turtle.done()