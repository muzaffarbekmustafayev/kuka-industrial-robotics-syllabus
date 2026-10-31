#!/usr/bin/env python3
"""
KUKA Industrial Robotics Course: 6-Phase / 25-Lesson Scaffolder
Creates complete boilerplate templates for all 6 Phase repositories and their 25 lesson directories.

Usage:
    python scripts/scaffold_phase_repos.py --target-dir ../
"""

import os
import sys
import argparse
from pathlib import Path

PHASES = {
    "kuka-robotics-phase-1-fundamentals": {
        "title": "Phase 1: Asoslar, Xavfsizlik va Digital Twin",
        "description": "KUKA KR 6 R900-2 manipulyatori anatomiyasi, smartPAD interfeysi, KUKA.Sim Pro va SafeOperation xavfsizlik zonalari.",
        "lessons": [
            {
                "id": "01-introduction-to-kuka-agilus",
                "title": "KUKA KR AGILUS manipulyatoriga kirish va xavfsizlik standartlari",
                "summary": "KR 6 R900-2 mexanik anatomiyasi, o'qlar joylashuvi (A1..A6), KRC4/KRC5 kontrollerlari va ISO 10218 xalqaro xavfsizlik normalari.",
                "tech": "KR AGILUS, KRC4/KRC5, ISO 10218, Workspace Envelope",
            },
            {
                "id": "02-smartpad-and-coordinate-systems",
                "title": "SmartPAD interfeysi va fazoviy koordinata tizimlari",
                "summary": "smartPAD boshqaruvi, 6D Space Mouse fizikasi. WORLD, BASE, TOOL va JOINT koordinata tizimlari mexanikasi va qo'lda boshqarish (Jogging).",
                "tech": "smartPAD, WORLD/BASE/TOOL/JOINT Jogging",
            },
            {
                "id": "03-simulation-setup-digital-twin",
                "title": "Virtual simulyatsiya va Digital Twin (KUKA.Sim Pro & OfficeLite)",
                "summary": "KUKA.Sim Pro va KUKA OfficeLite VRC ko'prigi, KR 6 R900-2 uchun raqamli egizak (Digital Twin) muhitini noldan sozlash.",
                "tech": "KUKA.Sim Pro, OfficeLite VRC, WorkVisual, Digital Twin",
            },
            {
                "id": "04-safety-and-safeoperation",
                "title": "Sanoat xavfsizligi va KUKA SafeOperation texnologiyasi",
                "summary": "ISO 13849-1 va ISO/TS 15066 normalari. SafeOperation monitoring zonalari, o'qlar cheklovlari va xavfsiz tezlik (Reduced Speed).",
                "tech": "KUKA SafeOperation, Safe Zones, Speed Monitoring",
            },
        ],
    },
    "kuka-robotics-phase-2-kinematics-and-math": {
        "title": "Phase 2: Fazoviy Geometriya va Kinematik Modellashtirish",
        "description": "Rodrigues formulasi, so(3) Lie algebrasi, Eyler burchaklari (A, B, C), Kvaternionlar, DH parametrlari va To'g'ri/Teskari kinematika.",
        "lessons": [
            {
                "id": "05-rodrigues-rotation-formula",
                "title": "Fazoviy burilishlar va Rodrigues aylantirish formulasi",
                "summary": "so(3) Lie algebrasi, skew-symmetric operator [k]_x va Rodrigues formulasining geometrik hamda matritsaviy eksponensial (e^{theta K}) keltirib chiqarilishi.",
                "tech": "Python, NumPy, Rodrigues Formula, Matrix Logarithm",
            },
            {
                "id": "06-rotation-matrices-and-quaternions",
                "title": "Aylanish matritsalari, Eyler burchaklari va Kvaternionlar",
                "summary": "KUKA Z-Y'-X'' (A, B, C) Eyler burchaklari, Gimbal Lock (B=+-90) muammosi va to'rt o'lchamli birlik kvaternionlar (H) orqali SLERP interpolyatsiyasi.",
                "tech": "Python, SciPy, KUKA Euler A-B-C, Quaternions, SLERP",
            },
            {
                "id": "07-dh-parameters-modelling",
                "title": "Denavit-Hartenberg (DH) parametrlari modellashtirishi",
                "summary": "Standart va Modifikatsiyalangan DH konvensiyalari. KUKA KR 6 R900-2 uchun rasmiy DH koordinata jadvallarini noldan qurish.",
                "tech": "DH Conventions, Link Coordinate Assignment, SymPy",
            },
            {
                "id": "08-forward-kinematics-solver",
                "title": "To'g'ri kinematika (Forward Kinematics) solveri",
                "summary": "SE(3) transformatsiya matritsalari zanjiri. Bo'g'in burchaklariga ko'ra flanetsning fazodagi yakuniy o'rnini hisoblash va $POS_ACT bilan tekshirish.",
                "tech": "Python, SE(3) Transformations, KRL $POS_ACT",
            },
            {
                "id": "09-inverse-kinematics-analytical",
                "title": "Analitik teskari kinematika (Pieper usuli)",
                "summary": "Sferik bilak uchun Piper (Pieper) dekouplingi, 8 ta analitik yechim, KUKA Status (S) va Turn (T) butun sonli bitlarining fizik ma'nosi.",
                "tech": "Pieper Criteria, Analytical IK (8 solutions), Status & Turn",
            },
            {
                "id": "10-numerical-inverse-kinematics",
                "title": "Raqamli (Numerical) teskari kinematika usullari",
                "summary": "Nyuton-Rafson iteratsiyasi, Yakobian transponirlangan va Levenberg-Marquardt (Damped Least Squares) optimallashtirish algoritmlari.",
                "tech": "Python, Newton-Raphson, Levenberg-Marquardt, Optimization",
            },
        ],
    },
    "kuka-robotics-phase-3-differential-kinematics": {
        "title": "Phase 3: Differensial Kinematika, Yakobian va Dinamika",
        "description": "Geometrik Yakobian, singulyarlik holatlari tahlili, Nyuton-Eyler dinamikasi va kuch-moment datchiklari (Force-Torque Control).",
        "lessons": [
            {
                "id": "11-jacobian-matrix-derivation",
                "title": "Geometrik Yakobian matritsasi va tezliklar tahlili",
                "summary": "Geometrik Yakobian J(q), bo'g'in tezliklarining flanets chiziqli va burchak tezliklariga differensial bog'liqligi va ramziy hisoblash.",
                "tech": "Geometric Jacobian, SymPy Symbolic Kinematics, Velocity Twist",
            },
            {
                "id": "12-singularity-analysis",
                "title": "Singulyarlik tahlili va manipulyativlik ellipsoidi",
                "summary": "det(J)=0 tahlili: Bilak (Wrist A5=0), Yelka (Shoulder) va Chegara singulyarliklari, Yoshikawa manipulyativlik indeksi va singulyarlikdan qochish.",
                "tech": "Singularity Avoidance, Yoshikawa Ellipsoid, Damped Inversion",
            },
            {
                "id": "13-robot-dynamics-and-forces",
                "title": "Robot dinamikasi va kuch-moment tenglamalari",
                "summary": "Nyuton-Eyler va Lagranj-Eyler tenglamalari. Massalar inersiyasi, Koriolis/markazdan qochma kuchlar va gravitatsiya kompensatsiyasi.",
                "tech": "Newton-Euler, Lagrange Dynamics, Torque Load Profiling",
            },
            {
                "id": "14-force-torque-control",
                "title": "Kuch-moment boshqaruvi (KUKA.ForceTorqueControl)",
                "summary": "6 o'qli kuch-moment datchiklari va KUKA.ForceTorqueControl paketi. Admittance va Impedance virtual moslashuvchanlik boshqaruvi.",
                "tech": "6-Axis F/T Sensors, Admittance / Impedance Control",
            },
        ],
    },
    "kuka-robotics-phase-4-krl-programming": {
        "title": "Phase 4: KUKA Robot Language (KRL) Dasturlash",
        "description": "Sanoat KRL sintaksisi, harakat buyruqlari (PTP, LIN, CIRC, Splines), asinxron INTERRUPT, ProfiNet/EtherCAT I/O va modulli arxitektura.",
        "lessons": [
            {
                "id": "15-krl-syntax-and-variables",
                "title": "KRL sintaksisi, o'zgaruvchilar va ma'lumotlar arxitekturasi",
                "summary": "KRL tili sintaksisi, .src va .dat fayllar tuzilishi, FRAME, POS, E6POS, AXIS, E6AXIS maxsus tiplari.",
                "tech": "KRL (.src, .dat), FRAME, POS, E6POS, WorkVisual",
            },
            {
                "id": "16-advanced-motion-commands",
                "title": "Harakat buyruqlari va trayektoriyani silliqlash",
                "summary": "PTP, LIN, CIRC buyruqlari, trayektoriyani silliqlash (C_PTP, C_DIS, C_ORI), $ADVANCE ko'rsatkichi va zamonaviy Spline (SLIN, SCIRC, SPL) bloklari.",
                "tech": "PTP/LIN/CIRC, Splines (SLIN/SCIRC), C_DIS, $ADVANCE",
            },
            {
                "id": "17-logic-and-interrupts",
                "title": "Mantiqiy operatorlar, sikllar va INTERRUPT mexanizmlari",
                "summary": "Mantiqiy shartlar, sikllar (LOOP, WHILE, FOR) hamda asinxron uzilishlar (INTERRUPT) orqali avariya to'xtashlari (BRAKE) va chekinish.",
                "tech": "INTERRUPT Logic, BRAKE, Event Handling, KRL",
            },
            {
                "id": "18-industrial-io-and-fieldbus",
                "title": "Sanoat tarmoqlari (Fieldbus) va raqamli I/O integratsiyasi",
                "summary": "ProfiNet, EtherCAT protokollari, WorkVisual orqali signallarni xaritalash, $IN va $OUT signallari orqali pnevmatik tutqichlarni boshqarish.",
                "tech": "ProfiNet, EtherCAT, WorkVisual Mapping, $IN/$OUT",
            },
            {
                "id": "19-subprograms-and-expert-programming",
                "title": "Subprogrammalar, funksiyalar va Expert KRL dasturlash",
                "summary": "Global va lokal qism-dasturlar, funksiyalar (DEFFCT), argument uzatish va modulli parametrik zavod avtomatizatsiyasi karkasini qurish.",
                "tech": "Expert KRL, Subroutines, Functions, Modular Architecture",
            },
        ],
    },
    "kuka-robotics-phase-5-advanced-integration": {
        "title": "Phase 5: Tashqi Interfeyslar, ROS2 va Sun'iy Intellekt",
        "description": "KUKA RSI real vaqtli interfeysi, ROS2 drayverlari, MoveIt2 to'siqlarni aylanib o'tish va Computer Vision (PnP, Hand-Eye AX=XB) integratsiyasi.",
        "lessons": [
            {
                "id": "20-kuka-rsi-interface",
                "title": "KUKA RSI (Robot Sensor Interface) real-time interfeysi",
                "summary": "KUKA RSI arxitekturasi: tashqi kompyuterdan real vaqtda (<12ms siklda) XML paketlar protokoli orqali to'g'ridan-to'g'ri boshqaruv.",
                "tech": "KUKA RSI, Real-Time XML Ethernet Protocol, Corrections",
            },
            {
                "id": "21-ros2-driver-integration",
                "title": "ROS 2 drayverlari integratsiyasi va RViz vizuallashtirish",
                "summary": "ROS 2 (Humble/Iron) arxitekturasi, rasmiy kuka_robot_drivers, robot holatini o'qish va RViz muhitida 3D URDF modelini harakatlantirish.",
                "tech": "ROS 2 Humble, kuka_robot_drivers, URDF, RViz2",
            },
            {
                "id": "22-moveit2-trajectory-planning",
                "title": "MoveIt 2 yordamida to'siqlarni aylanib o'tuvchi harakat rejalashtirish",
                "summary": "MoveIt 2 kutubxonasi, OMPL rejalashtiruvchilari, dinamik paydo bo'lgan to'siqlarni chetlab o'tish (Collision Avoidance).",
                "tech": "MoveIt2, OMPL, FCL Collision Avoidance, Trajectory Planning",
            },
            {
                "id": "23-computer-vision-pick-and-place",
                "title": "Computer Vision va Hand-Eye kalibratsiyasi (Pick-and-Place)",
                "summary": "Pinhole kamera modeli, OpenCV cv2.solvePnP, cv2.Rodrigues, Hand-Eye AX=XB (Tsai-Lenz) kalibratsiyasi va robotlashtirilgan saralash.",
                "tech": "OpenCV, PnP, Hand-Eye Calibration (AX=XB), Pick-and-Place",
            },
        ],
    },
    "kuka-robotics-phase-6-industrial-applications": {
        "title": "Phase 6: Sanoatdagi Amaliy Ishlab Chiqarish Loyihalari",
        "description": "Murakkab 3D choklar bo'ylab payvandlash/yelimlash traektoriyalari, konveyerga moslashuvchi (Conveyor Tracking) palletizatsiya va saralash.",
        "lessons": [
            {
                "id": "24-trajectory-welding-and-glueing",
                "title": "Payvandlash va yelim surtish traektoriyalarini dasturlash",
                "summary": "Payvandlash (Welding) va yelimlash (Glueing) texnologik talablari. Doimiy chiziqli tezlikda murakkab fazoviy 3D choklar bo'ylab harakat.",
                "tech": "3D Continuous Path, Welding/Glueing Dispensing, Splines",
            },
            {
                "id": "25-palletizing-and-sorting-system",
                "title": "Palletizatsiya va konveyerga dinamik moslashuvchi saralash tizimi",
                "summary": "Palletizatsiya va konveyer harakat tezligiga moslashuvchi (Conveyor Tracking) aqlli saralash tizimi. KRL va Python aralash master-loyihasi.",
                "tech": "Conveyor Tracking, Palletizing Pattern, Master Integration",
            },
        ],
    },
}

