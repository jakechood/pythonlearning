'''Bring in the turtles'''
import turtle

'''Import Math'''
import math

'''Open an image screen'''
s = turtle.getscreen

'''Shorten "Turtle"'''
t = turtle.Turtle()

'''Pick up the pen'''
t.up()

'''Set starting position'''
t.goto(0, -60)

'''Put the pen to the paper'''
t.down()

'''Draw the right half of the bottom 
of the image frame'''
t.fd(60)

'''Turn the turtle North'''
t.lt(90)

'''Draw the right side of the image frame'''
t.fd(140)

'''Turn the turtle West'''
t.lt(90)

'''Draw the top of the image frame'''
t.fd(120)

'''Turn the turtle South'''
t.lt(90)

'''Draw the left side of the image frame'''
t.fd(140)

'''Turn the turtle East'''
t.lt(90)

'''Complete the bottom side of the image frame'''
t.fd(90)

'''Turn the turtle North'''
t.lt(90)

'''Hide the pointer'''
t.hideturtle()