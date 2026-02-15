---
layout: default
title: Closed-Loop Temperature Control (Peltier + TMP117)
---

# Closed-Loop Temperature Control (Peltier + TMP117)

## Overview

Designed and implemented a closed-loop temperature regulation system for a custom acrylic enclosure using Peltier thermoelectric modules and a discrete-time controller derived from continuous-time control theory.

Unlike conventional PID-based thermostats, this system uses a **custom compensator discretized using the Tustin transform and deployed on an embedded microcontroller**, demonstrating full-stack integration of physical modeling, control design, and real-time embedded implementation.

**Key Contributions**
- Modeled enclosure thermal dynamics using lumped parameter approximation
- Designed continuous-time compensator and discretized for embedded execution
- Implemented real-time controller on Arduino Mega at 500 ms sampling
- Integrated PWM-controlled Peltier actuation with closed-loop feedback

---

## Physical System

**Enclosure**
- 30 × 30 × 30 cm acrylic thermal chamber

**Actuation**
- 4 × Peltier (TEC) modules
- Hot side facing inward, cold side outward
- Heat rejection via external heatsinks
- PWM control through H-bridge driver

**Sensing**
- TMP117 precision temperature sensor
- Suspended at geometric center to minimize boundary bias

**Controller Hardware**
- Arduino Mega executing real-time control loop (500 ms)

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermostat_build.jpg" width="750">
</p>

---

## Control Architecture

Closed-loop feedback structure:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/feedback_block_diagram.png" width="750">
</p>

**Control loop**
1. TMP117 measures enclosure temperature
2. Controller computes actuation command
3. PWM drives H-bridge and Peltier modules
4. Thermal dynamics determine next temperature

---

## Thermal System Modeling

The enclosure was modeled as a lumped thermal system with effective resistance and capacitance:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermal_lumped_model.png" width="650">
</p>

This abstraction captures dominant thermal dynamics while remaining computationally tractable for controller design.

---

## Controller Design

### Continuous-Time Compensator

\[
C(s) = 300\frac{(s + 0.05)}{(s + 0.35)}
\]

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/controller_tf.png" width="420">
</p>

This compensator improves system responsiveness while maintaining stability margins appropriate for slow thermal dynamics.

---

### Discretization (Tustin Transform)

Controller was discretized using the bilinear transform for digital execution:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/tustin_discretization.png" width="520">
</p>

Resulting difference equation implemented at 500 ms sampling:

\[
C[k] = 0.9656\,C[k-1] + 295\,(x[k]-x[k-1])
\]

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/discrete_equation.png" width="520">
</p>

This structure provides smooth control action without relying on PID formulation.

---

## Stability and Performance Analysis

Frequency and time-domain analysis validated controller behavior:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/bode_plot.png" width="720">
</p>

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/step_response.png" width="720">
</p>

Analysis confirmed stable operation and appropriate transient response for thermal system dynamics.

---

## Embedded Implementation

Controller deployed on Arduino Mega with real-time execution:

- 500 ms control loop
- Persistent state variables for discrete equation
- PWM output saturation to ensure safe operation
- Hysteresis logic to prevent actuator chatter

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/arduino_snippet.png" width="680">
</p>

---

## Engineering Challenges and Solutions

**Thermal system latency**
- Slow thermal dynamics required stability-focused controller design
- Addressed through compensator design rather than aggressive gain tuning

**Discrete implementation fidelity**
- Tustin discretization preserved continuous-time controller behavior

**Sensor placement accuracy**
- Center placement avoided wall-induced thermal bias

**Actuator constraints**
- PWM saturation and switching logic ensured safe and stable operation

---

## Results

- Successfully deployed physics-based controller on embedded hardware
- Demonstrated stable closed-loop temperature regulation
- Validated continuous-to-discrete control design workflow
- Established reproducible embedded controls architecture

---

## Technical Stack

- Control theory (continuous and discrete-time systems)
- Tustin transform discretization
- Embedded C++ (Arduino)
- PWM motor control
- Thermal system modeling
- TMP117 sensor integration

---

## Future Improvements

- Multi-point temperature sensing for spatial validation
- Automated performance logging and analysis
- Comparative evaluation against PID control
- Improved actuator thermal monitoring
