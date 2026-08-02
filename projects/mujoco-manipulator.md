---
layout: default
title: MuJoCo-Based Robotic Manipulator Simulation
description: UR10e simulation comparing forward and inverse kinematics under position and velocity command interfaces.
---

# MuJoCo-Based Robotic Manipulator Simulation (UR10e)

<div class="project-summary">
  <div><strong>Role</strong><span>Simulation and controller implementation</span></div>
  <div><strong>Context</strong><span>Independent manipulation study</span></div>
  <div><strong>Platform</strong><span>MuJoCo · Python · UR10e</span></div>
  <div><strong>Outcome</strong><span>Four FK/IK command configurations compared</span></div>
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← All Projects</a>
</div>

## Overview
Developed a physics-based simulation of a 6-DOF UR10e manipulator in MuJoCo to compare **joint-space vs task-space control** and study how **position vs velocity command interfaces** affect stability, convergence, and trajectory smoothness.

**Key contributions**
- Implemented FK and IK control pipelines under both position and velocity command modes  
- Evaluated controller behavior via convergence and qualitative trajectory smoothness comparisons  
- Visualized end-effector motion in Cartesian space to validate and debug controller behavior  

---

## Simulation Environment
- **Robot model:** UR10e (6-DOF serial manipulator)  
- **Simulator:** MuJoCo  
- **Implementation:** Python control loop with real-time visualization  

**Control configurations evaluated**
- **FK Position**
- **FK Velocity**
- **IK Position**
- **IK Velocity**

---

## Control Implementation
### Forward Kinematics (FK)
Joint-space targets are issued directly and propagated through the kinematic chain. FK modes serve as a stable baseline for validating joint-level motion and convergence.

### Inverse Kinematics (IK)
Cartesian targets (or Cartesian velocities) are mapped to joint commands using inverse kinematics / Jacobian relationships. IK enables intuitive task-space behavior but introduces solver sensitivity and constraint considerations.

### Position vs Velocity Interfaces
- **Position commands:** faster convergence but more abrupt transitions  
- **Velocity commands:** smoother trajectories and more continuous motion behavior  

---

## Control Experiments and Results

### FK — Position Control
Direct joint position commands used to validate joint-level convergence and establish baseline behavior.

<video class="project-media" controls loop muted playsinline preload="metadata" poster="{{ site.baseurl }}/assets/mujoco/ur10e_FK_position-poster.jpg" aria-label="UR10e forward-kinematics position-control simulation">
  <source src="{{ site.baseurl }}/assets/mujoco/ur10e_FK_position.mp4" type="video/mp4">
</video>

---

### FK — Velocity Control
Joint velocity commands produced smoother transitions and reduced motion discontinuities compared to position control.

<video class="project-media" controls loop muted playsinline preload="metadata" poster="{{ site.baseurl }}/assets/mujoco/ur10e_FK_velocity-poster.jpg" aria-label="UR10e forward-kinematics velocity-control simulation">
  <source src="{{ site.baseurl }}/assets/mujoco/ur10e_FK_velocity.mp4" type="video/mp4">
</video>

---

### IK — Position Control
Task-space targets mapped to joint configurations using inverse kinematics. Enabled intuitive Cartesian targeting while requiring solver convergence and constraint awareness.

<video class="project-media" controls loop muted playsinline preload="metadata" poster="{{ site.baseurl }}/assets/mujoco/ur10e_IK_position-poster.jpg" aria-label="UR10e inverse-kinematics position-control simulation">
  <source src="{{ site.baseurl }}/assets/mujoco/ur10e_IK_position.mp4" type="video/mp4">
</video>

---

### IK — Velocity Control
End-effector velocity commands mapped to joint velocities using Jacobian relationships, producing smooth and continuous Cartesian trajectories.

<video class="project-media" controls loop muted playsinline preload="metadata" poster="{{ site.baseurl }}/assets/mujoco/ur10e_IK_velocity-poster.jpg" aria-label="UR10e inverse-kinematics velocity-control simulation">
  <source src="{{ site.baseurl }}/assets/mujoco/ur10e_IK_velocity.mp4" type="video/mp4">
</video>

---

## Engineering Insights
- FK control is stable and predictable, but less intuitive for task-space objectives  
- IK control enables direct Cartesian motion but is more sensitive to numerical effects and constraints  
- Velocity interfaces yielded smoother motion and reduced discontinuities vs position commands  
- Physics-based simulation helped surface motion artifacts not visible in purely kinematic testing  
- Trajectory visualization significantly accelerated debugging and qualitative validation  

---

## Technical Stack
- MuJoCo
- Python
- Forward and Inverse Kinematics
- Jacobian-based velocity control
- End-effector trajectory visualization

---

## Future Improvements
- Add torque-based control via MuJoCo inverse dynamics and compare against position/velocity interfaces  
- Quantitatively benchmark tracking error and convergence across trajectories  
- Extend to contact-rich manipulation tasks (object interaction)  
- Evaluate controller behavior under dynamic loading and constraint variation  
