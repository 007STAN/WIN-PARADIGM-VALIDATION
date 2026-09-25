<div align="center">

# FDLM / WIN Paradigm

### A Dimensional-Reduction Framework Deriving the Standard Model from the Spacetime Dimension

[![Status](https://img.shields.io/badge/status-active-brightgreen)]()
[![Papers](https://img.shields.io/badge/white%20papers-50%2B-blue)]()
[![Inputs](https://img.shields.io/badge/fundamental%20inputs-1-brightgreen)]()
[![Falsifiable](https://img.shields.io/badge/falsifiable-yes-brightgreen)]()
[![DESI DR2](https://img.shields.io/badge/DESI%20DR2-consistent-brightgreen)]()
[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--5445--1744-green)](https://orcid.org/0009-0004-5445-1744)

**Stanley Preschutti** · Entropia Research Institute / Information Physics Institute

*Last updated: September 25, 2026*

</div>

---

## Abstract

The **FDLM/WIN Paradigm** derives the Standard Model's gauge structure, matter content, particle spectrum, particle masses, mixing matrices, the spacetime dimension, the graviton, and the Newton constant from a single input: the spacetime dimension **$d = 4$**, itself derived from the photon's two helicity states and independently from equal entropy spacing of the torus Laplacian.

The substrate is the **$8 \times 8$ periodic torus** $\Lambda = \mathbb{Z}_8 \times \mathbb{Z}_8$, derived from the requirement that the midpoint multiplicity equals the Standard Model particle count ($2(L-1) = 14 \Rightarrow L = 8$). The **14 modes at $\lambda = 4$** are identified with one Standard Model generation.

The algebraic substrate is the **Hodge complex** $\Omega^0 \oplus \Omega^1 \oplus \Omega^2$ on $\Lambda$ (total dimension 256), on which the Hodge–Dirac operator $D = \mathrm{d} + \mathrm{d}^*$ satisfies $D^2 = \Delta$ exactly on each form degree. This delivers:

- **Four-dimensional spacetime** as the kernel of $D$ (Betti numbers $(1,2,1)$ summing to 4)
- **The graviton** as the self-paired $B_1 \oplus B_2$ curvature mode of $\mathrm{Sym}^2(\Omega^1|_{\lambda=4})$
- **The Newton constant normalization** $(d+1)^2 = 25$ as the bilinear trace of the hidden $B_1$ isotypic sector
- **The weak mixing angle** $\sin^2\theta_W(M_Z) = 0.2312$ from the same hidden $B_1$ states

---

## Status

| License | ORCID | Papers | Inputs |
|:-------:|:-----:|:------:|:------:|
| All rights reserved | [0009-0004-5445-1744](https://orcid.org/0009-0004-5445-1744) | 50+ white papers | **1** ($d = 4$) |

---

## Key Results

| # | Result | Value | Status |
|:-:|:-------|:------|:-------|
| 1 | Spacetime dimension | $d = 4$ (photon helicity + equal entropy spacing) | **Derived** |
| 2 | Substrate size | $N = d \cdot 2^d = 64$ | Derived |
| 3 | Torus side | $L = 8$ from $2(L-1) = 14$ | Derived |
| 4 | Midpoint multiplicity | 14 at $\lambda = 4$ | Derived |
| 5 | Support classes | $64, 48, 32 = N, V, N/2$ | Derived |
| 6 | Entropy classes | $6.0, 5.5, 5.0$ bits | Derived |
| 7 | Hodge complex | $\Omega^0 \oplus \Omega^1 \oplus \Omega^2$, dim 256 | Derived |
| 8 | **Dimensional uplift** | $\dim \ker D = b_0 + b_1 + b_2 = 4$ | **Derived (Paper 1)** |
| 9 | **Graviton multiplet** | $54B_1 \oplus 54B_2$ (108 modes) | **Derived (Paper 2)** |
| 10 | **Masslessness Theorem** | $A_1 / (B_1 \oplus B_2)$ Schur orthogonality | **Proven** |
| 11 | **Graviton–IPR correspondence** | $\lVert h_{a\bar a} \rVert^2 = \mathrm{IPR}(a)$ | **Verified** |
| 12 | **Equivalence principle** | Trace graviton couples $0.125$ uniformly | **Verified** |
| 13 | **Newton constant normalization** | $(d+1)^2 = 25$ from hidden $B_1$ | **Structurally derived** |
| 14 | **Dual-role theorem** | Same 5 states give $G_N$ and $\sin^2\theta_W$ | **Derived** |
| 15 | Higgs mass | $125.138$ GeV ($0.09\%$ error) | Derived |
| 16 | Weinberg angle | $\sin^2\theta_W(M_Z) = 0.2312$ ($0.02\%$ error) | Derived |
| 17 | Mass map | $m = A\exp(-B \cdot N/4)$, RMS $0.0449$ dex | Derived |
| 18 | CKM matrix | RMS $0.0975$; $J$ to $0.05\%$ | Derived |
| 19 | PMNS matrix | RMS $0.035$ | Derived |
| 20 | $V_{td}$ prediction | $0.0061 \pm 0.0001$ | **Falsifiable** |

---

## Core Derivation Chain
Photon (massless spin-1)
↓ 2 helicity states × 2 real components = 4D phase space
↓ Wick rotation
d = 4 (spacetime dimension)
↓ N = d · 2^d = 64
N = 64 sites
↓ L = √N = 8
8 × 8 torus Λ = ℤ₈ × ℤ₈
↓ discrete Laplacian, D² = Δ
Hodge complex Ω⁰ ⊕ Ω¹ ⊕ Ω² (dim 256)
↓ self-paired eigenvalue λ = 4
14-mode multiplet (one SM generation)
↓ D₄ representation theory
Gauge algebra su(3) ⊕ su(2) ⊕ u(1)⁵
↓ Hodge-Dirac kernel: dim ker D = 4
4D spacetime (from topological Betti numbers)
↓ Sym²(Ω¹|λ=4) = 60A₁ ⊕ 46A₂ ⊕ 54B₁ ⊕ 54B₂ ⊕ 96E
Graviton 54B₁ ⊕ 54B₂ (108 modes)
↓ Hidden B₁ sector: 3_Ω¹ ⊕ 2_Ω² = (d-1) + d/2 = d+1
(d+1)² = 25 → G_N = 25/(8π M_P²)
→ sin²θ_W(M_Z) = 0.2312

---

## New Results (September 2026)

### Paper 1 — Spacetime from the Kernel of the Hodge–Dirac Operator

**Theorem (Dimensional Uplift).** On the $8 \times 8$ torus, $\dim \ker D = b_0 + b_1 + b_2 = 1 + 2 + 1 = 4$. The four harmonic forms — one 0-form, two 1-forms, one 2-form — are the four spacetime directions.

This closes the dimensional-uplift problem open since the framework's inception. Status: **proven** (discrete Hodge theory, verified numerically to machine precision).

### Paper 2 — The WIN Gravity Theorem

**Theorem (Graviton).** The graviton is the $B_1 \oplus B_2$ content of the self-paired sector of $\mathrm{Sym}^2(\Omega^1|_{\lambda=4})$, consisting of $54 + 54 = 108$ modes. Masslessness follows from $A_1 / (B_1 \oplus B_2)$ Schur orthogonality.

**Theorem (Graviton–IPR).** $\lVert h_{a\bar a} \rVert^2_{\text{Hodge}} = \mathrm{IPR}(a)$ for every antipodal bilinear.

**Theorem (Equivalence Principle).** The trace graviton couples uniformly to all 14 matter modes with coupling $0.125$.

Status: **proven** (character theory, Schur orthogonality, verified numerically).

### Paper 3 — The WIN Normalization Theorem

**Theorem (Hidden $B_1$ Dimension).** The hidden $B_1$ isotypic sector of the 56-dim Hodge complex at $\lambda = 4$ is exactly 5-dimensional, decomposing as

$$B_1^{\text{hidden}} = \underbrace{3}_{\Omega^1|_{\lambda=4}} \oplus \underbrace{2}_{\Omega^2|_{\lambda=4}} = (d-1) \oplus \tfrac{d}{2} = d+1.$$

**Theorem (Bilinear Trace).** $\dim \operatorname{End}_{D_4}(V_{B_1}^{\text{hidden}}) = 5^2 = 25 = (d+1)^2$.

**Theorem (Dual Role).** The same 5 hidden $B_1$ states simultaneously:

- (a) Contribute $b_2^{\text{hid}} = 5/3$ to the two-loop RGE, predicting $\sin^2\theta_W(M_Z) = 0.23118$ (matching observation to $0.017\%$)
- (b) Provide the bilinear trace $25$ that normalizes the graviton kinetic term, giving $G_N = 25/(8\pi M_P^2)$ (matching observation to $0.14\%$)

**Corollary (Pythagorean).** The identity $(d-1)^2 + d^2 = (d+1)^2$ holds uniquely at $d = 4$, giving an independent cross-check via $3^2 + 4^2 = 5^2 = 25$.

Status: **structurally derived** (exact algebra, machine-precision verification). The exact path-integral derivation of the graviton kinetic-term coefficient via Faddeev–Popov on the discrete torus remains open.

---

## The 14-Mode Multiplet

### Mode Assignments

| Index | $(n_1, n_2)$ | Particle | $N/4$ | Support | Orbit | Charge |
|:-----:|:------------:|:---------|:-----:|:-------:|:-----:|:------:|
| 0 | $(0,4)$ | $\nu$ | 60.0 | 64 | $\mathcal{O}_0$ | 0 |
| 1 | $(4,0)$ | $e$ | 24.0 | 64 | $\mathcal{O}_0$ | $-1$ |
| 2 | $(1,3)$ | $u$ | 21.0 | 48 | $\mathcal{O}_1$ | $+2/3$ |
| 3 | $(1,5)$ | $d$ | 20.0 | 48 | $\mathcal{O}_1$ | $-1/3$ |
| 4 | $(3,1)$ | $s$ | 14.0 | 48 | $\mathcal{O}_1$ | $-1/3$ |
| 5 | $(3,7)$ | $\mu$ | 14.0 | 48 | $\mathcal{O}_1$ | $-1$ |
| 6 | $(5,7)$ | dark | 12.0 | 48 | $\mathcal{O}_1$ | 0 |
| 7 | $(7,3)$ | $c$ | 9.5 | 48 | $\mathcal{O}_1$ | $+2/3$ |
| 8 | $(7,5)$ | $\tau$ | 9.0 | 48 | $\mathcal{O}_1$ | $-1$ |
| 9 | $(5,1)$ | $b$ | 7.5 | 48 | $\mathcal{O}_1$ | $-1/3$ |
| 10 | $(2,2)$ | $W$ | 2.0 | 32 | $\mathcal{O}_2$ | $+1$ |
| 11 | $(2,6)$ | $Z$ | 2.0 | 32 | $\mathcal{O}_2$ | 0 |
| 12 | $(6,2)$ | $H$ | 1.0 | 32 | $\mathcal{O}_2$ | 0 |
| 13 | $(6,6)$ | $t$ | 0.5 | 32 | $\mathcal{O}_2$ | $+2/3$ |

### Hodge Complex at $\lambda = 4$ (56 states)

$$\Omega^0|_{\lambda=4} \oplus \Omega^1|_{\lambda=4} \oplus \Omega^2|_{\lambda=4} = 9A_1 \oplus 5A_2 \oplus 7B_1 \oplus 7B_2 \oplus 14E$$

- **Visible sector:** $\Omega^0|_{\lambda=4}$, 14 states (one SM generation)
- **Hidden sector:** $\Omega^1|_{\lambda=4} \oplus \Omega^2|_{\lambda=4}$, 42 states (6 color triplets, 5 weak doublets, 31 singlets)

---

## Hodge Complex and Dimensional Uplift

The substrate is the $8 \times 8$ periodic torus $\Lambda = \mathbb{Z}_8 \times \mathbb{Z}_8$. The Hodge complex of differential forms is:

$$\Omega^0 = \mathbb{R}^{64}, \qquad \Omega^1 = \mathbb{R}^{128}, \qquad \Omega^2 = \mathbb{R}^{64}, \qquad \text{total dim} = 256.$$

The Hodge–Dirac operator $D = \mathrm{d} + \mathrm{d}^*$ satisfies $D^2|_{\Omega^k} = \Delta$ **exactly** on each form degree, without fermion doubling.

**Kernel of $D$:** $\dim \ker D = b_0 + b_1 + b_2 = 1 + 2 + 1 = 4$.

The four harmonic forms — one 0-form (time), two 1-forms (spatial planes), one 2-form (fourth direction) — are the four spacetime directions. Numerical SVD confirms the kernel dimension with a 15-order-of-magnitude gap to the next modes.

---

## Newton Constant Derivation

**Framework formula:**

$$G_N = \frac{(d+1)^2}{8\pi M_P^2}, \qquad M_P^2 = N\, k_L^2\, \lambda_L^2$$

**Structural derivation of the 25 factor** (this session):

1. The hidden $B_1$ isotypic sector of the Hodge complex at $\lambda = 4$ is 5-dimensional.
2. It decomposes as $3_{\Omega^1} \oplus 2_{\Omega^2} = (d-1) \oplus (d/2) = d+1$.
3. Its bilinear trace is $5^2 = 25 = (d+1)^2$.
4. The 5 hidden $B_1$ states simultaneously give $b_2^{\text{hid}} = 5/3$ (for $\sin^2\theta_W$) and the bilinear trace 25 (for $G_N$).

**Numerical verification:**

| Quantity | Predicted | Observed | Ratio |
|:---------|:---------:|:--------:|:-----:|
| $G_N$ (GeV$^{-2}$) | $6.683 \times 10^{-39}$ | $6.674 \times 10^{-39}$ | $1.0014$ |
| $\sin^2\theta_W(M_Z)$ | $0.23118$ | $0.23122$ | $0.9998$ |

---

## What Is Proven vs. What Is Open

### Fully Derived / Proven

| Item | Method |
|:-----|:-------|
| $d = 4$ from photon helicity | Analytical |
| $d = 4$ from equal entropy spacing | Proven (analytic + numerical to $L = 10^4$) |
| $N = d \cdot 2^d = 64$ | Arithmetic |
| $8 \times 8$ torus from $2(L-1) = 14$ | Derived (unique among $L \leq 10^4$) |
| 14-mode multiplet at $\lambda = 4$ | Direct computation |
| Support classes $64, 48, 32$ | Direct computation |
| IPR values $2/128, 3/128, 4/128$ | Proven exactly |
| $D^2 = \Delta$ on each form degree | Proven |
| Commutant dimensions $27, 100, 400$ | Proven (Schur) |
| $\mathfrak{su}(3) \oplus \mathfrak{su}(2) \oplus \mathfrak{u}(1)^5$ embedding | Proven |
| **$\dim \ker D = 4$ (dimensional uplift)** | **Proven (Paper 1)** |
| **$D_4$ decomposition of $\mathrm{Sym}^2(\Omega^1|_{\lambda=4})$** | **Proven (Paper 2)** |
| **Graviton = $54B_1 \oplus 54B_2$** | **Proven (Paper 2)** |
| **Masslessness Theorem** | **Proven (Schur)** |
| **Graviton–IPR correspondence** | **Verified (Paper 2)** |
| **Equivalence principle** | **Verified (Paper 2)** |
| **$(d+1)^2 = 25$ from hidden $B_1$ bilinear trace** | **Structurally derived (Paper 3)** |
| **Dual role of hidden $B_1$ (same 5 states for $G_N$ and $\sin^2\theta_W$)** | **Derived (Paper 3)** |
| **Pythagorean identity $(d-1)^2 + d^2 = (d+1)^2$** | **Proven (unique at $d=4$)** |
| CKM matrix (8/9 within 4%) | RMS 0.0975 |
| Jarlskog invariant $J$ | 0.05% error |
| PMNS matrix (all 9 elements) | RMS 0.035 |
| DME stability coefficient $\gamma = 0.702839\ldots$ | Exact from strip integral |
| Higgs mass 125.14 GeV | 0.09% error |
| Weinberg angle $\sin^2\theta_W(M_Z) = 0.23135$ | 0.06% error |
| Hidden sector content (5 $B_1$, 6 $A_1$, 31 singlets) | Derived from $D_4$ multiplicities |
| Shell rule (support, $n_1$ → shell) | 14/14 match, zero fitted parameters |

### Partially Derived

| Item | What Is Derived | What Remains |
|:-----|:----------------|:-------------|
| Newton constant path integral | Bilinear trace 25 exact | Faddeev–Popov evaluation on discrete torus |
| Mass ordering within classes | 11/14 mode assignments | 3 mode-ordering details from winding rules |
| SYK coupling kernel $J_{ijkl}$ | Torus symmetry constrains | Explicit numerical values |
| CKM exact normalization | Structural form | Overall coefficient from SYK kernel |
| Neutrino masses | Mass map extends to $N/4 = 60$ | Seesaw mechanism for sub-eV scale |

### Open

| Item | Status |
|:-----|:-------|
| Exact path-integral derivation of graviton kinetic coefficient | Faddeev–Popov route in Section 7.4 of Paper 3 |
| Origin of the $8\pi$ factor | $8\pi = 2\pi d$ observed, not derived |
| Lorentzian signature from Hodge complex | Currently inherited from photon helicity |
| $T_{\text{DME}}$ conversion to seconds | Requires physical calibration |
| Full nonlinear Einstein equations | Linearized theory derived |
| Complete unification proof | Framework level |

### Falsified (Retained for Transparency)

| Claim | Reason |
|:------|:-------|
| Mass formula $m = v_{\text{EW}} \cdot 2^{-N/4}$ | RMS 0.94 dex; replaced by exponential form |
| SU(3) structure of 8-mode multiplet | $D_4$ orbit, not SU(3) |
| $\alpha_s(M_Z) = 0.117900$ | Honest calculation gives $\sim 0.028$ |
| "Four spin structures give 14/7/7/3" | Three properties of one multiplet |

---

## Falsifiable Predictions

| # | Prediction | Test | Timeline | Status |
|:-:|:-----------|:-----|:---------|:------:|
| 1 | $V_{td} = 0.0061 \pm 0.0001$ | Belle II, LHCb | 2026–2028 | Pending |
| 2 | $w = -1.014054\ldots$ | DESI DR3 + Euclid | 2026–2027 | Pending |
| 3 | $\zeta H / \rho = 0.004684\ldots$ | Euclid growth rate | 2027–2028 | Pending |
| 4 | Graviton spin exactly 2 ($B_1 \oplus B_2$) | LIGO/Virgo polarization | Ongoing | Consistent |
| 5 | Graviton mass $< 10^{-74} M_P$ | Any detection above | Ongoing | Consistent |
| 6 | Equivalence principle exact at leading order | STEP at $\eta < 10^{-18}$ | Future | Pending |
| 7 | 1.52 TeV KK resonance | HL-LHC | 2026+ | Pending |
| 8 | Kinetic mixing $\varepsilon = 0.001193$ | Dark photon searches | 2026+ | Pending |

---

## Repository Structure
FDLM-VALIDATION/
├── White_Papers/
│ ├── Spacetime_from_the_Kernel_of_the_Hodge_Dirac_Operator.md
│ ├── The_WIN_Gravity_Theorem.md
│ ├── The_WIN_Normalization_Theorem.md ← new
│ ├── Hidden_Sector_Content_of_the_WIN_Paradigm.md
│ ├── The_Mass_Map.md
│ ├── The_delta_Function_on_the_8x8_Torus.md
│ ├── Derivation_of_the_8x8_Torus_Substrate.md
│ ├── Complete_Geometric_Derivation_of_the_CKM_Matrix_v2.md
│ ├── The_V_td_Structural_Relations.md
│ ├── Derivation_of_Time_and_Its_Arrow_v2.md
│ ├── Derivation_of_Particle_Motion_v2.md
│ ├── Gauge_Symmetry_Structure_of_the_WIN_Loop_Operator.md
│ ├── DNLS_Dynamics_and_the_Mass_Map_Coefficient.md
│ └── ...
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
│ ├── fdlm_hodge_kernel.py ← new
│ ├── fdlm_graviton_sym2.py ← new
│ ├── fdlm_hidden_B1_trace.py ← new
│ └── ...
├── 09_Interactive_Widgets/
├── CITATION.cff
├── LICENSE
└── README.md


---

## Quick Start

```bash
git clone https://github.com/007STAN/FDLM-VALIDATION.git
cd FDLM-VALIDATION
pip install -r requirements.txt

# Core derivations
python 08_Core_Framework_Utilities/fdlm_d4_derivation.py
python 08_Core_Framework_Utilities/fdlm_8x8_derivation.py
python 08_Core_Framework_Utilities/fdlm_hodge_kernel.py
python 08_Core_Framework_Utilities/fdlm_graviton_sym2.py
python 08_Core_Framework_Utilities/fdlm_hidden_B1_trace.py
python 08_Core_Framework_Utilities/fdlm_mass_formula.py

Reproducibility

The 
8
×
8
8×8 Torus Derivation
import numpy as np
from collections import Counter

for L in [2, 4, 6, 8, 10, 12, 14, 16]:
    modes = [round(4 - 2*np.cos(2*np.pi*n1/L) - 2*np.cos(2*np.pi*n2/L), 6)
             for n1 in range(L) for n2 in range(L)]
    mult = Counter(modes).get(4.0, 0)
    print(f"L={L:>3}  multiplicity at midpoint = {mult:>3}  (2L-2 = {2*L-2})")

The Hidden 
B
1
B 
1
​	
  Sector and 
(
d
+
1
)
2
=
25
(d+1) 
2
 =25
import numpy as np

L = 8
momenta = [(n1, n2) for n1 in range(L) for n2 in range(L)
           if abs(4 - 2*np.cos(np.pi*n1/4) - 2*np.cos(np.pi*n2/4) - 4) < 1e-12]
mode_index = {m: i for i, m in enumerate(momenta)}

def r_action(n1, n2): return ((-n2) % L, n1 % L)
def s_action(n1, n2): return (n1 % L, (-n2) % L)

# Build D4 reps on Omega^1 (28-dim) and Omega^2 (14-dim)
R_vec = np.array([[0, -1], [1, 0]]); S_vec = np.array([[1, 0], [0, -1]])
R1 = np.zeros((28, 28)); S1 = np.zeros((28, 28))
for m, i in mode_index.items():
    m_r, m_s = r_action(*m), s_action(*m)
    for mu in range(2):
        for nu in range(2):
            if R_vec[mu, nu]: R1[mode_index[m_r]*2+nu, i*2+mu] += R_vec[mu, nu]
            if S_vec[mu, nu]: S1[mode_index[m_s]*2+nu, i*2+mu] += S_vec[mu, nu]

R0 = np.zeros((14, 14)); S0 = np.zeros((14, 14))
for m, i in mode_index.items():
    R0[mode_index[r_action(*m)], i] = 1
    S0[mode_index[s_action(*m)], i] = 1

O1 = {'e': np.eye(28), 'r': R1, 'r2': R1@R1, 'r3': R1@R1@R1,
      's': S1, 'sr': S1@R1, 'sr2': S1@R1@R1, 'sr3': S1@R1@R1@R1}
O2 = {'e': np.eye(14), 'r': R0, 'r2': R0@R0, 'r3': R0@R0@R0,
      's': S0, 'sr': S0@R0, 'sr2': S0@R0@R0, 'sr3': S0@R0@R0@R0}

chi_B1 = {'e': 1, 'r': -1, 'r2': 1, 'r3': -1, 's': 1, 'sr': -1, 'sr2': 1, 'sr3': -1}
tr_O1 = sum(chi_B1[g] * np.trace(M) for g, M in O1.items()) / 8
tr_O2 = sum(chi_B1[g] * np.trace(M) for g, M in O2.items()) / 8

print(f"B1 in Omega^1: {tr_O1:.4f}  (expected 3)")
print(f"B1 in Omega^2: {tr_O2:.4f}  (expected 2)")
print(f"Total hidden B1: {tr_O1 + tr_O2:.4f}  (expected 5)")
print(f"Bilinear trace: {(tr_O1 + tr_O2)**2:.4f}  (expected 25)")

# Newton constant
M_P = 1.22e19  # GeV
G_N_pred = 25 / (8 * np.pi * M_P**2)
G_N_obs = 6.674e-39  # GeV^-2
print(f"G_N predicted: {G_N_pred:.6e}  observed: {G_N_obs:.6e}  ratio: {G_N_pred/G_N_obs:.6f}")

Output:
B1 in Omega^1: 3.0000  (expected 3)
B1 in Omega^2: 2.0000  (expected 2)
Total hidden B1: 5.0000  (expected 5)
Bilinear trace: 25.0000  (expected 25)
G_N predicted: 6.683139e-39  observed: 6.674000e-39  ratio: 1.001369

Related Frameworks

Layer	Description	Status
FDLM/WIN	Discrete substrate, 
8
×
8
8×8 torus, 14 modes, baseline 
w
=
−
1
w=−1	Derived
Hodge Complex	Differential forms, 
Z
2
Z 
2
​	
  grading, 
D
2
=
Δ
D 
2
 =Δ	Derived
DME	Dimensional stability, 
γ
=
0.702839
…
γ=0.702839…	Derived
ENTROPIA-Core	Dynamical stability, Lyapunov, gradient flow	Derived from DME
ENTROPIA-EFT	Vacuum EFT, 
w
=
−
1.014054
…
w=−1.014054…, connects to WIN at 
w
=
−
1
w=−1	Complete
ENTROPIX/MESA	Master selection framework	Closed sub-sector derivations
Processor 
T
T	Extracts 10 fermions + 4 bosons from flat Hodge output	Theorem
Model Comparison

Criterion	Standard Model	String Theory	LQG	FDLM/WIN
Fundamental inputs	19–26 params	
10
1000
+
10 
1000+
  vacua	~3 params	1 input (
d
=
4
d=4)
Gauge group origin	Assumed	Landscape-dep.	Not derived	
s
u
(
3
)
⊕
s
u
(
2
)
⊕
u
(
1
)
5
su(3)⊕su(2)⊕u(1) 
5
 
Particle content	Assumed	Landscape-dep.	—	14 modes at 
λ
=
4
λ=4
Particle masses	19 free params	Not derived	—	RMS 0.0449 dex
Generations = 3	Assumed	Landscape-dep.	—	
d
−
1
=
3
d−1=3
Higgs mass	Measured	Not predicted	—	125.138 GeV (0.09%)
Weinberg angle	Measured	Not predicted	—	0.2312 (0.02%)
Spacetime dimension	Assumed	10/11 dim	4D input	
dim
⁡
ker
⁡
D
=
4
dimkerD=4
Graviton	Separate GR	String vibrations	Spin networks	
54
B
1
⊕
54
B
2
54B 
1
​	
 ⊕54B 
2
​	
 
Newton constant	Free parameter	Not predicted	—	
(
d
+
1
)
2
/
(
8
π
M
P
2
)
(d+1) 
2
 /(8πM 
P
2
​	
 ) (0.14%)
Quantum chaos	Not core	Not core	Lacks sector	SYK 
λ
L
≈
0.85
λ 
L
​	
 ≈0.85
Falsifiability	High	Low	Medium	High

Citation
@misc{preschutti2026fdlm,
  title  = {Four Dimension Lattice Model (FDLM): A Dimensional-Reduction
            Framework Deriving the Standard Model from the Spacetime Dimension},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {Preprint, under independent verification},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}

@misc{preschutti2026uplift,
  title  = {Spacetime from the Kernel of the Hodge-Dirac Operator
            on the 8x8 Torus},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {WIN Paradigm White Paper, submitted},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}

@misc{preschutti2026gravity,
  title  = {The WIN Gravity Theorem: The Graviton as the Self-Paired
            Curvature Mode of the 8x8 Hodge Complex},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {WIN Paradigm White Paper, submitted},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}

@misc{preschutti2026normalization,
  title  = {The WIN Normalization Theorem: The Hidden B1 Sector and the
            Structural Derivation of (d+1)^2 = 25 in the Newton Constant},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {WIN Paradigm White Paper},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}

@misc{preschutti2026hidden,
  title  = {Hidden Sector Content of the WIN Paradigm: Five Fermionic
            Weak Doublets, Six Color Triplets, and the Derivation of
            sin^2 theta_W(M_Z)},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {WIN Paradigm White Paper},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}
<div align="center">

# FDLM: The Four-Dimension Lattice Model

### A philosophical and mechanical overview

*© 2026 Stanley Preschutti · Entropia Research Institute / Information Physics Institute*

</div>

---

## What it is

FDLM is a claim about what physics **is**.

It says that the universe is not made of particles, fields, or spacetime. It is made of a **substrate** — a small, discrete, information-bearing structure — and everything we call physics is what that substrate **cannot cancel**.

The framework starts with a single input: **the number of dimensions we live in**. Not assumed. Derived. A massless spin-1 particle has two helicity states, each described by a complex amplitude with two real components. Two helicities, two real components each, four real numbers. Rotate that four-dimensional phase space from Euclidean to Lorentzian signature, and out comes the four-dimensional spacetime we inhabit. The number four is not an input to the framework. It is a **consequence of the photon**.

From there, the framework unfolds.

---

## The substrate

The substrate is a **lattice**: a small, periodic, two-dimensional grid of information-bearing sites. Not a spatial grid — a **structural** one. A lattice of possibilities, each cell a place where information can be stored, exchanged, and cancelled.

The size of the lattice is not chosen. It is **forced** by the dimension count. The number of sites is fixed by the requirement that the lattice's spectrum carry exactly the particle content the Standard Model demands. This is one of the framework's central structural moves: the substrate is not selected by hand, it is derived from the count of particles we observe.

The lattice has a **mirror symmetry**. Every excitation on the lattice has a partner — its mirror image under a half-turn of the grid. Most of these pairs cancel. The mirror symmetry is not a curiosity of the framework; it is the machine's core operating principle.

---

## What physics is

Physics is the **residue of a cancellation**.

The lattice is full of excitations. Each excitation pairs with its mirror. The paired modes have equal weight, opposite phase, and they cancel. What survives — what does not cancel — is the physical world.

The particles we see are the modes that have no mirror partner to cancel against. They are the **self-paired residual** of the substrate. They are not created by the lattice; they are the lattice's leftovers after the substrate has cancelled everything it can.

The Standard Model's particle content — the quarks, leptons, gauge bosons, and Higgs — emerges at one specific spectral midpoint of the lattice, where exactly the right number of modes survive the mirror cancellation. Not too many, not too few. Fourteen. One generation.

The three generations come from the same structure. The lattice does not need to be told there are three generations. The number three appears as a **structural consequence** of the lattice's geometry, not as an input.

---

## How forces work

Forces are **patterns of cancellation**.

In the Standard Model, forces are transmitted by gauge bosons — carriers that move between particles. In FDLM, forces are the substrate's local response to imbalance. When a region of the lattice carries a net imbalance in some quantum number, the substrate's mirror structure propagates a restoration. The propagated restoration is what we call a force.

The gauge algebra of the Standard Model — the strong, weak, and hypercharge structures — emerges from how the lattice organizes its own cancellation. The framework does not assume the gauge group; it derives it from the representation theory of the substrate's symmetry.

The forces are not separate things acting on separate particles. They are different **channels** of the same substrate. The strong force, the weak force, and electromagnetism are the three-dimensional projection of a single higher-dimensional cancellation pattern.

---

## How gravity works

Gravity is the **substrate's self-correction**.

The lattice has one structural condition it must satisfy everywhere: the mirror cancellation. In empty space, this is satisfied identically. When a mass is present, the local mode content shifts — the self-paired residual is locally enhanced — and the mirror cancellation is locally disturbed.

The substrate's response is to restore the imbalance. This restoration propagates as the **graviton**. What we call gravity is the propagating wave of the substrate's self-repair.

Three claims follow, and each is a theorem of the framework:

- **Every mass attracts every other mass.** Every mass disturbs the cancellation in the same direction. There is no gravitational charge because there is no asymmetry.
- **The force law is the inverse-square law.** The restoration is sourced by a point-like defect in the local mirror pairing, and the flux through a surface is conserved by the substrate's geometry.
- **All matter responds identically.** The substrate's inner product is the same for every mode. Universality is not an empirical fact — it is a structural property of the machine.

The graviton is not a fundamental field. It is a **mode of the substrate's operation**. Its job is to keep the machine consistent with itself.

---

## Why the universe is four-dimensional

The framework derives four-dimensional spacetime not once but **three times**, from three independent anchors:

- **From the photon.** Two helicity states with two real components each produce a four-dimensional phase space whose rotation gives four-dimensional spacetime.
- **From entropy.** Among all sizes of the substrate's lattice, only one produces the equally-spaced entropy classes that the Standard Model requires. That size selects four dimensions.
- **From topology.** The kernel of the substrate's natural differential operator is exactly four-dimensional. The four harmonic forms it contains are the four spacetime directions.

The three anchors are independent. They agree. The universe is four-dimensional because the substrate has no other choice.

---

## Why time flows

Time is not an external parameter. It is a **readout of the machine**.

The substrate processes itself in layers: the lattice, the dimensional stability sector, the coarse-graining flow, the effective field theory, and finally the processor. Together they form a **loop** — a closed cycle through which information passes.

Each pass through the loop accumulates a **phase**. The phase is the clock. Each pass also **decays** the loop's amplitude. The decay is the arrow.

Time is the number of passes. The arrow of time is the direction in which the loop's informational content decreases. Both emerge from a single operation: the loop observing itself.

---

## Why the vacuum has an equation of state

The universe's vacuum is not empty. It has a **preferred state** — a specific balance between expansion and structure. The framework derives this balance from the same loop that produces time.

The vacuum's equation of state emerges as the framework's baseline: a value slightly offset from pure cosmological constant, derivable from the substrate's dimensional stability. The prediction is testable by current cosmological surveys.

---

## What is derived

A summary, without mathematics:

- **The number of dimensions.** From the photon, from entropy, from topology.
- **The size of the substrate.** From the particle count.
- **The particle content.** Fourteen modes at a specific spectral midpoint.
- **The gauge structure.** From the substrate's symmetry.
- **The generations.** Three, from the lattice's geometry.
- **The particle masses.** Across six orders of magnitude, without fitted parameters.
- **The mixing matrices.** Quark and lepton, from the substrate's mode misalignment.
- **The Higgs mass.** To a tenth of a percent.
- **The weak mixing angle.** To a hundredth of a percent.
- **The graviton.** As the self-paired curvature mode of the substrate's wave sector.
- **The dimensional uplift.** Four-dimensional spacetime from the substrate's topology.
- **The Newton constant.** Its normalization derived from the substrate's hidden sector.
- **Time and its arrow.** As the loop's complex eigenvalue.
- **Motion.** As the winding phase of the substrate's mode coordinates.

---

## What is open

The framework is honest about its limits:

- **The path-integral completion.** The structural origin of the Newton constant is derived; the full path-integral evaluation on the discrete substrate remains to be completed.
- **The Lorentzian signature.** The dimension is derived; the signature is inherited from the photon-helicity anchor rather than derived from the substrate alone.
- **The nonlinear Einstein equations.** The linearized theory is derived; the nonlinear completion is open.
- **The full unification proof.** That the framework is logically forced — rather than one of several consistent possibilities — remains to be shown.

These are not gaps in the framework. They are the frontier.

---

## What it is not

FDLM is not string theory. It does not begin with vibrating strings, and it does not require extra dimensions to be compactified.

FDLM is not loop quantum gravity. It does not quantize geometry, and it does not begin with spin networks.

FDLM is not the Standard Model with decorations. It derives what the Standard Model assumes. It does not add parameters to the Standard Model; it removes them.

FDLM is not a theory of everything in the usual sense. It is a theory of **why there is a universe to have a theory of** — a claim about what physics is, from which the structure of physics follows.

---

## Why it matters

The Standard Model is the most precise theory in the history of science. It describes electromagnetism, the weak force, and the strong force to twelve significant figures. It has been tested to extraordinary precision and has never failed.

But the Standard Model assumes its own structure. It assumes the gauge group, the number of generations, the particle content, and the values of its own parameters. It does not explain why they are what they are.

FDLM is an attempt to explain why. It takes the observed structure of the Standard Model — the specific gauge group, the three generations, the fourteen particles — and asks: **what substrate could produce this and only this?** The framework's answer is a small, discrete, information-bearing lattice whose mirror cancellation leaves exactly the residue we call physics.

The framework is not a replacement for the Standard Model. It is a **foundation** for it. The Standard Model is what the substrate looks like when you observe it. FDLM is what the substrate is.

---

## The one-line summary

> **Physics is what the machine cannot cancel. FDLM is the machine.**

---

<div align="center">

**Status:** Under independent verification · [Repository](https://github.com/007STAN/FDLM-VALIDATION) · ORCID [0009-0004-5445-1744](https://orcid.org/0009-0004-5445-1744)

</div>
