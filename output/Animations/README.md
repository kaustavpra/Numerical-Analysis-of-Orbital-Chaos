## Supplementary Video Animations

The animations in this repository were generated using Pygame to visualize the real-time, non-linear dynamics of the Circular Restricted Three-Body Problem (CR3BP). Below are descriptions of the key orbital behaviors captured in the `Output/Animations/` directory.

### 1. Chaotic Trajectory (Near Collinear Lagrange Points L1 / L2 / L3)
* **File:** `Lagrange_point_1.mp4` 
* **Initial Setup:** The massless third body is introduced with a slight perturbation near one of the collinear Lagrange points along the x-axis.
* **Observed Dynamics:** The video demonstrates extreme sensitivity to initial conditions. The trajectory rapidly diverges from the equilibrium point, resulting in unpredictable, macroscopic loops. The body is shown erratically transitioning between the gravitational wells of the two primary masses.
* **Conclusion:** This animation visually validates the theoretical instability of the collinear Lagrange points. It highlights the chaotic nature of the CR3BP, where bounded periodic orbits cannot be maintained without active station-keeping maneuvers.

### 2. Stable Orbit (Near Triangular Lagrange Points L4 / L5)
* **File:** `Lagrange_point_4.mp4` 
* **Initial Setup:** The massless third body is placed near the L4 equilibrium point, which forms an equilateral triangle with the two primary masses.
* **Observed Dynamics:** Unlike the chaotic escape seen in the collinear points, the third body remains bounded within the region. The animation shows it executing a stable, periodic oscillatory motion (often resembling a tadpole or horseshoe orbit) in the rotating reference frame.
* **Conclusion:** This visualizes the localized stability regions within the CR3BP. It proves that despite the system lacking a general analytical solution, natural accumulation zones exist where celestial objects (like Trojan asteroids) can remain indefinitely trapped by the competing gravitational forces.

### 3. Quasi-Periodic Bounded Orbit (Deep Primary Well)
* **File:** `point_(0.4920000000000000 ,-0.0128571428571429)_zero_velocity .mp4`
* **Initial Setup:** Initialized deep within the gravitational well of the primary mass at X = 0.492, Y = -0.012857 with zero initial velocity (Vx = 0, Vy = 0) in the rotating frame.
* **Observed Dynamics:** The third body executes a highly structured, dense, rosette-like orbital pattern. It remains tightly bound to the central primary mass without ever crossing over to the secondary mass.
* **Conclusion:** This demonstrates that when a body is deep within the primary's Roche lobe with low energy, the gravitational pull of the secondary body acts merely as a slight perturbation. Instead of inducing chaos, this perturbation causes the orbit to precess smoothly, resulting in stable, quasi-periodic motion.

### 4. Chaotic Scattering and System Ejection
* **File:** `point_(0.9720000000000000, -0.1414285714285715).mp4`
* **Initial Setup:** Initialized in close proximity to the smaller secondary mass at X = 0.972, Y = -0.141428.
* **Observed Dynamics:** The trajectory begins with tight, chaotic loops around the secondary body. It then transits across the system to orbit the primary in a wide arc before eventually being violently ejected outward, escaping the binary system entirely.
* **Conclusion:** This animation highlights the extreme instability near the secondary mass. It perfectly visualizes the phenomenon of "chaotic scattering," where the third body continuously exchanges energy and momentum with the rotating system until it gains enough energy to break free of the gravitational bounds entirely.
