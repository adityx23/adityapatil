---
layout: default
title: SLAM-Based Autonomous Navigation Robot
---

# SLAM-Based Autonomous Navigation Robot

<div class="project-summary">
<strong>Type:</strong> Autonomous Mobile Robot (ROS2)<br>
<strong>Focus:</strong> SLAM, localization, navigation, sensor integration, embedded motor control<br>
<strong>Platform:</strong> ROS2, Nav2, Cartographer, robot_localization, Raspberry Pi 4B, ESP32<br>
<strong>Outcome:</strong> Full autonomy pipeline integrated and validated end-to-end in Gazebo prior to hardware deployment
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← Back to Projects</a>
</div>

---

## Overview

A full-stack ROS2 autonomous mobile robot capable of indoor mapping and navigation using LiDAR and IMU sensor fusion — spanning embedded motor control, state estimation, SLAM, and autonomous exploration.

**Key contributions**
- Full autonomy pipeline: SLAM → state estimation → planning → motor execution
- EKF-based sensor fusion of IMU and wheel odometry via `robot_localization`
- Custom TurtleBot3-inspired chassis redesigned for non-proprietary components
- Simulation-first validation in Gazebo before hardware deployment

---

## System Architecture

<p align="center">
  <img src="{{ site.baseurl }}/assets/slam/slam_robot_system_architecture.svg"
       alt="SLAM Robot System Architecture"
       width="100%"
       style="max-width: 860px;">
</p>
<p align="center">
  <em>Distributed autonomy architecture — ROS2 stack on Raspberry Pi 4B with deterministic motor control offloaded to ESP32.</em>
</p>

LiDAR scans feed Cartographer for occupancy mapping; IMU and encoder odometry are fused by the EKF into `/odom`. Nav2 computes `/cmd_vel` commands, which the ESP32 executes as closed-loop PWM motor control, with encoder feedback looping back into the EKF.

---

## Hardware

| Component | Role |
|---|---|
| Raspberry Pi 4B (Ubuntu 22.04) | Main compute — all ROS2 nodes |
| ESP32 | Real-time motor controller |
| YDLiDAR X2 | 360° 2D scan |
| BNO055 IMU | Angular velocity + orientation |
| 2× 500 RPM DC encoder motors | Actuation + odometry source |
| Cytron MD10C | H-bridge PWM driver |
| Custom 3D-printed chassis | TurtleBot3 Waffle-inspired, redesigned for available parts |

---

## Key Engineering Decisions

**Offloading motor control to ESP32** — dedicating the ESP32 to closed-loop actuation freed up Raspberry Pi headroom for SLAM and Nav2.

**`robot_localization` over AMCL** — weights IMU estimation more heavily, reserving LiDAR primarily for mapping.

**Custom chassis** — TurtleBot3 plates redesigned in CAD to fit available hardware while preserving sensor alignment.

---

## Technical Stack

ROS2 · Nav2 · Cartographer · robot_localization (EKF) · Gazebo · Raspberry Pi 4B · ESP32 · YDLiDAR X2 · BNO055 IMU · Cytron MD10C · Python · C++
