---
layout: default
title: Projects
---

# Projects

A curated set of robotics projects spanning **perception**, **simulation**, and **embedded control**, with a focus on building complete systems from estimation and planning to real-time deployment.

<div class="project-grid">

  <div class="project-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/slam_final_result.png" alt="Stereo Visual-Inertial SLAM preview">
    <div class="project-card-body">
      <div class="project-card-title">Stereo Visual-Inertial SLAM</div>
      <div class="project-card-desc">
        Built a stereo visual-inertial SLAM system on EuRoC MAV using LK tracking, IMU fusion, bundle adjustment, loop closure, and sparse 3D mapping.
      </div>
      <a class="btn" href="{{ site.baseurl }}/projects/lk-stereo-visual-slam">View Project →</a>
    </div>
  </div>

  <div class="project-card">
    <img src="{{ site.baseurl }}/assets/thermostat/thermostat_build.jpg" alt="Thermostat project preview">
    <div class="project-card-body">
      <div class="project-card-title">Closed-Loop Temperature Control (Peltier + TMP117)</div>
      <div class="project-card-desc">
        Embedded thermal control system using a continuous-time compensator, Tustin discretization, and Arduino-based real-time deployment.
      </div>
      <a class="btn" href="{{ site.baseurl }}/projects/thermostat-closed-loop-control">View Project →</a>
    </div>
  </div>

  <div class="project-card">
    <img src="{{ site.baseurl }}/assets/mujoco/ur10e_IK_velocity.gif" alt="MuJoCo UR10e preview">
    <div class="project-card-body">
      <div class="project-card-title">MuJoCo-Based Robotic Manipulator Simulation (UR10e)</div>
      <div class="project-card-desc">
        Physics-based simulation comparing FK and IK control under position and velocity command interfaces.
      </div>
      <a class="btn" href="{{ site.baseurl }}/projects/mujoco-manipulator">View Project →</a>
    </div>
  </div>

<div class="project-card">
  <img src="{{ site.baseurl }}/assets/smolvla/smolvla_dataset_examples.png" alt="SmolVLA BridgeV2 drawer manipulation preview">
  <div class="project-card-body">
    <div class="project-card-title">SmolVLA for Language-Conditioned Robot Action Prediction</div>
    <div class="project-card-desc">
      Applied a pretrained 450M vision-language-action model to BridgeV2 drawer manipulation and analyzed language grounding, action consistency, and temporal behavior.
    </div>
    <a class="btn" href="{{ site.baseurl }}/projects/smolvla-action-prediction">View Project →</a>
  </div>
</div>

</div>

<hr>

## Upcoming Additions

Additional perception and navigation projects currently being prepared for the site:

- ORB-Based Vision Navigation
- Vision-Language-Action Navigation Evaluation
