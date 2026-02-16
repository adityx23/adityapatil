---
layout: default
title: Aditya Patil
---

<div class="hero" markdown="0">
  <h1>Aditya Patil</h1>
  <p class="hero-sub">
    Robotics &amp; Mechatronics graduate student at NYU Tandon School of Engineering with a focus on 
    <strong>autonomous systems</strong>, <strong>controls</strong>, and <strong>simulation-to-hardware deployment</strong>. 
    I build end-to-end robotic systems spanning state estimation, navigation, and embedded actuation. 
    My work includes MuJoCo-based manipulation and control studies, ROS2 SLAM and navigation pipelines, 
    and real-time closed-loop control implementations on embedded hardware.
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

- **SLAM-Based Autonomous Navigation Robot (ROS2 + Nav2 + Cartographer):** Designed a full autonomy stack integrating LiDAR, IMU, localization, and planning, with ESP32-based motor control and simulation-first validation in Gazebo.
  
- **Closed-Loop Temperature Control System (Peltier + TMP117):** Designed a continuous-time compensator, discretized via Tustin transform, and deployed a real-time difference-equation controller on Arduino Mega controlling thermal dynamics via PWM.

- **MuJoCo UR10e Manipulator Simulation:** Implemented and analyzed FK and IK control under position and velocity interfaces, validating controller stability, convergence, and task-space trajectory behavior in physics simulation.
</div>

<div class="card" markdown="1">
## Featured Projects

- [SLAM-Based Autonomous Navigation Robot]({{ site.baseurl }}/projects/slam-navigation-robot)
- [Closed-Loop Temperature Control (Peltier + TMP117)]({{ site.baseurl }}/projects/thermostat-closed-loop-control)
- [MuJoCo-Based Robotic Manipulator Simulation]({{ site.baseurl }}/projects/mujoco-manipulator)

</div>
