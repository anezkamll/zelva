from turtle import forward, left, right, shape, penup, pendown, exitonclick

from math import sqrt

shape('turtle')

# vesnice

for a in range (5):
    for a in range (2):
        left(45)
        forward(sqrt(2 * 50 ** 2))
        left(135)
        forward(50)
        left(135)
        forward(sqrt(2 * 50 ** 2))
        left(135)
        forward(50)
        left(45)
        forward(0.5*(sqrt(2 * 50 ** 2)))
        left(90)
        forward(0.5*(sqrt(2 * 50 ** 2)))
        left(45)
        forward(50)
        left(90)
        forward(50)
    
        if a == 0:
            penup()
            forward(10)
            left(90)
            forward(50)
            right(90)
            pendown()
        
        else: 
            penup()
            forward(10)
            right(90)
            forward(50)
            left(90)
            pendown()

# presun nad domky

penup()

for a in range (2):    
    left(90)
    forward(250)

pendown()

# slunicko

for a in range (12):
    right(90)
    forward(30)
    left(180)
    forward(30)
    right(90)
    for a in range (10):
        left(180-(180*(1-2/120)))
        forward(200/120)

# presun nad domky

penup()

forward(250)
left(90)
forward(100)
left(180)

pendown()

# ptaci

for a in range (60):
    right(180-(180*(1-2/120)))
    forward(100/120)
left(180)
for a in range (60):
    right(180-(180*(1-2/120)))
    forward(100/120)
        
penup()

for a in range (2):
    left(90)
    forward(40)

pendown()

for a in range (60):
    right(180-(180*(1-2/120)))
    forward(100/120)
left(180)
for a in range (60):
    right(180-(180*(1-2/120)))
    forward(100/120)

penup()

left(180)
forward(40)
left(90)
forward(110)
right(90)

pendown()

for a in range (60):
    right(180-(180*(1-2/120)))
    forward(100/120)
left(180)
for a in range (60):
    right(180-(180*(1-2/120)))
    forward(100/120)

penup()

right(90)
forward(250)
left(90)
forward(250)
left(90)
  
exitonclick()
