#https://github.com/ClementOsei-Agyeman/Data-structures
import numpy as np
L = 12
w = 10

#Question a
# first we calculate for the bending moment at first end,x=0
x = 0
M = (w*(-6*x**2 + 6*L*x-L**2))/12
V = w*(L/2-x)
print()
m = " The bending moment at x=0 is"
s = " The shear force at x=0 is"
print()
print(('[solution a(i)]:' + m + " " + str(M)+"kNm" + " " + 'and' + s + " " + str(V) +'kNm' ))
#Bending moment and shear force when x=L
x = L
M = (w*(-6*x**2 + 6*L*x-L**2))/12
V = w*(L/2-x)
m2 = " The bending moment at x=L is "
s2 = " The shear force at x=L is "
print()
print(('[solution a(ii)]:' + m2 + " " + str(M)+"kNm" + " " + 'and' + s2 + " " + str(V)+"kNm" ))
print()
#Question b
'''
when the bending moment is zero, we get an expression x**2 - Lx + L**2/6 = 0
'''
# based on the expression above,
a = 1
b= -L
c= L**2/6
# using the discriminant formula and applying the almighty formula, we have
discriminant = b**2 - 4*a*c
x1 = (-b + np.sqrt(discriminant))/2*a
x2 = (-b - np.sqrt(discriminant))/2*a
print('[solution b]:' +' The distance at which the Bending Moment will be zero is {} and {}'.format(x1,x2))
print()

#Question c
# The shear force will be zero at L/2
X = L/2
print("[solution c]:" + " The point at which the shear force will be 0 is {}".format(X))

#Question d
# 10mm is equal to 0.01m steps, whcih will be used in the solution below
steps_span = np.arange(0, L + 0.01, 0.01)
M = w*(-6*steps_span**2 + 6*L*steps_span - L**2)/12
print()
print("[solution d]:" + " Bending moment at each step of the array is {}".format(M))
print()
#Questions e
Shear_Force_each_step = w*(L/2 - steps_span)

print("[solution e]:" +" Shear Force at each step:",Shear_Force_each_step,"in kN")


#Question f
"""
Take absolute value of the bending moment array be AbM
Also let the minimum AM be m_AM
"""
AbM = abs(M)
m_AbM = min(AbM)
""" 
When the bending moment is m_AbM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AbM)/w = 0
"""
#from the above expression 
a = 1
b = -L
c = (L**2/6)+(2*m_AbM)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
x1_f = (-b + np.sqrt(discriminant))/2*a
x2_f = (-b - np.sqrt(discriminant))/2*a
print()
print('[solution f]:' + ' The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(x1_f,x2_f))
#Question g
"""
Let the relative errors be r_e
"""
r_e1 = ((x1 - x1_f)/x1*100) 
r_e2 = ((x2_f - x2)/x2_f*100)
print()
print('[solution g]:' + ' The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(r_e1,r_e2))
#Question h
"""
Let the maximum bending moment be max_M and the minimum bending moment be min_M
"""
#for the maximum
max_M = max(M)
""" 
When the bending moment is max_M, we get an expression x**2 - Lx + (L**2/6)+(2*max_M)/w = 0
"""
# therefore a,b and from the quadratic formula as follows,
a = 1
b = -L
c = (L**2/6)+(2*max_M)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
x1_h = (-b + np.sqrt(discriminant))/2*a
x2_h = (-b - np.sqrt(discriminant))/2*a
print()
print('[solution h.1]:' + ' The points at which the maximum bending moment occur are:' + str(x1_h) + " " + "and" + " " + str(x2_h))
#for the minimum
min_M = min(M)
""" 
When the bending moment is min_M, we get an expression x**2 - Lx + (L**2//6)+(2*min_M)/w = 0
"""
a = 1
b = -L
c = (L**2//6)+(2*min_M)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
x1_1h = (-b - np.sqrt(discriminant))/2*a
x2_2h = (-b + np.sqrt(discriminant))/2*a
print()
print('[solution h.2]:' + ' The points at which the minimum bending moment occur are {0} and {1}'.format(x1_1h,x2_2h))
#https://github.com/ClementOsei-Agyeman/Data-structures

