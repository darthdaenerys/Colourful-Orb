# import modules and libraries
from vpython import *
import time
import numpy as np

# vpython canvas
canvas(width=1320,height=680)

# parameters
red=0
green=0
blue=0
deltared=0.002
deltagreen=0.006
deltablue=0.014
orb_radius=2
cylinderlength=3
base_length=1
outer_cylinder_radius=0.35
inner_cylinder_radius=0.3

# create the orb
orb=sphere(radius=orb_radius,color=vector(red,green,blue),pos=vector(1.5,0,0),shininess=0.8)

# create display parameters
redcylinder=cylinder(
    pos=vector(-4*base_length,-cylinderlength/2,0),
    length=cylinderlength,
    axis=vector(0,1,0),
    color=color.red,
    radius=inner_cylinder_radius
)
greencylinder=cylinder(
    pos=vector(-3*base_length,-cylinderlength/2,0),
    length=cylinderlength,
    axis=vector(0,1,0),
    color=color.green,
    radius=inner_cylinder_radius
)
bluecylinder=cylinder(
    pos=vector(-2*base_length,-cylinderlength/2,0),
    length=cylinderlength,
    axis=vector(0,1,0),
    color=color.blue,
    radius=inner_cylinder_radius
)

attach_light(redcylinder)
attach_light(greencylinder)
attach_light(bluecylinder)
attach_light(orb)

cylinder(
    pos=vector(-4*base_length,-cylinderlength/2,0),
    length=cylinderlength,
    axis=vector(0,1,0),
    opacity=.3,
    radius=outer_cylinder_radius
)
cylinder(
    pos=vector(-3*base_length,-cylinderlength/2,0),
    length=cylinderlength,
    axis=vector(0,1,0),
    opacity=.3,
    radius=outer_cylinder_radius
)
cylinder(
    pos=vector(-2*base_length,-cylinderlength/2,0),
    length=cylinderlength,
    axis=vector(0,1,0),
    opacity=.3,
    radius=outer_cylinder_radius
)

redlabel=label(
    pos=vector(-4*base_length,-cylinderlength/2,0),
    color=color.red,
    text='Red\n'+str(int(red*255)),
    font='serif',
    border=10
)
greenlabel=label(
    pos=vector(-3*base_length,-cylinderlength/2,0),
    color=color.green,
    text='Green\n'+str(int(green*255)),
    font='serif',
    border=10
)
bluelabel=label(
    pos=vector(-2*base_length,-cylinderlength/2,0),
    color=color.blue,
    text='Blue\n'+str(int(blue*255)),
    font='serif',
    border=10
)

while True:
    rate(30)

    # check the upper and lower bound conditions
    if red+deltared>=1 or red+deltared<=0:
        deltared=-deltared
    if green+deltagreen>=1 or green+deltagreen<=0:
        deltagreen=-deltagreen
    if blue+deltablue>=1 or blue+deltablue<=0:
        deltablue=-deltablue
    
    # increment r,g,b values
    red+=deltared
    green+=deltagreen
    blue+=deltablue

    # reflecting the changes in the animation
    orb.color=vector(red,green,blue)
    redcylinder.length=3*red
    greencylinder.length=3*green
    bluecylinder.length=3*blue

    redlabel.text='Red\n'+str(int(red*255))
    greenlabel.text='Green\n'+str(int(green*255))
    bluelabel.text='Blue\n'+str(int(blue*255))