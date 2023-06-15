from math import pi, tan, cos

# acceleration
g = 9.81
# initial velocity
v0 = 44
# theta
theta = 80 * pi/180
# horizontal distance travelled
x = 0.5
# height of barrel
y0 = 1

print(theta)

# first part of the sum
a = y0 + x*tan(theta)
print(a)
# top part of the division
b = g*x**2
print(b)
# bottom part of the division
c = (2*((v0 * cos(theta))**2))
print(c)
# full sum
y = (a - b / c)
print('Y =', y)
