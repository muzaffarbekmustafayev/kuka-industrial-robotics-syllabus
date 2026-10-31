# KUKA Industrial Robotics Course: Master Navigator & Global Syllabus
## 25-Lesson Academic & Industrial Specialization Program | KUKA KR 6 R900-2 (KR AGILUS-2)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Manipulator: KUKA KR 6 R900-2](https://img.shields.io/badge/Manipulator-KUKA%20KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![Controller: KRC4 & KRC5](https://img.shields.io/badge/Controller-KUKA%20KR%20C4%20%7C%20KR%20C5-red.svg)](https://www.kuka.com)
[![Academic Alliance](https://img.shields.io/badge/Academic%20Alliance-SamDU%20%26%20TSU-blue.svg)](https://www.samdu.uz)
[![GitHub Topics](https://img.shields.io/badge/Topics-kuka--robotics--course%20%7C%20mechatronics%20%7C%20krl--programming%20%7C%20ros2--robotics%20%7C%20industrial--automation%20%7C%20samdu%20%7C%20tsu-lightgrey.svg)](#)

---

## 🧭 Kurs Arxitekturasi va Loyiha Konseptsiyasi

**KUKA Industrial Robotics Course** — zamonaviy sanoat robototexnikasi, manipulyatorlar kinematikasi/dinamikasi, KRL dasturlash va robotlashtirilgan sunʼiy intellekt integratsiyasi boʻyicha ishlab chiqilgan 25 darslik ochiq manbali fundamental taʼlim platformasi.

Kurs **Samarqand Davlat Universiteti (SamDU)** va **Milliy Tadqiqot Tomsk Davlat Universiteti (TSU)** Mexatronika va Robototexnika kafedralari hamda laboratoriyalarining koʻp yillik ilmiy-tadqiqot (PhD) va amaliy ishlab chiqarish tajribasi asosida shakllantirildi.

Ushbu repozitoriy (**Master Navigator**) butun oʻquv kursining **"Boshqaruv Pulti"** boʻlib, oʻzida hech qanday dars kodlarini saqlamaydi. U 6 ta ixtisoslashtirilgan Faza repozitoriyalariga yoʻllanma beruvchi global navigator, matematik formulalar markazi ([MATH_CHEATSHEET.md](file:///c:/Users/muzaf/Desktop/kuka-robotics-course/MATH_CHEATSHEET.md)) va loyiha vizitkasi vazifasini bajaradi.

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        kuka-industrial-robotics-course (Master Navigator Hub)                          │
│                Global Mundarija, Matematik Cheatsheet, Arxitektura Standartlari & Yoʻllanmalar         │
└───────────────────────────────────────────────────┬────────────────────────────────────────────────────┘
                                                    │
    ┌───────────────────────┬───────────────────────┼───────────────────────┬───────────────────────┐
    ▼                       ▼                       ▼                       ▼                       ▼
[ Phase 1: FUNDAMENTALS ]  [ Phase 2: KINEMATICS ] [ Phase 3: DIFFERENTIAL ] [ Phase 4: KRL CODING ] [ Phase 5: INTEGRATION ]
4 Dars: 01 - 04            6 Dars: 05 - 10         4 Dars: 11 - 14          5 Dars: 15 - 19         4 Dars: 20 - 23
                                                    │
                                                    └───────────────────────────────────────────────┐
                                                                                                    ▼
                                                                                        [ Phase 6: APPLICATIONS ]
                                                                                        2 Dars: 24 - 25
```

---

## 🦾 Asosiy Manipulyator: KUKA KR 6 R900-2 (KR AGILUS-2)

Kursdagi barcha simulyatsiyalar (`.vcmx`), URDF kinematik zanjirlari, Denavit-Hartenberg parametrlari, KRL harakat dasturlari va sunʼiy intellekt orqali tutish algoritmlari **KUKA KR 6 R900-2** (KR AGILUS-2 seriyasi, KRC4 compact / KRC5 micro kontrolleri) manipulyatoriga kalibrlangan.

| Parametr / Xususiyat | Qiymati | Muhandislik va Amaliy Ahamiyati |
| :--- | :--- | :--- |
| **Manipulyator Turi** | 6 oʻqli vertikal antropomorfik robot | 6 erkinlik darajasi (6-DoF) sferik bilak bilan ($A_4, A_5, A_6$) |
| **Maksimal Yuk Koʻtarish (Payload)** | $6.0\text{ kg}$ | Yuqori tezlikdagi yigʻuv, texnik koʻrish kameralari va tutqichlar uchun |
| **Maksimal Yetib Borish (Reach)** | $901.5\text{ mm}$ | Sferik ishchi fazo tahlili va chegaraviy nuqtalarni hisoblash |
| **Takrorlanuvchanlik (ISO 9283)** | $\pm 0.02\text{ mm}$ | Sub-millimetrli aniqlik: Hand-Eye kalibratsiya va nozik yigʻuv |
| **Boshqaruv Tizimi (Controller)** | KRC4 compact / KRC5 micro | KSS 8.3 / 8.6 / 8.7 proshivkalari, WorkVisual 6.0+ |
| **Dasturlash Pulti (Teach Pendant)** | KUKA smartPAD-2 | Multi-touch displey, 6D Space Mouse, holatlar monitoringi |
| **Oʻqlar Harakat Diapazoni** | $A_1: \pm 170^\circ, \quad A_2: -190^\circ / +45^\circ$ | Kinematik boʻgʻin cheklovlari va teskari kinematika |
| | $A_3: -120^\circ / +156^\circ, \quad A_4: \pm 185^\circ$ | Qulay ishchi hududni rejalashtirish |
| | $A_5: \pm 120^\circ, \quad A_6: \pm 350^\circ$ | Bilak singulyarligi tahlili ($A_5 = 0^\circ$) |
| **Oʻqlar Maksimal Burchak Tezliklari** | $A_1: 360^\circ/\text{s}, \quad A_2: 300^\circ/\text{s}, \quad A_3: 360^\circ/\text{s}$ | Yuqori dinamik trayektoriya rejalashtirish |
| | $A_4: 381^\circ/\text{s}, \quad A_5: 388^\circ/\text{s}, \quad A_6: 615^\circ/\text{s}$ | Singulyarlik hududidan oʻtishda tezlik sakrashlari nazorati |

---

## 🌐 7 Ta Repozitoriya va 25 Ta Darsning Global Xaritasi

| Faza | Repozitoriy Nomi va Havolasi | Darslar | Asosiy Texnologiyalar & Ilmiy Asos |
| :---: | :--- | :--- | :---: |
| **Navigator** | 🌐 [**`kuka-industrial-robotics-course`**](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus) | Mundarija, Formulalar markazi | Markdown, KaTeX, Python CLI Scaffolder |
| **Phase 1** | 📦 [**`kuka-robotics-phase-1-fundamentals`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-1-fundamentals)<br>*(Asoslar, Xavfsizlik va Digital Twin)* | • `01-introduction-to-kuka-agilus`<br>• `02-smartpad-and-coordinate-systems`<br>• `03-simulation-setup-digital-twin`<br>• `04-safety-and-safeoperation` | smartPAD, WORLD/BASE/TOOL/JOINT, KUKA.Sim Pro, OfficeLite VRC, SafeOperation (ISO 10218) |
| **Phase 2** | 📦 [**`kuka-robotics-phase-2-kinematics-and-math`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-2-kinematics-and-math)<br>*(Fazoviy Geometriya va Kinematika)* | • `05-rodrigues-rotation-formula`<br>• `06-rotation-matrices-and-quaternions`<br>• `07-dh-parameters-modelling`<br>• `08-forward-kinematics-solver`<br>• `09-inverse-kinematics-analytical`<br>• `10-numerical-inverse-kinematics` | Rodrigues $\mathfrak{so}(3)$, KUKA Euler $Z-Y'-X''$ ($A,B,C$), Quaternions $\mathbb{H}$, DH Parameters, Forward Kinematics, Pieper IK (8 yechim), Newton-Raphson |
| **Phase 3** | 📦 [**`kuka-robotics-phase-3-differential-kinematics`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-3-differential-kinematics)<br>*(Yakobian, Singulyarlik va Dinamika)* | • `11-jacobian-matrix-derivation`<br>• `12-singularity-analysis`<br>• `13-robot-dynamics-and-forces`<br>• `14-force-torque-control` | Geometrik Yakobian $J(\vec{q})$, Singulyarliklar (Wrist/Arm/Pitch), Nyuton-Eyler & Lagranj, KUKA.ForceTorqueControl (Impedance/Admittance) |
| **Phase 4** | 📦 [**`kuka-robotics-phase-4-krl-programming`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-4-krl-programming)<br>*(KRL Dasturlash Tili va Sanoat Tarmoqlari)* | • `15-krl-syntax-and-variables`<br>• `16-advanced-motion-commands`<br>• `17-logic-and-interrupts`<br>• `18-industrial-io-and-fieldbus`<br>• `19-subprograms-and-expert-programming` | KRL (`.src`, `.dat`), `FRAME`/`POS`/`E6POS`, `PTP`/`LIN`/`CIRC`/`SLIN`/`SCIRC`, `C_PTP`/`C_DIS`, `INTERRUPT`, ProfiNet, EtherCAT, WorkVisual |
| **Phase 5** | 📦 [**`kuka-robotics-phase-5-advanced-integration`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-5-advanced-integration)<br>*(RSI, ROS2, MoveIt2 va Computer Vision)* | • `20-kuka-rsi-interface`<br>• `21-ros2-driver-integration`<br>• `22-moveit2-trajectory-planning`<br>• `23-computer-vision-pick-and-place` | KUKA RSI (<12ms XML stream), ROS2 Humble/Iron, `kuka_robot_drivers`, MoveIt2 collision avoidance, OpenCV PnP, Hand-Eye $AX = XB$ |
| **Phase 6** | 📦 [**`kuka-robotics-phase-6-industrial-applications`**](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-6-industrial-applications)<br>*(Sanoatdagi Amaliy Loyihalar)* | • `24-trajectory-welding-and-glueing`<br>• `25-palletizing-and-sorting-system` | 3D payvandlash va yelimlash choklari, Konveyerga moslashuvchi (Conveyor Tracking) palletizatsiya va aqlli saralash |

---

## 📚 25 Ta Darsning Mukammal Nazariy va Amaliy Mundarijasi

---

### 📁 Phase 1: Asoslar, Xavfsizlik va Digital Twin
*Repozitoriy:* [`kuka-robotics-phase-1-fundamentals`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-1-fundamentals)

#### • 01-introduction-to-kuka-agilus
* **Nazariya:** KUKA KR 6 R900-2 manipulyatorining mexanik anatomiyasi, oʻqlar joylashuvi ($A_1 \dots A_6$), KRC4 va KRC5 kontrollerlarining arxitekturasi hamda ISO 10218-1/2 xalqaro xavfsizlik standartlari.
* **Amaliyot:** Robotning fazodagi ishchi zonasi (workspace reach envelope) chegaralarini aniqlash va virtual/real pultda oʻqlarni dastlabki tekshirish.

#### • 02-smartpad-and-coordinate-systems
* **Nazariya:** KUKA smartPAD interfeysi, tezkor tugmalar, 6D Space Mouse ishlash fizikasi. WORLD (dunyo), BASE (ish stoli), TOOL (asbob) va JOINT (oʻqlar) koordinata tizimlari mexanikasi.
* **Amaliyot:** Robotni turli koordinata rejimlarida qoʻlda (Jogging) xavfsiz boshqarish, asbob uchini bitta fazoviy nuqtada ushlab turib orientatsiyani oʻzgartirish.

#### • 03-simulation-setup-digital-twin
* **Nazariya:** KUKA.Sim Pro va KUKA OfficeLite (Virtual Robot Controller — VRC) oʻrtasidagi aloqa koʻprigi mexanizmi. Haqiqiy vaqtli deterministik simulyatsiya prinsiplari.
* **Amaliyot:** KR AGILUS manipulyatori uchun toʻliq Raqamli Egizak (Digital Twin) muhitini noldan sozlash, WorkVisual orqali robot modelini yuklash.

#### • 04-safety-and-safeoperation
* **Nazariya:** Sanoat xavfsizligi normalari (ISO 13849-1, ISO/TS 15066). KUKA SafeOperation apparat va dasturiy xavfsizlik texnologiyasi.
* **Amaliyot:** Virtual simulyator muhitida xavfsiz monitoring zonalari (Cell Safe Zones), oʻqlar chegaralari va xavfsiz tezlik cheklovlarini (Reduced Speed) dasturlash.

---

### 📁 Phase 2: Fazoviy Geometriya va Kinematik Modellashtirish
*Repozitoriy:* [`kuka-robotics-phase-2-kinematics-and-math`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-2-kinematics-and-math)

#### • 05-rodrigues-rotation-formula
* **Nazariya:** Fazoviy burilishlar nazariyasi, qiya-simmetrik matritsalar fazosi $\mathfrak{so}(3)$ va Lie algebrasi. Rodrigues formulasining vektorli va matritsaviy ($e^{\theta K}$) keltirib chiqarilishi:
  $$R(\vec{k}, \theta) = I + \sin(\theta) K + (1 - \cos(\theta)) K^2$$
* **Amaliyot:** Berilgan ixtiyoriy vektor va burchak boʻyicha $3\times 3$ aylanish matritsasini hamda uning teskarisini (matrix logarithm) hisoblovchi Python skriptini yaratish.

#### • 06-rotation-matrices-and-quaternions
* **Nazariya:** Eyler burchaklari (KUKA tizimidagi $Z-Y'-X''$ intrinsic $A, B, C$ burchaklari) va Gimbal Lock ($B = \pm 90^\circ$) muammosi. Toʻrt oʻlchamli Hamilton giperkompleks sonlari — birlik kvaternionlar ($\mathbb{H}$).
* **Amaliyot:** Eyler burchaklarini ($A, B, C$) kvaternionlarga ($[w, x, y, z]$) va teskarisiga oʻtkazuvchi, singulyarlikdan xoli konverter modulini tuzish va SLERP interpolyatsiyasini sinash.

#### • 07-dh-parameters-modelling
* **Nazariya:** Denavit-Hartenberg (DH) koordinatalar oʻrnatish standarti (Standart va Modifikatsiyalangan Craig konvensiyalari). KR 6 R900-2 ning barcha 6 ta oʻqi uchun bogʻlanish zanjiri.
* **Amaliyot:** Robotning geometrik chizmalari asosida uning rasmiy DH koordinata jadvallarini ($a_i, \alpha_i, d_i, \theta_i$) noldan qurish va boʻgʻin koordinata sistemalarini vizuallashtirish.

#### • 08-forward-kinematics-solver
* **Nazariya:** Toʻgʻri kinematika (Forward Kinematics) masalasi: Maxsus Evklid guruhi $SE(3)$ boʻyicha bir jinsli transformatsiya matritsalari koʻpaytmasi: $T_0^6(\vec{q}) = \prod_{i=1}^6 A_i(q_i)$.
* **Amaliyot:** Boʻgʻin burchaklariga koʻra effektorning fazodagi yakuniy oʻrnini $[X, Y, Z, A, B, C]$ aniqlovchi Python kinematik solverini tuzish va KUKA `$POS_ACT` bilan solishtirish.

#### • 09-inverse-kinematics-analytical
* **Nazariya:** Analitik va geometrik teskari kinematika (Inverse Kinematics). Sferik bilak uchun Piper (Pieper) kriteriyasini qoʻllash: bilak markazini ($\vec{p}_{wc}$) pozitsiyadan ajratish.
* **Amaliyot:** Maqsadli fazoviy nuqtaga yetishish uchun 6 ta motorning burchaklarini analitik usulda hisoblash, 8 ta geometrik yechim hamda KUKA Status ($S$) va Turn ($T$) bitlarini aniqlash.

#### • 10-numerical-inverse-kinematics
* **Nazariya:** Nyuton-Rafson iteratsiyasi, Yakobian transponirlangan va Levenberg-Marquardt (Damped Least Squares) algoritmlari orqali noaniq yoki murakkab kinematik zanjirlarni yechish.
* **Amaliyot:** Python muhitida iterativ teskari kinematik solver yaratish, yaqinlashish tezligi va cheklovlar doirasida global konvergensiyani optimallashtirish.

---

### 📁 Phase 3: Differensial Kinematika, Yakobian va Dinamika
*Repozitoriy:* [`kuka-robotics-phase-3-differential-kinematics`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-3-differential-kinematics)

#### • 11-jacobian-matrix-derivation
* **Nazariya:** Geometrik Yakobian matritsasi: Boʻgʻin burchak tezliklarining ($\dot{\vec{q}}$) effektor chiziqli va burchak tezliklariga ($\vec{v}_e, \vec{\omega}_e$) differensial bogʻliqligi:
  $$\vec{V}_e = J(\vec{q}) \cdot \dot{\vec{q}}$$
* **Amaliyot:** KR 6 R900-2 uchun geometrik Yakobian matritsasini hisoblovchi ramziy (symbolic SymPy) va raqamli (NumPy) kod yozish.

#### • 12-singularity-analysis
* **Nazariya:** Singulyarlik holatlari matematikasi ($\det(J) = 0$ va $\text{rank}(J) < 6$): Bilak singulyarligi (Wrist $A_5=0^\circ$), Yelka singulyarligi (Shoulder) va Chegara (Elbow/Boundary) singulyarliklari.
* **Amaliyot:** Determinant qiymatiga koʻra robot motorlari haddan tashqari tezlashib bloklanib qoladigan nuqtalarni aniqlash, Yoshikawa manipulyativlik ellipsoidini chizish va singulyarlikdan qochish traektoriyalari testi.

#### • 13-robot-dynamics-and-forces
* **Nazariya:** Manipulyator dinamikasi: Nyuton-Eyler va Lagranj-Eyler differensial tenglamalari. Massalar inersiyasi, Koriolis va markazdan qochma kuchlar matritsasi $C(\vec{q}, \dot{\vec{q}})$ hamda gravitatsiya kompensatsiyasi $\vec{g}(\vec{q})$.
* **Amaliyot:** Belgilangan traektoriya boʻyicha harakat davomida 6 ta boʻgʻinda paydo boʻladigan dinamik momentlar (Torque $\vec{\tau}$) yuklanishini hisoblash va grafik koʻrinishida vizuallashtirish.

#### • 14-force-torque-control
* **Nazariya:** 6 oʻqli kuch-moment datchiklari (Force-Torque Sensors) fizikasi va KUKA.ForceTorqueControl dasturiy paketining ishlash prinsipi.
* **Amaliyot:** Tashqi mexanik kuch taʼsirida robot xatti-harakatini virtual moslashtirish — Admittance va Impedance boshqaruv qonunlarini dasturlash.

---

### 📁 Phase 4: KUKA Robot Language (KRL) Dasturlash
*Repozitoriy:* [`kuka-robotics-phase-4-krl-programming`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-4-krl-programming)

#### • 15-krl-syntax-and-variables
* **Nazariya:** KRL dasturlash tili arxitekturasi, maʼlumot turlari: `INT`, `REAL`, `BOOL`, `CHAR` hamda geometrik tuzilmalar (`FRAME`, `POS`, `E6POS`, `AXIS`, `E6AXIS`).
* **Amaliyot:** `.src` (dastur mantigʻi) va `.dat` (maʼlumotlar bazasi va koordinatalar) fayllarining ichki arxitekturasini noldan yozish va WorkVisual orqali kontrollerga yuklash.

#### • 16-advanced-motion-commands
* **Nazariya:** Asosiy harakat buyruqlari: `PTP` (boʻgʻinlararo tezkor harakat), `LIN` (chiziqli), `CIRC` (aylana). Trayektoriyani silliqlash parametrlari (`C_PTP`, `C_DIS`, `C_ORI`, `C_VEL`) va `$ADVANCE` tizim koʻrsatkichi.
* **Amaliyot:** Uzluksiz egri chiziqli harakatlarni zamonaviy Spline bloklari (`SLIN`, `SCIRC`, `SPL`) orqali Expert KRL rejimida dasturlash.

#### • 17-logic-and-interrupts
* **Nazariya:** Mantiqiy operatorlar, sikllar (`LOOP`, `WHILE`, `FOR`) hamda asinxron uzilishlar — `INTERRUPT` mexanizmi arxitekturasi.
* **Amaliyot:** Avariya holati yuz berganda yoki tashqi datchikdan signal kelganda asosiy traektoriyani darhol toʻxtatib (`BRAKE`), xavfsiz pozitsiyaga chekinish dasturini tuzish.

#### • 18-industrial-io-and-fieldbus
* **Nazariya:** Sanoat tarmoqlari (Fieldbus): ProfiNet, EtherCAT protokollari va KUKA WorkVisual dasturi orqali I/O signallarini xaritalash (Signal Mapping).
* **Amaliyot:** Raqamli kirish (`$IN[n]`) va chiqish (`$OUT[n]`) signallarini robot dasturiga bogʻlash, pnevmatik klapan va vakuum datchiklari bilan ishlash.

#### • 19-subprograms-and-expert-programming
* **Nazariya:** Global va lokal qism-dasturlar (Subroutines), funksiyalar (`DEFFCT`), qiymat va koʻrsatkich orqali argument uzatish qoidalari.
* **Amaliyot:** Zavod ishlab chiqarish liniyasi uchun parametrik, xatoliklarni qayta ishlovchi va modulli avtomatlashtirish karkasini (framework) qurish.

---

### 📁 Phase 5: Tashqi Interfeyslar, ROS2 va Sunʼiy Intellekt
*Repozitoriy:* [`kuka-robotics-phase-5-advanced-integration`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-5-advanced-integration)

#### • 20-kuka-rsi-interface
* **Nazariya:** KUKA RSI (Robot Sensor Interface) arxitekturasi: tashqi boshqaruv kompyuteridan Ethernet orqali real vaqtda (<12ms siklda) toʻgʻridan-toʻgʻri boshqarish.
* **Amaliyot:** RSI XML-paketlar protokoli orqali robotga tashqi kompyuterdan oʻqlar va koordinatalar tuzatishlarini (corrections) uzatuvchi Python test serverini yozish.

#### • 21-ros2-driver-integration
* **Nazariya:** ROS 2 (Robot Operating System) arxitekturasi (Humble/Iron) va rasmiy KUKA ROS2 drayverlari (`kuka_robot_drivers`, `kuka_kr6_support`).
* **Amaliyot:** ROS 2 tugunlari (Nodes) orqali KR AGILUS holatlarini real vaqtda oʻqish va RViz muhitida robotning 3D URDF modelini harakatlantirish.

#### • 22-moveit2-trajectory-planning
* **Nazariya:** MoveIt2 kutubxonasi yordamida toʻsiqlarni avtomatik aylanib oʻtuvchi traektoriyalarni rejalashtirish (OMPL rejalashtiruvchilari va FCL toʻqnashuv detektori).
* **Amaliyot:** Virtual ishchi hududda dinamik paydo boʻlgan toʻsiqlarni chetlab oʻtib belgilangan manzilga xavfsiz yetib boruvchi traektoriyalarni hisoblash.

#### • 23-computer-vision-pick-and-place
* **Nazariya:** Pinhole kamera modeli, OpenCV `cv2.solvePnP` va Hand-Eye kalibratsiyasi (Tsai-Lenz va Park-Martin usullari boʻyicha $AX = XB$ matritsaviy tenglamasi).
* **Amaliyot:** Kamera orqali ishchi stoldagi tasodifiy obʼektning $[X, Y, Z, A, B, C]$ koordinatasini aniqlab, robot koordinata tizimiga oʻtkazish va obʼektni aniq ushlab oluvchi dastur.

---

### 📁 Phase 6: Sanoatdagi Amaliy Ishlab Chiqarish Loyihalari
*Repozitoriy:* [`kuka-robotics-phase-6-industrial-applications`](https://github.com/muzaffarbekmustafayev/kuka-robotics-phase-6-industrial-applications)

#### • 24-trajectory-welding-and-glueing
* **Texnologiya:** Sanoatda payvandlash (Arc Welding) va yelim surtish (Glueing/Dispensing) jarayonlarining qatʼiy texnologik talablari.
* **Amaliyot:** Doimiy chiziqli tezlikni ($v = \text{const}$) va asbob burchagini saqlagan holda murakkab fazoviy 3D choklar boʻylab robot harakatini KRL Spline vositalarida dasturlash.

#### • 25-palletizing-and-sorting-system
* **Texnologiya:** Palletizatsiya (mahsulotlarni tagliklarga tartibli taxlash), konveyerga dinamik moslashuv (Conveyor Tracking) va aqlli saralash tizimlari.
* **Amaliyot:** Konveyerdan uzluksiz kelayotgan mahsulotlarni sensorlar yordamida aniqlab, ularning oʻlchamiga koʻra turli qutilarga saralovchi yakuniy master-dasturni KRL va Python integratsiyasida yakunlash.

---

## 📐 Darslar Ichidagi Majburiy Boilerplate Standarti

Har bir dars papkasining ichki tuzilishi qatʼiy quyidagi arxitekturaga ega boʻladi:

```
[ikki-raqamli-indeks]-[mavzu-nomi]/
├── src/
│   ├── krl/            # KRL (.src, .dat, .sub) haqiqiy kontroller kodlari
│   └── scripts/        # Python / MATLAB tahlil va kinematik algoritmlari
├── sim/                # KUKA.Sim Pro (.vcmx), URDF va 3D CAD modellar
├── docs/               # Nazariy hisob-kitoblar, matematik isbotlar va sxemalar
├── CLAUDE.md           # AI yordamchi agent uchun qoidalar va tezkor buyruqlar
└── README.md           # Talaba uchun batafsil qoʻllanma, formulalar va laboratoriya vazifasi
```

---

## 🏷️ Majburiy Global GitHub Teglari (Topics)

Barcha 7 ta repozitoriya oʻzaro qulay qidiruv va filtrlash uchun quyidagi 7 ta tegga ega boʻlishi shart:
```
kuka-robotics-course, mechatronics, krl-programming, ros2-robotics, industrial-automation, samdu, tsu
```

---

## 👥 Mualliflik va Akademik Hamkorlik

* **Muzaffarbek Mustafayev** — Kurs Arxitektori va Muallifi  
  * Samarqand Davlat Universiteti (SamDU), Intellektual tizimlar va mexatronika kafedrasi  
  * Milliy Tadqiqot Tomsk Davlat Universiteti (TSU), Robototexnika va mexatronika laboratoriyasi  
  * GitHub: [@muzaffarbekmustafayev](https://github.com/muzaffarbekmustafayev)

* **Hamkor Universitetlar:**
  * **SamDU** — Samarqand Davlat Universiteti (Oʻzbekiston)
  * **TSU** — Milliy Tadqiqot Tomsk Davlat Universiteti (Rossiya)

---

## 📄 Litsenziya va Iqtibos

Ushbu kurs [MIT License](LICENSE) asosida ochiq tarqatiladi. Ilmiy maqola va tadqiqotlarda foydalanganda quyidagi iqtibosdan foydalaning:

```bibtex
@misc{mustafayev2026kuka,
  author = {Mustafayev, Muzaffarbek},
  title = {KUKA Industrial Robotics Course: 25-Lesson Academic & Industrial Specialization},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus}},
  note = {Joint educational and research program by Samarkand State University and Tomsk State University}
}
```
