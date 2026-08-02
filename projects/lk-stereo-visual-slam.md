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
  <a class="btn" href="https://github.com/adityx23/aap-slam-orb-nomad-navigation" target="_blank" rel="noopener noreferrer">ORB + NoMaD Repository ↗</a>
</div>

## Overview

Built a stereo visual-inertial SLAM pipeline on the EuRoC MAV dataset, starting from feature tracking and stereo geometry and extending through visual odometry, IMU-assisted estimation, local optimization, loop closure, and sparse 3D mapping.

The final system combined stereo tracking, PnP-based motion estimation, IMU-informed pose refinement, bundle adjustment, and graph-based loop closure to reduce drift and improve global consistency.

An additional **AAP-SLAM-ORB + NoMaD** notebook explores a related ORB-based frame-to-map frontend and converts its keyframes into a topological graph for goal-conditioned navigation. That executed run processed 3,630 EuRoC MH_01_easy frames, achieved 0.9002 m aligned SLAM ATE RMSE, and produced a graph with 244 nodes. Its recorded navigation stage used a documented lightweight NoMaD fallback, so the repository reports the navigation metrics separately from the stronger SLAM result.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_final_result.png" alt="Final SLAM result summary" width="900">
</p>
<p align="center">
  <em>Final result summary showing trajectory alignment, 3D motion structure, and visual-inertial performance improvement.</em>
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
- evaluation using trajectory alignment and error metrics

---

## Frontend: Tracking, Stereo Geometry, and Depth

The frontend used stereo image pairs and tracked visual features across time using Lucas-Kanade optical flow. Stereo correspondences and rectification were used to enforce geometric consistency and recover depth for tracked points.

<div class="figure-grid">

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/stereo_input_pair.png" alt="Stereo input pair">
    <div class="figure-card-body">
      <div class="figure-card-title">Stereo Input</div>
      <div class="figure-card-desc">
        Raw left-right image pair from the EuRoC MAV stereo camera stream.
      </div>
    </div>
  </div>

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/lk_optical_flow_tracking.png" alt="LK optical flow tracking">
    <div class="figure-card-body">
      <div class="figure-card-title">LK Optical Flow Tracking</div>
      <div class="figure-card-desc">
        Frame-to-frame feature tracking used to estimate motion robustly over time.
      </div>
    </div>
  </div>

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/epipolar_orb_validation.png" alt="Epipolar and ORB validation">
    <div class="figure-card-body">
      <div class="figure-card-title">Epipolar Validation</div>
      <div class="figure-card-desc">
        Rectified stereo geometry verified using epipolar alignment and stereo feature consistency.
      </div>
    </div>
  </div>

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/stereo_disparity_map.png" alt="Stereo disparity map">
    <div class="figure-card-body">
      <div class="figure-card-title">Depth from Stereo</div>
      <div class="figure-card-desc">
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
  <em>Baseline stereo visual odometry before visual-inertial refinement and backend optimization.</em>
</p>

The baseline pipeline worked, but accumulated noticeable drift over longer horizons, motivating the addition of IMU-informed estimation and backend optimization.

---

## Visual-Inertial Improvement

To improve rotational stability and overall trajectory consistency, IMU information was incorporated into the pipeline. This produced a substantially tighter trajectory estimate than the visual-only baseline.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/final_trajectory_vs_ground_truth.png" alt="Visual-inertial trajectory alignment" width="900">
</p>
<p align="center">
  <em>Visual-inertial refinement significantly improved alignment with ground truth compared to the original visual-only estimate.</em>
</p>

---

## Backend Optimization

After the frontend and visual-inertial estimation stages, the trajectory was refined using bundle adjustment. Local and sliding-window optimization were used to reduce drift and improve consistency across neighboring poses.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/bundle_adjustment_trajectory.png" alt="Bundle adjustment trajectory improvement" width="700">
</p>
<p align="center">
  <em>Sliding-window bundle adjustment improved local pose consistency and reduced accumulated drift.</em>
</p>

---

## Loop Closure and Pose Graph Refinement

To move from visual odometry toward a true SLAM system, the pipeline added loop closure using keyframes and graph-based trajectory correction. Revisited locations were detected and used to globally adjust the trajectory.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_loop_closure.png" alt="Loop closure trajectory refinement" width="900">
</p>
<p align="center">
  <em>Loop closure introduced global consistency by reconnecting revisited parts of the trajectory and reducing long-horizon drift.</em>
</p>

---

## Sparse 3D Mapping

Alongside trajectory estimation, the system reconstructed a sparse 3D landmark map from tracked stereo features. This demonstrated that the pipeline was simultaneously estimating motion and building a map.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_sparse_3d_map.png" alt="Sparse 3D landmark map" width="900">
</p>
<p align="center">
  <em>Sparse 3D landmark map reconstructed from stereo observations and tracked feature geometry.</em>
</p>

---

## Results and Validation

The final system was evaluated using aligned trajectory comparison and trajectory-error metrics on EuRoC MAV sequences.

<div class="figure-grid">

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/final_trajectory_vs_ground_truth.png" alt="Final trajectory vs ground truth">
    <div class="figure-card-body">
      <div class="figure-card-title">Trajectory Alignment</div>
      <div class="figure-card-desc">
        Final estimated trajectory aligned against ground truth to assess positional consistency.
      </div>
    </div>
  </div>

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/slam_benchmark_results.png" alt="Benchmark results">
    <div class="figure-card-body">
      <div class="figure-card-title">Multi-Sequence Benchmark</div>
      <div class="figure-card-desc">
        Evaluation across EuRoC Machine Hall sequences to test consistency beyond a single run.
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
- visual odometry / pose estimation
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
- compare alternative visual-inertial fusion strategies for long-horizon drift reduction
