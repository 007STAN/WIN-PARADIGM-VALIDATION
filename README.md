# Warped Information Number (WIN) Paradigm — Validation Suite

**Author:** Stanley Preschutti (Information Physics Institute,UK)  
**Framework:** Open-Source Empirical & Theoretical Verification Pipeline

---

## 🌌 Overview & Paradigm Definition

The **Warped Information Number (WIN) Paradigm** is a theoretical framework modeling atomic mass distribution, nuclear binding behaviors, holographic scaling, and parameter-free quantum transport across physical systems. This repository hosts the official validation suite, verification scripts, and interactive Colab-native measurement engines accompanying the framework. 

It provides an open-source, reproducible framework allowing independent researchers and peers to test theoretical derivations against empirical particle physics data, cosmological datasets, quantum scrambling metrics, black hole microstates, and table-top condensed matter experiments.

---

## 📂 Repository File Structure

* **`WIN.pdf`** — Official Warped Information Paradigm White Paper and theoretical foundation.
* **`WIN-MESA Page Curve Analyzer.py`** — Evaluates unitary black hole evaporation, Wishart fluctuation suppression, and archival persistence bounds.
* **`entropix_black_hole_test.py`** — $N=64$ Black Hole Verification script for microcanonical entropy partitioning.
* **`win_cosmology_validation.py`** — Cosmological data validation pipeline referencing large-scale structure metrics.
* **`win_dark_matter_engine.py`** — Computes protected Majorana bound states, relic density floors ($\Omega_{DM}h^2 \approx 0.12$), and stability lifetimes.
* **`win_dark_photon_validation.py`** — Audits dark photon coupling limits against fixed-target constraints (NA64).
* **`win_higgs_hiearchy_engine.py`** — Models 5D warped geometry ($kL \approx 38.44$), $A_5$ Higgs mass predictions ($126.09\text{ GeV}$), and KK graviton resonances ($1.52\text{ TeV}$).
* **`win_lattice_simulation.py`** — Discrete lattice simulation harness for QIN substrate dynamics.
* **`win_periodic_table_validation.py`** — Periodic table nuclear binding scaling script across elements $Z = 1$ to $118$.
* **`win_quantum_scrambling_validation.py`** — Simulates out-of-time-order correlators (OTOCs) and chaos damping zones ($\gamma = 0.05 + 0.10 \ln k$).
* **`win_transport_dissipation_engine.py`** — Computes parameter-free Planckian dissipation prefactors ($\alpha$) and linear-$T$ resistivity bounds for condensed matter systems.
* **`win_unit_converter.py`** — Utility conversion script across WIN paradigm energy, temporal, and substrate tiers.

---

## 🔬 Core Validation & Engine Pillars

The verification pipeline spans six primary experimental and computational domains:

### 1. Periodic Table & Nuclear Binding Validation
* **Methodology:** Tests the corrected mass formula and Information Dissipation Rate (`idr`) function across elements $Z = 1$ to $118$.
* **Core Baseline Statistics ($Z \ge 2$):** Maintains a multi-nucleon core mean scaling ratio of **$162.07 \pm 9.35$**, isolating single-proton boundary exceptions while capturing magic-number closures.

### 2. Particle Physics Constraints (NA64 / Dark Photon Limits)
* **Methodology:** Audits dark photon coupling predictions ($\epsilon \approx 1.2 \times 10^{-3}$) against public accelerator exclusion limits, ensuring safe margins outside fixed-target boundaries.

### 3. Observational Cosmology & Warped Hierarchy (Euclid / Planck)
* **Methodology:** Cross-references large-scale structure scaling ratios and models 5D warped geometry ($kL \approx 38.44$) to resolve the gauge hierarchy problem and anchor the Higgs mass ($126.09\text{ GeV}$) parameter-free.

### 4. Quantum Scrambling & Black Hole Information Engines
* **Methodology:** Computes unitary evaporation and Wishart ensemble variance suppression via the microcanonical entropy coefficient ($S_0 \approx 0.232$).
* **Dark Matter Integration:** Derives dark matter as protected Majorana bound states targeting $\Omega_{DM}h^2 \approx 0.12$.

### 5. Metric Rigidity & Compression Wall Analyzer
* **Methodology:** Operationalizes the 6D toroidal vault and the **$1068.81\text{ TeV}$ Compression Wall**, computing metric rigidity ($\hat{R} \to 1.0$) and temporal drift ($14,359\text{ as}^{-1}$) to resolve classical curvature singularities into smooth, bounded geometries.

### 6. Quantum Transport & Planckian Dissipation Engine
* **Methodology:** Bypasses ad-hoc effective mass fudge factors by deriving the universal Planckian dissipation prefactor ($\alpha \sim 1.0$) directly from topological network partitioning for table-top condensed matter testing.

---

## 📊 Summary Validation Matrix (Core Nuclear Sample)

| Z | Element | Mass Number (A) | Real Mass (u) | WIN Corrected | Residual (from Core Mean) |
|---|---|---|---|---|---|
| 2 | He | 4 | 4.003 | 0.026 | -8.55 |
| 8 | O | 16 | 15.999 | 0.079 | -10.15 |
| 20 | Ca | 40 | 40.078 | 0.267 | -11.99 |
| 54 | Xe | 131 | 131.293 | 0.762 | +10.14 |
| 82 | Pb | 208 | 207.200 | 1.204 | +8.91 |
| 118 | Og | 294 | 294.000 | 1.824 | -0.89 |

---

## 🚀 How to Run the Code

You can run the validation scripts locally or launch them directly via Google Colab.

### 1. Prerequisites
Ensure you have Python 3.8+ installed along with the required scientific libraries:
```bash
pip install numpy pandas matplotlib ipywidgets
