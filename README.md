# KUKA Industrial Robotics Course: Master Navigator & Syllabus
## 6-Axis Manipulator Kinematics, KRL Programming & Computer Vision Integration

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/Manipulator-KUKA%20KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![Controller: KUKA KRC4/KRC5](https://img.shields.io/badge/Controller-KUKA%20KR%20C4%20%7C%20KR%20C5-red.svg)](https://www.kuka.com)
[![Academic Alliance](https://img.shields.io/badge/Academic%20Alliance-SamDU%20%26%20TSU-blue.svg)](https://www.samdu.uz)
[![GitHub Topics](https://img.shields.io/badge/Topics-kuka--robotics--course%20%7C%20mechatronics%20%7C%20krl--programming%20%7C%20robot--kinematics%20%7C%20samdu%20%7C%20tsu-lightgrey.svg)](#)

---

## 🧭 Kurs Haqida va Umumiy Konseptsiya

**KUKA Industrial Robotics Course** — sanoat robototexnikasi bo'yicha professional ochiq ta'lim kursi va ilmiy-tadqiqot platformasi. Kurs 6 erkinlik darajali (6-DoF) **KUKA KR 6 R900-2 (KR AGILUS-2)** manipulyatori, KUKA KRC4/KRC5 kontrolleri va KUKA.Sim Pro simulyatsiya muhiti negizida ishlab chiqilgan.

Kurs **Samarqand Davlat Universiteti (SamDU)** hamda **Tomsk Davlat Universiteti (TSU)** Mexatronika va Robototexnika kafedralarining amaliy tajribasi va PhD ilmiy-tadqiqot ishlari asosida yaratilgan.

### 🏛️ Yangilangan Modulli Repozitoriylar Strukturasi (Boblar boʻyicha)

Monolitik tizim o'rniga kurs **1 ta Navigator (Mundarija) Hubi** va **5 ta mustaqil Bob (Phase) Repozitoriylari**ga ajratilgan:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│             kuka-industrial-robotics-course (Navigator / Syllabus Hub)                 │
│         Faqat umumiy kurs mundarijasi, matematik cheatsheet va havolalar (links)       │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
    ┌───────────────────┬───────────────────┼───────────────────┬────────────────────┐
    ▼                   ▼                   ▼                   ▼                    ▼
[ 1-BOB: BASICS ]  [ 2-BOB: KINEMATICS ] [ 3-BOB: SINGULARITY ] [ 4-BOB: KRL ]   [ 5-BOB: VISION ]
Phase 1 Repo       Phase 2 Repo         Phase 3 Repo           Phase 4 Repo     Phase 5 Repo
├── 01-intro       ├── 03-rodrigues     ├── 08-jacobian        ├── 10-krl-basics├── 13-cv-vision
└── 02-sim-setup   ├── 04-rot-matrices  └── 09-singularity     ├── 11-motion
                   ├── 05-dh-params                            └── 12-io
                   ├── 06-forward-kin
                   └── 07-inverse-kin
```

---

## 🌐 Boblar Repozitoriylari va Mavzular Mundarijasi

| Bob | Repozitoriy Havolasi (Phase Repo) | Ichki Mavzular Jildlari | Texnologiyalar & Stack |
| :---: | :--- | :--- | :---: |
| **1-Bob** | 🔗 [**`kuka-robotics-phase-1-basics`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-1-basics)<br>*(Kirish va Simulyatsiya)* | • [`01-introduction`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-1-basics/tree/main/01-introduction)<br>• [`02-simulation-setup`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-1-basics/tree/main/02-simulation-setup) | KUKA smartPAD, KUKA.Sim Pro, OfficeLite, WorkVisual, URDF |
| **2-Bob** | 🔗 [**`kuka-robotics-phase-2-kinematics`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-2-kinematics)<br>*(Matematika va Kinematika)* | • [`03-rodrigues-formula`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-2-kinematics/tree/main/03-rodrigues-formula)<br>• [`04-rotation-matrices`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-2-kinematics/tree/main/04-rotation-matrices)<br>• [`05-dh-parameters`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-2-kinematics/tree/main/05-dh-parameters)<br>• [`06-forward-kinematics`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-2-kinematics/tree/main/06-forward-kinematics)<br>• [`07-inverse-kinematics`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-2-kinematics/tree/main/07-inverse-kinematics) | Lie Algebra $\mathfrak{so}(3)$, $SO(3)$, Rodrigues, Quaternions, DH Parameters, Pieper IK |
| **3-Bob** | 🔗 [**`kuka-robotics-phase-3-singularity`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-3-singularity)<br>*(Yakobian va Singulyarlik)* | • [`08-jacobian-matrix`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-3-singularity/tree/main/08-jacobian-matrix)<br>• [`09-singularity-analysis`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-3-singularity/tree/main/09-singularity-analysis) | Geometrik Yakobian $J(\vec{q})$, $\det(J)=0$, Wrist / Shoulder / Boundary Singularity, Yoshikawa Ellipsoid |
| **4-Bob** | 🔗 [**`kuka-robotics-phase-4-krl-programming`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-4-krl-programming)<br>*(KRL Dasturlash)* | • [`10-krl-basics`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-4-krl-programming/tree/main/10-krl-basics)<br>• [`11-motion-commands`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-4-krl-programming/tree/main/11-motion-commands)<br>• [`12-io-interfacing`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-4-krl-programming/tree/main/12-io-interfacing) | KRL (`.src`, `.dat`), `PTP`, `LIN`, `CIRC`, `SLIN`, `SCIRC`, `$ADVANCE`, WorkVisual I/O, EtherCAT |
| **5-Bob** | 🔗 [**`kuka-robotics-phase-5-advanced-integration`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-5-advanced-integration)<br>*(Computer Vision)* | • [`13-computer-vision-integration`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-5-advanced-integration/tree/main/13-computer-vision-integration) | Pinhole Model, PnP, `cv2.Rodrigues()`, Hand-Eye $AX = XB$ (Tsai-Lenz), Visual Pick & Place |

---

## 🦾 KUKA KR 6 R900-2 (KR AGILUS-2) Texnik Tavsifi

Kursdagi barcha hisob-kitoblar, kinematik formulalar, DH jadvallari va KRL trayektoriyalari ushbu robot modeliga asoslangan:

* **Manipulyator turi:** 6 o'qli vertikal antropomorfik sanoat roboti
* **Maksimal yuk ko'tarish qobiliyati (Rated Payload):** $6\text{ kg}$
* **Maksimal yetib borish masofasi (Max Reach):** $901.5\text{ mm}$
* **Pozitsiya takrorlanuvchanligi (ISO 9283 Repeatability):** $\pm 0.02\text{ mm}$
* **Boshqaruv tizimi:** KUKA KRC4 compact / KRC5 micro (KSS 8.3 / 8.6 / 8.7)
* **O'qlar burilish burchaklari (Software Joint Limits):**
  * $A_1: \pm 170^\circ$
  * $A_2: -190^\circ / +45^\circ$
  * $A_3: -120^\circ / +156^\circ$
  * $A_4: \pm 185^\circ$
  * $A_5: \pm 120^\circ$
  * $A_6: \pm 350^\circ$
* **O'qlar maksimal tezliklari:**
  * $A_1: 360^\circ/\text{s}, \quad A_2: 300^\circ/\text{s}, \quad A_3: 360^\circ/\text{s}$
  * $A_4: 381^\circ/\text{s}, \quad A_5: 388^\circ/\text{s}, \quad A_6: 615^\circ/\text{s}$

---

## 📖 Chuqurlashtirilgan Nazariy va Amaliy O'quv Rejasi (Boblar Kesimida)

### ⚙️ 1-BOB: Kirish va Simulyatsiya Muhiti
*Ombor: [`kuka-robotics-phase-1-basics`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-1-basics)*

* **01-Mavzu. Sanoat robototexnikasi asoslari va KR AGILUS manipulyatori:**
  * Sanoat robotlari xavfsizlik standartlari (ISO 10218-1/2, ISO/TS 15066).
  * KUKA KR 6 R900-2 apparat arxitekturasi: bo'g'inlar, motorlar, tormozlar, resolverlar.
  * KUKA smartPAD yordamida robotni boshqarish: Jogging rejimlari (Axis, World, Tool, Base).
* **02-Mavzu. Virtual simulyatsiya muhitini o'rnatish va sozlash:**
  * **KUKA.Sim Pro (3.1 / 4.x)** dasturiy ta'minoti va 3D virtual hujayra qurish.
  * **KUKA OfficeLite** (Virtual Robot Controller — VRC) ni ishga tushirish va KSS sozlamalari.
  * **KUKA WorkVisual** loyihasini yaratish, robot kinematik parametrlarini yuklash.
  * URDF / Xacro modelini eksport qilish va ROS 2 MoveIt muhitiga integratsiya.

---

### 🧮 2-BOB: Matematika va Kinematika
*Ombor: [`kuka-robotics-phase-2-kinematics`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-2-kinematics)*

* **03-Mavzu. Fazoviy burilishlar va Rodrig formulasi:**
  * Koordinatalar tizimi va qiya-simmetrik (skew-symmetric) matritsalar $\mathfrak{so}(3)$.
  * Ixtiyoriy vektor $[\vec{k}]_\times$ operatori va vektorli ko'paytma.
  * Fazoda ixtiyoriy $\vec{k}$ o'qi atrofida $\theta$ burchakka burish:
    $$\vec{v}_{rot} = \vec{v}\cos\theta + (\vec{k}\times\vec{v})\sin\theta + \vec{k}(\vec{k}\cdot\vec{v})(1-\cos\theta)$$
  * Matritsaviy Rodrig formulasi:
    $$R(\vec{k}, \theta) = I + \sin(\theta) K + (1 - \cos(\theta)) K^2$$
  * Teskari Rodrig formulasi: $\text{tr}(R) = 1 + 2\cos\theta$ orqali $\theta$ va $\vec{k}$ ni ajratish.
* **04-Mavzu. Aylanish matritsalari, Eyler burchaklari va Kvaternionlar:**
  * Maxsus Ortogonal Guruh $SO(3)$ va uning Lie algebrasi.
  * KUKA $Z-Y'-X''$ (Tait-Bryan: $A, B, C$) burchaklari va Gimbal Lock ($B = \pm 90^\circ$).
  * Giperkompleks sonlar va birlik kvaternionlar: $\mathbf{q} = [w, x, y, z] = [\cos(\theta/2), \vec{k}\sin(\theta/2)]$.
  * Rodrig $\longleftrightarrow$ Kvaternion $\longleftrightarrow$ KUKA Euler o'zaro bog'liqlik ko'prigi.
* **05-Mavzu. Denavit-Hartenberg (DH) parametrlari:**
  * Standart va Modifikatsiyalangan DH qoidalari.
  * KUKA KR 6 R900-2 uchun 6 ta bo'g'in koordinatalar tizimini o'rnatish ($z_i, x_i$).
  * Link parametrlari jadvali ($a_i, \alpha_i, d_i, \theta_i$).
* **06-Mavzu. To'g'ri kinematika (Forward Kinematics):**
  * Bir hil transformatsiya matritsalari zanjiri: $T_0^6(\vec{q}) = A_1 A_2 A_3 A_4 A_5 A_6$.
  * Flanetsning fazoviy holati ($X, Y, Z, A, B, C$) ni hisoblash.
  * Hisoblangan natijalarni KUKA `$POS_ACT` tizim o'zgaruvchisi bilan solishtirish.
* **07-Mavzu. Teskari kinematika (Inverse Kinematics):**
  * Sferik bilak ($A_4, A_5, A_6$ o'qlari bitta nuqtada kesishishi) uchun Piper (Pieper) dekoupling usuli.
  * Bilak markazini ajratish: $\vec{p}_{wc} = \vec{p}_e - d_6 \vec{a}$.
  * 8 ta analitik kinematik yechim (Arm Right/Left, Elbow Up/Down, Wrist Flip/No-Flip).
  * KUKA Status ($S$) va Turn ($T$) butun sonli bitlarining fizik ma'nosi.

---

### 📉 3-BOB: Yakobian va Singulyarlik Tahlili
*Ombor: [`kuka-robotics-phase-3-singularity`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-3-singularity)*

* **08-Mavzu. Robot Yakobian matritsasi:**
  * Geometrik Yakobian $J(\vec{q}) \in \mathbb{R}^{6\times 6}$:
    $$\begin{bmatrix} \vec{v}_e \\ \vec{\omega}_e \end{bmatrix} = J(\vec{q}) \dot{\vec{q}}$$
  * Bo'g'in tezliklarini flanets chiziqli va burchak tezliklariga o'tkazish.
  * Kuchsizlantirilgan eng kichik kvadratlar (Damped Least Squares) orqali teskari tezliklarni hisoblash.
* **09-Mavzu. Singulyarlik tahlili va manipulyativlik:**
  * Singulyarlik sharti: $\det(J(\vec{q})) = 0$ va $\text{rank}(J) < 6$.
  * **Bilak singulyarligi (Wrist Singularity):** $A_5 = 0^\circ$ (4 va 6-o'qlar kollinear bo'lib qolishi).
  * **Yelka singulyarligi (Shoulder Singularity):** Bilak markazi $A_1$ o'qi ustiga tushishi.
  * **Chegara singulyarligi (Elbow / Boundary Singularity):** Qo'l to'liq cho'zilishi yoki bukilishi.
  * Yoshikawa manipulyativlik ellipsoidi $w = \sqrt{\det(J J^T)}$ tahlili.

---

### 💻 4-BOB: KUKA Robot Language (KRL) Dasturlash
*Ombor: [`kuka-robotics-phase-4-krl-programming`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-4-krl-programming)*

* **10-Mavzu. KRL asoslari va ma'lumotlar arxitekturasi:**
  * Modul tuzilishi: `.src` (dastur kodi) va `.dat` (ma'lumotlar deklaratsiyasi).
  * Ma'lumot tiplari: `INT`, `REAL`, `BOOL`, `CHAR`, `FRAME`, `POS`, `E6POS`, `AXIS`, `E6AXIS`.
  * Shartli operatorlar (`IF-THEN-ELSE`, `SWITCH-CASE`) va sikllar (`FOR`, `WHILE`, `LOOP`).
* **11-Mavzu. Harakat buyruqlari va trayektoriyani boshqarish:**
  * Nuqtadan-nuqtaga harakat: `PTP` (tez va optimallashtirilgan).
  * Dekart fazosidagi chiziqli va aylana harakatlar: `LIN`, `CIRC`.
  * Zamonaviy Spline harakatlari: `SLIN`, `SCIRC`, `SPL`.
  * Trayektoriyani silliqlash (Approximation): `C_PTP`, `C_DIS`, `C_ORI`, `C_VEL`.
  * Kontrollerning oldindan o'qish ko'rsatkichi: `$ADVANCE` tizim o'zgaruvchisi.
* **12-Mavzu. Sanoat I/O va tutqich (Gripper) integratsiyasi:**
  * Raqamli kirish va chiqish signallari: `$IN[n]` va `$OUT[n]`.
  * Dastur to'xtashlari va kutishlar: `WAIT SEC`, `WAIT FOR $IN[1]==TRUE`.
  * WorkVisual yordamida EtherCAT / PROFINET orqali Beckhoff yoki Festo modullarini ulash.
  * Pnevmatik va elektr tutqichni boshqarish uchun xavfsiz sikllar yaratish.

---

### 👁️ 5-BOB: Computer Vision (Texnik Ko'rish) va Kamerani Kalibrlash
*Ombor: [`kuka-robotics-phase-5-advanced-integration`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-5-advanced-integration)*

* **13-Mavzu. Kompyuter ko'rishi, PnP va Hand-Eye kalibratsiyasi:**
  * Pinhole kamera modeli va ichki parametrlar matritsasi $K$.
  * OpenCV yordamida kamerani shaxmat doskasi yoki ChArUco orqali kalibrlash.
  * Perspective-$n$-Point (PnP) masalasi: `cv2.solvePnP` va uning chiqishidagi Rodrig burilish vektori $\vec{r}$.
  * Python `cv2.Rodrigues()` orqali vektor va $3\times 3$ matritsa o'rtasida o'tish.
  * Hand-Eye kalibratsiyasi: **Eye-in-Hand** va **Eye-to-Hand** konfiguratsiyalari.
  * Klassik $AX = XB$ tenglamasi (Tsai-Lenz va Park-Martin usullari).
  * Kameradan olingan ob'ekt koordinatasini KUKA `$BASE` tizimiga o'tkazish va konveyerdan buyumni saralash (Pick-and-Place).

---

## 📐 Qisqa Matematik Formulalar

Barcha matematik isbotlar, qadam-baqadam keltirib chiqarishlar va algoritmlar uchun alohida [**`MATH_CHEATSHEET.md`**](file:///c:/Users/muzaf/Desktop/kuka-robotics-course/MATH_CHEATSHEET.md) fayliga murojaat qiling.

* **Qiya-simmetrik matritsa:**
  $$K = [\vec{k}]_\times = \begin{bmatrix} 0 & -k_z & k_y \\ k_z & 0 & -k_x \\ -k_y & k_x & 0 \end{bmatrix}$$
* **Rodrig formulasi:**
  $$R(\vec{k}, \theta) = I + \sin(\theta) K + (1 - \cos(\theta)) K^2$$
* **KUKA Euler $Z-Y'-X''$ ($A, B, C$) matritsasi:**
  $$R_{KUKA}(A, B, C) = R_z(A) \cdot R_y(B) \cdot R_x(C)$$
* **Hand-Eye tenglamasi:**
  $$A X = X B$$

---

## 🏷️ Repozitoriylar Standarti va Boilerplate

Har bir Bob (Phase) repozitoriyasi ichidagi har bir mavzu jildida quyidagi qat'iy standart saqlanadi:

```
kuka-robotics-phase-X-[nomi]/
├── [mavzu-jildi]/          # Masalan: 03-rodrigues-formula/
│   ├── src/
│   │   ├── krl/            # .src va .dat KRL dasturlari
│   │   └── scripts/        # Python / MATLAB skriptlari
│   ├── sim/                # KUKA.Sim .vcmx, URDF fayllari
│   ├── docs/               # Matematik hisoblar va rasmlar
│   ├── CLAUDE.md           # AI yo'riqnomasi
│   └── README.md           # Mavzu bo'yicha to'liq qo'llanma
```

---

## 👥 Hamkorlik va Mualliflik

* **Muzaffarbek Mustafayev** — Kurs Muallifi va Arxitektori  
  * Samarqand Davlat Universiteti (SamDU)  
  * Tomsk Davlat Universiteti (TSU)  
  * GitHub: [@muzaffarbekmustafayev](https://github.com/muzaffarbekmustafayev)

* **Hamkor Oliy Ta'lim Muassasalari:**
  * **SamDU** — Samarqand Davlat Universiteti (O'zbekiston)
  * **TSU** — Milliy Tadqiqot Tomsk Davlat Universiteti (Rossiya)

---

## 📄 Litsenziya

Ushbu kurs ochiq manbali bo'lib, [MIT License](LICENSE) litsenziyasi asosida tarqatiladi.
