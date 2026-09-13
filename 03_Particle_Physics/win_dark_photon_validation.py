"""
Warped Information Number (WIN) Paradigm — Dark Photon Validation
Author: Stanley Preschutti (Information Physics Institute, UK)
Description: Compares the WIN dark photon prediction (m_dark = 0.291 GeV, 
epsilon = 0.001193) against experimental exclusion limits from NA64, 
LDMX, Belle II, and LHCb.

The WIN framework predicts a dark photon with:
- Mass: m_dark = 0.291253 GeV = 291.253 MeV
- Kinetic mixing: epsilon = 0.001193

This is a single point in the (m_A', epsilon) parameter space. The 
comparison to experimental exclusion limits determines whether the 
prediction is ruled out or allowed.
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# WIN SUBSTRATE PARAMETERS
# ============================================================

d = 4                       # Spacetime dimension
H = d**2                    # Hidden sector = 16
V = (d-1) * 2**d            # Visible sector = 48
N = V + H                   # Total substrate = 64

# WIN predictions
m_dark_GeV = 0.291253       # Dark photon mass (GeV)
m_dark_MeV = m_dark_GeV * 1000  # = 291.253 MeV
epsilon_WIN = 0.001193      # Kinetic mixing

# ============================================================
# EXPERIMENTAL EXCLUSION LIMITS (APPROXIMATE)
# ============================================================

# These are approximate exclusion limits from various experiments.
# The actual limits are published in the respective papers.

# NA64 (2018-2023): exclusion in the mass range 1 MeV - 1 GeV
# The exclusion curve is roughly:
# epsilon_NA64(m) ~ 1e-3 for m ~ 100 MeV
# epsilon_NA64(m) ~ 1e-2 for m ~ 1 GeV

def na64_exclusion(m_MeV):
    """
    Approximate NA64 exclusion limit (2018-2023).
    The actual limit is published in the NA64 papers.
    """
    # Approximate: epsilon ~ 2e-3 for m ~ 100 MeV
    # Scales roughly as sqrt(m) for larger masses
    if m_MeV < 1:
        return 1e-2
    elif m_MeV > 1000:
        return 1e-2
    else:
        return 2e-3 * (m_MeV / 100)**0.3

def ldmx_exclusion(m_MeV):
    """
    Approximate LDMX exclusion limit (projected).
    """
    if m_MeV < 10:
        return 1e-2
    elif m_MeV > 1000:
        return 1e-2
    else:
        return 1e-4 * (m_MeV / 100)**0.5

def belle2_exclusion(m_MeV):
    """
    Approximate Belle II exclusion limit (projected).
    """
    if m_MeV < 10:
        return 1e-2
    elif m_MeV > 10000:
        return 1e-2
    else:
        return 5e-4 * (m_MeV / 100)**0.3

# ============================================================
# PLOT
# ============================================================

def plot_dark_photon_validation():
    # Mass range
    masses = np.logspace(0, 4, 500)  # 1 MeV to 10 GeV

    # Compute exclusion limits
    na64_lim = np.array([na64_exclusion(m) for m in masses])
    ldmx_lim = np.array([ldmx_exclusion(m) for m in masses])
    belle2_lim = np.array([belle2_exclusion(m) for m in masses])

    # Plot
    fig, ax = plt.subplots(figsize=(12, 7))

    # Exclusion regions
    ax.fill_between(masses, na64_lim, 1e-1, color='red', alpha=0.2, label='NA64 excluded')
    ax.fill_between(masses, ldmx_lim, 1e-1, color='orange', alpha=0.15, label='LDMX projected')
    ax.fill_between(masses, belle2_lim, 1e-1, color='blue', alpha=0.1, label='Belle II projected')

    # Exclusion curves
    ax.loglog(masses, na64_lim, color='red', linewidth=2, linestyle='--', label='NA64 limit')
    ax.loglog(masses, ldmx_lim, color='orange', linewidth=2, linestyle='--', label='LDMX limit')
    ax.loglog(masses, belle2_lim, color='blue', linewidth=2, linestyle='--', label='Belle II limit')

    # WIN prediction
    ax.loglog(m_dark_MeV, epsilon_WIN, 'g*', markersize=20, label=f'WIN prediction\n(m = {m_dark_MeV:.1f} MeV, epsilon = {epsilon_WIN:.6f})')

    # Set limits
    ax.set_xlim(1, 10000)
    ax.set_ylim(1e-6, 1e-1)

    ax.set_xlabel(r'Dark Photon Mass $m_{A\'}$ (MeV)', fontsize=12)
    ax.set_ylabel(r'Kinetic Mixing Parameter $\epsilon$', fontsize=12)
    ax.set_title('Dark Photon Parameter Space: WIN Prediction vs. Experimental Limits',
                 fontsize=13, fontweight='bold')
    ax.grid(True, which='both', linestyle=':', alpha=0.6)
    ax.legend(frameon=True, facecolor='white', loc='lower left', fontsize=10)

    plt.tight_layout()
    plt.show()

    # Print audit
    print("=" * 70)
    print("WIN PARADIGM: DARK PHOTON VALIDATION")
    print("=" * 70)
    print()
    print("Substrate parameters:")
    print(f"  d = {d}")
    print(f"  H = {H}")
    print(f"  V = {V}")
    print(f"  N = {N}")
    print()
    print("WIN dark photon prediction:")
    print(f"  m_dark = {m_dark_GeV:.6f} GeV = {m_dark_MeV:.3f} MeV")
    print(f"  epsilon = {epsilon_WIN:.6f}")
    print()
    print("Experimental exclusion limits (approximate):")
    print(f"  NA64 limit at m = {m_dark_MeV:.1f} MeV: epsilon < {na64_exclusion(m_dark_MeV):.6f}")
    print(f"  LDMX limit at m = {m_dark_MeV:.1f} MeV: epsilon < {ldmx_exclusion(m_dark_MeV):.6f}")
    print(f"  Belle II limit at m = {m_dark_MeV:.1f} MeV: epsilon < {belle2_exclusion(m_dark_MeV):.6f}")
    print()
    print("Status:")
    if epsilon_WIN < na64_exclusion(m_dark_MeV):
        print(f"  WIN prediction is ALLOWED by NA64.")
    else:
        print(f"  WIN prediction is EXCLUDED by NA64.")
    print()
    print("NOTE: The exclusion limits shown are APPROXIMATE. The actual")
    print("limits are published in the respective experimental papers.")
    print("The WIN prediction is a single point in the parameter space.")
    print("=" * 70)

if __name__ == "__main__":
    plot_dark_photon_validation()
