#!/usr/bin/env python3
"""
KUKA Industrial Robotics Course: Phase Repositories Scaffolder
Creates complete boilerplate templates for all 5 Phase repositories and their 13 topic subdirectories.

Usage:
    python scripts/scaffold_phase_repos.py --target-dir ../
"""

import os
import sys
import argparse
from pathlib import Path

PHASES = {
    "kuka-robotics-phase-1-basics": {
        "title": "1-Bob: Kirish va Simulyatsiya Muhiti",
        "description": "Sanoat robototexnikasi asoslari, KUKA KR 6 R900-2 manipulyatori, KUKA.Sim Pro va OfficeLite muhiti.",
        "topics": [
            {
                "id": "01-introduction",
                "title": "Sanoat robototexnikasi asoslari va KR AGILUS manipulyatori",
                "summary": "ISO 10218 xavfsizlik qoidalari, KR 6 R900-2 texnik tavsifi, KUKA smartPAD boshqaruvi va Jogging rejimlari.",
                "tech": "smartPAD, KRC4, Safety Standards",
            },
            {
                "id": "02-simulation-setup",
                "title": "Virtual simulyatsiya muhitini o'rnatish va sozlash",
                "summary": "KUKA.Sim Pro (3.1/4.x), KUKA OfficeLite VRC, WorkVisual loyihasini yaratish va URDF eksporti.",
                "tech": "KUKA.Sim Pro, OfficeLite, WorkVisual, URDF",
            },
        ],
    },
    "kuka-robotics-phase-2-kinematics": {
        "title": "2-Bob: Matematika va Kinematika",
        "description": "Fazoviy burilishlar, Qiya-simmetrik matritsalar, Rodrig formulasi, DH parametrlari va To'g'ri/Teskari kinematika.",
        "topics": [
            {
                "id": "03-rodrigues-formula",
                "title": "Fazoviy burilishlar va Rodrig formulasi",
                "summary": "so(3) Lie algebrasi, skew-symmetric operator, Rodrig formulasining geometrik va matritsaviy tahlili.",
                "tech": "Python, NumPy, SymPy, LaTeX",
            },
            {
                "id": "04-rotation-matrices",
                "title": "Aylanish matritsalari, Eyler burchaklari va Kvaternionlar",
                "summary": "SO(3) guruhi, KUKA Z-Y'-X'' (A, B, C) burchaklari, Gimbal Lock va Kvaternion SLERP interpolyatsiyasi.",
                "tech": "Python, SciPy, SpatialMath",
            },
            {
                "id": "05-dh-parameters",
                "title": "Denavit-Hartenberg (DH) parametrlari",
                "summary": "Standart va modifikatsiyalangan DH konventsiyalari, KR 6 R900-2 uchun koordinatalar tizimini o'rnatish.",
                "tech": "Python, SymPy, CAD Kinematics",
            },
            {
                "id": "06-forward-kinematics",
                "title": "To'g'ri kinematika (Forward Kinematics)",
                "summary": "SE(3) transformatsiya zanjiri, flanets pozitsiyasini hisoblash va $POS_ACT bilan solishtirish.",
                "tech": "Python, SymPy, KRL $POS_ACT",
            },
            {
                "id": "07-inverse-kinematics",
                "title": "Teskari kinematika (Inverse Kinematics)",
                "summary": "Sferik bilak uchun Piper (Pieper) dekoupling usuli, 8 ta analitik yechim, KUKA Status va Turn bitlari.",
                "tech": "Python, C++, Analytical Solvers",
            },
        ],
    },
    "kuka-robotics-phase-3-singularity": {
        "title": "3-Bob: Yakobian va Singulyarlik Tahlili",
        "description": "Geometrik Yakobian matritsasi, bo'g'in tezliklari, singulyarlik holatlari va manipulyativlik ellipsoidi.",
        "topics": [
            {
                "id": "08-jacobian-matrix",
                "title": "Robot Yakobian matritsasi va tezliklar tahlili",
                "summary": "Geometrik Yakobian J(q), flanets chiziqli va burchak tezliklari, Damped Least Squares usuli.",
                "tech": "Python, RoboticToolbox, Velocity Kinematics",
            },
            {
                "id": "09-singularity-analysis",
                "title": "Singulyarlik tahlili va manipulyativlik",
                "summary": "det(J)=0 tahlili, Bilak (Wrist A5=0), Yelka (Shoulder) va Chegara singulyarliklari, Yoshikawa indeksi.",
                "tech": "Python, MATLAB, Matplotlib 3D",
            },
        ],
    },
    "kuka-robotics-phase-4-krl-programming": {
        "title": "4-Bob: KUKA Robot Language (KRL) Dasturlash",
        "description": "Sanoat KRL sintaksisi, harakat buyruqlari (PTP, LIN, CIRC, Splines), signallar va uskunalar integratsiyasi.",
        "topics": [
            {
                "id": "10-krl-basics",
                "title": "KRL asoslari va ma'lumotlar arxitekturasi",
                "summary": ".src va .dat fayllar strukturasi, FRAME, POS, E6POS tiplari, shartli operatorlar va sikllar.",
                "tech": "KRL (.src, .dat), WorkVisual",
            },
            {
                "id": "11-motion-commands",
                "title": "Harakat buyruqlari va trayektoriyani boshqarish",
                "summary": "PTP, LIN, CIRC, Spline (SLIN, SCIRC), trayektoriyani silliqlash (C_PTP, C_DIS) va $ADVANCE.",
                "tech": "KRL Motion, Splines, KSS",
            },
            {
                "id": "12-io-interfacing",
                "title": "Sanoat I/O va tutqich (Gripper) integratsiyasi",
                "summary": "$IN va $OUT signallari, WAIT FOR buyruqlari, WorkVisual orqali EtherCAT modullarini sozlash.",
                "tech": "KRL I/O, EtherCAT, Pneumatics",
            },
        ],
    },
    "kuka-robotics-phase-5-advanced-integration": {
        "title": "5-Bob: Computer Vision (Texnik Ko'rish) va Kamerani Kalibrlash",
        "description": "Pinhole kamera modeli, OpenCV PnP, cv2.Rodrigues, Hand-Eye kalibratsiyasi (AX = XB) va saralash amaliyoti.",
        "topics": [
            {
                "id": "13-computer-vision-integration",
                "title": "Kompyuter ko'rishi, PnP va Hand-Eye kalibratsiyasi",
                "summary": "Kamera kalibrlash, cv2.solvePnP, cv2.Rodrigues, Hand-Eye AX=XB (Tsai-Lenz), Visual Pick-and-Place.",
                "tech": "Python, OpenCV, cv2.Rodrigues, KRL Base",
            },
        ],
    },
}

