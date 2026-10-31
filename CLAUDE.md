# AI Developer Instructions: KUKA Industrial Robotics Syllabus

## 🎯 Repository Purpose
This is the **Master Navigator / Syllabus Repository** (`kuka-industrial-robotics-syllabus` / `kuka-industrial-robotics-course`).
It contains:
* Master curriculum table of contents
* Deep theoretical syllabus across 5 Phases (13 Topics)
* Unified mathematical formulary ([MATH_CHEATSHEET.md](file:///c:/Users/muzaf/Desktop/kuka-robotics-course/MATH_CHEATSHEET.md))
* Cross-links to the 5 modular Phase repositories:
  - `kuka-robotics-phase-1-basics`
  - `kuka-robotics-phase-2-kinematics`
  - `kuka-robotics-phase-3-singularity`
  - `kuka-robotics-phase-4-krl-programming`
  - `kuka-robotics-phase-5-advanced-integration`

## ⚠️ Critical Architectural Constraints
* **NO LESSON CODE IN THIS REPO:** Do not add Python kinematics solvers or KRL `.src`/`.dat` files directly into this repository. All implementation code belongs in its designated Phase repository.
* **ROBOT MODEL:** All kinematics, specifications, and parameters must target the **KUKA KR 6 R900-2 (KR AGILUS-2)**.
* **MATHEMATICAL RIGOR:** Always maintain notation consistency with `MATH_CHEATSHEET.md` (e.g., $SO(3)$, skew-symmetric operator $[\vec{k}]_\times$, Rodrigues formula, Tait-Bryan $Z-Y'-X''$ Euler angles $A, B, C$, and unit quaternions).
* **GITHUB TOPICS:** Ensure all generated repo configurations tag:
  `kuka-robotics-course`, `mechatronics`, `krl-programming`, `robot-kinematics`, `samdu`, `tsu`.

## 📁 Standard Directory Structure for Downstream Phase Repositories
```
kuka-robotics-phase-X-[name]/
└── [two-digit-index]-[topic]/
    ├── src/
    │   ├── krl/
    │   └── scripts/
    ├── sim/
    ├── docs/
    ├── CLAUDE.md
    └── README.md
```