TOPIC_CLAUDE_MD = """# AI Developer Instructions: {lesson_id}

## 🎯 Lesson Context: {lesson_title}
Belongs to **{phase_title}** of the KUKA Industrial Robotics Course.
Target Manipulator: **KUKA KR 6 R900-2 (KR AGILUS-2)**.

## 📁 Internal Boilerplate Structure
* `src/krl/`: Industrial KRL files (`.src`, `.dat`) strictly formatted for KSS 8.3+.
* `src/scripts/`: Python 3.10+ verification scripts with type hinting and `pytest` tests.
* `sim/`: Simulation scenes (`.vcmx`, `.urdf`).
* `docs/`: Mathematical derivations and schematics.
* `README.md`: Comprehensive student guide in Uzbek/English with formulas and tasks.

## 📐 Mathematical Standards
Follow the notation defined in the course master cheatsheet:
* Skew-symmetric operator: $[\\vec{{k}}]_\\times$
* Rodrigues formula: $R(\\vec{{k}}, \\theta) = I + \\sin\\theta K + (1-\\cos\\theta)K^2$
* KUKA Euler convention: Tait-Bryan $Z-Y'-X''$ ($A, B, C$)
"""

TOPIC_README_MD = """# {lesson_title}
## {lesson_id} | {phase_title}

[![Phase](https://img.shields.io/badge/Phase-{phase_id}-blue.svg)](#)
[![Robot](https://img.shields.io/badge/KUKA-KR%206%20R900--2-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 📖 Dars Haqida (Overview)
{lesson_summary}

* **Texnologiyalar:** `{lesson_tech}`
* **Asosiy Manipulyator:** KUKA KR 6 R900-2 (KR AGILUS-2)

---

### 🗂️ Jild Tuzilishi (Mandatory Boilerplate)
```
{lesson_id}/
├── src/
│   ├── krl/            # KRL (.src, .dat) dasturlari
│   └── scripts/        # Python / MATLAB skriptlari
├── sim/                # KUKA.Sim Pro (.vcmx) va URDF simulyatsiya fayllari
├── docs/               # Matematik hisob-kitoblar va grafiklar
├── CLAUDE.md           # AI dasturchi ko'rsatmalari
└── README.md           # Ushbu to'liq dars qo'llanmasi
```

---

### 🎯 Laboratoriya Topshirig'i (Lab Assignment)
1. Nazariy qismdagi formulalar va algoritmlarni tahlil qilish.
2. `src/scripts/` jildidagi Python algoritmini ishga tushirib, hisob-kitoblarni tekshirish.
3. `src/krl/` jildidagi KRL dasturini KUKA.Sim Pro yoki OfficeLite virtual kontrolleriga yuklab simulyatsiya qilish.

---
🔗 **[Bosh Kurs Mundarijasiga Qaytish (Master Syllabus)](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
"""

