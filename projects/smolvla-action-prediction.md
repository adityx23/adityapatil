---
layout: default
title: SmolVLA for Language-Conditioned Robot Action Prediction
---

# SmolVLA for Language-Conditioned Robot Action Prediction

<div class="project-summary">
<strong>Type:</strong> Robot Learning / Vision-Language-Action<br>
<strong>Focus:</strong> Language grounding, action consistency, instruction sensitivity, temporal behavior<br>
<strong>Platform:</strong> Python, Transformers, LeRobot, SmolVLA-450M, BridgeV2<br>
<strong>Outcome:</strong> Analyzed a pretrained VLA model on real robot drawer manipulation and quantified action separation, temporal consistency, and instruction-conditioned behavior
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← Back to Projects</a>
</div>

## Overview

Applied **SmolVLA-450M**, a pretrained vision-language-action model, to **BridgeV2** real robot manipulation trajectories to study how language instructions influence predicted actions in drawer opening and closing tasks.

The project focused on whether the model produced physically meaningful action differences across instructions, how consistent its predicted actions were across similar episodes, and how its temporal behavior evolved during a manipulation sequence.

---

## Dataset and Model Setup

The project uses **BridgeV2**, a dataset of real **WidowX** robot manipulation demonstrations from UC Berkeley RAIL, focusing on **drawer open / close** tasks.

### Dataset
- 8 episodes total
- 7 open-drawer episodes
- 1 close-drawer episode
- 80 frames total
- 256×256 RGB observations

### Model
- **Checkpoint:** `lerobot/smolvla_base`
- **Parameters:** 450M
- **Action space:** 6D end-effector deltas  
  (`dx`, `dy`, `dz`, `droll`, `dpitch`, `grip`)

---

## Analysis Focus

The project explored four key questions:

- Does the model separate **open** vs **close** actions in a physically meaningful way?
- Are action predictions consistent across multiple episodes of the same task?
- Does the model respond differently to semantically different language instructions on the same image?
- How does action behavior evolve over time during an episode?

---

## Open vs Close Action Separation

A key result was that SmolVLA separated open and close actions most strongly along the **dy** axis.

- **dy difference:** `0.562`
- opening predicted negative `dy`
- closing predicted positive `dy`

This is physically consistent with a tabletop drawer task:
- **opening** pulls the drawer toward the robot
- **closing** pushes it away

Additional separation was observed in:
- `dz`
- `grip`

These results show that the model is not producing generic actions, but adapting its outputs to task direction.

---

## Action Consistency and Language Grounding

Across the 7 open-drawer episodes, the model showed varying consistency across action dimensions:

- **dpitch** was the most consistent dimension
- **grip** was the most variable
- translational components showed moderate variation depending on trajectory

Instruction sensitivity analysis showed that the model produced distinct predicted action distributions for different instructions on the **same image**, indicating genuine language conditioning.

<p align="center">
  <img src="{{ site.baseurl }}/assets/smolvla/smolvla_deep_evaluation.png" alt="SmolVLA deep evaluation" width="900">
</p>
<p align="center">
  <em>Action consistency and instruction sensitivity across multiple language prompts.</em>
</p>

### Key findings
- mean pairwise L2 distance across instructions: **0.262**
- max pairwise L2 distance: **0.376**
- model behavior changed meaningfully under different natural-language commands

---

## Temporal Behavior Analysis

Temporal analysis showed that model behavior evolved across an episode rather than remaining static.

Key observations:
- action standard deviation increased over time
- the model appeared more certain in early frames
- cumulative motion for **close** episodes was higher than for **open**
- `dy` separation remained consistent across all frames

This indicates that the model maintains task-specific structure throughout the sequence.

<p align="center">
  <img src="{{ site.baseurl }}/assets/smolvla/smolvla_temporal_consistency.png" alt="SmolVLA temporal consistency" width="900">
</p>
<p align="center">
  <em>Temporal trends in action predictions, variance, and cumulative motion.</em>
</p>

---

## Results Summary

### Strongest quantitative outcomes
- **dy separation:** `0.562` between open and close
- **mean instruction sensitivity:** `0.262` pairwise L2 distance
- **most consistent dimension:** `dpitch`
- **most variable dimension:** `grip`
- **close cumulative motion:** `7.580`
- **open cumulative motion:** `3.623`

### Interpretation
The results suggest that the pretrained SmolVLA policy:
- captures meaningful task-direction differences
- is sensitive to instruction semantics
- exhibits structured temporal behavior
- produces physically consistent action distributions

---

## Technical Stack

- Python
- Hugging Face Transformers
- LeRobot
- SmolVLA-450M
- BridgeV2 dataset
- NumPy / Matplotlib
- action-space statistics and temporal analysis

---

## Engineering Insights

- pretrained VLA models can demonstrate meaningful language grounding without task-specific retraining
- action-space analysis is effective for evaluating robot policy behavior
- temporal analysis reveals confidence trends that single-frame evaluation cannot capture
- simple tasks like drawer manipulation are powerful probes for physical correctness

---

## Future Improvements

- evaluate additional BridgeV2 task categories
- compare against other VLA models
- extend from analysis to rollout-based policy evaluation
- test robustness under ambiguous or conflicting instructions
- analyze internal representations and attention behavior
