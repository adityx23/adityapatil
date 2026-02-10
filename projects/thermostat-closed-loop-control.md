---
title: Closed-Loop Temperature Control (Peltier + TMP117)
---

# Closed-Loop Temperature Control (Peltier + TMP117)

**Project type:** Embedded controls + thermal system modeling  
**Platform:** Arduino Mega + TMP117 + PWM H-bridge + Peltier modules  
**Sampling time:** 500 ms (2 Hz)

## Overview

This project implements a closed-loop temperature regulation system for a custom acrylic enclosure using **Peltier (TEC) modules** driven by PWM through an H-bridge. I modeled the enclosure as a lumped thermal system, designed a compensator in continuous time, discretized it for real-time execution, and deployed it on an **Arduino Mega** with sensor feedback from a **TMP117** temperature sensor.

Unlike typical thermostat projects that rely on PID tuning, this controller was implemented using a **custom discrete-time control equation** derived from a continuous-time compensator and discretized using **Tustin (bilinear) transform**.

---

## Physical Build

- **Enclosure:** 30 × 30 × 30 cm clear acrylic box  
- **Heating:** 4× Peltier plates (hot side facing **inside**, cold side facing **outside**)  
- **Cold-side heat rejection:** external heatsinks attached to the cold side  
- **Actuation:** PWM via H-bridge to Peltier modules  
- **Sensing:** TMP117 temperature sensor **suspended at the geometric center of the enclosure** (mid-air midpoint) to reduce boundary effects

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermostat_build.jpg" alt="Thermostat physical build" width="750">
</p>
<p align="center">
  <em>Physical prototype: acrylic enclosure, Peltier actuation, Arduino Mega control, and TMP117 sensing.</em>
</p>

> **Note:** The sensor was intentionally placed at the center of the enclosure (mid-air) to capture a representative air temperature, rather than a wall/plate temperature.

---

## System Architecture

The system follows a standard closed-loop feedback structure:

- TMP117 measures enclosure temperature
- Controller computes actuation command at **500 ms**
- PWM command drives the H-bridge → Peltier modules
- Thermal dynamics of enclosure determine next temperature

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/feedback_block_diagram.png" alt="Feedback control block diagram" width="750">
</p>
<p align="center">
  <em>Closed-loop feedback structure used for control design and implementation.</em>
</p>

---

## Thermal Model (Plant Intuition)

I approximated the enclosure as a lumped thermal system with:
- Thermal resistances between ambient and enclosure
- An effective thermal capacitance representing stored heat

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermal_lumped_model.png" alt="Thermal lumped model" width="650">
</p>
<p align="center">
  <em>Lumped thermal model used to guide controller design (effective resistance/capacitance).</em>
</p>

---

## Controller Design (Continuous → Discrete)

### Continuous-time compensator
A lead/lag-style compensator was used:

\[
C(s) = 300\frac{(s + 0.05)}{(s + 0.35)}
\]

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/controller_tf.png" alt="Controller transfer function" width="420">
</p>

### Discretization (Tustin)
The controller was discretized using the **Tustin transform** (bilinear transform) for real-time execution.

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/tustin_discretization.png" alt="Tustin discretization output" width="520">
</p>

### Implemented discrete-time equation (500 ms loop)
The deployed controller was implemented as a difference equation using weighted history:

\[
C[k] = 0.9656\,C[k-1] + 295\,(x[k]-x[k-1])
\]

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/discrete_equation.png" alt="Discrete control equation" width="520">
</p>

This formulation gives the controller memory and smoothness without using a PID structure.

---

## Stability & Response (Analysis)

To validate stability margins and expected behavior, I evaluated frequency response and step response characteristics of the designed controller.

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/bode_plot.png" alt="Bode plot" width="720">
</p>
<p align="center">
  <em>Frequency-domain analysis (Bode plot) used to verify stability margins and robustness.</em>
</p>

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/step_response.png" alt="Step response" width="720">
</p>
<p align="center">
  <em>Step response used to sanity-check expected transient behavior for thermal dynamics.</em>
</p>

---

## Embedded Implementation (Arduino Mega)

The controller runs at **500 ms**, computes the new control effort using the discrete update equation, and outputs a saturated PWM command to the H-bridge.

Key implementation details:
- Difference-equation update with persistent state (`C[k-1]`, `x[k-1]`)
- PWM saturation to \[0, 255\] to ensure safe actuation bounds
- Practical switching logic (anti-chatter / hysteresis) to avoid rapid toggling

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/arduino_snippet.png" alt="Arduino control snippet" width="680">
</p>

---

## Engineering Challenges & Fixes

- **Thermal lag + slow dynamics:** thermal systems respond slowly, so controller design emphasized smoothness and robustness rather than aggressive action.
- **Peltier actuation constraints:** PWM/H-bridge control required bounded outputs and stability-aware tuning.
- **Sensor bias avoidance:** placing the TMP117 in mid-air at the enclosure midpoint reduced distortion from wall/contact temperatures.
- **Discrete-time implementation fidelity:** using **Tustin** helped preserve the intended continuous-time controller behavior when running digitally at 500 ms.

---

## What I’d Improve Next

- Add a second sensor near the enclosure wall to quantify gradients and validate lumped-model assumptions.
- Add explicit actuator thermal protection (current sensing / heatsink temperature).
- Compare against a baseline PID implementation for benchmarking, while keeping the same sampling and actuation constraints.
- Automate logging + plotting for repeatable performance evaluation across different setpoints and ambient conditions.

---

## Files / Artifacts

- Physical build photo
- Controller derivation and discretization screenshots
- Bode and step response plots
- Arduino implementation (.ino)

