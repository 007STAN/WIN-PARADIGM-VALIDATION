# WIN Paradigm Proof Series: Experiment 1
## Weinberg Angle: Bare GUT Value + RGE Running + Warped Threshold

---

**Author:** Stanley Preschutti (Entropia Research Institute / Information Physics Institute)
**ORCID:** 0009-0004-5445-1744
**Date:** September 13, 2026
**Status:** Working document — result correct, derivation of Δ_kL open

---

### Status of the Derivation

This document computes the Weinberg angle at M_Z from three ingredients:

1. **Bare GUT value** `sin²θ_W = 3/8` — DERIVED from SO(10) trace (standard GUT).
2. **RGE running** `Δ_RGE = 0.16550` — STANDARD 1-loop SM physics (standard).
3. **Warped threshold** `Δ_kL = kL/(5.6π·100)` — WIN-SPECIFIC, FORMULA NOT DERIVED.

**Result:** `sin²θ_W(M_Z) = 0.23135`, vs. experimental `0.23122`. Error: **0.06%**.

**Honest position:** The bare value and RGE running are standard GUT physics. The warped threshold formula is WIN-specific but not derived. The result is a consistency check, not a first-principles prediction.

---

### Theoretical Context

Under the WIN Paradigm, quantum gauge fields and spacetime geometry emerge as
low-energy holographic projections of an underlying `N = 64` entropic
state-space substrate. Grand unification is a topological property of the
substrate tensor structure rather than an arbitrary gauge group choice.

At the UV boundary (`M_GUT ≈ 2.0 × 10^16 GeV`), the `N = 64` substrate
projects onto the `SO(10)` spinor representation (`16` chiral fermion states
per generation). This topological boundary condition fixes the unrenormalized
(bare) weak mixing angle to its Lie algebra trace value `sin²θ_W^bare = 3/8`.

As gauge fields evolve along the warped fifth dimension parameterized by the
bulk metric scale factor `kL`, the coupling constants undergo standard 1-loop
renormalization group evolution modified by a non-perturbative Kaluza-Klein
(KK) boundary threshold shift `Δ_kL`.

---

### Executive Summary

| Parameter | Bare UV Value | Warped RGE Prediction (M_Z) | Experimental PDG (M_Z) | Residual | Relative Error |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **sin²θ_W** | 3/8 = 0.37500 | **0.23135** | 0.23122 | 0.00013 | **0.06%** |

---

### 1. Step 1: Bare Lie Algebra Trace (Standard SO(10) Result)

At the holographic unification scale `M_GUT`, the bare electroweak mixing
angle is determined by the ratio of the gauge coupling constants, which
corresponds to the trace ratio of the weak isospin and electric charge
generators across one complete `16`-plet fermion generation:

sin²θ_W^bare = g'²/(g² + g'²) = Tr(I₃L²)/Tr(Q²)


where `Q = I₃L + Y`.

#### 1.1 Complete 16-Plet Quantum Number Assignment

| State | Color Dim (d_c) | I₃L | Y | Q = I₃L + Y | d_c·I₃L² | d_c·Q² |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| u_L | 3 | +1/2 | +1/6 | +2/3 | 3/4 | 4/3 |
| d_L | 3 | −1/2 | +1/6 | −1/3 | 3/4 | 1/3 |
| u_R | 3 | 0 | +2/3 | +2/3 | 0 | 4/3 |
| d_R | 3 | 0 | −1/3 | −1/3 | 0 | 1/3 |
| ν_L | 1 | +1/2 | −1/2 | 0 | 1/4 | 0 |
| e_L | 1 | −1/2 | −1/2 | −1 | 1/4 | 1 |
| e_R | 1 | 0 | −1 | −1 | 0 | 1 |
| ν_R | 1 | 0 | 0 | 0 | 0 | 0 |

#### 1.2 Exact Trace Evaluation

1. `Tr(I₃L²) = 3/4 + 3/4 + 0 + 0 + 1/4 + 1/4 + 0 + 0 = 2`
2. `Tr(Q²) = 4/3 + 1/3 + 4/3 + 1/3 + 0 + 1 + 1 + 0 = 16/3`
3. `sin²θ_W^bare = 2/(16/3) = 6/16 = 3/8 = 0.37500` ✅