TOPIC_CLAUDE_MD = """# AI Developer Instructions: {topic_id}

## 🎯 Topic Context: {topic_title}
Belongs to **{phase_title}** of the KUKA Industrial Robotics Course.
Target Manipulator: **KUKA KR 6 R900-2 (KR AGILUS-2)**.

## 📁 Internal Structure
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

TOPIC_README_MD = """# {topic_title}
## {topic_id} | {phase_title}

[![Phase](https://img.shields.io/badge/Phase-{phase_id}-blue.svg)](#)
[![Robot](https://img.shields.io/badge/KUKA-KR%206%20R900--2-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 📖 Mavzu Haqida (Overview)
{topic_summary}

* **Texnologiyalar:** `{topic_tech}`
* **Asosiy Manipulyator:** KUKA KR 6 R900-2 (KR AGILUS-2)

---

### 🗂️ Jild Strukturasi
```
{topic_id}/
├── src/
│   ├── krl/            # KRL (.src, .dat) dasturlari
│   └── scripts/        # Python / MATLAB skriptlari
├── sim/                # KUKA.Sim Pro va URDF simulyatsiya fayllari
├── docs/               # Matematik hisob-kitoblar va rasmlar
├── CLAUDE.md           # AI dasturchi ko'rsatmalari
└── README.md           # Ushbu qo'llanma
```

---

### 🎯 Laboratoriya Topshirig'i (Lab Assignment)
1. Nazariy qismdagi formulalar va algoritmlarni tahlil qilish.
2. `src/scripts/` jildidagi Python algoritmini ishga tushirib, natijalarni tekshirish.
3. `src/krl/` jildidagi KRL dasturini KUKA.Sim Pro yoki OfficeLite virtual kontrolleriga yuklab simulyatsiya qilish.

---
🔗 **[Bosh Kurs Mundarijasiga Qaytish (Master Syllabus)](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
"""

PHASE_README_MD = """# {phase_title}
## {phase_id}

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Topics](https://img.shields.io/badge/Topics-kuka--robotics--course%20%7C%20mechatronics%20%7C%20krl--programming%20%7C%20samdu%20%7C%20tsu-blue.svg)](#)

---

### 📖 Bob Tavsifi
{phase_description}

Bu repozitoriy **KUKA Industrial Robotics Course** o'quv dasturining bir qismi bo'lib, quyidagi mavzularni o'z ichiga oladi:

### 📑 Mavzular Ro'yxati
{topics_list}

---

### 🏛️ Loyiha Strukturasi
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
    print(f"[*] Scaffolding Phase Repositories at: {target_root.resolve()}")

    for phase_id, phase_data in PHASES.items():
        phase_dir = target_root / phase_id
        phase_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n[+] Created Phase Repo Directory: {phase_id}")

        topics_list_md = []
        tree_md = []

        for topic in phase_data["topics"]:
            topic_id = topic["id"]
            topic_dir = phase_dir / topic_id
            topics_list_md.append(f"* [**{topic_id}**: {topic['title']}](./{topic_id}) — *{topic['summary']}*")
            tree_md.append(f"├── {topic_id}/")

            # Subfolders
            (topic_dir / "src" / "krl").mkdir(parents=True, exist_ok=True)
            (topic_dir / "src" / "scripts").mkdir(parents=True, exist_ok=True)
            (topic_dir / "sim").mkdir(parents=True, exist_ok=True)
            (topic_dir / "docs" / "figures").mkdir(parents=True, exist_ok=True)

            # Topic CLAUDE.md
            (topic_dir / "CLAUDE.md").write_text(
                TOPIC_CLAUDE_MD.format(
                    topic_id=topic_id,
                    topic_title=topic["title"],
                    phase_title=phase_data["title"],
                ),
                encoding="utf-8",
            )

            # Topic README.md
            (topic_dir / "README.md").write_text(
                TOPIC_README_MD.format(
                    topic_id=topic_id,
                    topic_title=topic["title"],
                    phase_id=phase_id,
                    phase_title=phase_data["title"],
                    topic_summary=topic["summary"],
                    topic_tech=topic["tech"],
                ),
                encoding="utf-8",
            )

            # Placeholder files
            (topic_dir / "src" / "scripts" / "__init__.py").write_text("", encoding="utf-8")
            (topic_dir / "sim" / ".gitkeep").write_text("", encoding="utf-8")
            (topic_dir / "docs" / "figures" / ".gitkeep").write_text("", encoding="utf-8")

        # Phase Top-Level README
        (phase_dir / "README.md").write_text(
            PHASE_README_MD.format(
                phase_title=phase_data["title"],
                phase_id=phase_id,
                phase_description=phase_data["description"],
                topics_list="\n".join(topics_list_md),
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
