---
layout: default
title: SLAM-Based Autonomous Navigation Robot
description: Simulation-first ROS2 mobile-robot architecture spanning LiDAR SLAM, EKF sensor fusion, Nav2 planning, and embedded motor control.
---

# SLAM-Based Autonomous Navigation Robot

<div class="project-summary">
  <div><strong>Role</strong><span>Autonomy architecture and integration</span></div>
  <div><strong>Context</strong><span>Simulation-first mobile robot design</span></div>
  <div><strong>Platform</strong><span>ROS2 · Nav2 · Cartographer · Gazebo</span></div>
  <div><strong>Outcome</strong><span>End-to-end autonomy pipeline validated in simulation</span></div>
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← All Projects</a>
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
<svg width="100%" viewBox="0 0 680 620" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
<!-- SENSORS -->
<g>
  <rect x="28" y="80" width="130" height="52" rx="8" stroke-width="0.5" fill="#085041" stroke="#5DCAA5"/>
  <text x="93" y="100" text-anchor="middle" dominant-baseline="central" fill="#9FE1CB" font-size="14" font-weight="500" font-family="system-ui,sans-serif">YDLiDAR X2</text>
  <text x="93" y="118" text-anchor="middle" dominant-baseline="central" fill="#5DCAA5" font-size="12" font-family="system-ui,sans-serif">360° 2D scan</text>
</g>
<g>
  <rect x="28" y="162" width="130" height="52" rx="8" stroke-width="0.5" fill="#085041" stroke="#5DCAA5"/>
  <text x="93" y="182" text-anchor="middle" dominant-baseline="central" fill="#9FE1CB" font-size="14" font-weight="500" font-family="system-ui,sans-serif">BNO055 IMU</text>
  <text x="93" y="200" text-anchor="middle" dominant-baseline="central" fill="#5DCAA5" font-size="12" font-family="system-ui,sans-serif">Angular velocity</text>
</g>
<g>
  <rect x="28" y="244" width="130" height="52" rx="8" stroke-width="0.5" fill="#085041" stroke="#5DCAA5"/>
  <text x="93" y="264" text-anchor="middle" dominant-baseline="central" fill="#9FE1CB" font-size="14" font-weight="500" font-family="system-ui,sans-serif">Encoder motors</text>
  <text x="93" y="282" text-anchor="middle" dominant-baseline="central" fill="#5DCAA5" font-size="12" font-family="system-ui,sans-serif">Wheel odometry</text>
</g>
<!-- RASPBERRY PI container -->
<rect x="196" y="40" width="300" height="380" rx="16" fill="#7F77DD" fill-opacity="0.1" stroke="#7F77DD" stroke-width="1" stroke-dasharray="6 4"/>
<text x="346" y="64" text-anchor="middle" dominant-baseline="central" fill="#AFA9EC" font-size="14" font-weight="500" font-family="system-ui,sans-serif">Raspberry Pi 4B · ROS2</text>
<!-- Cartographer -->
<g>
  <rect x="214" y="84" width="160" height="56" rx="8" stroke-width="0.5" fill="#3C3489" stroke="#7F77DD"/>
  <text x="294" y="106" text-anchor="middle" dominant-baseline="central" fill="#CECBF6" font-size="14" font-weight="500" font-family="system-ui,sans-serif">Cartographer SLAM</text>
  <text x="294" y="124" text-anchor="middle" dominant-baseline="central" fill="#AFA9EC" font-size="12" font-family="system-ui,sans-serif">Map + pose estimate</text>
</g>
<!-- robot_localization EKF -->
<g>
  <rect x="214" y="166" width="160" height="56" rx="8" stroke-width="0.5" fill="#3C3489" stroke="#7F77DD"/>
  <text x="294" y="188" text-anchor="middle" dominant-baseline="central" fill="#CECBF6" font-size="14" font-weight="500" font-family="system-ui,sans-serif">robot_localization</text>
  <text x="294" y="206" text-anchor="middle" dominant-baseline="central" fill="#AFA9EC" font-size="12" font-family="system-ui,sans-serif">EKF · fuses IMU + odom</text>
