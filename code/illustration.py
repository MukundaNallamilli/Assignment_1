import numpy as np
import matplotlib.pyplot as plt


#area of circle 
def arcir(r):
#r is the radius
   return np.pi*r*r

#area of rectangle
def arrec(l,b):
    return l*b
print("")
print("area of the requires region = area of rectangle - area of semcircle-area of quatercircle")
area_of_rectangle = arrec(14,7)
area_of_semcircle = 0.5*arcir(7/2)
area_of_quatercircle = 0.25*arcir(7)
area_of_the_required_region = (area_of_rectangle) - (area_of_semcircle) -(area_of_quatercircle)
print(f"required area = {area_of_rectangle}-{area_of_semcircle}-{area_of_quatercircle} = {area_of_the_required_region}")



x1 = np.linspace(0,14,num=25)
y1 = np.linspace(0,0,num=25)
y2 = np.linspace(7,7,num=25)
x2 = np.linspace(0,0,num=25)
x3 = np.linspace(14,14,num=25)
y3 = np.linspace(0,7,num = 25)
def circle(x,cx,cy,r):
    return cy + np.sqrt((r**2)-((cx-x)**2))
xpoints1 = np.linspace(0,7,num = 25)
ypoints1 = circle(xpoints1,7/2,0,7/2)
xpoints2 = np.linspace(7,14,num= 25)
ypoints2 = circle(xpoints2,14,0,7)
plt.figure(num= 0,dpi=90)
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.plot(x2,y3)
plt.plot(x3,y3)
plt.plot(xpoints1,ypoints1)
plt.plot(xpoints2,ypoints2)
plt.title("diagram")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

