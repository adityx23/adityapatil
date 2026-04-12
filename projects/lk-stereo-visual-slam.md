---
layout: default
title: Stereo Visual-Inertial SLAM with Optimization and Loop Closure
---

# Stereo Visual-Inertial SLAM with Optimization and Loop Closure

<div class="project-summary">
<strong>Type:</strong> Visual SLAM / State Estimation / Optimization<br>
<strong>Focus:</strong> Stereo visual odometry, IMU integration, bundle adjustment, loop closure, sparse mapping<br>
<strong>Platform:</strong> Python, OpenCV, NumPy, SciPy, EuRoC MAV dataset<br>
<strong>Outcome:</strong> Built a stereo visual-inertial SLAM pipeline and improved trajectory accuracy through tight IMU coupling, backend optimization, and loop closure
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← Back to Projects</a>
</div>

## Overview

Built a stereo visual-inertial SLAM pipeline on the EuRoC MAV dataset, starting from feature tracking and stereo geometry and extending through visual odometry, IMU-assisted estimation, local optimization, loop closure, and sparse 3D mapping.

The goal was to move beyond a baseline visual odometry pipeline and progressively improve trajectory quality using backend optimization and visual-inertial fusion. The final system combined stereo tracking, PnP-based motion estimation, IMU-informed pose refinement, bundle adjustment, and graph-based loop closure.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_result_final.png" alt="Final SLAM result summary" width="900">
</p>
<p align="center">
  <em>Final result summary showing trajectory alignment, error trends, and visual-inertial performance improvement.</em>
</p>

---

## Pipeline Overview

The system was built as a staged SLAM pipeline:

- stereo image loading and calibration parsing from EuRoC MAV
- stereo rectification and epipolar consistency verification
- LK optical flow tracking across frames
- stereo depth estimation through disparity / triangulation
- frame-to-frame motion estimation using visual correspondences
- IMU-assisted visual odometry refinement
- local and sliding-window bundle adjustment
- loop closure through keyframe graph optimization
- sparse 3D landmark map generation
- evaluation using trajectory alignment and ATE / RPE metrics

---

## Frontend: Tracking, Stereo Geometry, and Depth

The frontend used stereo image pairs and tracked visual features across time using Lucas-Kanade optical flow. Stereo correspondences and rectification were used to enforce geometric consistency and recover depth for tracked points.

<div class="project-grid">

  <div class="project-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/stereo_input_pair.png" alt="Stereo input pair">
    <div class="project-card-body">
      <div class="project-card-title">Stereo Input</div>
      <div class="project-card-desc">
        Raw left-right image pair from the EuRoC MAV stereo camera stream.
      </div>
    </div>
  </div>

  <div class="project-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/lk_optical_flow_tracking.png" alt="LK optical flow tracking">
    <div class="project-card-body">
      <div class="project-card-title">LK Optical Flow Tracking</div>
      <div class="project-card-desc">
        Tracked features across consecutive frames used to estimate motion robustly over time.
      </div>
    </div>
  </div>

  <div class="project-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/epipolar_orb_validation.png" alt="Epipolar and ORB validation">
    <div class="project-card-body">
      <div class="project-card-title">Epipolar Validation</div>
      <div class="project-card-desc">
        Rectified stereo geometry validated using epipolar alignment and feature match consistency.
      </div>
    </div>
  </div>

  <div class="project-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/stereo_disparity_map.png" alt="Stereo disparity map">
    <div class="project-card-body">
      <div class="project-card-title">Depth from Stereo</div>
      <div class="project-card-desc">
        Disparity-derived depth map used to recover 3D structure from stereo observations.
      </div>
    </div>
  </div>

</div>

---

## Baseline Visual Odometry

Using tracked features and stereo-derived 3D structure, the baseline system estimated frame-to-frame motion and recovered a visual odometry trajectory. This baseline established the reference point for later improvements.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/baseline_vo_trajectory.png" alt="Baseline visual odometry trajectory" width="700">
</p>
<p align="center">
  <em>Baseline stereo visual odometry trajectory before visual-inertial refinement and backend optimization.</em>
</p>

The baseline VO pipeline worked, but showed clear drift and accumulated trajectory error over longer horizons, motivating the addition of IMU-informed estimation and backend optimization.

---

## Visual-Inertial Improvement

