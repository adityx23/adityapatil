---
layout: default
title: Closed-Loop Temperature Control (Peltier + TMP117)
---

# Closed-Loop Temperature Control (Peltier + TMP117)

<div class="project-summary">
<strong>Type:</strong> Embedded Control System + Thermal Modeling<br>
<strong>Focus:</strong> Continuous-to-discrete control design, real-time implementation, actuation constraints<br>
<strong>Platform:</strong> Arduino Mega, TMP117, PWM H-bridge, Peltier modules<br>
<strong>Outcome:</strong> Designed a continuous-time compensator, discretized via Tustin, and deployed a difference-equation controller at 500 ms sampling
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← Back to Projects</a>
</div>

## Overview
Designed and implemented a closed-loop temperature regulation system for a custom acrylic enclosure using Peltier thermoelectric modules and a discrete-time controller derived from continuous-time control theory. The controller was discretized using the **Tustin transform** and deployed on an embedded microcontroller, enabling stable real-time regulation without relying on a standard PID formulation.

**Key contributions**
- Modeled enclosure thermal dynamics using a lumped parameter approximation  
- Designed a continuous-time compensator and discretized it for embedded execution  
- Implemented a real-time discrete-time controller on Arduino Mega (500 ms sampling)  
- Integrated PWM-controlled Peltier actuation through an H-bridge with closed-loop feedback  

---

## Physical System
**Thermal chamber**
- 30 × 30 × 30 cm acrylic enclosure  

**Actuation**
- 4 × Peltier (TEC) modules  
- Hot side facing inward, cold side outward  
- External heatsinks for heat rejection  
- PWM control via H-bridge driver  

**Sensing**
- TMP117 precision temperature sensor suspended at the geometric center (mid-air) to reduce boundary bias  

**Controller hardware**
- Arduino Mega executing the control loop at 500 ms  

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermostat_build.jpg" width="750">
</p>

---

## Control System Architecture
Closed-loop feedback structure:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/feedback_block_diagram.png" width="750">
</p>

**Control loop**
1. TMP117 measures enclosure air temperature  
2. Controller computes control effort at each sample  
3. PWM drives H-bridge and Peltier modules  
4. Thermal dynamics produce next temperature state  

---

## Thermal System Modeling
Approximated the enclosure as a lumped thermal system with effective resistance and capacitance:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermal_lumped_model.png" width="650">
</p>

This abstraction captures dominant thermal dynamics while remaining tractable for controller design and embedded implementation.

---

## Controller Design and Discretization

### Continuous-time compensator
\[
C(s) = 300\frac{(s + 0.05)}{(s + 0.35)}
\]

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/controller_tf.png" width="420">
</p>

### Discretization (Tustin)
Controller discretized using bilinear transform for digital execution at 500 ms sampling:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/tustin_discretization.png" width="520">
</p>

Resulting implemented difference equation:

\[
C[k] = 0.9656\,C[k-1] + 295\,(x[k]-x[k-1])
\]

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/discrete_equation.png" width="520">
</p>

---

## Embedded Implementation
Controller deployed on Arduino Mega with real-time execution:
- 500 ms loop timing  
- Persistent state for previous control effort and error terms  
- PWM saturation to maintain safe actuator bounds  
- Hysteresis / anti-chatter logic to reduce rapid switching  

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/arduino_snippet.png" width="680">
</p>

---

## Validation and Analysis
Validated expected closed-loop behavior using frequency and time-domain analysis:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/bode_plot.png" width="720">
</p>

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/step_response.png" width="720">
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
- Deployed a theory-driven controller on embedded hardware at 500 ms sampling  
- Demonstrated stable closed-loop regulation architecture using PWM actuation  
- Established an end-to-end workflow from modeling → controller design → discretization → embedded deployment  

---

## Technical Stack
- Continuous and discrete-time control systems
- Tustin transform discretization
- Arduino (embedded C++)
- PWM + H-bridge actuation
- Thermal system modeling
- TMP117 sensor integration

---

## Future Improvements
- Add multi-point sensing to measure gradients and validate lumped-model assumptions  
- Automate logging/plotting for repeatable evaluation across setpoints  
- Benchmark against PID baseline under identical constraints  
- Add actuator thermal monitoring and protection  
