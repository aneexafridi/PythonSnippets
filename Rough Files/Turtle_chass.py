from turtle import *
t = Turtle() #write the program in class
s=Screen()
s.bgcolor("#558888")
s.title(" SHAHAB  :: ??????????")
t.speed("fastest")
t._delay(1)
t.penup()
t.goto(-300,-320)
# t.pendown()
t.write("Chess Game Pattern   ?????? ",font=("Arial",20,"italic"))
t.color("red")
s.setup(1400,720,0,0)
t.pensize(2)
def Blocks():
    for i in range(4):
        t.fd(70)
        t.lt(90)
def Goxy(m,n):
    for i in range(4):
        t.penup()
        t.goto(630-(70*m),350-(70*n))
        t.pendown()
def Chass():
    for i in range(1,10):
        for j in range(1,19):
            if ((i+j)%3 == 0):
                Goxy(j,i)
                t.fillcolor("Black")
                t.begin_fill()
                Blocks()
                t.end_fill()
            elif((i+j)%2== 0):
                Goxy(j,i)
                t.fillcolor("white")
                t.begin_fill()
                Blocks()
                t.end_fill()
            else:
                Goxy(j,i)
                t.begin_fill()
                t.fillcolor("green")
                Blocks()
                t.end_fill()
Chass()
t.hideturtle()
done()
#########
##########
#######33
from turtle import *
t = Turtle() #write the program in class
s=Screen()
s.bgcolor("#558888")
s.title(" SHAHAB  :: ??????????")
t.speed("fastest")
t._delay(0)
t.penup()
t.goto(-300,-320)
# t.pendown()
t.write("Chess Game Pattern   ?????? ",font=("Arial",20,"italic"))
t.color("red")
s.setup(1400,720,0,0)
t.pensize(2)
def Blocks():
    for i in range(4):
        t.fd(70)
        t.lt(90)
def Goxy(m,n):
    for i in range(4):
        t.penup()
        t.goto(630-(70*m),350-(70*n))
        t.pendown()
def Chass():
    for i in range(1,9):
        for j in range(1,9):
            if ((i+j)%1 != 0):
                Goxy(j,i)
                t.fillcolor("Black")
                t.begin_fill()
                Blocks()
                t.end_fill()
            elif((i+j)%3== 0):
                Goxy(j,i)
                t.fillcolor("white")
                t.begin_fill()
                Blocks()
                t.end_fill()
            else:
                Goxy(j,i)
                t.begin_fill()
                t.fillcolor("green")
                Blocks()
                t.end_fill()
Chass()
t.hideturtle()
done()