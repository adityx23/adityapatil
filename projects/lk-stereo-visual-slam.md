---
layout: default
title: Stereo Visual-Inertial SLAM with Optimization and Loop Closure
description: Stereo visual-inertial SLAM on EuRoC with feature tracking, IMU fusion, bundle adjustment, loop closure, and sparse mapping.
project: true
image: /assets/thumbnails/lk-slam.webp
repository: https://github.com/adityx23/aap-slam-orb-nomad-navigation
date_modified: 2026-08-08
technologies: [Python, OpenCV, SciPy, EuRoC, Visual-Inertial Odometry]
built: Stereo visual-inertial and ORB frame-to-map evaluation notebooks covering tracking, geometry, PnP motion estimation, optimization, loop closure, sparse mapping, and topological navigation.
validated: A fresh 29-cell rerun completed without errors: the scoped 200-frame run improved ATE from 0.1924 m to 0.0304 m, while the three-sequence benchmark measured 0.2364 m, 0.1690 m, and 0.3405 m ATE.
why: Shows algorithmic depth from perception frontend through estimation backend and quantitative trajectory evaluation.
previous_project_url: /projects/ackermann-autonomous-robot
previous_project_title: Ackermann Robot Bring-Up & Native Autonomy
next_project_url: /projects/ecu-automatic-transmission-controller
next_project_title: Automatic Transmission Controller
---

# Stereo Visual-Inertial SLAM with Optimization and Loop Closure

<div class="project-summary">
  <div><strong>Role</strong><span>Perception pipeline and evaluation</span></div>
  <div><strong>Context</strong><span>Independent SLAM implementation</span></div>
  <div><strong>Platform</strong><span>Python · OpenCV · SciPy · EuRoC</span></div>
  <div><strong>Outcome</strong><span>0.0304 m scoped ATE · 0.2486 m three-sequence mean</span></div>
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← All Projects</a>
  <a class="btn" href="https://github.com/adityx23/aap-slam-orb-nomad-navigation" target="_blank" rel="noopener noreferrer">ORB + NoMaD Repository ↗</a>
</div>

{% include project-tldr.html %}

## Overview

Built a stereo visual-inertial SLAM pipeline on the EuRoC MAV dataset, starting from feature tracking and stereo geometry and extending through visual odometry, IMU-assisted estimation, local optimization, loop closure, and sparse 3D mapping.

The notebooks combine stereo tracking, PnP-based motion estimation, IMU-informed pose refinement, bundle adjustment, and graph-based loop-closure experiments. They retain both improvements and negative results: the strongest short-window run improves substantially, while some full-sequence optimization variants provide little benefit or increase error.

An additional **AAP-SLAM-ORB + NoMaD** notebook explores a related ORB-based frame-to-map frontend and converts its keyframes into a topological graph for goal-conditioned navigation. Its executed run processed 3,630 EuRoC MH_01_easy frames, achieved 0.9002 m aligned SLAM ATE RMSE, and produced a graph with 244 nodes. The repository includes both the supplied real-`nomad.pth` run and an alternate architecture notebook documenting the earlier lightweight fallback.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_final_result.png" alt="Final SLAM result summary" width="900" loading="lazy" decoding="async">
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
    <img src="{{ site.baseurl }}/assets/lk_slam/stereo_input_pair.png" alt="Stereo input pair" loading="lazy" decoding="async">
    <div class="figure-card-body">
      <div class="figure-card-title">Stereo Input</div>
      <div class="figure-card-desc">
        Raw left-right image pair from the EuRoC MAV stereo camera stream.
      </div>
    </div>
  </div>

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/lk_optical_flow_tracking.png" alt="LK optical flow tracking" loading="lazy" decoding="async">
    <div class="figure-card-body">
      <div class="figure-card-title">LK Optical Flow Tracking</div>
      <div class="figure-card-desc">
        Frame-to-frame feature tracking used to estimate motion robustly over time.
      </div>
    </div>
  </div>

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/epipolar_orb_validation.png" alt="Epipolar and ORB validation" loading="lazy" decoding="async">
    <div class="figure-card-body">
      <div class="figure-card-title">Epipolar Validation</div>
      <div class="figure-card-desc">
        Rectified stereo geometry verified using epipolar alignment and stereo feature consistency.
      </div>
    </div>
  </div>

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/stereo_disparity_map.png" alt="Stereo disparity map" loading="lazy" decoding="async">
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
  <img src="{{ site.baseurl }}/assets/lk_slam/baseline_vo_trajectory.png" alt="Baseline visual odometry trajectory" width="700" loading="lazy" decoding="async">
</p>
<p align="center">
  <em>Baseline stereo visual odometry before visual-inertial refinement and backend optimization.</em>
</p>

