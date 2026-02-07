---
layout: default
title: SLAM-Based Autonomous Navigation Robot
---

# SLAM-Based Autonomous Navigation Robot

## Overview
This project involved designing and integrating a mobile robot platform capable of autonomous indoor mapping and navigation. The focus was on full-system development: mechanical design, embedded motor control, sensor integration, simulation-based validation, and ROS2-based autonomy.

A strong emphasis was placed on simulation-to-hardware transfer, using the TurtleBot3 software ecosystem to validate navigation and SLAM behavior before deployment.

---

## Hardware Platform

**Compute & Control**
- Raspberry Pi 4B (Ubuntu 22.04, ROS2)
- ESP32 as a dedicated motor controller

**Sensors**
- YDLiDAR X2 (360° 2D LiDAR)
- BNO055 IMU (orientation & angular velocity)

**Actuation**
- 2 × 500 RPM DC encoder motors
- 2 × Cytron MD10C motor drivers

**Mechanical Design**
- Custom chassis using 3D-printed plates inspired by TurtleBot3 Waffle geometry
- Plates designed for modular mounting of compute, sensors, and motor drivers
- Components mounted using standoffs and fasteners for serviceability and stability

---

## Software Stack

**Operating System & Middleware**
- Ubuntu 22.04
- ROS2

**Simulation**
- Gazebo
- TurtleBot3 simulation environment

**Navigation & Localization**
- Nav2 for path planning and navigation
- `robot_localization` for sensor fusion
- Google Cartographer (via TurtleBot3 SLAM stack) for mapping

**Autonomy**
- Basic frontier exploration algorithm for autonomous mapping

**Drivers & Integration**
- YDLiDAR SDK integrated into ROS2
- Adafruit BNO055 drivers
- Custom ESP32 firmware for motor control and encoder feedback

---

## System Architecture (High-Level)

1. LiDAR and IMU publish sensor data to ROS2 topics on the Raspberry Pi
2. SLAM generates a map and estimates robot pose
3. `robot_localization` fuses IMU and odometry
4. Nav2 computes velocity commands
5. ESP32 receives commands and executes closed-loop motor control
6. Encoder feedback is used for odometry and debugging

Simulation was used extensively to validate this pipeline before hardware integration.

---

## Key Technical Contributions

### Mechanical & Hardware Integration
- Designed and fabricated a custom mobile robot chassis using 3D-printed plates
- Integrated motors, drivers, compute, and sensors into a compact, modular platform
- Routed power and communication interfaces for robustness and ease of debugging

### Embedded Motor Control
- Implemented motor control on ESP32 using encoder feedback
- Separated high-level planning (Raspberry Pi) from low-level actuation (ESP32)
- Enabled clean abstraction between autonomy and hardware execution

### Simulation-Based Validation
- Used TurtleBot3 Gazebo simulation to validate SLAM and navigation behavior
- Tuned Nav2 and localization parameters in simulation
- Tested autonomous frontier exploration to validate map coverage and navigation logic

### SLAM & Navigation
- Configured Cartographer-based SLAM for indoor mapping
- Integrated LiDAR and IMU data into localization pipeline
- Debugged common issues including transform consistency, update rates, and command latency

---

## Results (Qualitative)
- Achieved stable mapping and navigation behavior in simulation
- Successfully integrated hardware components into a deployable platform
- Demonstrated autonomous exploration using frontier-based mapping strategies
- Established a repeatable workflow for simulation-first validation of autonomy systems

---

## Lessons Learned
- Simulation is critical for reducing integration risk in mobile robotics
- Clear separation between autonomy, localization, and motor control simplifies debugging
- SLAM performance is highly sensitive to timing, frames, and sensor integration quality
- Mechanical design decisions directly affect sensing stability and navigation reliability

---

## Tools & Technologies
- ROS2, Nav2
- Gazebo simulation
- Google Cartographer
- `robot_localization`
- Raspberry Pi 4B, ESP32
- YDLiDAR X2, BNO055
- Embedded motor control with encoders
- 3D printing for robotic chassis design

---

## Future Improvements
- Extended real-world testing and benchmarking
- Improved sensor calibration and synchronization
- More advanced exploration and recovery behaviors
- Formal evaluation of localization drift and navigation accuracy
