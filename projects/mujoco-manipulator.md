---
layout: default
title: MuJoCo-Based Robotic Manipulator Simulation
---

# MuJoCo-Based Robotic Manipulator Simulation (UR10e)

## Overview
Developed a physics-based simulation of a 6-DOF UR10e manipulator in MuJoCo to study the behavior of joint-space vs task-space control and compare position vs velocity command interfaces.

**Key Contributions**
- Implemented FK and IK control pipelines using position and velocity command modes
- Analyzed stability, convergence, and motion smoothness across control configurations
- Visualized end-effector trajectories to evaluate controller behavior in task space

---

## System Architecture

**Platform**
- Robot: UR10e (6-DOF serial manipulator)
- Simulator: MuJoCo
- Implementation: Python control loop with real-time visualization

**Control Modes Evaluated**
- Joint-space control: Forward Kinematics (FK)
- Task-space control: Inverse Kinematics (IK)
- Command interfaces: position and velocity

This resulted in four tested configurations:
- FK Position
- FK Velocity
- IK Position
- IK Velocity

---

## Control Experiments

### FK — Position Control
Direct joint position commands propagated through the kinematic chain. Used to validate joint-level convergence and establish a stable baseline.

![FK Position Control](../assets/mujoco/ur10e_FK_position.gif)

---

### FK — Velocity Control
Joint velocity commands produced smoother motion and reduced abrupt transitions compared to position commands.

![FK Velocity Control](../assets/mujoco/ur10e_FK_velocity.gif)

---

### IK — Position Control
Task-space targets were mapped to joint configurations using inverse kinematics. Enabled intuitive Cartesian motion but required handling solver convergence and joint constraints.

![IK Position Control](../assets/mujoco/ur10e_IK_position.gif)

---

### IK — Velocity Control
End-effector velocity commands were mapped to joint velocities using Jacobian relationships, producing continuous and smooth Cartesian trajectories.

![IK Velocity Control](../assets/mujoco/ur10e_IK_velocity.gif)

---

## Engineering Observations

**Control behavior differences**
- FK control is stable and predictable, but less intuitive for task-space motion
- IK control enables direct Cartesian control but introduces numerical sensitivity

**Command interface impact**
- Velocity control produced smoother trajectories and reduced motion discontinuities
- Position commands resulted in faster convergence but more abrupt transitions

**Simulation advantages**
- Physics-based simulation exposed controller artifacts not visible in purely kinematic models
- Trajectory visualization enabled rapid debugging and validation of controller behavior

---

## Technical Stack
- MuJoCo physics engine
- Python simulation and control loop
- Forward and Inverse Kinematics
- Jacobian-based velocity control
- Real-time trajectory visualization

---

## Extensions and Future Work
- Implement torque-based control using MuJoCo inverse dynamics
- Benchmark tracking accuracy and convergence quantitatively
- Extend to manipulation tasks involving object interaction
- Compare controller performance under dynamic loading conditions