**This is the standard SO(10) GUT result.**

---

### 2. Step 2: RGE Running to M_Z (Standard SM Physics)

#### 2.1 Renormalization Group Running Shift

The logarithmic scale distance between the unification boundary and the
electroweak scale:
t = ln(M_GUT/M_Z) = ln(2.0e16/91.1876) = 33.0217


Using Standard Model 1-loop beta function coefficients:

- `b₁ = 41/10` (U(1)_Y, GUT-normalized)
- `b₂ = −19/6` (SU(2)_L)

The one-loop RGE shift:
Δ_RGE = −(5b₂ − 4b₁)/(16π) · α_EM(M_Z) · t


Substituting `α_EM(M_Z) = 1/127.95`:
Δ_RGE = 0.16550


**Note:** The `t` value in Rev 1.0 was misprinted as 32.7188. The correct
value for `M_GUT = 2.0e16` is 33.0217. The `Δ_RGE` value (0.16550) is
correct for the corrected `t`.

#### 2.2 Substrate Boundary Threshold Correction (WIN-specific)

The finite volume of the warped 5D bulk introduces KK mode threshold effects
at the IR boundary. For `kL`, the leading-order warped threshold contribution
is proposed as:
Δ_kL = kL/(5.6π·100)


For `kL = 38.44`:

**Status:** The formula `Δ_kL = kL/(5.6π·100)` is WIN-specific but not
derived. The constants `5.6` and `100` are framework constants (see the kL
derivation document), but the *form* of the correction is an ansatz. Whether
it can be derived from the substrate structure is an open problem.

#### 2.3 Net Electroweak Prediction
sin²θ_W(M_Z) = 0.37500 − 0.16550 + 0.02185 = 0.23135


Compared against the PDG experimental value (`0.23122`):

- Absolute residual: `|0.23135 − 0.23122| = 0.00013`
- Relative error: `0.06%`

---

### 3. Status of the Derivation

**Established:**

1. The bare value `3/8` is derived from the `SO(10)` trace (standard GUT).
2. The RGE running `Δ_RGE = 0.16550` is standard 1-loop SM physics.
3. The combination `3/8 − Δ_RGE + Δ_kL = 0.23135` matches experiment to 0.06%.

**Not established:**

1. The warped threshold formula `Δ_kL = kL/(5.6π·100)` is not derived.
2. `M_GUT = 2.0e16` is an input, not derived.
3. `α_EM(M_Z) = 1/127.95` is an input, not derived.
4. `kL` is used as an input (see the kL derivation document for its status).

**Conclusion:** This is a **consistency check**, not a first-principles
prediction. The result is correct, but the derivation depends on several
inputs and one ansatz.

---

### 4. What Remains Open

1. **Derivation of `Δ_kL`.** Why `kL/(5.6π·100)`?
2. **Derivation of `M_GUT`.** Why `2.0e16 GeV`?
3. **Derivation of `α_EM(M_Z)`.** Standard SM input, but not derived from WIN.
4. **One-way derivation of `kL`.** See the kL derivation document.
5. **The `Δ_RGE` coefficient.** The specific combination `5b₂ − 4b₁` should be derived from the framework.

---

### 5. Summary

The Weinberg angle is computed as:
sin²θ_W(M_Z) = 3/8 − Δ_RGE + Δ_kL = 0.23135


where:
- `3/8` is the standard `SO(10)` GUT value (DERIVED)
- `Δ_RGE = 0.16550` is standard 1-loop RGE running (STANDARD SM)
- `Δ_kL = kL/(5.6π·100) = 0.02185` is a WIN-specific threshold correction (ANSATZ)

Experimental value: `0.23122 ± 0.00004`. Error: **0.06%**.

**This is a consistency check, not a first-principles prediction.** The
`Δ_kL` formula is not derived.

---

### 6. Reproducible Verification Script

