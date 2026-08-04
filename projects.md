---
layout: default
title: Projects
description: Robotics projects spanning embedded control, SLAM, autonomy, robot learning, and physics-based simulation.
---

<p class="eyebrow">Engineering Portfolio</p>
# Projects

Each case study leads with the system problem, my contribution, implementation evidence, and measured result. Projects are ordered to emphasize robotics systems and embedded engineering depth.

<section class="portfolio-intro" aria-label="Portfolio focus">
  <p><strong>Robotics systems engineer specializing in embedded control, autonomy, state estimation, and learning-enabled robots.</strong> These case studies show how I take projects from hardware or dataset setup through implementation, debugging, and quantitative validation.</p>
  <div class="focus-list" aria-label="Project disciplines">
    <span>Embedded robotics</span>
    <span>Autonomy &amp; perception</span>
    <span>Robot learning</span>
  </div>
</section>

<div class="project-grid">

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/ackermann-autonomous-robot">
      <img src="{{ site.baseurl }}/assets/thumbnails/ackermann.webp" srcset="{{ site.baseurl }}/assets/thumbnails/ackermann-480.webp 480w, {{ site.baseurl }}/assets/thumbnails/ackermann.webp 960w" sizes="(max-width: 640px) 100vw, 50vw" alt="Ackermann autonomous robot with Raspberry Pi, Jetson, lidar, and RGB-D camera" width="960" height="540" fetchpriority="high">
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
      <img src="{{ site.baseurl }}/assets/thumbnails/lk-slam.webp" srcset="{{ site.baseurl }}/assets/thumbnails/lk-slam-480.webp 480w, {{ site.baseurl }}/assets/thumbnails/lk-slam.webp 960w" sizes="(max-width: 640px) 100vw, 50vw" alt="Stereo visual-inertial SLAM result summary" width="960" height="540" loading="lazy" decoding="async">
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
      <img src="{{ site.baseurl }}/assets/thumbnails/ecu.webp" srcset="{{ site.baseurl }}/assets/thumbnails/ecu-480.webp 480w, {{ site.baseurl }}/assets/thumbnails/ecu.webp 960w" sizes="(max-width: 640px) 100vw, 50vw" alt="Annotated automatic-transmission drivetrain test platform" width="960" height="540" loading="lazy" decoding="async">
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
      <img src="{{ site.baseurl }}/assets/thumbnails/thermostat.webp" srcset="{{ site.baseurl }}/assets/thumbnails/thermostat-480.webp 480w, {{ site.baseurl }}/assets/thumbnails/thermostat.webp 960w" sizes="(max-width: 640px) 100vw, 50vw" alt="Completed acrylic temperature-control enclosure and electronics" width="960" height="540" loading="lazy" decoding="async">
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
      <img src="{{ site.baseurl }}/assets/thumbnails/slam-navigation.webp" srcset="{{ site.baseurl }}/assets/thumbnails/slam-navigation-480.webp 480w, {{ site.baseurl }}/assets/thumbnails/slam-navigation.webp 960w" sizes="(max-width: 640px) 100vw, 50vw" alt="ROS2 navigation robot system architecture" width="960" height="540" loading="lazy" decoding="async">
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
      <img src="{{ site.baseurl }}/assets/thumbnails/smolvla.webp" srcset="{{ site.baseurl }}/assets/thumbnails/smolvla-480.webp 480w, {{ site.baseurl }}/assets/thumbnails/smolvla.webp 960w" sizes="(max-width: 640px) 100vw, 50vw" alt="BridgeV2 drawer-manipulation observations used for SmolVLA analysis" width="960" height="540" loading="lazy" decoding="async">
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
      <img src="{{ site.baseurl }}/assets/thumbnails/diffusion-policy.webp" srcset="{{ site.baseurl }}/assets/thumbnails/diffusion-policy-480.webp 480w, {{ site.baseurl }}/assets/thumbnails/diffusion-policy.webp 960w" sizes="(max-width: 640px) 100vw, 50vw" alt="PushT diffusion-policy evaluation dashboard" width="960" height="540" loading="lazy" decoding="async">
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
      <img src="{{ site.baseurl }}/assets/thumbnails/mujoco.webp" srcset="{{ site.baseurl }}/assets/thumbnails/mujoco-480.webp 480w, {{ site.baseurl }}/assets/thumbnails/mujoco.webp 960w" sizes="(max-width: 640px) 100vw, 50vw" alt="UR10e inverse-kinematics velocity-control simulation" width="960" height="540" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">MuJoCo</span><span class="tag">Kinematics</span><span class="tag">Control</span></div>
        <h2 class="project-card-title">UR10e Control in MuJoCo</h2>
        <p class="project-card-desc">Compared forward/inverse kinematics under position and velocity command interfaces in physics simulation.</p>
        <span class="project-card-cta">View project →</span>
      </div>
    </a>
  </article>

</div>
