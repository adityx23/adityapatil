---
layout: default
title: Projects
description: Robotics projects spanning embedded control, SLAM, autonomy, robot learning, and physics-based simulation.
---

<p class="eyebrow">Engineering Portfolio</p>
# Projects

Each case study leads with the system problem, my contribution, implementation evidence, and measured result. Projects are ordered to emphasize robotics systems and embedded engineering depth.

<div class="project-grid">

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/ackermann-autonomous-robot">
      <img src="{{ site.baseurl }}/assets/ackermann/robot-overview.jpeg" alt="Ackermann autonomous robot with Raspberry Pi, Jetson, lidar, and RGB-D camera" width="1373" height="1831">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">Autonomy</span><span class="tag">Embedded Python</span><span class="tag">Sensor Fusion</span></div>
        <h2 class="project-card-title">Ackermann Robot Bring-Up & Native Autonomy</h2>
        <p class="project-card-desc">STM32/C30D bring-up, validated motion primitives, safety-gated control, multi-sensor capture, odometry, and mapping foundations.</p>
        <span class="project-card-cta">View project &rarr;</span>
      </div>
    </a>
  </article>

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/lk-stereo-visual-slam">
      <img src="{{ site.baseurl }}/assets/lk_slam/slam_final_result.png" alt="Stereo visual-inertial SLAM result summary" width="2428" height="1975" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">OpenCV</span><span class="tag">VIO</span><span class="tag">Optimization</span></div>
        <h2 class="project-card-title">Stereo Visual-Inertial SLAM</h2>
        <p class="project-card-desc">Stereo tracking, IMU fusion, bundle adjustment, loop closure, sparse mapping, and EuRoC trajectory evaluation.</p>
        <span class="project-card-cta">View project →</span>
      </div>
    </a>
  </article>

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/ecu-automatic-transmission-controller">
      <img src="{{ site.baseurl }}/assets/ecu/drivetrain-hardware.png" alt="Annotated automatic-transmission drivetrain test platform" width="1536" height="2040" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">Embedded Control</span><span class="tag">Sensors</span><span class="tag">Telemetry</span></div>
        <h2 class="project-card-title">Automatic Transmission Controller</h2>
        <p class="project-card-desc">A physical 24 V three-speed drivetrain with concurrent sensing, encoder-based shifting, logging, and efficiency analysis.</p>
        <span class="project-card-cta">View project →</span>
      </div>
    </a>
  </article>

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/thermostat-closed-loop-control">
      <img src="{{ site.baseurl }}/assets/thermostat/thermostat_build.jpg" alt="Completed acrylic temperature-control enclosure and electronics" width="483" height="512" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">Arduino</span><span class="tag">Controls</span><span class="tag">TMP117</span></div>
        <h2 class="project-card-title">Closed-Loop Temperature Control</h2>
        <p class="project-card-desc">Modeled a thermal enclosure, discretized a compensator, and deployed the controller with TMP117 feedback and PWM heating.</p>
        <span class="project-card-cta">View project →</span>
      </div>
    </a>
  </article>

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/slam-navigation-robot">
      <img src="{{ site.baseurl }}/assets/slam/slam_robot_system_architecture.svg" alt="ROS2 navigation robot system architecture" width="680" height="620" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">ROS2</span><span class="tag">Nav2</span><span class="tag">Gazebo</span></div>
        <h2 class="project-card-title">SLAM-Based Navigation Robot</h2>
        <p class="project-card-desc">A simulation-first autonomy architecture spanning LiDAR SLAM, EKF fusion, planning, and embedded motor control.</p>
        <span class="project-card-cta">View project →</span>
      </div>
    </a>
  </article>

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/smolvla-action-prediction">
      <img src="{{ site.baseurl }}/assets/smolvla/smolvla_dataset_examples.png" alt="BridgeV2 drawer-manipulation observations used for SmolVLA analysis" width="1589" height="740" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">SmolVLA</span><span class="tag">LeRobot</span><span class="tag">BridgeV2</span></div>
        <h2 class="project-card-title">SmolVLA Action Analysis</h2>
        <p class="project-card-desc">Evaluated language sensitivity, open/close action separation, and temporal consistency on real robot observations.</p>
        <span class="project-card-cta">View project →</span>
      </div>
    </a>
  </article>

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/diffusion-policy-pusht">
      <img src="{{ site.baseurl }}/assets/diffusion_policy/diffusion_policy_results.png" alt="PushT diffusion-policy evaluation dashboard" width="1771" height="1280" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">Diffusion Policy</span><span class="tag">PyTorch</span><span class="tag">PushT</span></div>
        <h2 class="project-card-title">Diffusion Policy on PushT</h2>
        <p class="project-card-desc">Measured success, efficiency, reward behavior, and failure structure across 30 manipulation rollouts.</p>
        <span class="project-card-cta">View project →</span>
      </div>
    </a>
  </article>

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/mujoco-manipulator">
      <img src="{{ site.baseurl }}/assets/mujoco/ur10e_IK_velocity-poster.jpg" alt="UR10e inverse-kinematics velocity-control simulation" width="640" height="480" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">MuJoCo</span><span class="tag">Kinematics</span><span class="tag">Control</span></div>
        <h2 class="project-card-title">UR10e Control in MuJoCo</h2>
        <p class="project-card-desc">Compared forward/inverse kinematics under position and velocity command interfaces in physics simulation.</p>
        <span class="project-card-cta">View project →</span>
      </div>
    </a>
  </article>

</div>
