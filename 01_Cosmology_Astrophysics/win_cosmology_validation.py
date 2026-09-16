# ============================================================
# WIN PARADIGM — COSMOLOGICAL BACKGROUND: REVISED TREATMENT
# ============================================================
"""
Author: Stanley Preschutti (Entropia Research Institute / Information Physics Institute)
ORCID:  0009-0004-5445-1744
Status: REVISED September 16, 2026

============================================================================
PURPOSE
============================================================================
The previous WIN cosmological correction,

    epsilon(z) = (H/N) * (1 - H0^2 / H(z)^2)
    Omega_m_WIN(z) = Omega_m_LCDM(z) * (1 + epsilon(z))

was falsified (it produces Omega_m > 1 at z >~ 2, unphysical in a
flat FRW universe, and it was an ansatz not derived from the WIN
substrate).

This script re-derives the WIN cosmological background from the
substrate properties directly, without the failed ansatz. The key
inputs are:

  - The 8x8 torus substrate (derived from d = 4)
  - The 14-mode multiplet at lambda = 4 (derived)
  - The residual of the self-canceling vacuum: 28 out of 128, i.e. 7/32
  - The charge -1 per cell
  - The coupling J = kL/N

The revision has four parts:

  1. Falsification record (retained, correctly labeled)
  2. Substrate vacuum energy: derive the residual density from 7/32
  3. Expansion from the residual: check whether WIN reduces to LCDM
     at observable redshifts
  4. Open problems: what the framework does NOT yet provide
============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# SUBSTRATE PARAMETERS (from d = 4)
# ============================================================
d = 4
H_sector = 2**d              # 16
V_sector = (d - 1) * 2**d    # 48
N = V_sector + H_sector      # 64
L = 8
kL = 38.442527

# Derived quantities from the 8x8 torus
residual_fraction = 7 / 32   # 28 of 128 zero-point units survive
total_ZP = 128
residual_ZP = 28
charge_per_cell = -1

# ============================================================
# FALSIFIED CORRECTION (retained for the record)
# ============================================================
"""
The prior correction:

    epsilon(z) = (H_sector / N) * (1 - H0^2 / H(z)^2)

with H_sector / N = 16/64 = 1/4, was falsified because:

  1. At large z, 1 - H0^2/H(z)^2 -> 1, so epsilon -> 1/4.
  2. Omega_m_LCDM(z) * (1 + 1/4) exceeds 1 for z >~ 2.
  3. The ansatz was not derived from the WIN substrate.

The correction is shown for historical comparison only.
"""

OMEGA_M0 = 0.315
OMEGA_L0 = 0.685

def lcdm_matter(z):
    H_z_sq = OMEGA_M0 * (1 + z)**3 + OMEGA_L0
    return (OMEGA_M0 * (1 + z)**3) / H_z_sq

def lcdm_dark_energy(z):
    H_z_sq = OMEGA_M0 * (1 + z)**3 + OMEGA_L0
    return OMEGA_L0 / H_z_sq

def falsified_epsilon(z):
    """FALSIFIED correction. Shown for comparison only."""
    capacity_ratio = 1.0 / (OMEGA_M0 * (1 + z)**3 + OMEGA_L0)
    return (H_sector / N) * (1 - capacity_ratio)

def falsified_win_matter(z):
    return lcdm_matter(z) * (1 + falsified_epsilon(z))

# ============================================================
# PART 2: SUBSTRATE VACUUM ENERGY FROM 7/32
# ============================================================
"""
The self-canceling vacuum leaves a residual of 7/32 of the naive
zero-point sum. In natural units (Planck scale = 1), the naive
zero-point energy density of the substrate is of order the
Planck density. The residual after cancellation is:

    rho_WIN = (7/32) * rho_naive

If the substrate is the entire vacuum and rho_naive is the naive
Planck-scale zero-point density, this gives a residual that is
7/32 of the Planck density — about 22%. That is far too large
to match the observed cosmological constant.

However, the "naive" density is not the Planck density. It is the
density set by the substrate's own scale, which is the warp
factor. The warp factor kL = 38.44 is the logarithm of the
Planck-to-electroweak hierarchy. In warped-space scenarios, the
effective vacuum energy is suppressed by exp(-2*kL):

    rho_WIN = (7/32) * M_Planck^4 * exp(-2*kL)

