---
layout: default
---

# Projects

A curated selection of projects spanning **robot autonomy (SLAM + navigation)**, **simulation and control**, and **embedded feedback systems**.

---

## 1) SLAM-Based Autonomous Navigation Robot
End-to-end mobile robot platform built around **ROS2** with **SLAM, localization, navigation**, and **hardware/software integration**.

**Highlights**
- ROS2 autonomy stack: sensor drivers → SLAM → localization → Nav2
- IMU + LiDAR integration, odometry + state estimation, and autonomous frontier exploration
- Custom chassis plates modeled after TurtleBot3 Waffle (3D-printed + adapted to available hardware)

👉 **Read more:** [SLAM-Based Autonomous Navigation Robot]({{ site.baseurl }}/projects/slam-navigation-robot)

---

## 2) MuJoCo-Based Robotic Manipulator Simulation (UR10e)
Physics-based simulation of a 6-DOF industrial manipulator to study controller behavior, dynamics, and kinematics in simulation.

**Highlights**
- MuJoCo simulation pipeline with rendered rollouts for evaluation
- Joint-space control (position/velocity) with dynamics-aware implementation
- FK/IK-based end-effector motion and controller validation

👉 **Read more:** [MuJoCo-Based Robotic Manipulator Simulation (UR10e)]({{ site.baseurl }}/projects/mujoco-manipulator)

---

## 3) Closed-Loop Temperature Control (Peltier + TMP117)
Closed-loop thermostat system for a **30×30×30 cm acrylic enclosure** using **4× Peltier modules** driven by PWM through an H-bridge. Designed a continuous-time compensator, discretized it via **Tustin** at **500 ms**, and implemented the resulting difference equation on an Arduino Mega. The sensor was suspended **mid-air at the enclosure center** to reduce boundary bias.

**Highlights**
- Discrete-time controller with memory (**non-PID**) implemented as a difference equation at 500 ms sampling
- Stability + response validated via Bode and step response analysis
- PWM saturation + practical anti-chatter logic for real hardware constraints

👉 **Read more:** [Closed-Loop Temperature Control (Peltier + TMP117)]({{ site.baseurl }}/projects/thermostat-closed-loop-control)

---
