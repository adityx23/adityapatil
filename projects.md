---
layout: default
---

# Projects

## 1) MuJoCo-Based Robotic Manipulator Simulation (UR10e)
Physics-based simulation of an industrial manipulator to study control behavior and system dynamics.

👉 [Read more](projects/mujoco-manipulator.md)


---

## 2) Closed-Loop Thermostat Control System (TMP117)https://github.com/adityx23/adityapatil/blob/main/projects.md
## Closed-Loop Temperature Control (Peltier + TMP117)

A closed-loop thermostat system for a 30×30×30 cm acrylic enclosure using 4× Peltier modules driven by PWM through an H-bridge. Designed a continuous-time compensator, discretized it using Tustin (500 ms loop), and implemented the resulting difference equation on an Arduino Mega. Sensor was suspended mid-air at the enclosure midpoint to reduce boundary bias.

**Highlights**
- Discrete-time controller with memory (non-PID), implemented as a difference equation at 500 ms sampling
- Stability and response validated via Bode and step-response analysis
- Hardware actuation via PWM + H-bridge, with saturation and anti-chatter logic

➡️ **Read more:** [Closed-Loop Temperature Control (Peltier + TMP117)](/projects/thermostat-closed-loop-control)


---

## 3) SLAM-Based Autonomous Navigation Robot
End-to-end mobile robot platform with ROS2-based SLAM, navigation, and system integration.

👉 [Read more](projects/slam-navigation-robot.md)

