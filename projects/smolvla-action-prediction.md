---
layout: default
title: SmolVLA Evaluation for Language-Conditioned Robot Action Prediction
---

# SmolVLA Evaluation for Language-Conditioned Robot Action Prediction

<div class="project-summary">
<strong>Type:</strong> Robot Learning / Vision-Language-Action Evaluation<br>
<strong>Focus:</strong> Language grounding, action consistency, instruction sensitivity, temporal behavior<br>
<strong>Platform:</strong> Python, Transformers, LeRobot, SmolVLA-450M, BridgeV2<br>
<strong>Outcome:</strong> Evaluated a pretrained VLA model on real robot drawer manipulation and quantified action separation, temporal consistency, and instruction-conditioned behavior
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← Back to Projects</a>
</div>

## Overview

Evaluated **SmolVLA-450M**, a pretrained vision-language-action model, on **BridgeV2** real robot manipulation trajectories to study how language instructions influence predicted actions in drawer opening and closing tasks.

The project focused on whether the model produced physically meaningful action differences across instructions, how consistent its predictions were across similar episodes, and how its action uncertainty changed over time during a manipulation sequence.

<p align="center">
  <img src="{{ site.baseurl }}/assets/smolvla/smolvla_evaluation.png" alt="SmolVLA evaluation results" width="900">
</p>
<p align="center">
  <em>Evaluation summary showing action separation between open and close tasks, consistency across episodes, and instruction-conditioned action variation.</em>
</p>

---

## Dataset and Model Setup

The evaluation used **BridgeV2**, a dataset of real **WidowX** robot manipulation demonstrations from UC Berkeley RAIL. The selected task was **drawer open / close** manipulation.

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

## Task Context

The evaluation was built around drawer manipulation because it provides a clean test of language grounding: opening and closing require opposite motion directions while keeping most of the scene visually similar.

<p align="center">
  <img src="{{ site.baseurl }}/assets/smolvla/smolvla_dataset_examples.png" alt="BridgeV2 drawer task examples" width="950">
</p>
<p align="center">
  <em>Representative BridgeV2 drawer manipulation frames used for instruction-conditioned action prediction.</em>
</p>

---

## Evaluation Focus

The project evaluated four main questions:

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

These dimensions further indicated that the model was not outputting generic actions, but responding meaningfully to task direction.

---

## Action Consistency and Language Grounding

Across the 7 open-drawer episodes, the model showed varying consistency across action dimensions:

- **dpitch** was the most consistent dimension
- **grip** was the most variable
- translational components showed moderate variation depending on trajectory and object approach

Instruction sensitivity analysis showed that the model produced distinct predicted action distributions for different instructions on the **same image**, indicating genuine language conditioning rather than purely visual imitation.

<p align="center">
  <img src="{{ site.baseurl }}/assets/smolvla/smolvla_deep_evaluation.png" alt="SmolVLA deep evaluation" width="900">
</p>
<p align="center">
  <em>Deeper evaluation showing action consistency, instruction sensitivity, and separation across multiple language prompts.</em>
</p>

### Key findings
- mean pairwise L2 distance across instructions: **0.262**
- max pairwise L2 distance: **0.376**
- model behavior changed meaningfully under different natural-language commands

---

## Temporal Behavior Analysis

Temporal analysis showed that model behavior was not static across an episode.

Key observations:
- action standard deviation increased over time
- the model appeared more certain in early frames
- cumulative motion for **close** episodes was higher than for **open**
- `dy` separation remained consistent across the full 10-frame window

This suggests that SmolVLA maintained task-dependent action structure across time rather than only in the initial frame.

<p align="center">
  <img src="{{ site.baseurl }}/assets/smolvla/smolvla_temporal_consistency.png" alt="SmolVLA temporal consistency" width="900">
</p>
<p align="center">
  <em>Temporal consistency analysis showing frame-wise action behavior, variance trends, and cumulative motion differences across episodes.</em>
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
- shows structured temporal behavior across episodes
- produces action distributions consistent with real manipulation geometry

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

- pretrained VLA policies can show meaningful language grounding even without task-specific retraining
- action-space analysis is a useful way to evaluate language-conditioned robot behavior
- temporal consistency reveals confidence trends that single-frame evaluation can miss
- real manipulation tasks like drawer opening/closing are effective for testing whether action predictions match physical task structure

---

## Future Improvements

- evaluate on more BridgeV2 task categories beyond drawer manipulation
- compare SmolVLA predictions against additional VLA baselines
- extend from action prediction analysis to rollout-level policy execution
- test robustness under visually similar but semantically conflicting instructions
- analyze attention or representation behavior alongside action outputs
