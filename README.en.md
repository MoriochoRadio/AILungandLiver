# AILungandLiver — AI-Based Diagnosis and 3D Visualization System for Liver and Lung CT Images (L-POT)

🇰🇷 [한국어](README.md) · 🇬🇧 English

> *AI-Based Diagnosis and 3D Visualization System for Liver and Lung CT Images*
>
> A PyQt6 desktop app where a patient uploads their own liver/lung CT and the system **reconstructs it in 3D and marks suspected nodule regions**. The product name is **L-POT**. It is the follow-up to the previous semester's [LungCT3DNoduleAI](https://github.com/MoriochoRadio/LungCT3DNoduleAI) (lung only, 78% accuracy), **extended to multi-organ lung + liver coverage with accuracy raised to 93%**. On the same team, **T.O.P**, after serving as PM the previous semester, this time I took sole charge of **QA (Quality Assurance)**. It is the deliverable of two courses run in parallel — *Convergence Design and Project* + *DYC (Design Your Class)* — in the Department of Medical IT Engineering, 2nd semester of 2025.

![Status](https://img.shields.io/badge/status-preserved-blue) ![Year](https://img.shields.io/badge/year-2025--2-blue) ![Role](https://img.shields.io/badge/role-QA-orange) ![Stack](https://img.shields.io/badge/PyQt6-PyTorch%20%2B%20VTK%20%2B%20Open3D-success) ![Model](https://img.shields.io/badge/model-SpiralNet%20%2B%20PointNet%20%2B%20Transformer-red) ![Accuracy](https://img.shields.io/badge/accuracy-78%25%20→%2093%25-brightgreen) ![Organs](https://img.shields.io/badge/organs-Lung%20%2B%20Liver-yellow) ![Team](https://img.shields.io/badge/team-T.O.P-lightgrey)

![Title](assets/screenshots/title.png)

> Final presentation cover — **L-POT** · Team **T.O.P** · 2025.12.02 · Ver.1.0.0

---

## ⚠ About Build/Run Status

This repo **preserves the code exactly as it was at the December 2025 presentation**. It is a PyQt6 + PyTorch desktop app and was runnable at the time of writing.

To run it yourself:
- **Model weights** (`models/new_2.pth` lung 54MB + `models/mask_merged_ver4.pth` liver 54MB) are pushed via Git LFS. Run `git lfs pull` after cloning.
- **Training data is not included.** You must prepare public medical imaging data yourself (the deliverables state *"TCAI, Tainichi, etc."*).
- Run: `python dashboard_main.py`
- Or build a PyInstaller onefile executable: `pyinstaller L-POT.spec` (note: `LPOT.ico` must be placed in the project root)

> 📌 The entry point is `dashboard_main.py`. There is also a `main.py` in the root, but it is a **non-runnable fossil of an earlier version** (see [*Code That Preserves My Own Tone*](#-code-that-preserves-my-own-tone) below).

---

## 📚 Project Context

| Item | Details |
|---|---|
| **When** | 2nd semester, 2025 academic year (presented 2025.12.02) |
| **Affiliation** | Dept. of Medical IT Engineering, Konyang University |
| **Courses** | *Convergence Design and Project* + **DYC (Design Your Class)**, taken in parallel |
| **Team** | **T.O.P** (Technology Of Prognosis, *"prediction technology"*) — same team name as the previous semester's [LungCT3DNoduleAI](https://github.com/MoriochoRadio/LungCT3DNoduleAI) |
| **Team members (5)** | PM ◯◯◯ / PL ◯◯◯ / CM ◯◯◯ / **QA Kim TaeKyoung (me)** / ENG ◯◯◯ |
| **Advisors** | Prof. Song ◯◯ + Prof. Kim ◯◯ |
| **My (KimTaeKyoung) role** | ★ **QA (Quality Assurance), solo** — deliverable quality management · system risk management · model performance monitoring |
| **★ Role change** | Previous semester **PM** (LungCT3DNoduleAI) → this semester **QA** — *chosen voluntarily to experience a role I had not tried* |

> 📌 **Two courses in parallel (DYC)**: This project is the deliverable of the *Convergence Design and Project* course while it was simultaneously carried out in the *DYC (Design Your Class)* course. Because the two courses had separate presentation schedules and document formats, we produced three separate materials for the same system: **the presentation PPT + the department exhibition panel + the DYC Digital Healthcare Convergence event panel**.

---

## 🔄 Evolution from the Previous Project (78% → 93%)

![Evolution](assets/screenshots/evolution_78_to_93.png)

The core of this project is that it is an **extension and evolution** of the previous semester's [LungCT3DNoduleAI](https://github.com/MoriochoRadio/LungCT3DNoduleAI). Slide 6 of the presentation preserves the two-semester comparison verbatim:

> **2025-1 project (development result)** — chest CT nodule detection, **78% accuracy**
> **2025-2 project (improvements)** — chest **and abdominal** CT nodule detection, **93% accuracy**

| Item | 25-1 LungCT3DNoduleAI | **25-2 AILungandLiver (L-POT)** |
|---|---|---|
| Domain | Lung CT nodules | **Lung + liver CT nodules** (multi-organ) |
| **My role** | **PM** (schedule · progress · preprocessing) | **★ QA** (quality · risk · testing) |
| Model representation | 3D Voxel | **3D Mesh / Point Cloud** |
| Framework | TensorFlow `.h5` | **PyTorch `.pth`** |
| Architecture | 4-branch CNN | **SpiralNet + PointNet + Transformer hybrid** |
| **Accuracy** | **78%** | **★ 93%** (+15%p) |
| Infrastructure | Jupyter/Colab + Streamlit | **PyQt6 desktop app + exe** |
| Team | T.O.P (6 members) | T.O.P (5 members, same team name) |

This was not simply copying the lung code over to the liver. It is a **redesign that changed the representation itself from voxel grid to 3D mesh**, the infrastructure moved from notebooks/web app to a desktop app, and my own role changed from PM to QA.

---

## ❓ Problem Definition

![Problem Survival](assets/screenshots/problem_survival.png)

This project started from the problems surrounding liver and lung diagnosis:

1. **Lung and liver cancer = #1 and #2 in cancer mortality in Korea** — with early diagnosis, 5-year survival rates rise sharply: lung cancer 20%→61%, liver cancer 37%→70%.
2. **Physician-centered care, passive patients** — reports written in difficult medical terminology, a lack of visual materials, and image reading that takes days. While waiting for results, patients sit in anxiety, unable to intuitively understand their own condition.
3. **No patient-facing systems** — existing AI solutions are all clinician-only:

![Competitors](assets/screenshots/competitors.png)

| Organ | Organization | Solution | Users |
|---|---|---|---|
| Lung | VUNO | Med-LungCT AI™ (MFDS 2020) | Clinicians |
| Lung | DEEP:NOID | DEEP:LUNG (accuracy ~92.2%) | Clinicians |
| Liver | MEDICAL IP | DeepFore (MFDS 2025) | Clinicians |
| Liver | Quibim | QP-Liver® (European CE) | Clinicians |

→ ★ All clinician-only. **L-POT's differentiator is *"used directly by patients"***.

---

## 💡 Solution — L-POT

![Solution](assets/screenshots/solution.png)

> *"A patient-centered AI diagnostic-support system — a reference tool that does not replace diagnosis, but fills the gap before and after it."*

1. **Patient-centered image reading** — patients upload their own CT-DICOM directly
2. **CT 3D visualization** — converts grayscale CT into a color 3D model to support intuitive understanding
3. **Lung/liver AI nodule prediction** — AI automatically detects and marks nodules (abnormal regions)

This positioning is a consistent message across my portfolio — from [MedQueue](https://github.com/MoriochoRadio/MedQueue) (patients checking waiting status themselves) to L-POT (patients checking their own CT), *"tools for the patient, not the clinician."*

---

## 🛠️ Tech Stack

| Area | Technology |
|---|---|
| **GUI** | PyQt6 (desktop app) + PyInstaller (onefile exe) |
| **Deep learning** | PyTorch (SpiralNet + PointNet + Transformer hybrid) |
| **3D processing** | VTK · Open3D · Trimesh · scikit-image (marching cubes) |
| **Medical imaging** | pydicom (DICOM) · nibabel (NIfTI) |
| **Numerics** | NumPy · SciPy |

See [`requirements.txt`](requirements.txt) for full dependencies.

---

## 🏗️ System Design — Unified Lung-Liver OOP

The cleanest part of L-POT's code structure is that **lung and liver are unified through OOP abstraction**:

```
BaseCTPipeline (shared abstraction)
  ├── load_ct()                          load DICOM
  ├── _compute_f1()                      compute F1
  ├── _estimate_axial_max_diameter_mm()  "hospital-style axial max diameter"
  └── make_result()                      result dict
        │
        ▼ (subclass)
OrganCTPipeline(organ: str)
  └── run(folder, model_manager, progress_cb)
        │
        ▼ (each a 3-line stub)
LungPipeline  → super().__init__("lung")
LiverPipeline → super().__init__("liver")
```

→ ★ **Multi-organ extension = two 3-line stubs.** The liver code was not created by copying the lung code; shared logic was lifted into the parent class and only the organ name is passed differently. Together with the *"voxel→mesh redesign,"* this is the evidence that this project is not a simple extension.

### Data Flow

```
DICOM ZIP upload
  │  [utils/dicom_processor.py] unzip → HU conversion → [1,1,1]mm resample → lung mask
  ▼
Mesh generation  [utils/mesh_processor.py — 17 free functions + MeshProcessor]
  │  marching cubes → trimesh → ICP alignment → KDTree reorder → (N,7) per-vertex features
  ▼
AI inference  [models/model_manager.py] predict_for_organ('lung'|'liver', features)
  │  HybridSpiralNetPointNetTransformer → SpiralNet + PointNet/Transformer ensemble → sigmoid
  ▼
Results  [pipelines/common_pipeline.py] F1 + nodule diameter in mm
  ▼
3D visualization  [pages/dashboard_page.py] matplotlib 3D + nodule vertices in red + "does not replace clinical reading" warning
```

---

## 🤖 Model Architecture — SpiralNet + PointNet + Transformer

The 6 classes in [`models/spiralnet.py`](models/spiralnet.py):

| Class | Role |
|---|---|
| `SpiralConv` | Core — 1D convolution over spiral neighbors of mesh vertices |
| `SpiralBlock` | SpiralConv + residual + dropout |
| `SEBlock` | Squeeze-Excitation (channel attention) |
| `ImprovedSpiralNet` | encoder-decoder + SE + multi-scale |
| `SimplePointTransformerBlock` | multi-head self-attention |
| `HybridSpiralNetPointNetTransformer` | ★ Main — ensemble of a SpiralNet branch + a PointNet/Transformer branch |

- **Input**: `(N_vertices, 7)` — 3 channels of (x,y,z) coordinates + 4 channels of normal/curvature
- **Output**: `(N_vertices,)` — per-vertex probability of nodule(1)/normal(0) (★ vertex-level segmentation, not bounding boxes)
- **Same architecture, independent weights for lung/liver**: `new_2.pth` (lung) + `mask_merged_ver4.pth` (liver)

> ⚠ **Honest disclosure**: The model design and training were mainly handled by the ENG/PL teammates. My role (QA) was model *performance monitoring* — validating the 78%→93% improvement and managing quality, risk, and testing. See [*My Contributions*](#-my-contributions-kimtaekyoung--solo-qa) below.

---

## ✨ Key Features / UI

L-POT is a PyQt6 desktop app:
- Automatic DICOM ZIP extraction + HU conversion + isotropic resampling
- Lung mode / liver mode radio selection
- 3D viewer (matplotlib 3D, wheel zoom) + 2D CT slice slider
- Nodule vertices highlighted in red + F1 + maximum nodule diameter (mm)
- Ethics warning *"This system does not replace clinical reading"* displayed at all times

### Demo Video

<video src="assets/videos/demo.mp4" controls width="800"></video>

> If the video above does not display, play [`assets/videos/demo.mp4`](assets/videos/demo.mp4) directly (1920×1080, 0:52 — the video embedded in presentation slide 12).

---

## 👤 My Contributions (KimTaeKyoung · Solo QA)

If in the previous semester's [LungCT3DNoduleAI](https://github.com/MoriochoRadio/LungCT3DNoduleAI) I was responsible as **PM** for schedule, progress, and deliverables, this semester I was responsible as **QA (Quality Assurance)** for quality, risk, and testing. **I deliberately picked a role I had not tried before.**

![Team Org](assets/screenshots/team_org.png)

My QA duties on the org chart (slide 4): **deliverable quality management · system risk management · model performance monitoring**.

### Track 1 — 37 Pages of QA First-Author Deliverables

Five documents are listed in the deliverables register with me as sole first author; extracted from the integrated volume, they form [`docs/deliverables_authored_by_kim_taekyoung.pdf`](docs/deliverables_authored_by_kim_taekyoung.pdf) (37 pages, teammate PII masked):

| Deliverable | Pages | Content |
|---|---|---|
| Quality Management Plan | 11p | ISO 9126-based checklist covering 10 deliverables |
| Risk Management Plan | 9p | assessment of 10 risk items (5 critical) |
| Unit Test Plan | 8p | test environment and scenarios |
| Unit Test Report | 5p | test results |

### Track 2 — Model Performance Monitoring (78% → 93%)

The *"model performance monitoring"* duty of QA means validating the [78%→93% evolution](#-evolution-from-the-previous-project-78--93) above. Knowing the limitations of the previous semester's lung-only 78% model, my role was to track and verify performance through the lung+liver extension until it reached 93%.

### Track 3 — ★ Self-Reflection in the Risk Management Plan

The most meaningful deliverable is the Risk Management Plan. In the risk assessment table I wrote, 5 of the 10 items are rated *"high likelihood + critical impact"*:

| Critical Risk Item | Likelihood | Impact |
|---|---|---|
| All team members need an understanding of CT | High | Critical |
| **Insufficient knowledge of AI models** | High | Critical |
| All team members need an understanding of deep learning and CT DICOM | High | Critical |
| Development environments and tools need to interoperate | High | Critical |
| **Insufficient knowledge of preprocessing** | High | Critical |

These risk items are not abstract textbook risks. They are **exactly the difficulties I experienced firsthand while running [LungCT3DNoduleAI](https://github.com/MoriochoRadio/LungCT3DNoduleAI) as PM the previous semester**. The struggles with *"insufficient AI model knowledge"* and *"insufficient preprocessing knowledge"* back then are what I, as QA, stamped into the risk assessment table as *"critical."* In effect, one semester's trial and error was distilled into the next semester's risk analysis.

---

## 🧪 Performance / Expected Impact

![Expected Effects](assets/screenshots/expected_effect.png)

- **93% nodule detection accuracy** (exceeding the 90% target; +15%p over the previous semester's lung-only 78%)
- **Integrated multi-organ lung + liver coverage**
- **Expected impact**: patients can check their own CT directly → reduced anxiety while waiting · better understanding of their disease · improved treatment adherence

---

## ✍️ Code That Preserves My Own Tone

This repo is not a *finished commercial product* but the unaltered *trace of a third-year undergraduate team building its first lung/liver medical imaging AI desktop app*.

### 1) Traces of GPT/Claude Use — `:contentReference[]` Markers

```python
# models/model_loader.py line 6
from utils.helper import resource_path  # get paths relative to the project root :contentReference[oaicite:5]{index=5}
```

`:contentReference[oaicite:5]{index=5}` is a citation-reference marker that tags along when copy-pasting answers from ChatGPT/Claude. It remains verbatim in two places in the code (lines 6 and 24) — an honest trace of an undergraduate writing code with LLM help. I preserved it rather than deleting it.

### 2) Two Entry Points — `main.py` Is a Non-Runnable Fossil

There are two entry points in the root, `main.py` and `dashboard_main.py`. The 4 modules `main.py` imports (`upload_page`, `viewer_page`, `feature_label_viewer_page`, `utils.model_loader`) are **all absent from the current folder**. In other words, running `main.py` today raises an ImportError. It is a *"fossil"* abandoned when the UI structure was consolidated mid-semester, left in place rather than deleted, as a preserved trace of the code's evolution.

### 3) Ten Missing Modules — 4 Pages → 1 Dashboard Consolidation

In the `main.py` era the structure had 4 pages (upload / viewer / result / feature_label_viewer) and 6 visualization utils (ct_loader / lung_3d_viewer / vtk_viewer / viewer_2d / viewer_3d / model_loader). Mid-semester this was consolidated into **1 dashboard page + 2 utils (dicom_processor / mesh_processor)**. Traces of the abandoned modules remain in `__pycache__`, which made it possible to reverse-trace the pre-consolidation structure.

### 4) Model File Names — `new_2.pth`, `mask_merged_ver4.pth`

The lung model is `new_2.pth` ("second new version") and the liver model is `mask_merged_ver4.pth` ("mask-merged version 4"). Rather than renaming them formally (`lung_model.pth`), the version traces of training trial and error were preserved as-is. The same vein as the previous project's `dhkstjd.pth` (a Korean IME typo).

### 5) The "◯◯◯ (PL) Twice" Typo in the Panel PPT

In the participating-students list of the department/DYC panel PPTs, the PL's name appears twice (after masking: `◯◯◯ (PL), ... , ◯◯◯ (PL)`). A typo made while hastily assembling the presentation materials, preserved without correction.

### 6) Domain-Aware Comments + Ethics Disclaimer

```python
# pipelines/common_pipeline.py
# Measure nodule size in mm using the "axial max diameter" method hospitals commonly use
```

The comment computing nodule size via the *"hospital-style axial max diameter"*, and the warning *"This system does not replace clinical reading"* embedded in 3 places in the code (`dashboard_page.py`, `main.py`, `LICENSE.md`) — traces of a medical IT major's domain awareness and ethical self-awareness.

### 7) A Hand-Me-Down Template — the School's 4-Year-Old Deck

The panel PPT's creation date is 2021-10-28. It is a trace of a presentation template distributed by the department being handed down among students for four years — one facet of Korean undergraduate deliverables culture.

---

## 📂 Archive

| Material | Path | Notes |
|---|---|---|
| 🎤 Final presentation (15 slides) | [`docs/presentation_redacted.pptx`](docs/presentation_redacted.pptx) | Git LFS |
| 🪧 Panels ×2 (department + DYC) | [`docs/panel_dept_redacted.pptx`](docs/) · panel_dyc | Git LFS |
| 📑 User manual | [`docs/user_manual_redacted.pdf`](docs/user_manual_redacted.pdf) | Hancom HWP→PDF |
| 📑 Development completion report | [`docs/final_report_redacted.pdf`](docs/final_report_redacted.pdf) | Hancom HWPX→PDF |
| 📑 Integrated deliverables volume (162p) | [`docs/deliverables_full_redacted.pdf`](docs/deliverables_full_redacted.pdf) | teammate PII masked |
| ★ 📖 My first-author deliverables (37p) | [`docs/deliverables_authored_by_kim_taekyoung.pdf`](docs/deliverables_authored_by_kim_taekyoung.pdf) | QA quality·risk·testing |
| 🤖 Model weights (lung+liver) | [`models/`](models/) | Git LFS (54 MB each) |
| 🎬 Demo video | [`assets/videos/demo.mp4`](assets/videos/demo.mp4) | Git LFS (0:52) |

> 📌 The names of the 4 teammates and 2 professors other than myself are masked as `◯◯◯` in the presentation materials, deliverables, and metadata. The medical imaging data and the original MS Project files are kept in `docs/_archive/local-only/` and are not pushed to GitHub.

---

## 📚 References

The 17 references on presentation slide 14 (National Cancer Information Center cancer mortality statistics, 5-year survival rate press releases, Cancer Support Community / Cancer.net materials on scanxiety, Radiology: AI journal articles on patient-centered image reading, and solution materials from VUNO, Deepnoid, MEDICAL IP, Quibim, etc.).

---

## 🎯 Interview Prep — Technology Choice Q&A

A summary that condenses the *"why was it built this way"* scattered throughout the sections above into interview form. Detailed evidence is in each linked section.

**Q1. Why mesh instead of voxel?**
We redesigned the representation itself, from the previous semester's voxel grid + 4-branch CNN (78%) to a 3D mesh + SpiralNet hybrid (93%). Because it is a mesh representation, vertex-level segmentation output is possible instead of bounding boxes. → [Evolution (78%→93%)](#-evolution-from-the-previous-project-78--93) · [Model Architecture](#-model-architecture--spiralnet--pointnet--transformer)

**Q2. Wasn't the liver code just a copy of the lung code?**
No. Shared logic was lifted into the `BaseCTPipeline` parent class and only the organ name is passed down, in a 3-layer OOP structure — so multi-organ extension ends with two 3-line stubs. → [System Design](#-system-design--unified-lung-liver-oop)

**Q3. Why for patients rather than clinicians?**
Because existing AI solutions (VUNO, DEEP:NOID, MEDICAL IP, Quibim) are all clinician-only, and the starting problem was the patient's information gap while waiting for reading results. The positioning is not replacing diagnosis but *"a reference tool that fills the gap before and after diagnosis."* → [Problem Definition](#-problem-definition) · [Solution](#-solution--l-pot)

**Q4. Why QA after PM?**
I chose it voluntarily to experience a role I had not tried. The real payoff of the role change was being able to carry the trial and error I went through as PM (*"insufficient AI model knowledge"*, *"insufficient preprocessing knowledge"*) into the *"critical risk"* items of the QA Risk Management Plan. → [My Contributions](#-my-contributions-kimtaekyoung--solo-qa)

**Q5. Why TensorFlow → PyTorch, and web app → desktop app (PyQt6)?**
The explicit reasons for the switch are not preserved in the deliverables of the time (honest disclosure). What is recorded is that, along with the architecture redesign (4-branch CNN → SpiralNet hybrid), the framework changed from `.h5` to `.pth` and the infrastructure moved from a Jupyter/Colab + Streamlit web app to a PyQt6 + PyInstaller exe. → [Evolution (78%→93%)](#-evolution-from-the-previous-project-78--93)

---

## ✍️ Retrospective — From PM to QA, From 78% to 93%

This project is both the **culmination of the medical imaging AI line** in my portfolio and a record of **experiencing the same system across two semesters in different roles**.

In the previous semester's [LungCT3DNoduleAI](https://github.com/MoriochoRadio/LungCT3DNoduleAI), I was the PM. While being responsible for the schedule, progress, and deliverables of a 6-person team, I directly ran into difficulties like *"we lack AI model knowledge"* and *"I don't understand preprocessing."* This semester I deliberately picked QA, a role I had not tried. And in the Risk Management Plan I wrote as QA, I stamped those very difficulties from my semester as PM in as *"critical risks."* Because they were not risks copied from a textbook but trial and error I had personally gone through, that risk assessment table is still the most honest deliverable when I look at it now.

Technically, too, this project was not a simple extension. We expanded from lung-only (78%) to lung+liver (93%), changed the model representation from voxel grid to 3D mesh (4-branch CNN → SpiralNet+PointNet+Transformer), and moved the infrastructure from notebooks/web app to a PyQt6 desktop app. The structure unifying lung and liver in the 3-layer OOP `BaseCTPipeline → OrganCTPipeline → Lung/LiverPipeline` lets the code itself say, *"the liver was not made by copying the lung code."*

What I want to keep is not the resulting number (93%) but the process. The non-runnable fossil `main.py`, the `:contentReference[]` GPT markers, trial-and-error file names like `new_2.pth` — these traces honestly show *"the fumbling process of a third-year undergraduate building a lung/liver AI desktop app for the first time."* The two semesters of leading a team as PM and scrutinizing quality, risk, and testing as QA will, I think, stay with me longer than the code as I head toward the medical IT and hospital information systems field.

---

## 🗂️ Related Repositories

### ★ Medical Imaging AI Line (3-Step Evolution)
- **MAC** (2024-II) — medical twin pulmonary vessel model *(3D technology base)*
- [`LungCT3DNoduleAI`](https://github.com/MoriochoRadio/LungCT3DNoduleAI) (2025-1) — lung CT nodules, 78% *(me: PM)*
- **AILungandLiver / L-POT** (2025-2, this project) — lung+liver nodules, 93% *(me: QA)*

### Same Patient-Centered Healthcare Line
- [`MedQueue`](https://github.com/MoriochoRadio/MedQueue) — real-time hospital waiting info (checked directly by patients)
- [`SchoolbusRFID`](https://github.com/MoriochoRadio/SchoolbusRFID) — location-based child drop-off tagging
- [`ElderCaringApp`](https://github.com/MoriochoRadio/ElderCaringApp) — health monitoring for seniors living alone
- [`sperm-ai`](https://github.com/MoriochoRadio/sperm-ai) · [`seed-project`](https://github.com/MoriochoRadio/seed-project)

---

## License

See [`LICENSE.md`](LICENSE.md) (MIT). This repo publishes the learning outcome of an undergraduate team project for portfolio purposes. Medical imaging data follows the license of each public dataset. **This system does not replace clinical reading and is a reference tool for research and educational purposes.**

---

*Author: [MoriochoRadio](https://github.com/MoriochoRadio) (KimTaeKyoung) · Dept. of Medical IT Engineering, Konyang University · Team T.O.P QA · 2025-2 · presented 2025.12.02*
