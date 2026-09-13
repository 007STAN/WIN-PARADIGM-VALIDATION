"""
Warped Information Number (WIN) Paradigm — Observational Cosmology Validation
Author: Stanley Preschutti (Information Physics Institute, UK)
Status: CORRECTED Sept 13, 2026 — falsified correction removed.

============================================================================
TRIPWIRE NOTICE
============================================================================
The previous version of this widget applied a correction:
    ε(z) = (H/N) · (1 − H₀²/H(z)²)
    Ω_m_WIN(z) = Ω_m_LCDM(z) · (1 + ε(z))

This correction is FALSIFIED. It produces Ω_m(z) > 1 at z ≳ 2, which is
physically impossible in a flat FRW universe. The widget no longer applies
any correction. If a future correction is proposed, it MUST satisfy:
    Ω_m(z) ≤ 1 for all z ≥ 0
and MUST be derived from the WIN substrate, not invented.

See: WIN Research — Sept 13, 2026, Section 5.3 (dark photon falsification
analogous: formulas that don't compute must be retracted, not rationalized).
============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# WIN SUBSTRATE PARAMETERS (from Sept 13 paper)
# ============================================================

d = 4                       # Spacetime dimension (input)
H = 2**d                    # Hidden sector = 16  [FIXED: was d**2]
V = (d - 1) * 2**d          # Visible sector = 48
N = V + H                   # Total substrate = 64

# Derived kL from the Sept 13 paper:
#   kL = N·(d−1)/(d+1) + sin²θ_W / [5.6 − d/(d+1)²]
# with sin²θ_W = 0.23135 (framework prediction)
sin2_theta_W = 0.23135
kL_derived = N * (d - 1) / (d + 1) + sin2_theta_W / (5.6 - d / (d + 1)**2)

# Observed value for comparison
kL_observed = 38.442488

# TRIPWIRE: kL derivation must match observation to < 0.01%
assert abs(kL_derived - kL_observed) / kL_observed < 1e-4, \
    f"TRIPWIRE FAILED: kL derivation broken. Derived={kL_derived}, Observed={kL_observed}"

# ============================================================
# UNEXPLAINED CONSTANTS — FLAGGED, NOT USED
# ============================================================

# The following constants appeared in the previous version but are NOT
# derived in any of the four Sept 13 papers. They are retained here as
# placeholders pending derivation. DO NOT use them in any calculation
# until their origin is established.
#
# gamma_MESA = 0.542133     # "7D MESA minimum" — NO DERIVATION FOUND
# lambda_L   = 0.85         # "chaos bound" — NO DERIVATION FOUND
# Delta_tax  = (1 - gamma_MESA) * (lambda_L / 2)  # AD HOC — NOT DERIVED
# w_WIN      = -1 + Delta_tax                      # AD HOC — NOT DERIVED

# If you wish to use these, you MUST first derive them from d=4, N, H, V.
# Until then, this widget does NOT make a dark-energy prediction.

# ============================================================
# ΛCDM BASELINE (Planck 2018)
# ============================================================

OMEGA_M0 = 0.315
OMEGA_L0 = 0.685

def lcdm_matter(z):
    """Standard ΛCDM matter density parameter Ω_m(z)."""
    H_z_sq = OMEGA_M0 * (1 + z)**3 + OMEGA_L0
    return (OMEGA_M0 * (1 + z)**3) / H_z_sq

def lcdm_dark_energy(z):
    """Standard ΛCDM dark energy density parameter Ω_Λ(z)."""
    H_z_sq = OMEGA_M0 * (1 + z)**3 + OMEGA_L0
    return OMEGA_L0 / H_z_sq

# ============================================================
# WIN PREDICTION — ONLY IF DERIVED
# ============================================================

def win_matter(z):
    """
    WIN-corrected matter density.

    STATUS: OPEN PROBLEM. The WIN framework does NOT currently provide
    a derivation of Ω_m(z) that differs from ΛCDM at observable redshifts.
    The previous widget's correction is falsified (produces Ω_m > 1).

    Until a derivation is provided, WIN reduces to ΛCDM at the background level.
    """
    return lcdm_matter(z)

# ============================================================
# VALIDATION
# ============================================================

def run_cosmology_validation():
    z = np.linspace(0, 3.0, 200)
    lcdm_vals = lcdm_matter(z)
    win_vals = win_matter(z)

    print("=" * 70)
    print("WIN PARADIGM: COSMOLOGICAL BACKGROUND AUDIT")
    print("=" * 70)
    print()
    print("Substrate parameters (from d = 4):")
    print(f"  d = {d}")
    print(f"  H = 2^d = {H}  [FIXED: was d**2]")
    print(f"  V = (d-1)·2^d = {V}")
    print(f"  N = V + H = {N}")
    print()
    print("Warp factor (DERIVED, not input):")
    print(f"  kL_derived  = {kL_derived:.6f}")
    print(f"  kL_observed = {kL_observed:.6f}")
    print(f"  Error       = {abs(kL_derived - kL_observed)/kL_observed * 100:.4f}%")
    print(f"  TRIPWIRE:   PASSED")
    print()
    print("STATUS: The previous WIN cosmological correction is FALSIFIED.")
    print("  Reason: ε(z) = (H/N)·(1 − H₀²/H(z)²) produces Ω_m(z) > 1 at z ≳ 2.")
    print("  Action: Correction removed. WIN reduces to ΛCDM at background level")
    print("          until a derivation is provided.")
    print()
    print("-" * 70)
    print(f"{'z':<8} | {'Ω_m ΛCDM':<12} | {'Ω_Λ ΛCDM':<12} | {'Ω_m WIN':<12} | {'Physical?'}")
    print("-" * 70)
    for z_val in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        om = lcdm_matter(z_val)
        ol = lcdm_dark_energy(z_val)
        ow = win_matter(z_val)
        physical = "YES" if ow <= 1.0 else "NO — FALSIFIED"
        print(f"{z_val:<8.1f} | {om:<12.6f} | {ol:<12.6f} | {ow:<12.6f} | {physical}")
    print("-" * 70)
    print()
    print("NOTE: No observational data (Planck, Euclid, BAO, SNe) is loaded.")
    print("      This widget validates the FRAMEWORK's internal consistency only.")
    print("      A data-comparison widget requires real likelihood code.")
    print("=" * 70)

    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.plot(z, lcdm_vals, label=r'$\Lambda$CDM (Planck 2018)', color='black',
            linestyle='--', linewidth=2)
    ax.plot(z, win_vals, label='WIN (no correction — falsified correction removed)',
            color='#2ca02c', linewidth=2.5, alpha=0.7)
    ax.axhline(y=1.0, color='red', linestyle=':', alpha=0.5,
               label='Physical bound Ω_m ≤ 1')
    ax.set_xlabel('Redshift z', fontsize=11)
    ax.set_ylabel(r'Matter Density Parameter $\Omega_m(z)$', fontsize=11)
    ax.set_title('WIN vs. ΛCDM Matter Density — Falsified Correction Removed',
                 fontsize=12, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(frameon=True, facecolor='white')
    ax.set_ylim(0, 1.05)
    plt.tight_layout()
    plt.show()

    return z, lcdm_vals, win_vals

if __name__ == "__main__":
    run_cosmology_validation()
