# Robot Learning Project Selection Task

A 24-hour mini project for undergraduate robot-learning applicants.

## Setup

No GPU or local simulator is required. Google Colab is the intended interface.

Open `colab/robot_learning_selection.ipynb`, upload this folder, and run the notebook
cells to reproduce the public metrics.

You may use Chinese or English and may use online resources / AI assistants.
Your write-up must include a short **related work** section (see `README_submission.md`):
what others have done on similar problems, and what that suggested to you here.

## Submission (24 hours)

- Your code (typically `src/policy.py` and any helpers you add)
- Completed `README_submission.md` (including related work)
- One figure you think best supports your write-up

## Task

A point robot moves in a bounded 2D workspace with **random axis-aligned obstacles**
(blocks). You only receive **relative** observations `[Δx, Δy]` toward the goal —
**not** absolute coordinates and **not** a map of the blocks. Actions are 2D velocity
commands. Everything runs on CPU in NumPy.

You are given a **fixed demonstration budget** (`make_dataset`, default 4000 noisy
expert samples) and a **linear behavioral-cloning baseline**. The expert uses
short-horizon path information internally when generating demos; your policy must
learn from `(observation, action)` pairs only. Under that budget, do as well as you
can. There is no single required algorithm: explain what you tried, how you define
“good”, and the trade-offs you see.

Even if you fail, **don't worry**, that happens a lot of time in research. Summary why you fail, what you have learned from this failure and what you try to solve this problem is what we treasure.

Organizers may re-run your policy on held-out scenarios (different layouts, more
blocks, noise, shorter horizons). **Do not hard-code test targets, obstacle layouts,
or scenario lists.**

## Public metrics

The evaluator reports:

- **success rate** — final distance `< 0.05` and not inside a block
- **mean final distance**
- **mean episode length (steps)**
- **collision episode rate** — fraction of rollouts with at least one blocked step

## Environment summary

- Step size `0.08`, default max **80** steps on the public set
- If a step would enter a block, the robot **does not move** (collision counted)
- Demonstrations: grid-based expert with **action noise**
- Observations may include small noise during evaluation
