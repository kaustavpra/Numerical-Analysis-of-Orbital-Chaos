import numpy as np
from scipy.optimize import fsolve

miu = 0.01215453528917472227184607343007 # miu = m2/(m1+m2) [Here Earth-moon system]

def collinear_acc(x , miu):
    r1 = np.abs(x + miu)  #Distance from 3rd body to earth
    r2 = np.abs(x + miu - 1) #..to moon
    return x - ((1 - miu) * (x + miu) / r1**3) - (miu * (x - 1 + miu) / r2**3)  #the equation of motion corresponding to x

def lagrange(miu):
    v = (7/12)*miu
    b = v*(1 + ((23/84)*v**2))
    a = (miu / 3*(1 - miu))**(1/3)
    
    guess_L1 = (1 - miu) - (a * (1 - (a/3) - (a**2/9)))
    guess_L2 = (1 - miu) + (a * (1 + (a/3) - (a**2/9)))
    guess_L3 = - miu - b - 1
    
    L1 = fsolve(collinear_acc, guess_L1, args=(miu))
    L2 = fsolve(collinear_acc, guess_L2, args=(miu))
    L3 = fsolve(collinear_acc, guess_L3, args=(miu))
    
    L4_x, L4_y = 0.5 - miu, np.sqrt(3)/2
    L5_x, L5_y = 0.5 - miu, -np.sqrt(3)/2
    return {
        "L1": [L1[0], 0.0],
        "L2": [L2[0], 0.0],
        "L3": [L3[0], 0.0],
        "L4": [L4_x, L4_y],
        "L5": [L5_x, L5_y]
    }

def main():
    points = lagrange(miu)
    print("The Lagrange Points are :")
    print("--"*26)
    for name, point in points.items():
        print(f"{name}: X = {point[0]:.16f}, Y = {point[1]:.16f}")
    return points

if __name__ == "__main__":
    main()