```python
# ==============================================================================
# WIN PARADIGM PROOF: EXPERIMENT 1 (Rev 1.1)
# Target: Weinberg Angle — Bare GUT + RGE + Warped Threshold
# ==============================================================================

import numpy as np
from fractions import Fraction

def run_experiment_1():
    print("--- STEP 1: BARE LIE ALGEBRA TRACE (STANDARD SO(10)) ---")

    # 16-state chiral fermion generation: (Name, Multiplet_Dim, I3_L, Q)
    fermion_generation = [
        ("u_L", 3, Fraction(1, 2),  Fraction(2, 3)),
        ("d_L", 3, Fraction(-1, 2), Fraction(-1, 3)),
        ("u_R", 3, Fraction(0, 1),  Fraction(2, 3)),
        ("d_R", 3, Fraction(0, 1),  Fraction(-1, 3)),
        ("nu_L", 1, Fraction(1, 2),  Fraction(0, 1)),
        ("e_L",  1, Fraction(-1, 2), Fraction(-1, 1)),
        ("e_R",  1, Fraction(0, 1),  Fraction(-1, 1)),
        ("nu_R", 1, Fraction(0, 1),  Fraction(0, 1)),
    ]

    tr_I3_sq = sum(state[1] * (state[2]**2) for state in fermion_generation)
    tr_Q_sq = sum(state[1] * (state[3]**2) for state in fermion_generation)
    sin2_bare = tr_I3_sq / tr_Q_sq

    print(f"Tr(I_3L^2) across 16-plet = {tr_I3_sq}")
    print(f"Tr(Q^2)    across 16-plet = {tr_Q_sq}")
    print(f"Bare sin^2(theta_W)       = {tr_I3_sq} / {tr_Q_sq} = {float(sin2_bare):.5f}")

    assert sin2_bare == Fraction(3, 8), "Bare symmetry trace proof failed!"

    print("\n--- STEP 2: RGE RUNNING TO M_Z ---")

    M_GUT = 2.0e16              # Unification Scale (GeV)
    M_Z = 91.1876               # Electroweak Scale (GeV)
    alpha_EM_MZ = 1.0 / 127.95  # Fine-structure constant at M_Z
    kL = 38.44                  # Warped substrate scale factor

    # Beta function coefficients: b1 = 41/10 (GUT norm), b2 = -19/6
    b1, b2 = 41.0 / 10.0, -19.0 / 6.0
    t = np.log(M_GUT / M_Z)

    # 1-loop RGE running shift
    delta_RGE = -((5.0 * b2 - 4.0 * b1) / (16.0 * np.pi)) * alpha_EM_MZ * t

    # TRIPWIRE: t must be positive and match expected magnitude
    assert 32.0 < t < 34.0, f"t = {t} outside expected range"

    print(f"Log scale distance (t)            = {t:.4f}")
    print(f"RGE shift (Delta_RGE)             = {delta_RGE:.5f}")

    print("\n--- STEP 3: WARPED THRESHOLD (ANSATZ) ---")

    # Warped substrate threshold shift
    delta_kL = kL / (5.6 * np.pi * 100.0)

    print(f"Warped threshold (Delta_kL)       = {delta_kL:.5f}")
    print("STATUS: Delta_kL formula is an ansatz, not derived.")

    print("\n--- STEP 4: COMBINED RESULT ---")

    sin2_MZ = float(sin2_bare) - delta_RGE + delta_kL
    pdg_exp = 0.23122
    residual = abs(sin2_MZ - pdg_exp)
    rel_error = (residual / pdg_exp) * 100.0

    print(f"Calculated sin^2(theta_W) @ M_Z   = {sin2_MZ:.5f}")
    print(f"Experimental PDG Value @ M_Z      = {pdg_exp:.5f}")
    print(f"Absolute Residual                 = {residual:.5f}")
    print(f"Relative Error                    = {rel_error:.2f}%")

    assert residual < 2.0e-3, "Electroweak scale precision check failed!"
    print("\n>>> CONSISTENCY CHECK PASSED (0.06% ERROR).")

if __name__ == "__main__":
    run_experiment_1()

