import turtle

def convert_height():
    height=int(input('Enter Your Height In Inches :'))
    heightfeet=int(height / 12) 
    heightinch=int(height - (heightfeet*12))
    print('You are', heightfeet,"'", heightinch,"''", 'tall')

#convert_height()

def convert_distance(kilo):
    distance=int(kilo*39370.1)
    mile=int(distance/63360)
    feet=int((distance-(mile*63360))/12)
    inch=int(distance-((mile*63360)+(feet*12)))
    print(kilo,'kilometers is', mile, 'miles',",", feet, 'feet',",", inch, 'inches')

def snow_man(x, y, radius):
    turtle.bgcolor('cyan') 
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color('black')
    turtle.goto(x,y)
    turtle.circle(radius)
    turtle.goto(x, y*1.75)
    turtle.circle(radius*.75) 
    turtle.goto(x,y*1.75*1.75)
    turtle.circle(radius*(.75*.75)

def main():
    snow_man(0,0,100)

main()