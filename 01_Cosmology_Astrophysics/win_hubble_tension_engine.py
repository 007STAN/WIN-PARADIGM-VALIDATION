"""
Warped Information Number (WIN) Paradigm — Hubble Tension Analysis
Author: Stanley Preschutti (Information Physics Institute, UK)
Status: CORRECTED Sept 13, 2026 — falsified correction removed.

============================================================================
TRIPWIRE NOTICE
============================================================================
The previous version of this widget applied a correction:
    ΔH/H(z) = (H/N) · (1 − H₀²/H(z)²)

This correction is FALSIFIED for three reasons:

  1. It vanishes at z = 0, which is where the local H₀ measurement is made.
     To get any effect, the code had to fudge z_local = 0.01 — an arbitrary
     choice with no physical justification.

  2. Even with the fudge, the correction at z = 0.01 is ~0.024%, which closes
     only ~3% of the ~8.3% Hubble tension. The mechanism is ~350× too weak.

  3. The correction has no derivation from the WIN substrate. It is an ansatz.

Any future WIN correction to H(z) MUST:
  - Be derived from d=4, N, H, V (not invented).
  - Be non-zero at z = 0 if it claims to address the local measurement.
  - Have the correct sign to reconcile high-z and low-z measurements.
  - Be large enough to matter (~8% at z=0, or scale-dependent in a way that
    matches the observed tension profile).

See: WIN Research — Sept 13, 2026, Section 5.3 (falsified formulas must be
retracted, not rationalized).
============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

try:
    import ipywidgets as widgets
    from IPython.display import display, clear_output
    HAS_WIDGETS = True
except ImportError:
    HAS_WIDGETS = False
    print("NOTE: ipywidgets not available. Run interactively or install with:")
    print("      pip install ipywidgets")

# ============================================================
# WIN SUBSTRATE PARAMETERS (from Sept 13 paper)
# ============================================================

d = 4                       # Spacetime dimension (input)
H = 2**d                    # Hidden sector = 16  [FIXED: was d**2]
V = (d - 1) * 2**d          # Visible sector = 48
N = V + H                   # Total substrate = 64

# Derived kL
sin2_theta_W = 0.23135
kL_derived = N * (d - 1) / (d + 1) + sin2_theta_W / (5.6 - d / (d + 1)**2)
kL_observed = 38.442488

# TRIPWIRE: kL derivation must match observation
assert abs(kL_derived - kL_observed) / kL_observed < 1e-4, \
    f"TRIPWIRE FAILED: kL derivation broken."

# ============================================================
# COSMOLOGICAL MEASUREMENTS
# ============================================================

H_0_CMB = 67.4              # km/s/Mpc (Planck 2018)
H_0_CMB_err = 0.5
H_0_local = 73.0            # km/s/Mpc (SH0ES 2022)
H_0_local_err = 1.0

TENSION_PERCENT = (H_0_local - H_0_CMB) / H_0_CMB * 100  # ~8.3%

# ============================================================
# ΛCDM BASELINE
# ============================================================

OMEGA_M0 = 0.315
OMEGA_L0 = 0.685

def lcdm_H(z):
    """Standard ΛCDM Hubble parameter (in units of H_0)."""
    return np.sqrt(OMEGA_M0 * (1 + z)**3 + OMEGA_L0)

# ============================================================
# WIN PREDICTION — STATUS: OPEN PROBLEM
# ============================================================

def win_correction(z):
    """
    WIN correction to H(z).

    STATUS: OPEN PROBLEM. The WIN framework does NOT currently provide a
    derivation of a scale-dependent H(z) correction. The previous ansatz
    is falsified (see TRIPWIRE NOTICE above).

    This function returns zero — i.e., WIN reduces to ΛCDM — until a
    derivation is provided.
    """
    return np.zeros_like(np.asarray(z, dtype=float))

def win_H(z):
    """WIN Hubble parameter. Currently identical to ΛCDM."""
    return lcdm_H(z) * (1 + win_correction(z))

def required_correction_to_resolve():
    """
    What correction would be needed to resolve the Hubble tension?

    Returns the required ΔH/H at z = 0 to bring H_0_CMB up to H_0_local.
    """
    return (H_0_local - H_0_CMB) / H_0_CMB

# ============================================================
# DIAGNOSTIC OUTPUT
# ============================================================

def print_diagnostic():
    print("=" * 70)
    print("WIN PARADIGM: HUBBLE TENSION — DIAGNOSTIC")
    print("=" * 70)
    print()
    print("Substrate parameters:")
    print(f"  d = {d}")
    print(f"  H = 2^d = {H}  [FIXED: was d**2]")
    print(f"  V = (d-1)·2^d = {V}")
    print(f"  N = {N}")
    print(f"  kL (derived) = {kL_derived:.6f}  (observed: {kL_observed:.6f})")
    print()
    print("Observed tension:")
    print(f"  CMB (Planck 2018):  H_0 = {H_0_CMB:.2f} ± {H_0_CMB_err:.2f} km/s/Mpc")
    print(f"  Local (SH0ES 2022): H_0 = {H_0_local:.2f} ± {H_0_local_err:.2f} km/s/Mpc")
    print(f"  Tension:            {TENSION_PERCENT:.2f}% (~5σ)")
    print()
    print("WIN status:")
    print("  The previous WIN correction is FALSIFIED.")
    print("  Reasons:")
    print("    1. Vanishes at z=0 (where local measurement is made).")
    print("    2. Even with z=0.01 fudge, closes only ~3% of the tension.")
    print("    3. Not derived from the substrate.")
    print()
    print("Required correction to resolve tension:")
    print(f"  ΔH/H at z=0 must be ≥ {required_correction_to_resolve()*100:.2f}%")
    print(f"  (i.e., the local measurement is {required_correction_to_resolve()*100:.2f}% higher")
    print(f"   than the CMB baseline, and any WIN mechanism must bridge this.)")
    print()
    print("=" * 70)

def plot_diagnostic():
    z = np.logspace(-3, 4, 300)
    H_lcdm = lcdm_H(z)
    H_win = win_H(z)
    correction = win_correction(z)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Top: H(z)
    ax1.semilogx(z, H_lcdm * H_0_CMB, color='black', linestyle='--',
                 linewidth=2, label=f'ΛCDM (CMB baseline H₀={H_0_CMB})')
    ax1.semilogx(z, H_win * H_0_CMB, color='#2ca02c', linewidth=2.5,
                 alpha=0.7, label='WIN (no correction — falsified correction removed)')
    ax1.axhline(H_0_local, color='green', linestyle='-.', alpha=0.7,
                label=f'Local measurement H₀={H_0_local}')
    ax1.set_ylabel(r'$H(z)$ (km/s/Mpc)', fontsize=11)
    ax1.set_title('WIN Paradigm: Hubble Tension — Falsified Correction Removed',
                  fontsize=12, fontweight='bold')
    ax1.grid(True, which="both", linestyle=':', alpha=0.6)
    ax1.legend(loc='upper right', frameon=True, facecolor='white')

    # Bottom: correction
    ax2.semilogx(z, correction * 100, color='#d62728', linewidth=2.5)
    ax2.axhline(0, color='black', linestyle='--', alpha=0.5)
    ax2.axhline(required_correction_to_resolve() * 100, color='blue',
                linestyle=':', alpha=0.7,
                label=f'Required at z=0: {required_correction_to_resolve()*100:.2f}%')
    ax2.set_xlabel(r'Redshift $z$ (log scale)', fontsize=11)
    ax2.set_ylabel(r'$\Delta H / H$ (%)', fontsize=11)
    ax2.set_title('WIN Correction — Currently Zero (Open Problem)', fontsize=12,
                  fontweight='bold')
    ax2.grid(True, which="both", linestyle=':', alpha=0.6)
    ax2.legend(loc='upper right', frameon=True, facecolor='white')

    plt.tight_layout()
    plt.show()

# ============================================================
# INTERACTIVE WIDGET (if available)
# ============================================================

if HAS_WIDGETS:
    h_early_slider = widgets.FloatSlider(
        value=H_0_CMB, min=60.0, max=72.0, step=0.1,
        description='CMB baseline H₀:',
        style={'description_width': 'initial'}
    )
    out = widgets.Output()

    def update(h_early):
        with out:
            clear_output(wait=True)
            print(f"CMB baseline: {h_early:.2f} km/s/Mpc")
            print(f"Local measurement: {H_0_local:.2f} km/s/Mpc")
            print(f"Tension: {(H_0_local - h_early)/h_early*100:.2f}%")
            print()
            print("WIN correction at z=0: 0.00% (falsified mechanism removed)")
            print("WIN cannot currently resolve the Hubble tension.")
            print()
            print(f"Required correction: ≥ {(H_0_local - h_early)/h_early*100:.2f}% at z=0")

    display(widgets.interactive(update, h_early=h_early_slider), out)

if __name__ == "__main__":
    print_diagnostic()
    plot_diagnostic()
