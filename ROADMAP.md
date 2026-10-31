# Course Roadmap & Learning Pathways (25 Lessons)
## KUKA Industrial Robotics Program | KUKA KR 6 R900-2 (KR AGILUS-2)

This roadmap outlines structured academic curricula and industrial training tracks designed for undergraduate, graduate (MSc/PhD) coursework at **Samarkand State University (SamDU)** and **Tomsk State University (TSU)**, as well as industrial commissioning engineers.

---

## 🧭 Visual 6-Phase Matrix (25 Lessons)

```
Phase 1: FUNDAMENTALS & DIGITAL TWIN
Repository: kuka-robotics-phase-1-fundamentals
├── 01-introduction-to-kuka-agilus      (Mechanical Anatomy, KRC4/KRC5, ISO 10218)
├── 02-smartpad-and-coordinate-systems  (smartPAD Jogging, WORLD, BASE, TOOL, JOINT)
├── 03-simulation-setup-digital-twin    (KUKA.Sim Pro, OfficeLite VRC Bridge)
└── 04-safety-and-safeoperation         (KUKA SafeOperation, Safe Zones, Speed Limits)
                        │
Phase 2: SPATIAL KINEMATICS & MATHEMATICS
Repository: kuka-robotics-phase-2-kinematics-and-math
├── 05-rodrigues-rotation-formula       (so(3) Lie Algebra, Skew Operator, Matrix Exponential)
├── 06-rotation-matrices-and-quaternions(KUKA Euler A-B-C, Gimbal Lock, Quaternions, SLERP)
├── 07-dh-parameters-modelling          (Standard & Modified DH for KR 6 R900-2)
├── 08-forward-kinematics-solver        (SE(3) Chain, Flange Pose, $POS_ACT Validation)
├── 09-inverse-kinematics-analytical    (Pieper's Decoupling, 8 Solutions, Status & Turn)
└── 10-numerical-inverse-kinematics     (Newton-Raphson, Levenberg-Marquardt DLS)
                        │
Phase 3: DIFFERENTIAL KINEMATICS & DYNAMICS
Repository: kuka-robotics-phase-3-differential-kinematics
├── 11-jacobian-matrix-derivation       (Geometric Jacobian, Velocity Propagation)
├── 12-singularity-analysis             (Wrist A5=0, Shoulder, Boundary, Yoshikawa Ellipsoid)
├── 13-robot-dynamics-and-forces        (Newton-Euler, Lagrange, Torque Profiles)
└── 14-force-torque-control             (6-Axis F/T Sensors, Impedance & Admittance)
                        │
Phase 4: INDUSTRIAL KRL PROGRAMMING
Repository: kuka-robotics-phase-4-krl-programming
├── 15-krl-syntax-and-variables         (.src/.dat Architecture, FRAME, POS, E6POS)
├── 16-advanced-motion-commands         (PTP, LIN, CIRC, Splines, Approximation, $ADVANCE)
├── 17-logic-and-interrupts             (Loops, Logic, Asynchronous INTERRUPT & BRAKE)
├── 18-industrial-io-and-fieldbus       (ProfiNet, EtherCAT, WorkVisual Signal Mapping)
└── 19-subprograms-and-expert-programming (Global/Local Subroutines, Parametric Frameworks)
                        │
Phase 5: ADVANCED INTEGRATION & ROBOTICS AI
Repository: kuka-robotics-phase-5-advanced-integration
├── 20-kuka-rsi-interface               (KUKA RSI <12ms Real-Time XML Stream)
├── 21-ros2-driver-integration          (ROS 2 Humble/Iron, kuka_robot_drivers, URDF)
├── 22-moveit2-trajectory-planning      (MoveIt2, Dynamic Obstacle Collision Avoidance)
└── 23-computer-vision-pick-and-place   (Pinhole Model, PnP, Hand-Eye AX=XB, Visual Servoing)
                        │
Phase 6: INDUSTRIAL MANUFACTURING APPLICATIONS
Repository: kuka-robotics-phase-6-industrial-applications
├── 24-trajectory-welding-and-glueing   (Continuous Path Velocity, 3D Bead Profiling)
└── 25-palletizing-and-sorting-system   (Conveyor Tracking, Real-Time Sensor-Based Sorting)
```

---

## 🎓 3 Specialized Learning Tracks

### Track A: Academic / Research Track (PhD & MSc)
* **Target Audience:** Master's and PhD candidates in Mechatronics, Robotics, and Applied Mathematics.
* **Prerequisites:** Multivariable calculus, Linear algebra, Classical mechanics.
* **Focal Repositories:** `phase-2-kinematics-and-math`, `phase-3-differential-kinematics`, `phase-5-advanced-integration`.
* **Key Milestones:**
  1. Symbolically derive the Rodrigues formula, matrix logarithm, and quaternion equivalence.
  2. Implement an analytical 8-solution Inverse Kinematics solver for the KUKA KR 6 R900-2 in Python and verify it against KSS OfficeLite `$POS_ACT`.
  3. Derive the analytical singularity manifold of the spherical wrist ($A_5 = 0^\circ$) and implement damped least-squares pseudo-inverse Jacobian control.
  4. Perform Hand-Eye calibration ($AX = XB$) using dual quaternions and publish reproducible experimental results.

### Track B: Industrial Automation & System Integrator Track
* **Target Audience:** Automation engineers, robotics technicians, PLC programmers.
* **Prerequisites:** Industrial electrical safety, basic programming, CAD reading.
* **Focal Repositories:** `phase-1-fundamentals`, `phase-4-krl-programming`, `phase-6-industrial-applications`.
* **Key Milestones:**
  1. Commission a virtual cell in KUKA.Sim Pro connected to KUKA OfficeLite over VRC.
  2. Configure digital fieldbus communication (EtherCAT / PROFINET) in KUKA WorkVisual.
  3. Program a multi-point palletizing and depalletizing routine using structured KRL subprograms (`.src` and `.dat`), tool coordinate offsets (`$TOOL`), and base calibration (`$BASE`).
  4. Implement real-time conveyor tracking and 3D trajectory dispensing with safety interlocks.

### Track C: Robotics AI & Computer Vision Track
* **Target Audience:** Software engineers, machine learning engineers, perception researchers.
* **Prerequisites:** Python, OpenCV, ROS 2, basic linear algebra.
* **Focal Repositories:** `phase-2-kinematics-and-math`, `phase-4-krl-programming`, `phase-5-advanced-integration`.
* **Key Milestones:**
  1. Calibrate camera intrinsics $K$ and radial-tangential distortion parameters.
  2. Detect AprilTags / ArUco markers and estimate 6-DoF poses using `cv2.solvePnP` and Rodrigues angle-axis conversion.
  3. Calibrate Eye-in-Hand camera pose using the Tsai-Lenz algorithm.
  4. Integrate ROS 2 MoveIt2 with the KUKA RSI real-time driver to dynamically execute vision-guided pick-and-place tasks.
