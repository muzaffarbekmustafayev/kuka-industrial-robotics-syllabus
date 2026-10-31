# AI Developer Instructions: KUKA Industrial Robotics Master Navigator

## 🎯 Repository Purpose
This is the **Master Navigator / Syllabus Repository** (`kuka-industrial-robotics-course` / `kuka-industrial-robotics-syllabus`).
It serves as the central control panel and global syllabus hub for the **25-lesson KUKA Industrial Robotics Course**, cross-linking the 6 Phase repositories:
1. `kuka-robotics-phase-1-fundamentals` (Lessons 01 - 04)
2. `kuka-robotics-phase-2-kinematics-and-math` (Lessons 05 - 10)
3. `kuka-robotics-phase-3-differential-kinematics` (Lessons 11 - 14)
4. `kuka-robotics-phase-4-krl-programming` (Lessons 15 - 19)
5. `kuka-robotics-phase-5-advanced-integration` (Lessons 20 - 23)
6. `kuka-robotics-phase-6-industrial-applications` (Lessons 24 - 25)

## ⚠️ Critical Architectural & Mathematical Constraints
* **NO LESSON CODE IN THIS REPO:** Do not add Python kinematics solvers or KRL `.src`/`.dat` files directly into this repository. All implementation code belongs in its designated Phase repository.
* **ROBOT MODEL:** All kinematics, specifications, and parameters must strictly target the **KUKA KR 6 R900-2 (KR AGILUS-2)**.
* **MATHEMATICAL RIGOR & PROOFS MANDATE (Qat'iy Matematik Talab):**
  Har bir darsda KUKA ning ishlash mexanikasi yoki kinematikasi kelsa, quyidagilar bo'lishi SHART:
  1. **Qaysi formulaga / teoremaga asoslangani** (masalan, Euler-Rodrigues teoremasi, Pieper dekoupling teoremasi, Lie algebrasi $\mathfrak{so}(3)$ eksponensiali, Frenet-Serret egri chiziqlar nazariyasi, Tsai-Lenz $AX=XB$ teoremasi).
  2. **Formulaning qadam-baqadam keltirib chiqarilishi va matematik isboti** (Step-by-step rigorous proof).
  3. **KUKA KR 6 R900-2 manipulyatoriga tatbiqi** (aniq o'lchamlar, $d_1=400\text{mm}, a_1=25\text{mm}, a_2=455\text{mm}, d_4=420\text{mm}, d_6=80\text{mm}$).
  4. **KUKA KSS kontrollerining ichki hisoblash algoritmi** (masalan, $B=\pm 90^\circ$ da Gimbal Lock ni yechish, Status va Turn bitlarini hisoblash, singulyarlikda burchak tezliklarini cheklash).
  5. **Python / MATLAB da tasdiqlovchi dasturiy kod** (`src/scripts/` da to'liq unit testlari bilan).
* **MANDATORY GITHUB TOPICS:**
  `kuka-robotics-course`, `mechatronics`, `krl-programming`, `ros2-robotics`, `industrial-automation`, `samdu`, `tsu`.

## 📁 Standard Directory Structure for All 25 Lesson Directories
```
[two-digit-index]-[topic-name]/
├── src/
│   ├── krl/            # KRL (.src, .dat) files for KSS 8.3+
│   └── scripts/        # Python 3.10+ scripts (PEP 8, type hints, pytest)
├── sim/                # KUKA.Sim Pro (.vcmx), URDF models
├── docs/               # Math proofs, figures, schematics
├── CLAUDE.md           # Topic-specific AI developer guidelines
└── README.md           # Comprehensive student guide (theory, equations, lab task)
```
