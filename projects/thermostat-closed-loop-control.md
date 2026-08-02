---
layout: default
title: Closed-Loop Temperature Control (Peltier + TMP117)
description: Thermal modeling, loop-shaping controller design, Tustin discretization, and Arduino deployment for a Peltier-heated enclosure.
---

# Closed-Loop Temperature Control (Peltier + TMP117)

<div class="project-summary">
  <div><strong>Role</strong><span>Controls and embedded implementation · Group 15</span></div>
  <div><strong>Context</strong><span>NYU ROB-GY 5103 Mechatronics</span></div>
  <div><strong>Platform</strong><span>Arduino Mega · TMP117 · Peltier heating</span></div>
  <div><strong>Outcome</strong><span>70 °F toward 77 °F closed-loop test</span></div>
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← All Projects</a>
  <a class="btn" href="https://github.com/adityx23/closed-loop-temperature-control-system" target="_blank" rel="noopener noreferrer">GitHub Repository ↗</a>
</div>

## Overview
Designed and implemented a closed-loop temperature regulation system for a custom acrylic enclosure using Peltier thermoelectric modules and a discrete-time controller derived from continuous-time control theory. The controller was discretized using the **Tustin transform** and deployed on an embedded microcontroller, enabling stable real-time regulation without relying on a standard PID formulation.

**Key contributions**
- Modeled enclosure thermal dynamics using a lumped parameter approximation  
- Designed a continuous-time compensator and discretized it for embedded execution  
- Implemented a real-time discrete-time controller on Arduino Mega
- Integrated PWM-controlled Peltier heating with closed-loop feedback

---

## Physical System
**Thermal chamber**
- 30 × 30 × 30 cm acrylic enclosure  

**Actuation**
- 4 × Peltier (TEC) modules  
- Hot side facing inward, cold side outward  
- External heatsinks for heat rejection  
- PWM control in heating mode

**Sensing**
- TMP117 precision temperature sensor suspended at the geometric center (mid-air) to reduce boundary bias  

**Controller hardware**
- Arduino Mega executing the control loop and multiplexing two temperature displays

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermostat_build.jpg" alt="Completed acrylic temperature-control enclosure with Peltier modules, sensor, displays, and Arduino electronics" width="750" height="795" loading="lazy" decoding="async">
</p>

---

## Control System Architecture
Closed-loop feedback structure:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/feedback_block_diagram.png" alt="Closed-loop temperature-control block diagram" width="750" loading="lazy" decoding="async">
</p>

**Control loop**
1. TMP117 measures enclosure air temperature  
2. Controller computes control effort at each sample  
3. PWM drives the Peltier heating modules
4. Thermal dynamics produce next temperature state  

---

## Thermal System Modeling
Approximated the enclosure as a lumped thermal system with effective resistance and capacitance:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermal_lumped_model.png" alt="Lumped thermal resistance and capacitance model of the enclosure" width="650" loading="lazy" decoding="async">
</p>

This abstraction captures dominant thermal dynamics while remaining tractable for controller design and embedded implementation.

---

## Controller Design and Discretization

### Continuous-time compensator
<div class="equation" role="math" aria-label="C of s equals 300 times s plus 0.05 divided by s plus 0.35">
  C(s) = 300 · (s + 0.05) / (s + 0.35)
</div>

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/controller_tf.png" alt="Continuous-time controller transfer function" width="420" loading="lazy" decoding="async">
</p>

### Discretization (Tustin)
Controller discretized using a bilinear transform with a 0.1 s design interval:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/tustin_discretization.png" alt="Tustin discretization result for the controller" width="520" loading="lazy" decoding="async">
</p>

Resulting implemented difference equation:

<div class="equation" role="math" aria-label="C at sample k equals 0.9656 times the previous C plus 295 times the change in error">
  C[k] = 0.9656 C[k−1] + 295 (x[k] − x[k−1])
</div>

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/discrete_equation.png" alt="Discrete-time controller difference equation" width="520" loading="lazy" decoding="async">
</p>

---

## Embedded Implementation
Controller deployed on Arduino Mega with real-time execution:
- Persistent state for previous control effort and error terms  
- PWM saturation to maintain safe actuator bounds  
- Potentiometer-adjustable 50–80 °F setpoint
- Dual multiplexed displays for setpoint and measured temperature

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/arduino_snippet.png" alt="Arduino implementation of the stateful controller and saturated PWM output" width="680" loading="lazy" decoding="async">
</p>

---

## Validation and Analysis
Validated expected closed-loop behavior using frequency and time-domain analysis:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/bode_plot.png" alt="Compensated open-loop Bode magnitude and phase plot" width="720" loading="lazy" decoding="async">
</p>

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/step_response.png" alt="Modeled closed-loop temperature step response" width="720" loading="lazy" decoding="async">
</p>

---

## Engineering Challenges and Solutions
**Thermal latency and slow dynamics**
- Required stability-focused design and smooth control effort  
- Addressed via compensator design rather than aggressive gain  

**Continuous-to-discrete fidelity**
- Needed discrete implementation to preserve continuous-time behavior  
- Tustin discretization helped maintain stability and response shape  

**Measurement bias**
- Wall and surface temperature bias avoided by suspending sensor at enclosure midpoint  

**Actuation constraints**
- PWM saturation and switching logic implemented to keep control stable and safe  

---

## Results
- Deployed a theory-driven controller on embedded hardware
- Demonstrated stable closed-loop regulation architecture using PWM actuation  
- Raised the enclosure temperature from approximately 70 °F toward a 77 °F setpoint during experimental validation
- Established an end-to-end workflow from modeling → controller design → discretization → embedded deployment  

---

## Technical Stack
- Continuous and discrete-time control systems
- Tustin transform discretization
- Arduino (embedded C++)
- PWM Peltier heating
- Thermal system modeling
- TMP117 sensor integration

---

## Future Improvements
- Add multi-point sensing to measure gradients and validate lumped-model assumptions  
- Automate logging/plotting for repeatable evaluation across setpoints  
- Benchmark against PID baseline under identical constraints  
- Add actuator thermal monitoring and protection  
- Add active cooling to reduce overshoot and support bidirectional regulation