To improve rotational stability and overall trajectory consistency, IMU information was incorporated into the pipeline. This significantly improved alignment with ground truth and reduced drift relative to the baseline visual-only estimate.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_result_tight_coupling_ate.png" alt="Tight coupling improvement and ATE comparison" width="900">
</p>
<p align="center">
  <em>IMU-assisted visual estimation reduced trajectory error significantly compared to the original visual-only baseline.</em>
</p>

This was one of the strongest improvements in the system. The visual-inertial version produced a much tighter trajectory estimate and reduced the absolute trajectory error substantially.

---

## Backend Optimization

After the frontend and visual-inertial estimation stages, the trajectory was refined using bundle adjustment. Local and sliding-window optimization were used to reduce drift and improve consistency across neighboring poses.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/bundle_adjustment_trajectory.png" alt="Bundle adjustment trajectory improvement" width="700">
</p>
<p align="center">
  <em>Sliding-window bundle adjustment refined local pose consistency and reduced accumulated drift.</em>
</p>

This stage improved the smoothness and structure of the estimated trajectory, especially in regions where raw odometry had begun to diverge.

---

## Loop Closure and Pose Graph Refinement

To move from visual odometry toward a true SLAM system, the pipeline added loop closure using keyframes and graph-based trajectory correction. Revisited locations were detected and used to globally adjust the trajectory.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_loop_closure.png" alt="Loop closure trajectory refinement" width="900">
</p>
<p align="center">
  <em>Loop closure introduced global consistency by reconnecting revisited parts of the trajectory and reducing long-horizon drift.</em>
</p>

This was the most important backend addition because it corrected accumulated trajectory drift over longer sequences and clearly separated the system from a pure VO pipeline.

---

## Sparse 3D Mapping

Alongside trajectory estimation, the system reconstructed a sparse 3D landmark map from tracked stereo features. This provided a visual representation of scene structure and demonstrated that the pipeline was simultaneously estimating motion and building a map.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_sparse_3d_map.png" alt="Sparse 3D landmark map" width="900">
</p>
<p align="center">
  <em>Sparse 3D landmark map reconstructed from stereo observations and tracked feature geometry.</em>
</p>

---

## Results and Validation

The final system was evaluated using aligned trajectory comparison and trajectory-error metrics on EuRoC MAV sequences.

<div class="project-grid">

  <div class="project-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/final_trajectory_vs_ground_truth.png" alt="Final trajectory vs ground truth">
    <div class="project-card-body">
      <div class="project-card-title">Trajectory Alignment</div>
      <div class="project-card-desc">
        Final estimated trajectory aligned against ground truth to assess overall positional consistency.
      </div>
    </div>
  </div>

  <div class="project-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/slam_3d_trajectory.png" alt="3D trajectory visualization">
    <div class="project-card-body">
      <div class="project-card-title">3D Trajectory Visualization</div>
      <div class="project-card-desc">
        Multi-view trajectory visualization used to inspect motion structure beyond the standard x-z plot.
      </div>
    </div>
  </div>

</div>

### Key validated outcomes
- built a full stereo visual-inertial SLAM pipeline from frontend tracking through backend optimization
- improved trajectory quality significantly over the baseline visual-only odometry pipeline
- demonstrated the effect of IMU-assisted estimation on drift reduction
- added loop closure to enforce global consistency
- generated a sparse 3D landmark map from stereo observations

---

## Technical Stack

- Python
- OpenCV
- NumPy
- SciPy
- EuRoC MAV dataset
- stereo rectification and triangulation
- Lucas-Kanade optical flow
- PnP / visual odometry
- IMU-assisted pose refinement
- bundle adjustment
- pose graph loop closure

---

## Engineering Insights

- frontend quality matters: stable tracking and stereo consistency strongly affect everything downstream
- stereo rectification quality is critical for reliable depth estimation
- IMU information is especially valuable for improving rotational stability and trajectory consistency
- backend optimization adds substantial value beyond raw frame-to-frame odometry
- loop closure is the key transition point from VO to a more complete SLAM system

---

## Future Improvements

- replace parts of the handcrafted frontend with more robust feature management under challenging motion
- improve loop candidate validation and graph edge selection
- extend from sparse mapping toward denser scene reconstruction
- benchmark more rigorously across additional EuRoC sequences and failure cases
- test alternative visual-inertial fusion strategies and compare their effect on long-horizon drift
