---
layout: default
title: SmolVLA for Language-Conditioned Robot Action Prediction
description: Open-loop SmolVLA-450M action variation, prompt sensitivity, and temporal analysis on sampled BridgeV2 drawer observations.
project: true
image: /assets/thumbnails/smolvla.webp
repository: https://github.com/adityx23/smolvla-bridgev2-action-analysis
date_modified: 2026-08-08
technologies: [PyTorch, SmolVLA, LeRobot, BridgeV2, Robot Learning]
built: An open-loop inference workflow for measuring prompt sensitivity and temporal variation in predicted actions on real robot observations.
validated: Eight BridgeV2 episodes, 80 sampled frames, and six prompts, with seven open examples and one exploratory close example.
why: Quantifies how a pretrained vision-language-action model's predictions vary with observations and prompts without claiming closed-loop task success.
previous_project_url: /projects/slam-navigation-robot
previous_project_title: SLAM-Based Navigation Robot
next_project_url: /projects/diffusion-policy-pusht
next_project_title: Diffusion Policy on PushT
---

# SmolVLA for Language-Conditioned Robot Action Prediction

<div class="project-summary">
  <div><strong>Role</strong><span>VLA inference and behavioral analysis</span></div>
  <div><strong>Context</strong><span>Independent robot-learning study</span></div>
  <div><strong>Platform</strong><span>SmolVLA-450M · LeRobot · BridgeV2</span></div>
  <div><strong>Outcome</strong><span>8 episodes · 80 frames · 6 prompts</span></div>
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← All Projects</a>
  <a class="btn" href="https://github.com/adityx23/smolvla-bridgev2-action-analysis" target="_blank" rel="noopener noreferrer">GitHub Repository ↗</a>
</div>

{% include project-tldr.html %}

## Overview

Applied **SmolVLA-450M**, a pretrained vision-language-action model, to sampled **BridgeV2** real-robot observations to study how prompts influence open-loop action predictions for drawer-opening and drawer-closing examples.

The project measures whether predicted actions differ across prompts, how much they vary across similar episodes, and how they evolve over a sampled sequence. It does not execute the predictions on a robot or measure task success.

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

- How do predicted **open** and **close** action vectors differ in this sample?
- How variable are action predictions across multiple episodes with the same label?
- Does the model respond differently to semantically different language instructions on the same image?
- How does action behavior evolve over time during an episode?

---

## Open vs Close Action Separation

A key result in the supplied run was that sampled open and close predictions differed most strongly in **dy** (0.562), followed by **grip** (0.461) and **dz** (0.458).

- **dy difference:** `0.562`
- **grip difference:** `0.461`
- **dz difference:** `0.458`

These differences show that the model did not produce one identical mean action vector for both sampled task labels. Because the evaluation includes seven open episodes but only one close episode—and uses a zero-valued state placeholder—the comparison is exploratory rather than a balanced physical-control benchmark.

---

## Action Consistency and Language Grounding

Across the 7 open-drawer episodes, the model showed varying consistency across action dimensions:

- **dpitch** was the most consistent dimension
- **grip** was the most variable
- translational components showed moderate variation depending on trajectory

Instruction sensitivity analysis showed that the model produced distinct predicted action distributions for different instructions on the **same image**, indicating genuine language conditioning.

<p align="center">
  <img src="{{ site.baseurl }}/assets/smolvla/smolvla_deep_evaluation.png" alt="SmolVLA deep evaluation" width="900" loading="lazy" decoding="async">
</p>
<p align="center">
  <em>Action consistency and instruction sensitivity across multiple language prompts.</em>
</p>

### Key findings
- mean pairwise L2 distance across prompts: **0.262**
- max pairwise L2 distance: **0.376**
- model behavior changed meaningfully under different natural-language commands

---

## Temporal Behavior Analysis

Temporal analysis showed that model behavior evolved across an episode rather than remaining static.

Key observations:
- `dpitch` had the lowest mean per-frame standard deviation (`0.048`)
- `grip` had the highest mean per-frame standard deviation (`0.393`)
- cumulative motion magnitude was `3.623` for the mean open trajectory and `7.580` for the single close trajectory
- action values evolved across the ten sampled frames rather than remaining constant

This shows temporal structure in the predicted action sequence; it does not establish closed-loop task completion.

<p align="center">
  <img src="{{ site.baseurl }}/assets/smolvla/smolvla_temporal_consistency.png" alt="SmolVLA temporal consistency" width="900" loading="lazy" decoding="async">
</p>
<p align="center">
  <em>Temporal trends in action predictions, variance, and cumulative motion.</em>
</p>

---

## Results Summary

### Strongest quantitative outcomes
- **dy separation:** `0.562` between sampled open and close predictions
- **grip separation:** `0.461`
- **dz separation:** `0.458`
- **mean prompt sensitivity:** `0.262` pairwise L2 distance
- **most consistent dimension:** `dpitch`
- **most variable dimension:** `grip`
- **close cumulative motion:** `7.580`
- **open cumulative motion:** `3.623`

### Interpretation
The sampled predictions suggest that the pretrained SmolVLA policy:
- produces different mean vectors for the sampled task labels
- is sensitive to prompt changes in the sampled image
- exhibits structured temporal behavior
- produces structured but variable action distributions

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

- pretrained VLA predictions can be measurably prompt-sensitive without task-specific retraining; closed-loop tests are still required to establish language grounding and task success
- action-space analysis is effective for evaluating robot policy behavior
- temporal analysis reveals confidence trends that single-frame evaluation cannot capture
- simple tasks like drawer manipulation are useful probes for prediction structure before closed-loop evaluation

---

## Future Improvements

- evaluate additional BridgeV2 task categories
- compare against other VLA models
- extend from analysis to rollout-based policy evaluation
- test robustness under ambiguous or conflicting instructions
- analyze internal representations and attention behavior

{% include project-footer.html %}
