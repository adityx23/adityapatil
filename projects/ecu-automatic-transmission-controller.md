---
layout: default
title: Embedded ECU-Style Automatic Transmission Controller
---

# Embedded ECU-Style Automatic Transmission Controller

<div class="project-summary">
<strong>Type:</strong> Embedded Drivetrain Control + Mechatronic System Integration<br>
<strong>Focus:</strong> Concurrent sensing, automatic shift logic, encoder-based actuation, performance analysis<br>
<strong>Platform:</strong> Parallax Propeller Activity Board, Propeller C, external ADC, Python, Jupyter<br>
<strong>Outcome:</strong> Integrated a three-speed drivetrain test platform that measures two RPM channels and motor current, executes automatic shifts, and evaluates motor performance across operating conditions
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← Back to Projects</a>
  <a class="btn" href="https://github.com/adityx23/ecu-automatic-transmission-controller" target="_blank" rel="noopener">GitHub Repository ↗</a>
</div>

## Overview

Developed an embedded ECU-style controller for a physical drivetrain test platform. The system acquires motor RPM, output RPM, and current; applies automatic three-gear shift logic; drives a bidirectional encoder-tracked shift actuator; sweeps the operating point through a digital potentiometer; and displays live telemetry.

The project combines real-time embedded control with Python analysis of motor voltage, current, speed, load, and calculated efficiency.

**Key contributions**
- integrated three concurrent sensing and actuation tasks on a multicore Propeller microcontroller
- implemented thresholded pulse timing for two independent RPM channels
- designed three-gear automatic shifting with separate upshift and downshift thresholds
- closed the shift-position loop using motor direction and encoder ticks
- built notebook workflows for comparing drivetrain performance and efficiency across experimental runs
- documented the firmware, hardware interfaces, analysis dependencies, and known safety limitations in a public repository

---

## Hardware Demonstration

<video class="project-video" controls preload="metadata">
  <source src="{{ site.baseurl }}/assets/ecu/demo.mp4" type="video/mp4">
  Your browser does not support embedded MP4 video. <a href="{{ site.baseurl }}/assets/ecu/demo.mp4">Download the demonstration</a>.
</video>

---

## System Architecture

The firmware partitions work across independent Propeller cogs:

1. **ADC sensing task** samples two RPM channels and motor current.
2. **Encoder task** tracks signed transmission-selector motion.
3. **Potentiometer task** sweeps the drivetrain operating point.
4. **Main control loop** selects gears and refreshes the telemetry display.

The external ADC receives analog motor-speed, output-speed, and current signals. The controller converts threshold crossings into RPM estimates, evaluates the active gear against calibrated thresholds, and commands a bidirectional shift motor. Encoder feedback determines when the requested gear displacement has been reached.

---

## Automatic Shift Strategy

| Transition | Shift condition |
|---|---:|
| Gear 1 → Gear 2 | Motor speed ≥ 600 RPM |
| Gear 2 → Gear 3 | Motor speed ≥ 1,400 RPM |
| Gear 3 → Gear 2 | Motor speed ≤ 1,200 RPM |
| Gear 2 → Gear 1 | Motor speed ≤ 400 RPM |

Using different upshift and downshift thresholds introduces hysteresis, preventing repeated gear changes near a single boundary. Adjacent shifts use calibrated signed encoder displacements; the archived firmware uses 100 ticks per transition.

---

## Sensing and Telemetry

The controller monitors:

- motor-side RPM
- output-side RPM
- motor current
- current gear
- shift-motor encoder position

RPM is estimated from the time between analog threshold crossings, with separate high and low thresholds to reject repeated detections from one pulse. The live display reports both RPM values and selected gear at a fixed screen position.

---

## Performance and Efficiency Analysis

The analysis notebooks compare motor voltage, current, motor RPM, output RPM, load condition, and calculated system efficiency across multiple experimental logs.

<p align="center">
  <img src="{{ site.baseurl }}/assets/ecu/efficiency-comparison.png" alt="Comparison plots for motor voltage, current, motor RPM, output RPM, and calculated efficiency across three drivetrain runs" width="950">
</p>

The plots show how motor current rises and then levels with increasing speed, while the calculated efficiency varies across operating points and experimental conditions. These comparisons provide a basis for selecting gear and operating regions using measured drivetrain behavior instead of shift speed alone.

The archived project folder did not contain the raw CSV logs referenced by the notebooks. The public repository therefore retains the notebook outputs as evidence and identifies the expected data columns, but fully regenerating the plots requires restoring those logs.

---

## Engineering Challenges

**Concurrent embedded tasks**
- sensing, encoder tracking, potentiometer control, shifting, and display updates must operate without losing speed pulses
- independent Propeller cogs isolate time-sensitive acquisition from the main shift loop

**Stable gear selection**
- a single RPM threshold can cause gear hunting near the transition point
- distinct upshift and downshift thresholds introduce useful hysteresis

**Mechanical shift positioning**
- the controller needs repeatable selector displacement despite motor direction changes
- signed encoder ticks provide feedback for adjacent gear movements

**Experimental interpretation**
- voltage, current, speed, load, and efficiency must be compared across multiple runs
- the notebooks overlay operating paths and generate multi-variable performance plots

---

## Technical Stack

- Propeller C / SimpleIDE
- Parallax Propeller Activity Board
- external SPI ADC
- analog RPM and current sensing
- DC motor and encoder feedback
- digital potentiometer control
- multicore embedded task execution
- Python, pandas, NumPy, Matplotlib, and SciPy
- Jupyter notebooks

---

## Limitations and Next Steps

- add shift-motion timeouts and physical limit validation so an actuator fault cannot block indefinitely
- calibrate the RPM conversion against a reference tachometer and document pulses per revolution
- replace fixed encoder displacements with per-gear calibration and fault detection
- snapshot shared sensor state explicitly before control decisions
- restore the raw CSV logs and formalize the efficiency calculation pipeline
- separate hardware drivers, transmission control, and telemetry into testable firmware modules
