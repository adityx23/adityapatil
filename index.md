---
layout: default
title: Aditya Patil
---

<div class="hero" markdown="0">
  <h1>Aditya Patil</h1>
  <p class="hero-sub">
    Robotics &amp; Mechatronics Graduate Student at NYU Tandon. I build end-to-end robotic systems across
    <strong>simulation</strong>, <strong>controls</strong>, and <strong>embedded autonomy</strong>—from kinematic control
    studies in MuJoCo to ROS2 navigation stacks and real-time closed-loop hardware.
  </p>

  <div class="hero-links">
    <a class="btn" href="{{ site.baseurl }}/projects">📌 Projects</a>
    <a class="btn" href="{{ site.baseurl }}/resume.pdf">📄 Resume</a>
    <a class="btn" href="mailto:aditya.a.patil2@gmail.com">✉️ Email</a>
    <a class="btn" href="https://www.linkedin.com/in/aditya-patil-4a5735217" target="_blank" rel="noopener">🔗 LinkedIn</a>
  </div>
</div>

<div class="card" markdown="1">
## Highlights

- **SLAM-Based Autonomous Navigation Robot (ROS2 + Nav2 + Cartographer):** Full-stack autonomy pipeline with LiDAR/IMU integration, `robot_localization`, and ESP32 motor control; validated simulation-first in Gazebo.
- **Closed-Loop Temperature Control (Peltier + TMP117):** Continuous-time compensator discretized via Tustin (500 ms loop) and deployed as a difference-equation controller on Arduino Mega driving a PWM H-bridge.
- **MuJoCo UR10e Manipulator Simulation:** Compared FK/IK under position vs velocity control and visualized task-space behavior to analyze convergence, stability, and trajectory quality.
</div>

<div class="card" markdown="1">
## Featured Projects

- [SLAM-Based Autonomous Navigation Robot]({{ site.baseurl }}/projects/slam-navigation-robot)
- [Closed-Loop Temperature Control (Peltier + TMP117)]({{ site.baseurl }}/projects/thermostat-closed-loop-control)
- [MuJoCo-Based Robotic Manipulator Simulation]({{ site.baseurl }}/projects/mujoco-manipulator)
</div>