We evaluate this and compare to the observed cosmological
constant.
"""

M_Planck_GeV = 1.22e19  # GeV
M_Planck_4 = M_Planck_GeV**4
warp_suppression = np.exp(-2 * kL)

rho_naive = M_Planck_4
rho_residual = (7 / 32) * rho_naive
rho_warped = (7 / 32) * rho_naive * warp_suppression

# Convert to GeV^4 (already done)
# Observed cosmological constant density in GeV^4
# rho_Lambda_obs ~ 2.5e-47 GeV^4 (from Planck 2018)
rho_Lambda_obs = 2.5e-47

print("=" * 78)
print("PART 2: SUBSTRATE VACUUM ENERGY FROM 7/32")
print("=" * 78)
print()
print(f"  Naive Planck zero-point density: {rho_naive:.4e} GeV^4")
print(f"  Residual fraction (7/32):        {residual_fraction:.4f}")
print(f"  rho_residual (no warping):       {rho_residual:.4e} GeV^4")
print(f"  Warp suppression exp(-2*kL):     {warp_suppression:.4e}")
print(f"  rho_warped:                      {rho_warped:.4e} GeV^4")
print()
print(f"  Observed Lambda density:         {rho_Lambda_obs:.4e} GeV^4")
print(f"  Ratio (warped/observed):         "
      f"{rho_warped / rho_Lambda_obs:.4e}")
print()
print("  The warped residual is not yet in agreement with the observed")
print("  cosmological constant. The suppression factor exp(-2*kL) = "
      f"{warp_suppression:.3e}")
print("  is not small enough. A different suppression mechanism (e.g.,")
print("  exp(-kL^2), exp(-N*kL/d), or an additional geometric factor)")
print("  would be required. This is an OPEN PROBLEM.")
print()

# ============================================================
# PART 3: EXPANSION FROM THE RESIDUAL
# ============================================================
"""
The WIN residual gives a constant vacuum energy density (the
substrate is static and the residual is fixed by the geometry).
This corresponds to a cosmological constant.

The Friedmann equation for a flat FRW universe with matter and
a cosmological constant is:

    H(z)^2 = H0^2 * [Omega_m0 * (1+z)^3 + Omega_Lambda0]

This is identical to LCDM. So if the WIN residual contributes a
constant vacuum energy, the expansion history is LCDM at the
background level.

The question is whether the WIN framework predicts any
deviation from LCDM at observable redshifts. The answer, as
established by the falsification of the earlier ansatz, is:

    NOT YET.

The framework currently reduces to LCDM at the background level.
Any WIN-specific prediction must come from:
  - Perturbations (structure growth, CMB)
  - A derived time-variation of the vacuum energy
  - A derived coupling to matter

None of these are currently in the framework.
"""

def win_matter(z):
    """WIN matter density. Currently reduces to LCDM."""
    return lcdm_matter(z)

def win_dark_energy(z):
    """WIN dark energy density. Currently reduces to LCDM."""
    return lcdm_dark_energy(z)

# ============================================================
# PART 4: OPEN PROBLEMS
# ============================================================
"""
The following are open problems in WIN cosmology:

1. Derivation of the vacuum energy magnitude.
   The 7/32 residual is derived. The overall scale (why ~10^-47
   GeV^4 rather than 10^76 GeV^4) is not derived. The warp
   suppression exp(-2*kL) is not sufficient.

2. Time-variation of the vacuum energy.
   The substrate is static. If the Wick angle evolves (see
   the processor white paper), the vacuum energy might have a
   time-dependent component. This is unobservable at current
   precision but is a structural prediction.

3. Coupling to matter.
   If the mesh couples to matter beyond gravity, there could be
   a fifth-force signature. No such coupling is currently in
   the framework.

4. Perturbation growth.
   WIN derives the background. It does not yet derive the growth
   of structure. Whether the substrate modifies the growth factor
   is open.

5. CMB and BAO.
   The framework has no specific predictions for CMB peak
   positions or BAO scale. These are tests of any complete
   cosmology.

6. The 7/32 residual vs the observed Lambda.
   Whether the 7/32 residual maps quantitatively to the observed
   cosmological constant is an open question. The current
   estimate (with exp(-2*kL) suppression) is off by many orders
   of magnitude.
