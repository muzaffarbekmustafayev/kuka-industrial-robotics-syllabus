# Contributing to the KUKA Industrial Robotics Course

Thank you for your interest in contributing to the **KUKA Industrial Robotics Course**! This project is maintained jointly under academic collaboration between **Samarkand State University (SamDU)** and **Tomsk State University (TSU)**.

To maintain production-grade quality, rigorous mathematical consistency, and clean separation across the multi-repository ecosystem, all contributors must adhere to the following standards.

---

## 🏛️ 1. Multi-Repository Architecture Standards

The course is modularized into:
* **1 Master Navigator Repository:** `kuka-industrial-robotics-course` (or `-syllabus`) — contains no lesson code; acts as syllabus, mathematical cheatsheet, and navigation hub.
* **6 Phase Repositories:** Independent repositories containing code, simulation assets, and laboratory exercises organized by phase:
  1. `kuka-robotics-phase-1-fundamentals` (Lessons 01 - 04)
  2. `kuka-robotics-phase-2-kinematics-and-math` (Lessons 05 - 10)
  3. `kuka-robotics-phase-3-differential-kinematics` (Lessons 11 - 14)
  4. `kuka-robotics-phase-4-krl-programming` (Lessons 15 - 19)
  5. `kuka-robotics-phase-5-advanced-integration` (Lessons 20 - 23)
  6. `kuka-robotics-phase-6-industrial-applications` (Lessons 24 - 25)

### Mandatory Global GitHub Topics
Every repository in the course ecosystem MUST be tagged with the following 7 identical topics:
```
kuka-robotics-course, mechatronics, krl-programming, ros2-robotics, industrial-automation, samdu, tsu
```

---

## 📁 2. Mandatory Topic Directory Boilerplate Structure

Inside each Phase repository, every individual topic folder (e.g., `05-rodrigues-rotation-formula/`, `15-krl-syntax-and-variables/`) must maintain this standard internal hierarchy:

```
[two-digit-index]-[topic-name]/
├── src/
│   ├── krl/                # Industrial KRL programs (.src, .dat, .sub)
│   │   ├── main.src
│   │   └── main.dat
│   └── scripts/            # Computation & verification scripts (Python, MATLAB)
│       ├── kinematics.py
│       └── test_solution.py
├── sim/                    # Simulation assets & models
│   ├── kr6_r900_2.urdf     # Robot description format
│   └── cell_scene.vcmx     # KUKA.Sim Pro simulation layout
├── docs/                   # Documentation assets
│   ├── figures/            # Diagrams, trajectory plots, schematics (.png, .svg)
│   └── derivations.md      # In-depth mathematical proofs
├── CLAUDE.md               # AI developer guidelines & repository context
└── README.md               # Student-facing guide, theory, equations, laboratory task
```

---

## 💻 3. Coding & Notation Standards

### 3.1 Python Standards
* Python 3.10+ compatibility.
* Follow **PEP 8** style guidelines (`flake8`, `black`).
* Use type annotations for all mathematical functions:
  ```python
  import numpy as np
  from numpy.typing import NDArray

  def rodrigues_to_rotation_matrix(axis: NDArray[np.float64], theta: float) -> NDArray[np.float64]:
      """Computes 3x3 rotation matrix using Rodrigues formula."""
      ...
  ```
* Include unit tests using `pytest` for all forward/inverse kinematics, Jacobian, and vision algorithms.

### 3.2 KRL (KUKA Robot Language) Standards
* All KRL files must be paired: `.src` (logic) and `.dat` (data definitions).
* Capitalize all KRL keywords, system variables, and motion commands (`DEF`, `END`, `PTP`, `LIN`, `CIRC`, `SLIN`, `SCIRC`, `$POS_ACT`, `$BASE`, `$TOOL`).
* Initialize all `FRAME` and `E6POS` variables with descriptive names.

### 3.3 Mathematical & LaTeX Standards
* Follow the notation defined in [MATH_CHEATSHEET.md](file:///c:/Users/muzaf/Desktop/kuka-robotics-course/MATH_CHEATSHEET.md).
* Coordinate frames must be enclosed in curly braces: $\{W\}$, $\{B\}$, $\{F\}$, $\{T\}$, $\{C\}$.
* Transformation matrices must be written as $T_{\text{source}}^{\text{target}}$.
* Vectors are denoted with an arrow $\vec{v}$ or bold lowercase $\mathbf{v}$, and matrices with uppercase $R, T, K$.

---

## 🔄 4. Git Commit & Pull Request Guidelines

We enforce the **Conventional Commits** specification:
* `feat:` A new feature or lesson exercise.
* `fix:` A bug fix or typo correction.
* `docs:` Documentation or mathematical write-up changes.
* `math:` Mathematical derivations, proofs, or symbolic simplifications.
* `krl:` Changes to KRL `.src` or `.dat` source code.
* `sim:` Changes to `.vcmx`, URDF, or simulation assets.
* `test:` Adding or updating unit tests.
