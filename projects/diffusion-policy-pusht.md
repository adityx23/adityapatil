---
layout: default
title: Diffusion Policy for Robot Control — PushT Task Analysis
---

# Diffusion Policy for Robot Control — PushT Task Analysis

<div class="project-summary">
<strong>Type:</strong> Robot Learning / Policy Evaluation<br>
<strong>Focus:</strong> diffusion policies, control performance, success rate, trajectory efficiency<br>
<strong>Platform:</strong> Python, PyTorch, pretrained diffusion policy, PushT environment<br>
<strong>Outcome:</strong> Analyzed a pretrained diffusion-based control policy and quantified success rate, trajectory efficiency, and reward behavior across multiple episodes
</div>

<div class="project-links" markdown="0">
  <a class="btn" href="{{ site.baseurl }}/projects">← Back to Projects</a>
  <a class="btn" href="https://github.com/adityx23/diffusion-policy-pusht-evaluation" target="_blank" rel="noopener noreferrer">GitHub Repository ↗</a>
</div>

## Overview

Applied a pretrained diffusion policy to the **PushT** manipulation task to study how a learned control policy performs in terms of success rate, efficiency, and reward behavior across repeated rollouts.

The project focused on whether the policy could reliably complete the task, how successful and failed runs differed in efficiency, and how closely the observed performance matched reported benchmark results for the pretrained checkpoint.

<p align="center">
  <img src="{{ site.baseurl }}/assets/diffusion_policy/diffusion_policy_results.png" alt="Diffusion policy PushT results" width="950">
</p>
<p align="center">
  <em>Evaluation summary showing success rate trends, reward distribution, rollout efficiency, and representative successful and failed outcomes.</em>
</p>

---

## Task Setup

The evaluation was performed on the **PushT** task, a planar manipulation environment where the policy must push an object to a target configuration.

### Evaluation setup
- 30 rollout episodes
- pretrained diffusion policy checkpoint
- DDIM sampling with 10 steps
- GPU inference (T4)

### Metrics tracked
- success / failure per episode
- cumulative reward
- steps to completion
- success rate progression over time

---

## Performance Overview

The policy achieved a **66.7% success rate (20/30)** across 30 rollout episodes.

Performance is consistent with the reported benchmark (~70%), indicating correct implementation and stable policy behavior.

---

## Results Summary

| Metric                | Value         |
|-----------------------|---------------|
| Episodes evaluated    | 30            |
| Success rate          | 66.7% (20/30) |
| Avg steps             | 210.4         |
| Avg steps (success)   | 165.6         |
| Avg steps (fail)      | 300.0         |
| Avg reward            | 100.05        |
| Avg reward (success)  | 71.32         |
| Inference time        | ~3.2s/chunk   |
| Total eval time       | 6.6 min       |

Paper-reported success rate: **~70%** — the observed result of **66.7%** is consistent with expected checkpoint performance.

The gap between successful and failed episodes is clearly reflected in both step count and reward distribution, reinforcing that trajectory efficiency is the dominant factor in task completion.

---

## Success vs Failure Behavior

A clear separation was observed between successful and failed episodes:

- successful runs clustered at lower step counts
- failed runs frequently reached the maximum step limit
- reward distributions differed, but reward alone did not perfectly determine success

### Key observations
- success is strongly correlated with **trajectory efficiency**
- failures are systematic rather than random
- step count is a stronger completion indicator than reward alone

---

## Trajectory Efficiency

Step distribution analysis showed:

- successful episodes typically finished in **~165.6 steps**
- failed episodes consistently reached **300 steps**
- the policy either converged efficiently or failed to recover

This suggests the policy behaves more like a trajectory generator than a strongly reactive controller with mid-course correction.

---

## Reward Behavior

Reward trends revealed that:

- successful episodes achieved more stable reward accumulation
- failed episodes could still receive relatively high reward without completing the task
- reward shaping does not perfectly reflect final task completion

This highlights the importance of evaluating:
- success rate
- steps to completion
- failure structure

rather than relying on reward alone.

---

## Key Insights

- diffusion policies can achieve strong task performance without explicit online planning
- policy success depends heavily on early trajectory quality
- learned policies may lack robust recovery once off-course
- rollout efficiency provides important information beyond scalar reward
- benchmark-aligned evaluation is useful for validating implementation correctness

---

## Technical Stack

- Python
- PyTorch
- pretrained diffusion policy inference
- DDIM sampling
- rollout-based evaluation
- NumPy / Matplotlib

---

## Engineering Insights

- multi-episode rollout evaluation is critical for understanding policy robustness
- success rate alone is insufficient without efficiency and failure analysis
- diffusion-based policies behave more like structured motion generators than reactive feedback controllers
- consistent failure patterns can reveal limitations in recovery behavior

---

## Future Improvements

- compare against behavior cloning and RL-based baselines
- evaluate on additional manipulation environments beyond PushT
- analyze action trajectories directly instead of only episode-level metrics
- test recovery-aware variants under perturbations
- visualize latent sampling behavior for deeper interpretation
