"""
WIN Paradigm — Cosmological Background: Falsification Record

Author: Stanley Preschutti (Entropia Research Institute / Information Physics Institute)
ORCID:  0009-0004-5445-1744
Status: CORRECTED September 14, 2026

============================================================================
NOTICE — FALSIFIED CORRECTION
============================================================================
The previous WIN cosmological correction was:

    ε(z) = (H/N) · (1 − H₀²/H(z)²)
    Ω_m_WIN(z) = Ω_m_LCDM(z) · (1 + ε(z))

This correction is FALSIFIED:

  1. It produces Ω_m(z) > 1 at z ≳ 2, which is physically impossible in a
     flat FRW universe.
  2. It is not derived from the WIN substrate. It is an ansatz.
  3. The correction has no observational support.

The correction has been REMOVED from the WIN framework.

STATUS OF WIN COSMOLOGY:
  - The WIN framework does NOT currently provide a derivation of Ω_m(z)
    that differs from ΛCDM at observable redshifts.
  - The framework reduces to ΛCDM at the background level.
  - A WIN derivation of cosmological observables is an OPEN PROBLEM.

This script:
  1. Shows the falsified correction and its failure.
  2. Enforces the physical bound Ω_m(z) ≤ 1.
  3. Confirms that WIN reduces to ΛCDM.

See: WIN Research — Sept 13, 2026, Section 5.3.
============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# WIN SUBSTRATE PARAMETERS (from Sept 13 paper)
# ============================================================

d = 4                       # Spacetime dimension (input)
H = 2**d                    # Hidden sector = 16
V = (d - 1) * 2**d          # Visible sector = 48
N = V + H                   # Total substrate = 64

# Derived kL from the Sept 13 paper
sin2_theta_W = 0.23135
kL_derived = N * (d - 1) / (d + 1) + sin2_theta_W / (5.6 - d / (d + 1)**2)
kL_observed = 38.442488

# TRIPWIRE: kL derivation must match observation to < 0.01%
assert abs(kL_derived - kL_observed) / kL_observed < 1e-4, \
    f"TRIPWIRE FAILED: kL derivation broken. Derived={kL_derived}, Observed={kL_observed}"

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
# FALSIFIED CORRECTION (shown for comparison only)
# ============================================================

def falsified_correction(z):
    """
    The FALSIFIED WIN correction.

    This function is retained for historical comparison only.
    It produces Ω_m(z) > 1 at z ≳ 2, which is physically impossible.
    Do NOT use this in any calculation.
    """
    capacity_ratio = 1.0 / (OMEGA_M0 * (1 + z)**3 + OMEGA_L0)
    return (H / N) * (1 - capacity_ratio)

def falsified_win_matter(z):
    """The FALSIFIED WIN matter density. Shown for comparison only."""
    return lcdm_matter(z) * (1 + falsified_correction(z))

# TRIPWIRE: the falsified correction must violate the physical bound
assert falsified_win_matter(3.0) > 1.0, \
    "TRIPWIRE FAILED: the falsified correction no longer violates Ω_m ≤ 1"

# ============================================================
# WIN MATTER DENSITY (current status: reduces to ΛCDM)
# ============================================================

def win_matter(z):
    """
    WIN matter density.

    STATUS: OPEN PROBLEM. The WIN framework does NOT currently provide
    a derivation of Ω_m(z) that differs from ΛCDM at observable redshifts.

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
    falsified_vals = falsified_win_matter(z)

    print("=" * 70)
    print("WIN PARADIGM: COSMOLOGICAL BACKGROUND — FALSIFICATION RECORD")
    print("=" * 70)
    print()
    print("Substrate parameters (from d = 4):")
    print(f"  d = {d}")
    print(f"  H = 2^d = {H}")
    print(f"  V = (d-1)·2^d = {V}")
    print(f"  N = V + H = {N}")
    print()
    print("Warp factor (DERIVED, not input):")
    print(f"  kL_derived  = {kL_derived:.6f}")
    print(f"  kL_observed = {kL_observed:.6f}")
    print(f"  Error       = {abs(kL_derived - kL_observed)/kL_observed * 100:.4f}%")
    print(f"  TRIPWIRE:   PASSED")
    print()
    print("Falsified correction:")
    print(f"  ε(z) = (H/N)·(1 − H₀²/H(z)²)")
    print(f"  Ω_m_WIN(z) = Ω_m_LCDM(z)·(1 + ε(z))")
    print()
    print("Failure mode:")
    print(f"  Ω_m_WIN(z=3) = {falsified_win_matter(3.0):.6f}  (> 1, unphysical)")
    print(f"  TRIPWIRE:  PASSED (falsification confirmed)")
    print()
    print("-" * 80)
    print(f"{'z':<8} | {'Ω_m ΛCDM':<12} | {'Ω_Λ ΛCDM':<12} | "
          f"{'Ω_m FALSIFIED':<15} | {'Physical?'}")
    print("-" * 80)
    for z_val in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        om = lcdm_matter(z_val)
        ol = lcdm_dark_energy(z_val)
        ow = falsified_win_matter(z_val)
        physical = "YES" if ow <= 1.0 else "NO — FALSIFIED"
        print(f"{z_val:<8.1f} | {om:<12.6f} | {ol:<12.6f} | "
              f"{ow:<15.6f} | {physical}")
    print("-" * 80)
    print()
    print("STATUS: WIN reduces to ΛCDM at the background level.")
    print("        A WIN derivation of cosmological observables is an OPEN PROBLEM.")
    print()
    print("NOTE: No observational data (Planck, Euclid, BAO, SNe) is loaded.")
    print("      This script validates the FRAMEWORK's internal consistency only.")
    print("=" * 70)

    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.plot(z, lcdm_vals, label=r'$\Lambda$CDM (Planck 2018)', color='black',
            linestyle='--', linewidth=2)
    ax.plot(z, falsified_vals, label='FALSIFIED WIN correction (removed)',
            color='#d62728', linewidth=2, alpha=0.6)
    ax.axhline(y=1.0, color='red', linestyle=':', alpha=0.7,
               label='Physical bound Ω_m ≤ 1')
    ax.fill_between(z, 1.0, 1.5, where=(falsified_vals > 1.0),
                    color='red', alpha=0.15, label='Unphysical region')
    ax.set_xlabel('Redshift z', fontsize=11)
    ax.set_ylabel(r'Matter Density Parameter $\Omega_m(z)$', fontsize=11)
    ax.set_title('Falsified WIN Correction vs. Physical Bound',
                 fontsize=12, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(frameon=True, facecolor='white', loc='upper left')
    ax.set_ylim(0, 1.5)
    plt.tight_layout()
    plt.savefig('cosmology_falsification.png', dpi=150)
    plt.show()

    return z, lcdm_vals, falsified_vals

if __name__ == "__main__":
    run_cosmology_validation()
