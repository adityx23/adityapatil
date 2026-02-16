---
layout: default
title: Projects
---

# Projects

A curated set of robotics projects showcasing **full-stack system integration** across simulation, autonomy, and embedded control.

<div class="projects-grid" markdown="0">

  <div class="project-card">
    <h3>SLAM-Based Autonomous Navigation Robot</h3>
    <p>End-to-end ROS2 autonomy pipeline: SLAM → state estimation → planning → embedded motor execution.</p>
    <div class="project-meta"><strong>Focus:</strong> ROS2, Nav2, Cartographer, robot_localization, ESP32 motor control</div>
    <div class="project-actions">
      <a class="btn" href="{{ site.baseurl }}/projects/slam-navigation-robot">View Project →</a>
      <a class="btn" href="{{ site.baseurl }}/assets/slam/slam_system_architecture.png">Architecture</a>
    </div>
  </div>

  <div class="project-card">
    <h3>Closed-Loop Temperature Control (Peltier + TMP117)</h3>
    <p>Controls project from modeling → compensator design → Tustin discretization → embedded deployment.</p>
    <div class="project-meta"><strong>Focus:</strong> Discrete-time control, PWM actuation, embedded implementation</div>
    <div class="project-actions">
      <a class="btn" href="{{ site.baseurl }}/projects/thermostat-closed-loop-control">View Project →</a>
    </div>
  </div>

  <div class="project-card">
    <h3>MuJoCo-Based Robotic Manipulator Simulation (UR10e)</h3>
    <p>Compared FK vs IK control under position vs velocity command interfaces using physics-based simulation.</p>
    <div class="project-meta"><strong>Focus:</strong> MuJoCo, kinematics, Jacobian velocity control, trajectory visualization</div>
    <div class="project-actions">
      <a class="btn" href="{{ site.baseurl }}/projects/mujoco-manipulator">View Project →</a>
    </div>
  </div>

</div>

<hr>

### Notes
- Each project page is structured to highlight **architecture, implementation, validation, and engineering tradeoffs**.
- If you'd like, we can add a lightweight **Skills** page next to make the portfolio feel even more complete.
