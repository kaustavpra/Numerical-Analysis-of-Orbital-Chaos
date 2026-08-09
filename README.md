# Numerical Analysis of Orbital Chaos: Simulating the Restricted Three-Body Problem

**Category:** 1 - Undergraduate (UG)  
**Theme:** Foundations of Computational Physics  
**Event:** National Competition in Computational Physics (NCICP-2026)  

## Project Overview
This repository contains the computational simulation and numerical analysis for the Circular Restricted Three-Body Problem (CR3BP). Unlike the classical two-body problem, the CR3BP lacks a general analytical solution and exhibits highly non-linear, chaotic dynamics. 

Using Python, this project mathematically models the trajectory of a massless third body (e.g., a satellite) under the gravitational influence of two massive primary bodies orbiting their common barycenter. The equations of motion are solved in a rotating synodic reference frame using advanced numerical integration methods (Runge-Kutta RK45) to map regions of orbital stability and chaos near the Lagrange points.

## Key Features
* **Custom Integration Functions:** Mathematical functions are built from scratch to cleanly separate the physical equations from the integration processes.
* **Phase-Space Mapping:** Generates 2D phase-space trajectories to visually distinguish periodic orbits from chaotic escape trajectories.
* **Poincaré section:** Generate 2D Poincaré sections graph to analyse system stability, periodicity, chaos. 
* **Real-time Animation:** Utilizes Pygame to render the orbital dynamics dynamically.

## Repository Structure
* `01_Lagrange_point.py` - Contains script to run and find the initial lagrange point for the simulations.
* `02-CR3BP_code.py` - Contains the custom ODE formulations, mathematical solvers and execution script to run the simulations.
* `03_Animation_code.py` - Handles the generation of Pygame animations.
* `/Output/` - Contains phase-space plots, Poincaré sections, and video animations.

## Installation & Usage
1. Clone this repository to your local machine.
2. Install the required scientific libraries using the provided requirements file:
   `pip install -r requirements.txt`
3. Execute `03_Animation_code.py` to initiate the simulation and generate the plots.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
