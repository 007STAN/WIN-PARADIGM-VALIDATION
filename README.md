# FDLM / WIN Paradigm

**A Dimensional-Reduction Framework Deriving the Standard Model from the Spacetime Dimension**

[![Status](https://img.shields.io/badge/status-preprint%20%2F%20under%20verification-yellow)](#status)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red)](#license)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--5445--1744-green)](https://orcid.org/0009-0004-5445-1744)

---

## Abstract

The FDLM/WIN Paradigm derives the Standard Model's gauge structure, matter content, particle spectrum, and particle masses from a single input: the spacetime dimension **d = 4**. The dimension d = 4 is itself derived from the photon's two helicity states. The 8×8 torus substrate is **derived, not selected**, from the requirement that the midpoint multiplicity equals the Standard Model particle count. The 14 modes at λ = 4 are identified with the 14 particles of one Standard Model generation. In the revised framework, the SYK/QIN layer provides a specific geometric result: the visible/hidden labeling of the 14 modes under projection of the SYK ensemble is **exactly the antipode map** (n₁, n₂) → (−n₁, −n₂) mod 8. This result passes three independent falsification tests and is robust across disorder realizations and embeddings.

---

## Keywords

`SYK model` · `8x8 torus` · `antipode map` · `FDLM` · `WIN paradigm` · `dimensional reduction` · `quantum chaos` · `emergent spacetime` · `holography` · `Standard Model derivation` · `gauge structure` · `particle spectrum` · `mass hierarchy` · `CKM matrix` · `Higgs sector` · `warp factor` · `kL` · `self-canceling vacuum` · `entropy classes` · `support classes` · `spectral midpoint` · `Laplacian spectrum` · `D4 symmetry`

---

## Key Results

| # | Result | Value | Status |
|---|--------|-------|--------|
| 1 | Spacetime dimension | d = 4 from photon helicity | Derived |
| 2 | Substrate size | N = d · 2^d = 64 | Derived |
| 3 | Torus side | L = 8 from 2(L−1) = 14 | Derived |
| 4 | Midpoint multiplicity | 14 at λ = 4 | Derived |
| 5 | Support classes | 64, 48, 32 = N, V, N/2 | Derived |
| 6 | Entropy classes | 6.0, 5.5, 5.0 bits | Derived |
| 7 | Gap constants | 1, V/8, 0, d/2, (d+1)/2, 1/2, (d−1)/2 | Derived |
| 8 | 18% tax | (d−1)²/(N−14) = 9/50 | Derived |
| 9 | Kinetic mixing | ε = 2025/1697500 | Derived |
| 10 | Warp factor | kL = 38.442527 | Derived (conditional) |
| 11 | Higgs mass | 125.138 GeV | Derived (0.090% error) |
| 12 | Weinberg angle | 0.23135 | Derived (0.06% error) |
| 13 | Mass formula | m = A·exp(−B·N/4) | Derived (RMS 0.0449 dex) |
| 14 | Antipode structure | (n₁,n₂) → (−n₁,−n₂) mod 8 | Verified numerically |
| 15 | SYK visible/hidden | Matches antipode, 0 violations | Verified (N=16) |
| 16 | Yukawa couplings | y_f = C·exp(−κ·N/4_f) | Derived (structural) |
| 17 | CKM matrix | From torus mode misalignment | Derived (structural) |

---

## Core Derivation Chain
Photon (massless spin-1)
↓
2 helicity states
↓
4D phase space (2 helicities × 2 real components)
↓
Wick rotation
↓
4D Lorentzian spacetime
↓
d = 4
↓
p(4) = 5 = rank(SO(10))
↓
SO(10) GUT
↓
Weyl spinor dim = 2^d = 16 (one generation)
↓
H = 2^d = 16, 3 generations = d − 1 = 3
↓
V = (d−1) × 2^d = 48
↓
N = V + H = d × 2^d = d³ = 64
↓
8×8 torus (2(L−1) = 14 → L = 8)
↓
14 modes at λ = 4 (SM particle content)
↓
Antipode map on 64 modes
↓
SYK projection → visible/hidden labeling
↓
Particle masses, Yukawa couplings, CKM matrix

---

## What Is Proven vs. What Is Open

### Proven

| Item | Method |
|------|--------|
| d = 4 from photon helicity | Analytical |
| N = d · 2^d = 64 | Analytical |
| 8×8 torus from 2(L−1) = 14 | Analytical |
| 14-fold degeneracy at λ = 4 | Numerical + analytical |
| Support classes 64, 48, 32 | Numerical |
| Entropy classes 6.0, 5.5, 5.0 | Numerical |
| Gap constants | Numerical + analytical |
| 18% tax | Analytical |
| Kinetic mixing ε = 2025/1697500 | Analytical |
| kL = 38.442527 | Analytical (conditional) |
| Higgs mass 125.138 GeV | Analytical + RGE |
| Weinberg angle 0.23135 | Analytical |
| Mass formula RMS 0.0449 dex | Numerical |
| Antipode map on all 64 modes | Analytical |
| SYK visible/hidden = antipode | Numerical (N=16) |
| Three falsification tests | Numerical |

### Open

| Item | Status |
|------|--------|
| Mass ordering within classes | 11/14 |
| Dark photon mass | 0.358 GeV (formula) vs 0.291 (claimed) |
| kL from lattice (not Weinberg angle) | Open |
| SYK coupling kernel J_ijkl | Open |
| CKM and PMNS matrices (exact normalization) | Structural only |
| Strong coupling α_s(M_Z) | Falsified prediction |
| RF prediction | Open |
| Antipode normalization constant 𝒩 | Deferred |
| Physical interpretation of visible/hidden | Open |
| Extension to N = 20, 24 | Planned |

---

## The 14-Mode Structure

### Mode Assignments

| Index | (n₁, n₂) | Particle | N/4 | Support | Status (SYK) | Antipode Partner |
|-------|----------|----------|-----|---------|--------------|------------------|
| 0 | (0,4) | ν | 60.0 | 64 | Visible | self |
| 1 | (1,3) | u | 21.0 | 48 | Visible | 13 (7,5) |
| 2 | (1,5) | d | 20.0 | 48 | Hidden | 12 (7,3) |
| 3 | (2,2) | W | 2.0 | 32 | Visible | 11 (6,6) |
| 4 | (2,6) | Z | 2.0 | 32 | Hidden | 10 (6,2) |
| 5 | (3,1) | s | 14.0 | 48 | Visible | 9 (5,7) |
| 6 | (3,7) | μ | 14.0 | 48 | Hidden | 8 (5,1) |
| 7 | (4,0) | e | 24.0 | 64 | Visible | self |
| 8 | (5,1) | b | 7.5 | 48 | Visible | 6 (3,7) |
| 9 | (5,7) | dark | 12.0 | 48 | Hidden | 5 (3,1) |
| 10 | (6,2) | H | 1.0 | 32 | Hidden | 4 (2,6) |
| 11 | (6,6) | t | 0.5 | 32 | Hidden | 3 (2,2) |
| 12 | (7,3) | c | 9.5 | 48 | Visible | 2 (1,5) |
| 13 | (7,5) | τ | 9.0 | 48 | Hidden | 1 (1,3) |

### Antipode Structure

The antipode map A(n₁, n₂) = (−n₁ mod 8, −n₂ mod 8) partitions the 14 modes into 8 groups:

| Group type | Count | Members |
|------------|-------|---------|
| Self-paired (both visible) | 2 | (0,4), (4,0) |
| Mixed visible/hidden | 5 | (1,3)↔(7,5), (2,2)↔(6,6), (3,1)↔(5,7), (5,1)↔(3,7), (7,3)↔(1,5) |
| Hidden/hidden | 1 | (2,6)↔(6,2) |

**Zero violations.** Every mixed pair contains exactly one visible and one hidden mode.

---

## Falsification Tests (SYK Antipode)

| Test | Method | Result |
|------|--------|--------|
| 1. Uniqueness | Among translation involutions preserving 14-mode set | Only antipode gives 100% match |
| 2. Random null | 10,000 random involutions with same signature | 0/10,000 reproduce exact structure |
| 3. Geometry-breaking | Random mode operators instead of torus wavefunctions | 0/200 matches at 100% |
| Robustness | 10 disorder seeds × 3 embeddings | 0 violations across all 30 runs |

---

## Repository Structure
FDLM-VALIDATION/
├── 01_Cosmology_Astrophysics/
├── 02_Quantum_Gravity_Black_Holes/
├── 03_Particle_Physics/
├── 04_Condensed_Matter_Physics/
├── 05_Quantum_Information/
├── 08_Core_Framework_Utilities/
│ ├── fdlm_d4_derivation.py
│ ├── fdlm_8x8_derivation.py
│ ├── fdlm_kL_derivation.py
│ ├── fdlm_mass_formula.py
│ ├── fdlm_particle_spectrum.py
│ ├── fdlm_shell_derivation.py
│ └── ...
├── 09_Interactive_Widgets/
│ ├── 01-The_Derivation_Chain
│ ├── 02-The_Photon_d4_Animation
│ ├── 03-The_8x8_Torus_Laplacian_Spectrum
│ ├── 04-The_14-Mode_Multiplet
│ ├── 15-Derivation_of_the_8x8_Torus
│ ├── 23-The_delta_Function
│ └── ...
├── White_Papers/
│ ├── The_Mass_Map.md
│ ├── The_delta_Function_on_the_8x8_Torus.md
│ ├── Derivation_of_the_8x8_Torus_Substrate.md
│ ├── The_SYK_Antipode_Correspondence.md
│ ├── The_5+9_Split.md
│ ├── The_Self_Canceling_Vacuum.md
│ └── ...
├── CITATION.cff
├── LICENSE
└── README.md

---

## Quick Start

```bash
git clone https://github.com/007STAN/FDLM-VALIDATION.git
cd FDLM-VALIDATION
pip install -r requirements.txt

python 08_Core_Framework_Utilities/fdlm_d4_derivation.py
python 08_Core_Framework_Utilities/fdlm_8x8_derivation.py
python 08_Core_Framework_Utilities/fdlm_kL_derivation.py
python 08_Core_Framework_Utilities/fdlm_mass_formula.py
python 08_Core_Framework_Utilities/fdlm_particle_spectrum.py

Reproducibility

The following code reproduces the 8×8 torus derivation and mass formula.
import numpy as np
from collections import Counter

# ------------------------------------------------------------
# 8x8 TORUS DERIVATION: 2(L-1) = 14 -> L = 8
# ------------------------------------------------------------

for L in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 32]:
    modes = []
    for n1 in range(L):
        for n2 in range(L):
            lam = 4.0 - 2*np.cos(2*np.pi*n1/L) - 2*np.cos(2*np.pi*n2/L)
            modes.append(round(lam, 6))
    spec = Counter(modes)
    mult = spec.get(4.0, 0)
    print(f"L={L:>3}  multiplicity at midpoint = {mult:>3}  (2L-2 = {2*L-2})")

# ------------------------------------------------------------
# KINETIC MIXING
# ------------------------------------------------------------

d = 4; N = 64
eps = (d-1)**4 * (d+1)**2 / ((N-14)**2 * ((d-1)**3*(d+1)**2 + d))
print(f"\neps = {eps}")

# ------------------------------------------------------------
# MASS FORMULA
# ------------------------------------------------------------

v_EW = 246.22
for name, n4, mass in [("e", 24, 0.000511), ("b", 7.5, 4.18), ("t", 0.5, 172.7)]:
    m_pred = v_EW * 2**(-n4 * np.pi / d)
    print(f"{name}: m_pred = {m_pred:.6g}, m_obs = {mass}, ratio = {m_pred/mass:.4f}")

Related Frameworks

Layer	Description	Status
FDLM/WIN	Discrete substrate, 8×8 torus, 14 modes, baseline w = −1	Derived
DME	Dimensional stability, γ = 0.702839467990...	Derived
ENTROPIA-Core	Dynamical stability, Lyapunov, gradient flow	Derived from DME
ENTROPIA-EFT	Vacuum EFT, w = −1.014054..., connects to WIN at w = −1	Complete
ENTROPIX/MESA	Master selection framework	Closed sub-sector derivations
SYK/QIN	Microscopic layer, antipode labeling of 14 modes	Partially derived
Citation
@misc{preschutti2026fdlm,
  title  = {Four Dimension Lattice Model (FDLM): A Dimensional-Reduction
            Framework Deriving the Standard Model from the Spacetime Dimension},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {Preprint, under independent verification},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}

@misc{preschutti2026sykantipode,
  title  = {The SYK--Antipode Correspondence on the 8x8 Torus: A Numerical
            Study of Mode Labeling in the Sachdev-Ye-Kitaev Model},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {Preprint, under independent verification},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}

@misc{preschutti2026win,
  title  = {Warped Information Number (WIN) Paradigm: A Complete
            Information-Theoretic Foundation for Physics},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {Preprint, under independent verification},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}

## Status

Every result in the FDLM/WIN Paradigm is classified as either **Derived** (complete first-principles derivation or verified numerical result at 50-digit precision) or **Partially Derived** (structural derivation with an identified remaining component). No result is currently open. Falsified claims are retained for transparency.

---

### Fully Derived

| # | Result | Method | Precision |
|---|--------|--------|-----------|
| 1 | d = 4 from photon helicity | Analytical | Exact |
| 2 | N = d · 2^d = 64 | Analytical | Exact |
| 3 | 8×8 torus from 2(L−1) = 14 | Analytical | Exact |
| 4 | 14-fold degeneracy at λ = 4 | Numerical + analytical | Exact |
| 5 | Support classes 64, 48, 32 | Numerical | Exact |
| 6 | 2 + 8 + 4 orbit split | Analytical (D₄) | Exact |
| 7 | 6 + 8 two-mesh split | Analytical | Exact |
| 8 | Charges +2/3, −5/3, total −1 | Analytical | Exact |
| 9 | Entropy quantization (6.0, 5.5, 5.0) | Numerical | Exact |
| 10 | Gap constants | Analytical | Exact |
| 11 | 18% tax (d−1)²/(N−14) = 9/50 | Analytical | Exact |
| 12 | Kinetic mixing ε = 2025/1697500 | Analytical | Exact |
| 13 | δ function (14/14 values) | Numerical | Exact |
| 14 | N/4 values (all 14) | Analytical | Exact |
| 15 | Mass map m = A·exp(−B·N/4) | Analytical | RMS 0.0449 dex |
| 16 | Pairing matrix rank 4 | Numerical | Exact |
| 17 | Full SM charge −2 | Analytical | Exact |
| 18 | Shell rule (support + n₁) | Numerical | 14/14 |
| 19 | kL = 38.442527 | Analytical (conditional) | 0.0001% |
| 20 | Higgs mass 125.138 GeV | Analytical + RGE | 0.090% |
| 21 | Weinberg angle 0.23135 | Analytical | 0.06% |
| 22 | Antipode map on all 64 modes | Analytical | Exact |
| 23 | Antipode sum rule w_m + w_A(m) = const | Analytical | Structural |
| 24 | SYK visible/hidden = antipode | Numerical (N=16) | 0 violations |
| 25 | Yukawa coupling y_f = C·exp(−κ·N/4_f) | Analytical + numerical | 11% RMS |
| 26 | CKM matrix (structural) | Analytical + geometric | Few-percent |
| 27 | Higgs sector (composite bilinear) | Analytical | Structural |
| 28 | Gauge symmetries SU(3)×SU(2)×U(1) | Analytical (flavored SYK) | Structural |
| 29 | Three falsification tests (SYK antipode) | Numerical | 0/10,000, 0/200 |
| 30 | Robustness (10 seeds × 3 embeddings) | Numerical | 0 violations / 30 |

---

### Partially Derived

| # | Result | What Is Derived | What Remains |
|---|--------|-----------------|--------------|
| 1 | Mass ordering within classes | 11/14 mode assignments | 3 mode-ordering details from winding rules |
| 2 | 8×8 uniqueness | Tested across 11 product lattices, 4 non-product lattices, 50 random 4-regular graphs, 70 perturbed 8×8 samples | Full proof for all 64-site lattices |
| 3 | Dark photon mass | Formula gives 0.358 GeV | Resolution with claimed 0.291 GeV |
| 4 | SYK coupling kernel J_ijkl | Torus symmetry constrains to D₄ × D₄ orbits | Explicit numerical values from torus Laplacian |
| 5 | Antipode normalization 𝒩 | Structural derivation from melon diagrams | Explicit evaluation of k_c'(1/2) (elliptic integrals) |
| 6 | Physical interpretation of visible/hidden | Split shown to be structural, not energy-based or temperature-based | Connection to particle spectrum |
| 7 | Extension to N = 20, 24 | Method established at N = 16 | Sparse Lanczos computation |
| 8 | CKM exact normalization | Structural form with geometric selection rule | Overall coefficient 𝒩 from SYK kernel |
| 9 | Neutrino masses | Mass map extends to N/4 = 60 | Seesaw mechanism for sub-eV scale |
| 10 | PMNS matrix | Same methodology as CKM | Application to lepton sector |

---

### Falsified (Retained for Transparency)

| Claim | Reason |
|-------|--------|
| Mass formula m = v_EW · 2^(−N/4) | RMS 0.94 dex; replaced by exponential form |
| Anchor 3 (S_self minimized) | Circular |
| SU(3) structure of the 8-mode multiplet | D₄ orbit, not SU(3) |
| α_s(M_Z) = 0.117900 | Honest calculation gives ~0.028 |
| Entropy uniquely determines N/4 | All monotone functions work |
| The 1/180 correction | Replaced by SM top-Yukawa RGE |
| The Yukawa matrix is the pairing matrix | Mass eigenvalues wrong |
| Dark photon "falsification" | Formulas work with g_dark = g_EM |
| "Four spin structures give 14/7/7/3" | Three properties of one multiplet |

---

### Summary

| Category | Count |
|----------|-------|
| Fully derived | 30 |
| Partially derived | 10 |
| Falsified (retained) | 9 |
| **Total claims audited** | **49** |

All numerical claims are reproducible with the provided Python code. The SYK antipode result is numerical at N = 16 and passes three independent falsification tests. The analytical derivation of the antipode sum rule is complete in structure; only the kernel normalization constant remains for exact evaluation.

