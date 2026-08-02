---
layout: default
title: STM32 MCU Bring-Up & Robot Control
description: Reverse-engineering and safety-focused embedded control for an Ackermann-steered mobile robot using STM32 and Raspberry Pi.
---

<p class="eyebrow">Embedded Robotics · Systems Debugging</p>
# STM32 MCU Bring-Up: Motor, Steering & Sensor Control

<div class="project-summary">
  <div><strong>Role</strong><span>Embedded systems developer</span></div>
  <div><strong>Context</strong><span>Independent mobile-robot integration</span></div>
  <div><strong>Platform</strong><span>STM32 · Embedded C · Raspberry Pi</span></div>
  <div><strong>Outcome</strong><span>Repeatable safety-gated route execution</span></div>
</div>

<div class="project-links">
  <a class="btn" href="{{ site.baseurl }}/projects">← All Projects</a>
  <a class="btn" href="{{ site.baseurl }}/resume.pdf">Résumé</a>
</div>

## Problem

Bring up an undocumented STM32-based controller for an Ackermann-steered mobile robot without board-level documentation, then establish a safe command path from a Linux route executor to deterministic motor and steering actuation.

<img class="project-media" src="{{ site.baseurl }}/assets/stm32/system-architecture.svg" alt="Architecture showing Raspberry Pi route commands, safety-gated STM32 control, encoder feedback, drive motor, and steering servo" width="1200" height="675" loading="lazy" decoding="async">

## My Contribution

- Reverse-engineered motor, steering, and electrical-polarity mappings using the STM32 datasheet, reference manual, and controlled hardware tests.
- Configured alternate functions, prescalers, PWM channels, encoder inputs, and GPIO directly in the firmware toolchain.
- Wrote motor/servo PWM and encoder drivers behind an explicit arm-before-move sequence.
- Built a Raspberry Pi route-execution layer that armed, issued motion primitives, and logged multi-segment runs.
- Managed iterative STM32CubeCLT, CMake/Ninja, and SWD flashing workflows while preserving safety behavior.

## Safety and Debugging

The command path defaults to a non-moving state. Motion is available only after an explicit arming step, and route commands pass through calibrated primitives rather than raw unbounded PWM values.

Two failures required system-level isolation:

1. A timer-prescaler value of 83 prevented the steering servo from responding. Correcting it to 15 restored the intended PWM timing.
2. Intermittent serial/USB CDC command corruption initially appeared mechanical. Reproducible logging isolated the fault to communication rather than the drivetrain.

## Validation

| Test | Observed result |
|---|---:|
| Straight motion primitive | Approximately 15.24 cm increments |
| Turn primitive | Approximately 59.73° |
| Drift | Near zero in the calibrated test setup |
| Route reliability exercise | 3 consecutive full runs within a 5-run test |

These measurements validate the integrated command path; they are not a complete statistical characterization of the robot across surfaces, loads, or battery conditions.

## Engineering Takeaways

- Board bring-up is an evidence-driven process across schematics, registers, waveforms, and mechanical response.
- Safety state should be explicit and preserved across firmware revisions.
- Reproducible logs are essential when electrical, communication, firmware, and mechanical faults produce similar symptoms.
- Toolchain reliability is part of embedded-system reliability: build, flash, and configuration changes must remain traceable.

## Technical Stack

STM32 (ARM Cortex-M) · Embedded C · STM32CubeCLT · CMake/Ninja · SWD/ST-Link · PWM/timers · quadrature encoders · USB CDC/Serial · Raspberry Pi · Linux

## Next Steps

- Add watchdog-backed command timeouts and explicit fault codes.
- Quantify motion repeatability over more runs and operating conditions.
- Add automated hardware-in-the-loop checks for arming, PWM limits, and encoder direction.
- Publish a sanitized firmware repository when the hardware-specific source package is ready for release.
