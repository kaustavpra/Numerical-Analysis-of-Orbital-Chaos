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
    t_span = (0, 200)   # longer integration for more crossings
    t_ev = np.linspace(0, 200, 50000)
    sol = solve_ivp(cr3bp, t_span, y_initial, t_eval=t_ev, rtol=1e-9, atol=1e-12)  
    return sol.t, sol.y

# Function to compute Poincaré section (y=0 crossings with vy>0)
def poincare_section(states):
    x, y, vx, vy = states
    crossings_x = []
    crossings_vx = []
    for i in range(len(y)-1):
        if y[i] < 0 and y[i+1] > 0:   # crossing upward through y=0
            # Linear interpolation for better accuracy
            alpha = -y[i] / (y[i+1] - y[i])
            x_cross = x[i] + alpha * (x[i+1] - x[i])
            vx_cross = vx[i] + alpha * (vx[i+1] - vx[i])
            crossings_x.append(x_cross)
            crossings_vx.append(vx_cross)
    return crossings_x, crossings_vx

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

    # Phase space plots
    plt.figure(figsize=(6,6))
    plt.plot(states[0], states[2], color="blue", lw=0.5)
    plt.xlabel("x")
    plt.ylabel("vx")
    plt.title("Phase Space Plot (x vs vx)")
    plt.grid(True)

    plt.figure(figsize=(6,6))
    plt.plot(states[1], states[3], color="green", lw=0.5)
    plt.xlabel("y")
    plt.ylabel("vy")
    plt.title("Phase Space Plot (y vs vy)")
    plt.grid(True)

    # Poincaré section
    px, pvx = poincare_section(states)
    plt.figure(figsize=(6,6))
    plt.scatter(px, pvx, s=5, c="purple")
    plt.xlabel("x")
    plt.ylabel("vx")
    plt.title("Poincaré Section (y=0, vy>0)")
    plt.grid(True)
    plt.show()