</g>
<!-- Nav2 -->
<g>
  <rect x="214" y="248" width="160" height="56" rx="8" stroke-width="0.5" fill="#3C3489" stroke="#7F77DD"/>
  <text x="294" y="270" text-anchor="middle" dominant-baseline="central" fill="#CECBF6" font-size="14" font-weight="500" font-family="system-ui,sans-serif">Nav2</text>
  <text x="294" y="288" text-anchor="middle" dominant-baseline="central" fill="#AFA9EC" font-size="12" font-family="system-ui,sans-serif">Planning + execution</text>
</g>
<!-- Frontier exploration -->
<g>
  <rect x="214" y="330" width="160" height="56" rx="8" stroke-width="0.5" fill="#3C3489" stroke="#7F77DD"/>
  <text x="294" y="352" text-anchor="middle" dominant-baseline="central" fill="#CECBF6" font-size="14" font-weight="500" font-family="system-ui,sans-serif">Frontier exploration</text>
  <text x="294" y="370" text-anchor="middle" dominant-baseline="central" fill="#AFA9EC" font-size="12" font-family="system-ui,sans-serif">Autonomous coverage</text>
</g>
<!-- ESP32 container -->
<rect x="528" y="216" width="130" height="140" rx="16" fill="#D85A30" fill-opacity="0.1" stroke="#D85A30" stroke-width="1" stroke-dasharray="6 4"/>
<text x="593" y="238" text-anchor="middle" dominant-baseline="central" fill="#F0997B" font-size="14" font-weight="500" font-family="system-ui,sans-serif">ESP32</text>
<!-- Motor control -->
<g>
  <rect x="542" y="252" width="102" height="52" rx="8" stroke-width="0.5" fill="#712B13" stroke="#D85A30"/>
  <text x="593" y="272" text-anchor="middle" dominant-baseline="central" fill="#F5C4B3" font-size="14" font-weight="500" font-family="system-ui,sans-serif">Motor control</text>
  <text x="593" y="290" text-anchor="middle" dominant-baseline="central" fill="#F0997B" font-size="12" font-family="system-ui,sans-serif">Closed-loop PWM</text>
</g>
<!-- Cytron MD10C -->
<g>
  <rect x="542" y="326" width="102" height="44" rx="8" stroke-width="0.5" fill="#633806" stroke="#EF9F27"/>
  <text x="593" y="344" text-anchor="middle" dominant-baseline="central" fill="#FAC775" font-size="14" font-weight="500" font-family="system-ui,sans-serif">Cytron MD10C</text>
  <text x="593" y="360" text-anchor="middle" dominant-baseline="central" fill="#EF9F27" font-size="12" font-family="system-ui,sans-serif">H-bridge driver</text>
</g>
<!-- DC Motors -->
<g>
  <rect x="528" y="400" width="130" height="52" rx="8" stroke-width="0.5" fill="#633806" stroke="#EF9F27"/>
  <text x="593" y="420" text-anchor="middle" dominant-baseline="central" fill="#FAC775" font-size="14" font-weight="500" font-family="system-ui,sans-serif">DC motors × 2</text>
  <text x="593" y="438" text-anchor="middle" dominant-baseline="central" fill="#EF9F27" font-size="12" font-family="system-ui,sans-serif">500 RPM + encoders</text>
</g>
<!-- Gazebo -->
<g>
  <rect x="196" y="460" width="300" height="52" rx="8" stroke-width="0.5" fill="#2C2C2A" stroke="#888780"/>
  <text x="346" y="480" text-anchor="middle" dominant-baseline="central" fill="#D3D1C7" font-size="14" font-weight="500" font-family="system-ui,sans-serif">Gazebo simulation</text>
  <text x="346" y="498" text-anchor="middle" dominant-baseline="central" fill="#888780" font-size="12" font-family="system-ui,sans-serif">TurtleBot3 env · validation-first</text>
