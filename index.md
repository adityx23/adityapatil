---
layout: default
title: Aditya Patil
description: NYU M.S. Robotics student and AI4CE researcher building embedded, autonomous, and learning-enabled robotic systems.
---

<section class="hero">
  <p class="eyebrow">NYU M.S. Robotics · AI4CE Researcher</p>
  <h1>Robotics systems from firmware to autonomy.</h1>
  <p class="hero-sub">
    I build and debug complete robotic systems across <strong>embedded control</strong>,
    <strong>state estimation</strong>, and <strong>robot learning</strong>—from STM32 bring-up and CAN-based actuation
    to visual-inertial SLAM and language-conditioned policies.
  </p>
  <div class="hero-links">
    <a class="btn btn-primary" href="{{ site.baseurl }}/projects">View Projects →</a>
    <a class="btn" href="{{ site.baseurl }}/resume.pdf">Résumé</a>
    <a class="btn" href="https://github.com/adityx23" target="_blank" rel="noopener noreferrer">GitHub</a>
    <a class="btn" href="https://www.linkedin.com/in/aditya-patil-4a5735217" target="_blank" rel="noopener noreferrer">LinkedIn</a>
    <a class="btn" href="mailto:aditya.a.patil2@gmail.com">Email</a>
  </div>
</section>

<section class="metric-grid" aria-label="Selected engineering outcomes">
  <div class="metric"><strong>0.031 m</strong><span>best reported SLAM trajectory error after optimization</span></div>
  <div class="metric"><strong>3,630</strong><span>EuRoC frames processed in ORB frame-to-map evaluation</span></div>
  <div class="metric"><strong>33 Hz</strong><span>embedded drivetrain telemetry logging rate</span></div>
  <div class="metric"><strong>3 stacks</strong><span>firmware, estimation, and robot-learning depth</span></div>
</section>

<div class="section-heading">
  <div>
    <p class="eyebrow">Selected Work</p>
    <h2>Systems engineering in evidence</h2>
  </div>
  <p>Three projects that best show hardware ownership, algorithmic depth, and end-to-end validation.</p>
</div>

<section class="featured-grid" aria-label="Featured projects">
  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/stm32-robot-control-system">
      <img src="{{ site.baseurl }}/assets/stm32/system-architecture.svg" alt="STM32 robot-control stack from Raspberry Pi commands to drive and steering actuation" width="1200" height="675">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">STM32</span><span class="tag">Embedded C</span><span class="tag">Linux</span></div>
        <h3 class="project-card-title">STM32 MCU Bring-Up & Robot Control</h3>
        <p class="project-card-desc">Reverse-engineered an undocumented controller, wrote safety-gated motor and servo drivers, and validated repeatable route execution.</p>
        <span class="project-card-cta">Read case study →</span>
      </div>
    </a>
  </article>

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/lk-stereo-visual-slam">
      <img src="{{ site.baseurl }}/assets/lk_slam/slam_final_result.png" alt="Stereo visual-inertial SLAM trajectory and evaluation summary" width="2428" height="1975" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">OpenCV</span><span class="tag">IMU Fusion</span><span class="tag">Optimization</span></div>
        <h3 class="project-card-title">Stereo Visual-Inertial SLAM</h3>
        <p class="project-card-desc">Built a full EuRoC pipeline from stereo tracking through bundle adjustment, loop closure, and sparse mapping.</p>
        <span class="project-card-cta">Read case study →</span>
      </div>
    </a>
  </article>

  <article class="project-card">
    <a href="{{ site.baseurl }}/projects/ecu-automatic-transmission-controller">
      <img src="{{ site.baseurl }}/assets/ecu/drivetrain-hardware.png" alt="Annotated physical three-speed drivetrain and shift mechanism" width="1536" height="2040" loading="lazy" decoding="async">
      <div class="project-card-body">
        <div class="tag-list"><span class="tag">Embedded Control</span><span class="tag">Telemetry</span><span class="tag">Hardware</span></div>
        <h3 class="project-card-title">Automatic Transmission Controller</h3>
        <p class="project-card-desc">Integrated a physical 24 V drivetrain with concurrent sensing, encoder-tracked shifting, data logging, and efficiency analysis.</p>
        <span class="project-card-cta">Read case study →</span>
      </div>
    </a>
  </article>
</section>

<div class="section-heading">
  <div>
    <p class="eyebrow">Current Experience</p>
    <h2>Research at NYU CREO / AI4CE</h2>
  </div>
</div>

<section class="experience-card">
  <div>
    <h3>Student Researcher</h3>
    <p>CREO / AI4CE Lab · NYU</p>
    <p>May 2026–Present</p>
  </div>
  <div>
    <ul>
      <li>Support multi-camera teleoperation dataset pipelines and Linux hardware/firmware diagnostics.</li>
      <li>Patched a PD + feedforward-torque command path, correcting torque encoding, mode activation, and CAN frame structure for safe manipulator actuation.</li>
      <li>Contribute to research on vision-language-action and vision-language models for a dual-arm mobile manipulator.</li>
    </ul>
  </div>
  <div class="experience-media">
    <figure class="experience-media-item experience-media-photo">
      <img src="{{ site.baseurl }}/assets/ai4ce/yor-platform.jpg" alt="YOR dual-arm mobile manipulator in the NYU robotics lab" width="1200" height="1594" loading="lazy" decoding="async">
      <figcaption>YOR, the dual-arm mobile manipulator used in CREO / AI4CE research.</figcaption>
    </figure>
    <figure class="experience-media-item">
      <video controls muted playsinline preload="metadata" poster="{{ site.baseurl }}/assets/ai4ce/yor-manipulation-poster.jpg" aria-label="YOR dual-arm robot manipulation demonstration">
        <source src="{{ site.baseurl }}/assets/ai4ce/yor-manipulation-demo.mp4" type="video/mp4">
        Your browser does not support embedded video.
      </video>
      <figcaption>YOR manipulation demonstration during lab integration and testing.</figcaption>
    </figure>
  </div>
</section>

<div class="section-heading">
  <div>
    <p class="eyebrow">Background</p>
    <h2>Education and direction</h2>
  </div>
</div>

<section class="experience-card">
  <div>
    <h3>New York University</h3>
    <p>M.S. Robotics, Mechatronics Track</p>
    <p>Expected May 2027</p>
  </div>
  <div>
    <p>I am targeting robotics systems, embedded robotics, autonomy, controls, and robot-learning roles where I can connect algorithms to reliable hardware behavior.</p>
    <div class="hero-links">
      <a class="btn" href="{{ site.baseurl }}/skills">Technical Skills</a>
      <a class="btn" href="{{ site.baseurl }}/projects">All Projects</a>
    </div>
  </div>
</section>
