# Exercise L2.E1

x=float(input('Enter angle 1: '))   # Input angles
y=float(input('Enter angle 2: '))
z=float(input('Enter angle 3: '))

if x+y+z==180:      # Check whether the given angles form a triangle
    if (x==0.0) or (y==0.0) or (z==0.0):    # Angles can't be zero
        print("Angle can't be a zero.")
    elif (x==90.0) or (y==90.0) or (z==90.0):   # Type of the triangle - Right angled
        print('Right angled')
    elif (x<90.0) and (y<90.0) and (z<90.0):    # Type of the triangle - Acute angled
        print('Acute angled')
    else:                                        # Type of the triangle - Obtuse angled
        print('Obtuse angled')
else:
    print('Angles do not form a triangle')
        