</g>
<!-- Legend -->
<rect x="28" y="540" width="12" height="12" rx="2" fill="#085041" stroke="#5DCAA5" stroke-width="0.5"/>
<text x="46" y="551" dominant-baseline="central" fill="#888780" font-size="12" font-family="system-ui,sans-serif">Sensors / hardware</text>
<rect x="172" y="540" width="12" height="12" rx="2" fill="#3C3489" stroke="#7F77DD" stroke-width="0.5"/>
<text x="190" y="551" dominant-baseline="central" fill="#888780" font-size="12" font-family="system-ui,sans-serif">ROS2 nodes (RPi)</text>
<rect x="330" y="540" width="12" height="12" rx="2" fill="#712B13" stroke="#D85A30" stroke-width="0.5"/>
<text x="348" y="551" dominant-baseline="central" fill="#888780" font-size="12" font-family="system-ui,sans-serif">Embedded controller</text>
<rect x="482" y="540" width="12" height="12" rx="2" fill="#633806" stroke="#EF9F27" stroke-width="0.5"/>
<text x="500" y="551" dominant-baseline="central" fill="#888780" font-size="12" font-family="system-ui,sans-serif">Actuation</text>
<!-- ARROWS -->
<line x1="158" y1="106" x2="212" y2="106" fill="none" stroke="#1D9E75" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="185" y="99" text-anchor="middle" fill="#888780" font-size="12" font-family="system-ui,sans-serif">/scan</text>
<line x1="158" y1="194" x2="212" y2="194" fill="none" stroke="#1D9E75" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="185" y="187" text-anchor="middle" fill="#888780" font-size="12" font-family="system-ui,sans-serif">/imu/data</text>
<path d="M158 270 L185 270 L185 210 L212 210" fill="none" stroke="#1D9E75" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="175" y="242" text-anchor="middle" fill="#888780" font-size="12" font-family="system-ui,sans-serif">/odom</text>
<line x1="294" y1="140" x2="294" y2="164" fill="none" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="326" y="155" text-anchor="start" fill="#888780" font-size="12" font-family="system-ui,sans-serif">/map</text>
<line x1="294" y1="222" x2="294" y2="246" fill="none" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="318" y="237" text-anchor="start" fill="#888780" font-size="12" font-family="system-ui,sans-serif">/odom</text>
<line x1="294" y1="304" x2="294" y2="328" fill="none" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="318" y="319" text-anchor="start" fill="#888780" font-size="12" font-family="system-ui,sans-serif">goal</text>
<path d="M376 276 L496 276 L496 268 L526 268" fill="none" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="450" y="266" text-anchor="middle" fill="#888780" font-size="12" font-family="system-ui,sans-serif">/cmd_vel</text>
<line x1="593" y1="304" x2="593" y2="324" fill="none" stroke="#D85A30" stroke-width="1.5" marker-end="url(#arrow)"/>
<line x1="593" y1="370" x2="593" y2="398" fill="none" stroke="#BA7517" stroke-width="1.5" marker-end="url(#arrow)"/>
<path d="M528 426 L480 426 L480 194 L212 194" fill="none" stroke="#BA7517" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#arrow)"/>
<text x="468" y="415" text-anchor="end" fill="#888780" font-size="12" font-family="system-ui,sans-serif">encoder feedback</text>
<path d="M346 460 L346 422" fill="none" stroke="#888780" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow)"/>
<text x="360" y="444" text-anchor="start" fill="#888780" font-size="12" font-family="system-ui,sans-serif">sim topics</text>
</svg>
</p>

<p align="center"><em>Distributed autonomy architecture — ROS2 stack on Raspberry Pi 4B with deterministic motor control offloaded to ESP32.</em></p>

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