PHASE_README_MD = """# {phase_title}
## {phase_id}

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Topics](https://img.shields.io/badge/Topics-kuka--robotics--course%20%7C%20mechatronics%20%7C%20krl--programming%20%7C%20ros2--robotics%20%7C%20industrial--automation%20%7C%20samdu%20%7C%20tsu-blue.svg)](#)

---

### 📖 Bob Tavsifi
{phase_description}

Bu repozitoriy **KUKA Industrial Robotics Course** o'quv dasturining bir qismi bo'lib, quyidagi darslarni o'z ichiga oladi:

### 📑 Darslar Mundarijasi
{lessons_list}

---

### 🏛️ Repozitoriya Tuzilishi
```
{phase_id}/
{tree_structure}
```

---

### 👥 Hamkorlik va Mualliflik
* **Muallif:** Muzaffarbek Mustafayev (SamDU & TSU)
* 🔗 **[Bosh Kurs Mundarijasi (Master Navigator Hub)](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
"""


def scaffold(target_root: Path):
    target_root.mkdir(parents=True, exist_ok=True)
    print(f"[*] Scaffolding 6 Phase Repositories at: {target_root.resolve()}")

    for phase_id, phase_data in PHASES.items():
        phase_dir = target_root / phase_id
        phase_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n[+] Created Phase Repo: {phase_id}")

        lessons_list_md = []
        tree_md = []

        for lesson in phase_data["lessons"]:
            lesson_id = lesson["id"]
            lesson_dir = phase_dir / lesson_id
            lessons_list_md.append(f"* [**{lesson_id}**: {lesson['title']}](./{lesson_id}) — *{lesson['summary']}*")
            tree_md.append(f"├── {lesson_id}/")

            # Subfolders
            (lesson_dir / "src" / "krl").mkdir(parents=True, exist_ok=True)
            (lesson_dir / "src" / "scripts").mkdir(parents=True, exist_ok=True)
            (lesson_dir / "sim").mkdir(parents=True, exist_ok=True)
            (lesson_dir / "docs" / "figures").mkdir(parents=True, exist_ok=True)

            # Lesson CLAUDE.md
            (lesson_dir / "CLAUDE.md").write_text(
                TOPIC_CLAUDE_MD.format(
                    lesson_id=lesson_id,
                    lesson_title=lesson["title"],
                    phase_title=phase_data["title"],
                ),
                encoding="utf-8",
            )

            # Lesson README.md
            (lesson_dir / "README.md").write_text(
                TOPIC_README_MD.format(
                    lesson_id=lesson_id,
                    lesson_title=lesson["title"],
                    phase_id=phase_id,
                    phase_title=phase_data["title"],
                    lesson_summary=lesson["summary"],
                    lesson_tech=lesson["tech"],
                ),
                encoding="utf-8",
            )

            # Placeholder files
            (lesson_dir / "src" / "scripts" / "__init__.py").write_text("", encoding="utf-8")
            (lesson_dir / "sim" / ".gitkeep").write_text("", encoding="utf-8")
            (lesson_dir / "docs" / "figures" / ".gitkeep").write_text("", encoding="utf-8")

        # Phase Top-Level README
        (phase_dir / "README.md").write_text(
            PHASE_README_MD.format(
                phase_title=phase_data["title"],
                phase_id=phase_id,
                phase_description=phase_data["description"],
                lessons_list="\n".join(lessons_list_md),
                tree_structure="\n".join(tree_md),
            ),
            encoding="utf-8",
        )


def main():
    parser = argparse.ArgumentParser(description="KUKA Robotics Course Scaffolder")
    parser.add_argument(
        "--target-dir",
        default="../",
        help="Directory where Phase repositories should be created (default: ../)",
    )
    args = parser.parse_args()
    scaffold(Path(args.target_dir))


if __name__ == "__main__":
    main()
