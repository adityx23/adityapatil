---
layout: default
title: SLAM-Based Autonomous Navigation Robot
---

# SLAM-Based Autonomous Navigation Robot

## Overview
Designed and integrated a ROS2-based autonomous mobile robot capable of indoor mapping and navigation using LiDAR and IMU sensor fusion. The project covered full-stack development: mechanical design, embedded motor control, sensor integration, simulation validation, and autonomy pipeline implementation.

**Key Contributions**
- Built complete ROS2 autonomy stack: SLAM → localization → planning → motor execution
- Integrated LiDAR, IMU, encoder feedback, and motor control across Raspberry Pi and ESP32
- Designed custom TurtleBot3-inspired chassis adapted to non-proprietary hardware
- Validated full navigation pipeline in Gazebo before hardware integration

---

## System Architecture

<p align="center">
  <img src="{{ site.baseurl }}/assets/slam/slam_system_architecture.png" alt="SLAM System Architecture" width="850">
</p>
<p align="center">
  <em>ROS2 autonomy stack running on Raspberry Pi with deterministic motor control offloaded to ESP32.</em>
</p>

**Data Flow**
- `/scan` (LiDAR) and `/imu/data` (IMU) provide sensor input
- Cartographer generates map and pose estimate
- `robot_localization` fuses IMU and encoder odometry
- Nav2 computes velocity commands (`/cmd_vel`)
- ESP32 executes closed-loop motor control
- Encoder feedback generates odometry (`/odom`)

Simulation in Gazebo was used to validate this pipeline prior to deployment.

---

## Hardware Platform

**Compute & Control**
- Raspberry Pi 4B (Ubuntu 22.04, ROS2)
- ESP32 dedicated motor controller

**Sensors**
- YDLiDAR X2 (360° 2D LiDAR)
- BNO055 IMU

**Actuation**
- 2 × 500 RPM encoder DC motors
- Cytron MD10C motor drivers

**Mechanical Design**
- Custom 3D-printed chassis inspired by TurtleBot3 Waffle
- Redesigned geometry to fit available components
- Modular mounting for serviceability and sensor alignment

---

## Software Stack

**Core Autonomy**
- ROS2 middleware
- Nav2 navigation stack
- Google Cartographer SLAM
- `robot_localization` EKF state estimator

**Simulation**
- Gazebo using TurtleBot3 simulation environment

**Integration**
- YDLiDAR SDK integrated into ROS2
- BNO055 ROS2 driver integration
- Custom ESP32 firmware for motor control and encoder feedback

**Autonomous Behavior**
- Frontier exploration for autonomous map coverage

---

## Engineering Challenges and Solutions

**Compute limitations (Raspberry Pi 4B)**
- Full autonomy stack pushed CPU limits
- Solution: separated low-level control to ESP32 and optimized node execution

**Sensor driver compatibility (ROS2 + Ubuntu 22.04)**
- LiDAR and IMU drivers required rebuilding and API adaptation
- Resolved dependency and SDK compatibility issues

**Localization architecture selection**
- Evaluated AMCL vs `robot_localization`
- Selected `robot_localization` for IMU-integrated state estimation
- Allowed LiDAR to focus on mapping rather than pose correction

**Mechanical design constraints**
- TurtleBot3 hardware unavailable
- Redesigned chassis plates to accommodate available motors, drivers, and compute

**Frontier exploration integration**
- Implemented goal selection and frontier detection logic
- Tuned exploration behavior to avoid redundant navigation

---

## Simulation and Validation Strategy

Followed staged integration approach:

1. Validate individual sensor drivers
2. Verify TF tree and coordinate consistency (`map → odom → base_link`)
3. Validate SLAM and localization in simulation
4. Integrate Nav2 navigation stack
5. Test autonomous exploration behavior

Simulation-first validation significantly reduced hardware debugging time.

---

## Results

- Successfully deployed full autonomy stack capable of mapping and navigation
- Achieved stable SLAM and localization behavior in simulation
- Demonstrated autonomous frontier-based exploration
- Established reproducible architecture for simulation-to-hardware transfer

---

## Technical Stack

- ROS2, Nav2, Cartographer, robot_localization
- Gazebo simulation
- Raspberry Pi 4B, ESP32
- YDLiDAR X2, BNO055 IMU
- Embedded motor control with encoder feedback
- Custom 3D-printed robot chassis

---

## Future Improvements

- Quantitative evaluation of localization accuracy and drift
- Improved exploration efficiency and recovery behaviors
- Sensor time synchronization and calibration improvements
- Extension to multi-robot mapping or manipulation tasks