"""

# ============================================================
# VALIDATION
# ============================================================
def run_cosmology_validation():
    z = np.linspace(0, 3.0, 200)
    lcdm_vals = lcdm_matter(z)
    win_vals = win_matter(z)
    falsified_vals = falsified_win_matter(z)

    print("=" * 78)
    print("WIN PARADIGM: COSMOLOGICAL BACKGROUND — REVISED TREATMENT")
    print("=" * 78)
    print()
    print("Substrate parameters (from d = 4):")
    print(f"  d = {d}")
    print(f"  H_sector = 2^d = {H_sector}")
    print(f"  V_sector = (d-1)*2^d = {V_sector}")
    print(f"  N = V_sector + H_sector = {N}")
    print(f"  L = {L} (8x8 torus)")
    print(f"  kL = {kL}")
    print()
    print("Derived quantities from the 8x8 torus:")
    print(f"  Total zero-point units: {total_ZP}")
    print(f"  Residual zero-point units: {residual_ZP}")
    print(f"  Residual fraction: {residual_fraction:.4f} = 7/32")
    print(f"  Charge per cell: {charge_per_cell}")
    print()
    print("-" * 78)
    print(f"{'z':<8} | {'Omega_m LCDM':<14} | {'Omega_L LCDM':<14} | "
          f"{'Omega_m FALSIFIED':<18} | Physical?")
    print("-" * 78)
    for z_val in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        om = lcdm_matter(z_val)
        ol = lcdm_dark_energy(z_val)
        ow = falsified_win_matter(z_val)
        physical = "YES" if ow <= 1.0 else "NO - FALSIFIED"
        print(f"{z_val:<8.1f} | {om:<14.6f} | {ol:<14.6f} | "
              f"{ow:<18.6f} | {physical}")
    print("-" * 78)
    print()
    print("STATUS:")
    print("  - WIN currently reduces to LCDM at the background level.")
    print("  - The falsified correction has been removed.")
    print("  - A derivation of the vacuum energy magnitude is OPEN.")
    print("  - A derivation of cosmological observables is OPEN.")
    print()

    # Plot: three panels
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

    # Panel 1: Falsified correction
    ax = axes[0]
    ax.plot(z, lcdm_vals, label='LCDM', color='black',
            linestyle='--', linewidth=2)
    ax.plot(z, falsified_vals, label='FALSIFIED (removed)',
            color='#d62728', linewidth=2, alpha=0.6)
    ax.axhline(y=1.0, color='red', linestyle=':', alpha=0.7,
               label='Physical bound')
    ax.fill_between(z, 1.0, 1.5, where=(falsified_vals > 1.0),
                    color='red', alpha=0.15, label='Unphysical')
    ax.set_xlabel('Redshift z', fontsize=11)
    ax.set_ylabel(r'$\Omega_m(z)$', fontsize=11)
    ax.set_title('Falsified correction vs physical bound',
                 fontsize=12, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(frameon=True, facecolor='white', loc='upper left')
    ax.set_ylim(0, 1.5)

    # Panel 2: Revised WIN (reduces to LCDM)
    ax = axes[1]
    ax.plot(z, lcdm_vals, label='LCDM', color='black',
            linestyle='--', linewidth=2)
    ax.plot(z, win_vals, label='WIN (revised)', color='#2E8B57',
            linewidth=2)
    ax.axhline(y=1.0, color='red', linestyle=':', alpha=0.7)
    ax.set_xlabel('Redshift z', fontsize=11)
    ax.set_ylabel(r'$\Omega_m(z)$', fontsize=11)
    ax.set_title('Revised WIN: reduces to LCDM',
                 fontsize=12, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(frameon=True, facecolor='white', loc='upper right')
    ax.set_ylim(0, 1.1)

    # Panel 3: Residual energy scale
    ax = axes[2]
    scales = {
        "Naive Planck": rho_naive,
        "7/32 residual": rho_residual,
        "7/32 * exp(-2kL)": rho_warped,
        "Observed Lambda": rho_Lambda_obs,
    }
    names = list(scales.keys())
    values = list(scales.values())
    colors_bar = ['#888888', '#4C72B0', '#55A868', '#C44E52']
    ax.barh(names, values, color=colors_bar,
            edgecolor='black', linewidth=1)
    ax.set_xscale('log')
    ax.set_xlabel(r'Energy density [GeV$^4$]', fontsize=11)
    ax.set_title('Vacuum energy scales (log)',
                 fontsize=12, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6, axis='x')
    for i, v in enumerate(values):
        ax.text(v * 1.5, i, f'{v:.1e}', va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig('cosmology_revised.png', dpi=150)
    plt.show()

    return z, lcdm_vals, win_vals, falsified_vals

if __name__ == "__main__":
    run_cosmology_validation()
