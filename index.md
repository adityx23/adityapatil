---
layout: default
title: Aditya Patil
---

<div class="hero" markdown="0">
  <h1>Aditya Patil</h1>

  <p class="hero-sub">
    Robotics &amp; Mechatronics graduate student at NYU Tandon focused on
    <strong>autonomous systems</strong>, <strong>controls</strong>, and <strong>simulation-to-hardware deployment</strong>.
    I build end-to-end robotic systems spanning <strong>state estimation</strong>, <strong>navigation</strong>, and
    <strong>embedded actuation</strong>—from MuJoCo manipulation/control studies to ROS2 SLAM + Nav2 pipelines and
    real-time closed-loop controllers on embedded hardware.
  </p>

  <div class="hero-links">
    <a class="btn" href="{{ site.baseurl }}/projects">📌 Projects</a>
    <a class="btn" href="{{ site.baseurl }}/skills">🛠 Skills</a>
    <a class="btn" href="{{ site.baseurl }}/resume.pdf">📄 Resume</a>
    <a class="btn" href="mailto:aditya.a.patil2@gmail.com">✉️ Email</a>
    <a class="btn" href="https://www.linkedin.com/in/aditya-patil-4a5735217" target="_blank" rel="noopener">🔗 LinkedIn</a>
  </div>
</div>

<div class="card" markdown="1">
## Highlights (Selected Work)

- **SLAM-Based Autonomous Navigation Robot (ROS2 + Nav2 + Cartographer):** Built a full autonomy pipeline integrating LiDAR + IMU, `robot_localization` state estimation, planning/execution in Nav2, and ESP32-based motor control; validated end-to-end in Gazebo (simulation-first workflow).

- **Closed-Loop Temperature Control (Peltier + TMP117):** Designed a continuous-time compensator, discretized it via the Tustin transform (500 ms loop), and deployed a memory-based difference-equation controller on an Arduino Mega driving PWM actuation through an H-bridge.

- **MuJoCo UR10e Manipulator Simulation:** Implemented FK vs IK control under position vs velocity command interfaces, and analyzed stability/convergence and task-space trajectory behavior using physics-based simulation rollouts and visualization.
</div>

<div class="card" markdown="1">
## Featured Projects

- [SLAM-Based Autonomous Navigation Robot]({{ site.baseurl }}/projects/slam-navigation-robot)
- [Closed-Loop Temperature Control (Peltier + TMP117)]({{ site.baseurl }}/projects/thermostat-closed-loop-control)
- [MuJoCo-Based Robotic Manipulator Simulation (UR10e)]({{ site.baseurl }}/projects/mujoco-manipulator)

</div>

<div class="card" markdown="1">
## What I’m Looking For

I’m actively applying for **Robotics / Autonomy / Controls** internships (Summer 2026) where I can contribute to
system integration, motion planning and navigation, simulation-to-real transfer, and embedded real-time control.
</div>
