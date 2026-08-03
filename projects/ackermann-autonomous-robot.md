---
layout: default
title: Native Ackermann Autonomous Robot
description: Safety-first native Python autonomy stack integrating Raspberry Pi supervision, Jetson edge compute, C30D vehicle control, lidar, and RGB-D perception.
---

<p class="eyebrow">Mobile Robotics &middot; Embedded Autonomy</p>
# Native Ackermann Autonomous Robot

<div class="project-summary">
  <div><strong>Role</strong><span>Robotics systems developer</span></div>
  <div><strong>Context</strong><span>Independent autonomy platform</span></div>
  <div><strong>Platform</strong><span>Python &middot; Raspberry Pi 5 &middot; Jetson Orin Nano</span></div>
  <div><strong>Outcome</strong><span>Safety-gated sensing, control, and mapping foundation</span></div>
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">&larr; All Projects</a>
  <a class="btn" href="https://github.com/adityx23/ackermann-autonomous-robot" target="_blank" rel="noopener">GitHub Repository &nearr;</a>
</div>

## Overview

Built a native, non-ROS software stack for a four-wheel Ackermann-steering research robot. A Raspberry Pi 5 owns low-level supervision, safety, hardware interfaces, and logging, while a Jetson Orin Nano provides additional compute for vision, mapping, and future learned navigation workloads.

The platform integrates an OAK-D Lite RGB-D camera, an RPLIDAR C1, and a C30D controller connected to the drive motors, steering servo, wheel encoders, and onboard IMU. The repository captures the engineering path from hardware discovery and passive protocol analysis through guarded control experiments, provisional odometry, synchronized sensor recording, and occupancy-grid generation.

<img class="project-media" src="{{ site.baseurl }}/assets/ackermann/robot-overview.jpeg" alt="Ackermann-steering robot with onboard Raspberry Pi, Jetson compute, lidar, and camera hardware" width="1373" height="1831" loading="lazy" decoding="async">

## System Architecture

<img class="project-media" src="{{ site.baseurl }}/assets/ackermann/system-architecture.svg" alt="Architecture linking lidar, RGB-D camera, Jetson edge compute, Raspberry Pi safety supervisor, C30D controller, and vehicle hardware" width="1200" height="675" loading="lazy" decoding="async">

The architecture keeps the safety boundary local to the Raspberry Pi. Commands from higher-level autonomy components must pass through freshness checks, motion limits, and explicit arming gates before reaching the vehicle controller.

## My Contribution

- Structured the native Python stack around separate driver, control, state, odometry, mapping, communication, and utility layers.
- Implemented a mock-backed robot supervisor with command filtering, stale-data handling, and conservative motion limits.
- Built passive C30D serial-capture and frame-analysis tools without requiring motor or steering writes.
- Confirmed the feedback frame delimiters and XOR checksum, then developed candidate field decoders for motion, yaw, IMU, and battery data.
- Added bounded RPLIDAR and OAK-D capture utilities plus synchronized read-only sensor-run recording.
- Implemented offline run validation, lidar visualization, ray-traced occupancy grids, and provisional straight-line dead reckoning.
- Developed guarded diagnostic utilities for neutral-frame and low-speed command research with explicit physical-safety requirements.

## Safety-First Control

The software defaults to dry-run operation. The main supervisor currently composes a safety manager, command filter, robot state, and mock C30D driver; serial writes remain disabled in the standard configuration.

Safety mechanisms include:

- limits on forward speed, reverse speed, steering angle, acceleration, and test duration;
- manual-enable and wheels-lifted requirements for hardware experiments;
- neutral-command defaults and safe-stop behavior for stale inputs;
- battery, checksum, and serial-feedback readiness checks; and
- finite test sequences with an explicit manual power-cutoff requirement.

These constraints allow protocol and sensor work to progress without presenting the repository as a ready-to-deploy autonomous driving package.

<img class="project-media" src="{{ site.baseurl }}/assets/ackermann/compute-stack.jpeg" alt="Raspberry Pi and Jetson edge-compute stack mounted on the Ackermann robot chassis" width="1823" height="1367" loading="lazy" decoding="async">

## C30D Protocol Investigation

Passive captures established a fixed 24-byte feedback frame with `0x7B` and `0x7D` delimiters. The checksum is the XOR of bytes 0 through 21 and is stored at byte 22. Offline tools extract valid frames, compare payload variation across experiments, export candidate fields, and plot time series.

Reference firmware also informed an 11-byte host-command candidate. The frame representation is implemented, but drive and steering behavior remains under validation because controller mode, active UART path, and board-variant behavior can affect the hardware response. The project deliberately labels inferred fields and experimental commands rather than treating them as confirmed interfaces.

<img class="project-media" src="{{ site.baseurl }}/assets/ackermann/c30d-controller.jpeg" alt="Close-up of the C30D motor, steering, encoder, and IMU controller mounted below the compute stack" width="1373" height="1831" loading="lazy" decoding="async">

## Current Status

| Capability | Status |
|---|---|
| Native supervisor, state model, configuration, and logging | Implemented |
| Safety evaluation and command filtering | Implemented and unit tested |
| Passive C30D feedback capture and checksum validation | Implemented |
| Candidate feedback analysis and plotting | Implemented |
| RPLIDAR and OAK-D bounded capture | Implemented |
| Sensor-run validation, replay, and occupancy grids | Implemented |
| Straight-line dead reckoning | Provisional; calibration required |
| Reliable closed-loop C30D drive and steering | In validation |
| Multi-sensor SLAM and autonomous navigation | Planned |

## Engineering Takeaways

- Unknown embedded interfaces should be approached through passive observation before actuation.
- Safety gates belong near the hardware boundary, not only in high-level autonomy code.
- Candidate protocol fields must stay explicitly labeled until controlled experiments establish their physical meaning.
- Unified capture and offline replay make sensor and state-estimation work testable without repeatedly operating the robot.
- Separating real hardware drivers from control logic makes meaningful mock-based testing possible.

## Technical Stack

Python &middot; Raspberry Pi 5 &middot; Jetson Orin Nano &middot; C30D/STM32 vehicle controller &middot; OAK-D Lite &middot; RPLIDAR C1 &middot; serial protocols &middot; RGB-D perception &middot; occupancy grids &middot; dead reckoning &middot; pytest &middot; YAML configuration

## Next Steps

- Complete repeatable steering and longitudinal-command validation.
- Calibrate wheel motion and yaw feedback against measured chassis motion.
- Fuse encoder, IMU, and lidar observations for planar localization.
- Add scan matching and pose-aware occupancy mapping.
- Connect Jetson perception through a bounded, freshness-checked command interface.
- Evaluate closed-loop waypoint following and obstacle-aware planning.
