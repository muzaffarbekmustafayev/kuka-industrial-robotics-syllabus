# Course Roadmap & Learning Pathways
## KUKA Industrial Robotics Curriculum (KR AGILUS KR 6 R900-2)

This roadmap outlines structured academic curricula and industrial training tracks designed for undergraduate and graduate coursework at **Samarkand State University (SamDU)** and **Tomsk State University (TSU)**, as well as industrial commissioning engineers.

---

## 🧭 Visual Course Matrix & Phase Repositories

```
Week  1 - 3    [ 1-BOB: KIRISH VA SIMULYATSIYA ]
               Repository: kuka-robotics-phase-1-basics
               ├── 01-introduction          (Safety, Hardware Architecture, smartPAD)
               └── 02-simulation-setup      (KUKA.Sim Pro, OfficeLite, WorkVisual)
                               │
Week  4 - 7    [ 2-BOB: MATEMATIKA VA KINEMATIKA ]
               Repository: kuka-robotics-phase-2-kinematics
               ├── 03-rodrigues-formula     (so(3), Lie Algebra, Rodrigues Matrix)
               ├── 04-rotation-matrices     (Euler A-B-C, Gimbal Lock, Quaternions)
               ├── 05-dh-parameters         (Standard/Modified DH for KR 6 R900-2)
               ├── 06-forward-kinematics    (SE(3) Chain, Flange Pose, $POS_ACT)
               └── 07-inverse-kinematics    (Pieper's Solution, S & T Bits, 8 Configs)
                               │
Week  8 - 10   [ 3-BOB: YAKOBIAN VA SINGULYARLIK ]
               Repository: kuka-robotics-phase-3-singularity
               ├── 08-jacobian-matrix       (Geometric Jacobian, Velocity Propagation)
               └── 09-singularity-analysis  (Wrist, Shoulder, Boundary, Yoshikawa Index)
                               │
Week 11 - 13   [ 4-BOB: KRL DASTURLASH ]
               Repository: kuka-robotics-phase-4-krl-programming
               ├── 10-krl-basics            (SRC/DAT architecture, FRAME, POS, E6POS)
               ├── 11-motion-commands       (PTP, LIN, CIRC, SLIN, SCIRC, Approximation)
               └── 12-io-interfacing        (EtherCAT, Digital I/O, Pneumatics, Grippers)
                               │
Week 14 - 16   [ 5-BOB: COMPUTER VISION VA INTEGRATSIYA ]
               Repository: kuka-robotics-phase-5-advanced-integration
               └── 13-computer-vision       (PnP, cv2.Rodrigues, Hand-Eye AX=XB, Pick&Place)
```

---

## 🎓 3 Specialized Learning Tracks

### Track A: Academic / Research Track (PhD & MSc)
* **Target Audience:** Master's and PhD candidates in Mechatronics, Robotics, and Applied Mathematics.
* **Prerequisites:** Multivariable calculus, Linear algebra, Classical mechanics.
* **Focal Repositories:** `phase-2-kinematics`, `phase-3-singularity`, `phase-5-advanced-integration`.
* **Key Milestones:**
  1. Symbolically prove the Rodrigues formula and its matrix exponential limit $e^{\theta K}$.
  2. Implement an analytical 8-solution Inverse Kinematics solver for the KUKA KR 6 R900-2 in Python and verify it against KSS OfficeLite.
  3. Derive the analytical singularity manifold of the spherical wrist when $A_5 = 0^\circ$ and implement damped least-squares pseudo-inverse Jacobian control.
  4. Perform Hand-Eye calibration ($AX = XB$) using dual quaternions and publish reproducible experimental results.

### Track B: Industrial Automation & System Integrator Track
* **Target Audience:** Automation engineers, robotics technicians, PLC programmers.
* **Prerequisites:** Industrial electrical safety, basic programming, CAD reading.
* **Focal Repositories:** `phase-1-basics`, `phase-4-krl-programming`, `phase-5-advanced-integration`.
* **Key Milestones:**
  1. Commission a virtual cell in KUKA.Sim Pro connected to KUKA OfficeLite over VRC.
  2. Configure digital fieldbus communication (EtherCAT / PROFINET) in KUKA WorkVisual.
  3. Program a multi-point palletizing and depalletizing routine using structured KRL subprograms (`.src` and `.dat`), tool coordinate offsets (`$TOOL`), and base calibration (`$BASE`).
  4. Integrate safety logic, fence interlocks, and vacuum gripper actuation via `$OUT` and `$IN`.

