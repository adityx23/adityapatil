---
layout: default
title: Closed-Loop Temperature Control (Peltier + TMP117)
---

# Closed-Loop Temperature Control (Peltier + TMP117)

## Overview
Designed and implemented a closed-loop thermal regulation system for a custom acrylic enclosure using Peltier thermoelectric modules and a discrete-time controller deployed on an embedded microcontroller. The controller was derived from a continuous-time compensator using the Tustin transform, enabling stable real-time temperature regulation.

This project demonstrates full-stack control system development, including physical system modeling, controller design, discretization, and embedded deployment.

**Key contributions**
- Modeled enclosure thermal dynamics using lumped parameter approximation  
- Designed continuous-time compensator and discretized it for digital implementation  
- Implemented real-time discrete-time controller on Arduino Mega (500 ms sampling)  
- Integrated PWM-controlled Peltier actuation with closed-loop temperature feedback  

---

## Physical System

**Thermal chamber**
- 30 × 30 × 30 cm acrylic enclosure  

**Actuation**
- 4 × Peltier thermoelectric modules  
- Hot side oriented inward for heating  
- Cold side connected to external heatsinks for heat rejection  
- Actuated via PWM-controlled H-bridge  

**Temperature sensing**
- TMP117 precision temperature sensor  
- Suspended at geometric center of enclosure to minimize measurement bias  

**Embedded controller**
- Arduino Mega executing discrete-time control loop  

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermostat_build.jpg" width="750">
</p>

---

## Control System Architecture

Closed-loop feedback system structure:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/feedback_block_diagram.png" width="750">
</p>

**Control loop execution**
1. TMP117 measures enclosure temperature  
2. Controller computes control effort  
3. PWM signal drives H-bridge and Peltier modules  
4. Thermal system responds, producing next temperature state  

This architecture enables continuous temperature regulation through feedback control.

---

## Thermal System Modeling

The enclosure was approximated as a lumped thermal system characterized by effective thermal resistance and capacitance:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/thermal_lumped_model.png" width="650">
</p>

This abstraction captures dominant thermal dynamics while remaining computationally tractable for controller design and embedded implementation.

---

## Controller Design and Discretization

### Continuous-Time Controller

A compensator was designed in continuous time:

\[
C(s) = 300\frac{(s + 0.05)}{(s + 0.35)}
\]

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/controller_tf.png" width="420">
</p>

This formulation improves system responsiveness while maintaining stability appropriate for slow thermal dynamics.

---

### Discrete-Time Implementation

The controller was discretized using the Tustin (bilinear) transform to enable execution on embedded hardware.

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/tustin_discretization.png" width="520">
</p>

Resulting difference equation:

\[
C[k] = 0.9656\,C[k-1] + 295\,(x[k]-x[k-1])
\]

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/discrete_equation.png" width="520">
</p>

This discrete formulation provides smooth control behavior without relying on conventional PID structure.

---

## Embedded Controller Implementation

Controller was deployed on Arduino Mega with real-time execution:

- Control loop executed every 500 ms  
- Persistent state variables maintained previous system state  
- PWM output used to drive H-bridge and Peltier modules  
- Output saturation applied to maintain safe actuator limits  
- Hysteresis logic implemented to prevent actuator chatter  

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/arduino_snippet.png" width="680">
</p>

---

## System Validation and Analysis

Controller performance validated using both frequency and time-domain analysis:

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/bode_plot.png" width="720">
</p>

<p align="center">
  <img src="{{ site.baseurl }}/assets/thermostat/step_response.png" width="720">
</p>

Analysis confirmed:

- Stable closed-loop system behavior  
- Appropriate transient response for thermal dynamics  
- Successful preservation of continuous-time controller behavior after discretization  

---

## Engineering Challenges and Solutions

**Thermal system latency**
- Thermal systems exhibit slow response and high inertia  
- Solution: designed compensator emphasizing stability and smooth response  

**Continuous-to-discrete controller conversion**
- Discrete implementation must preserve continuous-time behavior  
- Solution: used Tustin transform for stable and accurate discretization  

**Measurement accuracy**
- Temperature readings near enclosure walls introduce bias  
- Solution: suspended sensor at enclosure center for representative measurement  

**Actuator limitations**
- Peltier modules require bounded actuation to avoid instability  
- Solution: implemented PWM saturation and switching logic  

---

## Technical Stack

**Control theory**
- Continuous-time control systems  
- Discrete-time control systems  
- Tustin transform discretization  

**Embedded systems**
- Arduino Mega (C++ embedded implementation)  
- Real-time discrete control loop  

**Hardware integration**
- Peltier thermoelectric modules  
- PWM H-bridge motor driver  
- TMP117 precision temperature sensor  

**System modeling and validation**
- Thermal system modeling  
- Frequency-domain and time-domain analysis  

---

## Future Improvements

- Add multiple temperature sensors for spatial thermal analysis  
- Implement automated performance logging and controller evaluation  
- Compare controller performance against PID-based implementation  
- Add actuator thermal monitoring and protection mechanisms  
