---
layout: default
title: MuJoCo-Based Robotic Manipulator Simulation
---

# MuJoCo-Based Robotic Manipulator Simulation (UR10e)

## Overview
This project explores kinematic control behavior of a 6-DOF industrial robotic manipulator (UR10e) using MuJoCo. The goal was to study how forward and inverse kinematics-based control strategies behave in a physics-based simulation, and to analyze stability, convergence, and motion quality under position and velocity control modes.

The work focused on implementing and comparing four control configurations (FK/IK × position/velocity) and using visualization to understand end-effector motion in task space.

---

## System Setup
- **Robot:** UR10e (6-DOF serial manipulator)
- **Simulation Engine:** MuJoCo
- **Control Interfaces:** Joint-space position commands and joint-space velocity commands
- **Kinematic Modes:** Forward Kinematics (FK) and Inverse Kinematics (IK)
- **Implementation:** Python-based simulation loop with trajectory visualization

---

## Control Experiments and Simulation Results
Four control configurations were implemented and evaluated to study the behavior of the UR10e manipulator under different kinematic formulations and command interfaces.

---

### Forward Kinematics (FK) — Position Control
Joint positions are commanded directly, and the resulting end-effector motion is observed through the robot’s kinematic chain. This mode is useful for validating joint-level stability and convergence.

![FK Position Control](../assets/mujoco/ur10e_FK_position.gif)

---

### Forward Kinematics (FK) — Velocity Control
Joint velocities are commanded instead of absolute positions, resulting in smoother motion and improved dynamic behavior compared to position control.

![FK Velocity Control](../assets/mujoco/ur10e_FK_velocity.gif)

---

### Inverse Kinematics (IK) — Position Control
Desired end-effector positions are mapped to joint targets using inverse kinematics. This enables intuitive task-space motion but introduces sensitivity to solver stability and joint constraints.

![IK Position Control](../assets/mujoco/ur10e_IK_position.gif)

---

### Inverse Kinematics (IK) — Velocity Control
End-effector velocity commands are mapped to joint velocities (e.g., via Jacobian-based relationships), producing smooth task-space trajectories.  
The cyan line visualizes the end-effector path in Cartesian space.

![IK Velocity Control](../assets/mujoco/ur10e_IK_velocity.gif)

---

## Key Observations
- IK-based control enables intuitive end-effector motion but is more sensitive to solver behavior and joint constraints than FK control.
- Velocity control produced smoother motion profiles compared to direct position commands.
- FK control provided a stable baseline for validating joint-level behavior, while IK control better matched task-space objectives.
- Trajectory visualization was highly effective for debugging and verifying motion quality.

---

## Lessons Learned
- Separating joint-space vs task-space control logic is critical for debugging robotic systems.
- IK controllers require careful handling of numerical stability, constraints, and joint limits.
- Physics-based simulation can reveal motion artifacts that do not appear in purely kinematic models.
- Visualizing end-effector trajectories dramatically reduces iteration time during controller development.

---

## Tools \& Technologies
- MuJoCo
- Python
- Robot Kinematics (FK/IK)
- Velocity and Position Control Interfaces
- Trajectory Visualization

---

## Future Extensions
- Add torque-based control and compare against position/velocity command modes.
- Evaluate IK behavior under different constraints and solver configurations.
- Introduce contact interactions and object manipulation tasks.
- Benchmark tracking error and stability across multiple trajectories.