### Track C: Robotics AI & Computer Vision Track
* **Target Audience:** Software engineers, machine learning engineers, perception researchers.
* **Prerequisites:** Python, OpenCV, basic linear algebra.
* **Focal Repositories:** `phase-2-kinematics`, `phase-4-krl-programming`, `phase-5-advanced-integration`.
* **Key Milestones:**
  1. Calibrate camera intrinsics $K$ and radial-tangential distortion parameters.
  2. Detect AprilTags / ArUco markers and estimate 6-DoF poses using `cv2.solvePnP` and Rodrigues angle-axis conversion.
  3. Calibrate Eye-in-Hand camera pose using the Tsai-Lenz algorithm.
  4. Stream target 6D coordinates (`FRAME {X, Y, Z, A, B, C}`) over TCP/IP or EthernetKRL to guide the KR AGILUS for dynamic object sorting.

---

## 📅 Semester Schedule (16-Week University Syllabus)

| Week | Lecture Topic (Uzbek / English) | Phase Repository & Directory |
| :---: | :--- | :--- |
| **Week 1** | Robototexnika asoslari va KR AGILUS xavfsizlik qoidalari | `kuka-robotics-phase-1-basics/01-introduction` |
| **Week 2** | Virtual simulyatsiya muhiti: KUKA.Sim Pro va OfficeLite | `kuka-robotics-phase-1-basics/02-simulation-setup` |
| **Week 3** | KUKA WorkVisual konfiguratsiyasi va loyiha yuklash | `kuka-robotics-phase-1-basics/02-simulation-setup` |
| **Week 4** | Fazoviy burilishlar va Qiya-simmetrik matritsalar $\mathfrak{so}(3)$ | `kuka-robotics-phase-2-kinematics/03-rodrigues-formula` |
| **Week 5** | Rodrig formulasining geometrik va matritsaviy tahlili | `kuka-robotics-phase-2-kinematics/03-rodrigues-formula` |
| **Week 6** | Eyler burchaklari ($A, B, C$), Kvaternionlar va Gimbal Lock | `kuka-robotics-phase-2-kinematics/04-rotation-matrices` |
| **Week 7** | Denavit-Hartenberg (DH) parametrlari va koordinatalar bog'lanishi | `kuka-robotics-phase-2-kinematics/05-dh-parameters` |
| **Week 8** | To'g'ri kinematika (Forward Kinematics) analitik yechimi | `kuka-robotics-phase-2-kinematics/06-forward-kinematics` |
| **Week 9** | Teskari kinematika (Inverse Kinematics) va Piper (Pieper) usuli | `kuka-robotics-phase-2-kinematics/07-inverse-kinematics` |
| **Week 10** | Geometrik Yakobian matritsasi va burchak tezliklari | `kuka-robotics-phase-3-singularity/08-jacobian-matrix` |
| **Week 11** | Singulyarlik tahlili va Yoshikawa manipulyativlik indeksi | `kuka-robotics-phase-3-singularity/09-singularity-analysis` |
| **Week 12** | KRL dasturlash tili asoslari: Sintaksis, massivlar va tiplar | `kuka-robotics-phase-4-krl-programming/10-krl-basics` |
| **Week 13** | Harakat buyruqlari (`PTP`, `LIN`, `CIRC`, `SLIN`, `SCIRC`) | `kuka-robotics-phase-4-krl-programming/11-motion-commands` |
| **Week 14** | Raqamli I/O va pnevmatik tutqichni (Gripper) boshqarish | `kuka-robotics-phase-4-krl-programming/12-io-interfacing` |
| **Week 15** | Pinhole kamera modeli, kalibrlash va PnP masalasi | `kuka-robotics-phase-5-advanced-integration/13-computer-vision-integration` |
| **Week 16** | Hand-Eye kalibratsiya ($AX = XB$) va Yakuniy Vision Pick-and-Place | `kuka-robotics-phase-5-advanced-integration/13-computer-vision-integration` |
