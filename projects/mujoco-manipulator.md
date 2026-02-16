---
layout: default
title: MuJoCo-Based Robotic Manipulator Simulation
---

# MuJoCo-Based Robotic Manipulator Simulation (UR10e)

## Overview
Developed a physics-based simulation of a 6-DOF UR10e manipulator in MuJoCo to compare **joint-space vs task-space control** and evaluate how **position vs velocity command interfaces** affect stability, convergence, and motion smoothness.

**Key contributions**
- Implemented FK and IK control pipelines under both position and velocity command modes  
- Evaluated controller behavior through convergence and trajectory smoothness comparisons  
- Visualized end-effector motion in Cartesian space for debugging and qualitative validation  

---

## Simulation Environment
**Platform**
- **Robot:** UR10e (6-DOF serial manipulator)  
- **Simulator:** MuJoCo  
- **Implementation:** Python-based control loop with real-time visualization  

**Control formulations and interfaces**
- **Joint-space control:** Forward Kinematics (FK)  
- **Task-space control:** Inverse Kinematics (IK)  
- **Command interfaces:** Position commands and velocity commands  

This produced four evaluated configurations:
- FK Position  
- FK Velocity  
- IK Position  
- IK Velocity  

---

## Control Implementation
### Forward Kinematics (FK)
Joint-space targets are issued directly and propagated through the manipulator’s kinematic chain. FK modes were used as a stable baseline for validating joint-level convergence and motion behavior.

### Inverse Kinematics (IK)
Cartesian targets (or Cartesian velocities) are mapped to joint commands using inverse kinematics / Jacobian relationships. IK modes enable intuitive task-space control but introduce numerical sensitivity and constraint-handling considerations.

### Position vs Velocity Interfaces
- **Position commands:** faster convergence but more abrupt transitions  
- **Velocity commands:** smoother trajectories and more continuous motion behavior  

---

## Control Experiments and Results

### FK — Position Control
Direct joint position commands used to validate joint-level convergence and establish a baseline behavior.

![FK Position Control](../assets/mujoco/ur10e_FK_position.gif)

---

### FK — Velocity Control
Joint velocity commands produced smoother transitions and reduced abrupt motion compared to position-based control.

![FK Velocity Control](../assets/mujoco/ur10e_FK_velocity.gif)

---

### IK — Position Control
Task-space goals mapped to joint configurations via inverse kinematics. Enabled intuitive Cartesian targeting while requiring solver convergence and constraint awareness.

![IK Position Control](../assets/mujoco/ur10e_IK_position.gif)

---

### IK — Velocity Control
End-effector velocity commands mapped to joint velocities using Jacobian relationships, producing continuous and smooth Cartesian trajectories.

![IK Velocity Control](../assets/mujoco/ur10e_IK_velocity.gif)

---

## Engineering Insights

**Joint-space vs task-space control**
- FK control is stable and predictable, but less intuitive for task-space behavior  
- IK control enables direct Cartesian motion but is more sensitive to numerical and constraint effects  

**Position vs velocity interfaces**
- Velocity control yielded smoother motion and reduced discontinuities  
- Position control converged faster but introduced sharper transitions  

**Why simulation mattered**
- Physics-based MuJoCo simulation revealed motion artifacts not visible in purely kinematic testing  
- End-effector trajectory visualization significantly accelerated debugging and validation  

---

## Technical Stack
- **Simulation:** MuJoCo  
- **Programming:** Python  
- **Robotics:** Forward/Inverse Kinematics, Jacobian-based velocity control  
- **Validation:** Real-time end-effector trajectory visualization  

---

## Future Improvements
- Add torque-based control using MuJoCo inverse dynamics and compare against position/velocity command modes  
- Quantitatively benchmark tracking error and convergence (across multiple trajectories)  
- Extend to contact-rich manipulation (object interaction, grasping, collision constraints)  
- Evaluate controller behavior under dynamic loading and constraint variation  