The baseline pipeline worked, but accumulated noticeable drift over longer horizons, motivating the addition of IMU-informed estimation and backend optimization.

---

## Visual-Inertial Improvement

To improve rotational stability and overall trajectory consistency, IMU information was incorporated into the pipeline. This produced a substantially tighter trajectory estimate than the visual-only baseline.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/final_trajectory_vs_ground_truth.png" alt="Visual-inertial trajectory alignment" width="900" loading="lazy" decoding="async">
</p>
<p align="center">
  <em>Visual-inertial refinement significantly improved alignment with ground truth compared to the original visual-only estimate.</em>
</p>

---

## Backend Optimization

After the frontend and visual-inertial estimation stages, local and sliding-window bundle adjustment reduced reprojection error in the optimized windows. In the fresh run, this did not improve global ATE, reinforcing the distinction between local objective improvement and trajectory accuracy.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/bundle_adjustment_trajectory.png" alt="Bundle adjustment trajectory improvement" width="700" loading="lazy" decoding="async">
</p>
<p align="center">
  <em>Sliding-window bundle adjustment reduced local reprojection error; global ATE remained approximately unchanged.</em>
</p>

---

## Loop Closure and Pose Graph Refinement

The pipeline also evaluates loop closure using keyframes and graph-based trajectory correction. The fresh run detected 65 loop edges, but the resulting optimization worsened aligned MH_01 trajectory error from 0.2317 m to 0.3300 m. This identifies loop validation and constraint weighting as unresolved engineering work.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_loop_closure.png" alt="Loop closure trajectory refinement" width="900" loading="lazy" decoding="async">
</p>
<p align="center">
  <em>Negative result: graph cost fell by 60%, while aligned ATE increased by 42.4%.</em>
</p>

---

## Sparse 3D Mapping

Alongside trajectory estimation, the system reconstructed a sparse 3D landmark map from tracked stereo features. This demonstrated that the pipeline was simultaneously estimating motion and building a map.

<p align="center">
  <img src="{{ site.baseurl }}/assets/lk_slam/slam_sparse_3d_map.png" alt="Sparse 3D landmark map" width="900" loading="lazy" decoding="async">
</p>
<p align="center">
  <em>Sparse 3D landmark map reconstructed from stereo observations and tracked feature geometry.</em>
</p>

---

## Results and Validation

The notebook was rerun from a fresh kernel on August 8, 2026; all 29 cells completed without an error output. Results depend strongly on evaluation length and configuration. The tightly coupled 200-frame run over frames 50–249 improved ATE from 0.1924 m to 0.0304 m. The full-sequence benchmark measured 0.2364 m on MH_01_easy, 0.1690 m on MH_02_easy, and 0.3405 m on MH_03_medium, for a mean of 0.2486 m.

The fresh full-sequence loop-closure experiment found 65 loop edges but worsened MH_01 ATE from 0.2317 m to 0.3300 m (+42.4%). It is retained as a negative result showing that reducing an internal pose-graph cost does not guarantee better aligned trajectory accuracy.

<div class="figure-grid">

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/slam_final_result.png" alt="Fresh scoped SLAM v3 evaluation" loading="lazy" decoding="async">
    <div class="figure-card-body">
      <div class="figure-card-title">Trajectory Alignment</div>
      <div class="figure-card-desc">
        Fresh 200-frame tightly coupled evaluation: 0.1924 m baseline ATE reduced to 0.0304 m.
      </div>
    </div>
  </div>

  <div class="figure-card">
    <img src="{{ site.baseurl }}/assets/lk_slam/slam_benchmark_results.png" alt="Benchmark results" loading="lazy" decoding="async">
    <div class="figure-card-body">
      <div class="figure-card-title">Multi-Sequence Benchmark</div>
      <div class="figure-card-desc">
        Fresh full-sequence results: 0.2364 m on MH_01, 0.1690 m on MH_02, and 0.3405 m on MH_03.
      </div>
    </div>
  </div>

</div>

### Key validated outcomes
- built a full stereo visual-inertial SLAM pipeline from frontend tracking through backend optimization
- improved trajectory quality significantly in the scoped 200-frame tightly coupled experiment
- demonstrated the effect of IMU-assisted estimation on drift reduction
- evaluated loop closure and documented that the current constraint design worsens full-sequence ATE
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
- backend optimization can add value, but must be validated against trajectory metrics rather than internal cost alone
- loop closure requires stronger geometric validation and weighting before it improves this full-sequence result

---

## Future Improvements

- replace parts of the handcrafted frontend with more robust feature management under challenging motion
- improve loop candidate validation and graph edge selection
- extend from sparse mapping toward denser scene reconstruction
- benchmark more rigorously across additional EuRoC sequences and failure cases
- compare alternative visual-inertial fusion strategies for long-horizon drift reduction

{% include project-footer.html %}
