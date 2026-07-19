import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
mu = 0.0121545352
def cr3bp(t, r):
    x, y, vx, vy = r
# Distances to the two primaries
    r1 = np.sqrt((x + mu)**2 + y**2)
    r2 = np.sqrt((x - 1 + mu)**2 + y**2)
# Equations of motion
    dvxdt = (2*vy
             + x
             - (1-mu)*(x+mu)/r1**3
             - mu*(x-1+mu)/r2**3)
    
    dvydt = (-2*vx
             + y
             - (1-mu)*y/r1**3
             - mu*y/r2**3)
    
    return [vx, vy, dvxdt, dvydt]
# Simulation function
def simulation(x0, y0, vx0=0.0, vy0=0.22):
    y_initial = [x0, y0, vx0, vy0]
    t_span=(0,50)
    t_ev = np.linspace(0,50, 15000)
# Solve ODEs
    sol=solve_ivp(cr3bp,t_span,y_initial,t_eval=t_ev, rtol=1e-9, atol=1e-12)  
    return sol.t, sol.y  # time array and [x,y,vx,vy] arrays
if __name__ == "__main__":
    # User input
    x0 = float(input("Enter initial x: "))
    y0 = float(input("Enter initial y: "))
    t, states = simulation(x0, y0)
# Plot trajectory
    plt.figure(figsize=(6,6))
    plt.plot(states[0], states[1], label="Trajectory")
    plt.scatter([-0.0121505856, 1-0.0121505856], [0,0], c='red', marker='o', label="Primaries")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.axis("equal")
    plt.title("CR3BP Trajectory")
    plt.grid(True)
    plt.show()

