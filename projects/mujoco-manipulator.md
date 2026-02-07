---
layout: default
title: MuJoCo-Based Robotic Manipulator Simulation
---

# MuJoCo-Based Robotic Manipulator Simulation (UR10e)

## Overview
This project focuses on building a physics-based simulation of a 6-DOF industrial robotic manipulator (UR10e) in MuJoCo to study controller behavior, system dynamics, and stability under different control strategies. The goal was to evaluate control performance in simulation and build intuition for simulation-to-real transfer.

---

## Problem Statement
Industrial manipulators operate under complex nonlinear dynamics, gravity effects, and actuator limits. Before deploying control strategies on real hardware, it is critical to understand how controllers behave in a physically accurate simulation environment. This project explores joint-space control strategies and evaluates their stability, responsiveness, and robustness through simulation rollouts.

---

## System Architecture
**Manipulator:** UR10e (6-DOF)  
**Simulation Engine:** MuJoCo  
**Control Mode:** Joint-space torque and velocity control  
**Compute:** Python-based simulation loop  

**High-level flow:**
1. Desired joint targets provided to controller
2. Control torques computed using feedback laws
3. MuJoCo physics engine simulates dynamics
4. Joint states logged and analyzed over time

*(A system block diagram is provided below.)*

---

## Control Strategy
Two baseline controllers were implemented and evaluated:

### 1. Joint-Space PD Torque Control
- Proportional and derivative feedback on joint position and velocity
- Gravity and passive forces compensated using MuJoCo inverse dynamics (`mj_inverse`)
- Used as a baseline for stability and convergence behavior

### 2. Velocity Control
- Direct velocity commands to joints
- Evaluated for responsiveness and smoothness
- Compared against torque-based control for tracking accuracy

These controllers provided a reference point for evaluating stability, transient response, and sensitivity to disturbances.

---

## Simulation and Rollout Evaluation
Simulation rollouts were performed to evaluate:
- Joint tracking accuracy
- Convergence time
- Stability under different gain values
- Effects of gravity compensation

Joint trajectories, velocities, and control torques were logged and analyzed to understand system behavior over time.

---

## Key Results
- Gravity compensation significantly improved tracking performance and reduced steady-state error
- Torque-based control provided smoother and more stable convergence than velocity-only control
- Improper gain selection led to oscillations, highlighting the importance of tuning and physical realism in simulation

---

## Lessons Learned
- Physically accurate simulation is essential for understanding controller behavior before real-world deployment
- Gravity and passive forces cannot be ignored in manipulator control
- Simulation rollouts are an effective tool for identifying instability and tuning control gains
- MuJoCo provides valuable insight into real-world dynamics when used carefully

---

## Tools and Technologies
- MuJoCo
- Python
- Control Theory
- Numerical Simulation
- Data Logging and Analysis

---

## Future Work
- Extend to Cartesian-space control
- Introduce external disturbances and contact interactions
- Compare classical controllers against learning-based policies
- Validate simulation results against real manipulator hardware
