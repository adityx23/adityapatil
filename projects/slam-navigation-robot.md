---
layout: default
title: SLAM-Based Autonomous Navigation Robot
---

# SLAM-Based Autonomous Navigation Robot

<div class="project-summary">
<strong>Type:</strong> Autonomous Mobile Robot (ROS2)<br>
<strong>Focus:</strong> SLAM, localization, navigation, sensor integration, embedded motor control<br>
<strong>Platform:</strong> ROS2, Nav2, Cartographer, robot_localization, Raspberry Pi 4B, ESP32<br>
<strong>Outcome:</strong> Integrated full autonomy pipeline and validated end-to-end behavior in Gazebo prior to hardware deployment
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← Back to Projects</a>
  <a class="btn" href="{{ site.baseurl }}/assets/slam/slam_system_architecture.png">System Architecture</a>
</div>

## Overview
Designed and integrated a ROS2-based autonomous mobile robot capable of indoor mapping and navigation using LiDAR and IMU sensor fusion. The project involved full-stack robotics development spanning mechanical design, embedded motor control, sensor integration, simulation validation, and autonomy pipeline implementation.

**Key contributions**
- Built full autonomy pipeline: SLAM → state estimation → planning → motor execution  
- Integrated LiDAR, IMU, and encoder feedback into ROS2 navigation stack  
- Designed and fabricated custom TurtleBot3-inspired robot chassis adapted to available hardware  
- Validated the navigation pipeline in Gazebo using a simulation-first workflow  

---

## Autonomy Software Architecture

<p align="center">
  <img src="{{ site.baseurl }}/assets/slam/slam_system_architecture.png" alt="SLAM System Architecture" width="850">
</p>
<p align="center">
  <em>Distributed autonomy architecture with ROS2 on Raspberry Pi and deterministic low-level motor control on ESP32.</em>
</p>

**Core data flow**
- `/scan` (LiDAR) + `/imu/data` (IMU) provide sensor inputs  
- Cartographer generates map and pose estimate  
- `robot_localization` EKF fuses IMU + encoder odometry into `/odom`  
- Nav2 computes `/cmd_vel` commands  
- ESP32 executes closed-loop motor control and publishes encoder-based odometry  

---

## Hardware Platform
**Compute and control**
- Raspberry Pi 4B (Ubuntu 22.04, ROS2)
- ESP32 used as dedicated real-time motor controller

**Sensors**
- YDLiDAR X2 (360° 2D LiDAR)
- BNO055 IMU

**Actuation**
- 2 × 500 RPM DC encoder motors
- Cytron MD10C motor drivers

**Mechanical design**
- Custom 3D-printed chassis inspired by TurtleBot3 Waffle geometry  
- Redesigned plates to accommodate non-proprietary components  
- Modular mounting using standoffs for maintainability and sensor alignment  

---

## Autonomy Pipeline Implementation
### SLAM
- Configured Cartographer SLAM using LiDAR scans for occupancy grid mapping and pose estimation  

### State estimation
- Used `robot_localization` EKF to fuse IMU and wheel odometry, emphasizing IMU-informed state estimation  

### Navigation
- Integrated Nav2 for planning and execution using velocity commands  
- Implemented basic frontier exploration for autonomous map coverage  

### Motor execution
- ESP32 executed low-level closed-loop motor control using encoder feedback  
- Offloaded actuation to improve determinism and reduce computational load on the Raspberry Pi  

---

## Simulation and System Validation
Simulation-first development used TurtleBot3 Gazebo environment to reduce hardware risk and accelerate iteration.

**Validation approach**
1. Validate sensor drivers and ROS2 topic publishing  
2. Verify TF tree consistency (`map → odom → base_link`)  
3. Validate SLAM and localization independently  
4. Integrate Nav2 planning and execution  
5. Validate exploration behavior (frontier selection + navigation)  

---

## Engineering Challenges and Solutions
**Compute limitations (Raspberry Pi 4B)**
- Running SLAM + navigation pushed CPU limits  
- Mitigation: offloaded motor control to ESP32 and optimized node execution / update rates  

**Driver compatibility (Ubuntu 22.04 + ROS2)**
- LiDAR and IMU SDKs required rebuilds and adaptation  
- Resolved dependency conflicts and ensured stable data publishing  

**Localization architecture selection**
- Evaluated AMCL vs `robot_localization`  
- Selected `robot_localization` to emphasize IMU-driven estimation and use LiDAR primarily for mapping/navigation  

**Mechanical constraints**
- Proprietary TurtleBot3 parts unavailable  
- Redesigned chassis plates to fit available components while maintaining rigidity and sensor alignment  

**Frontier exploration**
- Implemented frontier detection and goal selection logic  
- Tuned behavior to reduce redundant exploration and unstable navigation loops  

---

## Results
- Built a reproducible autonomy architecture integrating sensing, estimation, planning, and embedded actuation  
- Achieved stable SLAM + navigation behavior in simulation  
- Demonstrated autonomous frontier-based exploration workflow and staged integration methodology  

---

## Technical Stack
- ROS2, Nav2, Cartographer, robot_localization (EKF)
- Gazebo (TurtleBot3 simulation environment)
- Raspberry Pi 4B, ESP32
- YDLiDAR X2, BNO055 IMU
- Encoder-based motor control + odometry
- Custom 3D-printed chassis design

---

## Future Improvements
- Quantitative evaluation of localization drift and path tracking error  
- Improve exploration efficiency and recovery behaviors  
- Improve sensor calibration and time synchronization  
- Extend architecture to multi-robot mapping / coordination  
