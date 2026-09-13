"""
Warped Information Number (WIN) Paradigm — 5D Warped Hierarchy & Higgs Mass
Author: Stanley Preschutti (Information Physics Institute, UK)
Description: Interactive Colab widget for computing the 5D warped geometry 
hierarchy resolution (kL = 38.44) and the WIN Higgs mass prediction.

The WIN framework derives the Higgs mass from:
  m_H = sqrt(2 lambda_eff) × v_EW
where:
  lambda_tree = ln(kL) / (3 pi^2)
  lambda_eff = lambda_tree + 1/180
  v_EW = 246.22 GeV (calibration input)

The WIN prediction is m_H = 124.968 GeV, which matches experiment
(125.25 +/- 0.17 GeV) to 0.22%.

The KK graviton resonance is NOT currently derived from WIN principles.
"""

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import ipywidgets as widgets
except ImportError:
    install("ipywidgets")
    import ipywidgets as widgets

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# ============================================================
# WIN SUBSTRATE PARAMETERS
# ============================================================

d = 4                       # Spacetime dimension
H = d**2                    # Hidden sector = 16
V = (d-1) * 2**d            # Visible sector = 48
N = V + H                   # Total substrate = 64

# Calibration input
M_Planck = 1.220910e19      # Planck mass (GeV)
v_EW = 246.22               # Electroweak VEV (GeV)
kL_calibration = np.log(M_Planck / v_EW)  # = 38.44251

# ============================================================
# WIN HIGGS MASS DERIVATION
# ============================================================

def win_higgs_mass(kL):
    """
    Compute the WIN Higgs mass prediction.

    m_H = sqrt(2 lambda_eff) × v_EW

    where:
    lambda_tree = ln(kL) / (3 pi^2)
    lambda_eff = lambda_tree + 1/180
    """
    lambda_tree = np.log(kL) / (3 * np.pi**2)
    lambda_eff = lambda_tree + 1/180
    m_H = np.sqrt(2 * lambda_eff) * v_EW
    return m_H, lambda_tree, lambda_eff

def hierarchy_suppression(kL):
    """Compute the hierarchy suppression factor exp(-kL)."""
    return np.exp(-kL)

# ============================================================
# WIDGET
# ============================================================

# Create slider
kl_slider = widgets.FloatSlider(
    value=38.44251, min=30.0, max=45.0, step=0.01,
    description='Warp Factor (kL):',
    style={'description_width': 'initial'}, layout={'width': '500px'}
)

out = widgets.Output()

def update_hierarchy_audit(kL):
    with out:
        clear_output(wait=True)

        # Compute WIN Higgs mass
        m_H, lambda_tree, lambda_eff = win_higgs_mass(kL)

        # Hierarchy suppression
        hierarchy_supp = hierarchy_suppression(kL)

        # Print audit
        print("=" * 70)
        print("WIN PARADIGM: 5D WARPED HIERARCHY & HIGGS MASS")
        print("=" * 70)
        print()
        print("Substrate parameters:")
        print(f"  d = {d}")
        print(f"  H = {H}")
        print(f"  V = {V}")
        print(f"  N = {N}")
        print()
        print("Calibration input:")
        print(f"  kL = ln(M_Planck/v_EW) = {kL_calibration:.5f}")
        print(f"  M_Planck = {M_Planck:.3e} GeV")
        print(f"  v_EW = {v_EW} GeV")
        print()
        print(f"Current kL: {kL:.5f}")
        print()
        print("WIN Higgs mass derivation:")
        print(f"  lambda_tree = ln(kL)/(3 pi^2) = {lambda_tree:.6f}")
        print(f"  lambda_eff = lambda_tree + 1/180 = {lambda_eff:.6f}")
        print(f"  m_H = sqrt(2 lambda_eff) × v_EW = {m_H:.3f} GeV")
        print()
        print("Comparison:")
        print(f"  WIN prediction: {m_H:.3f} GeV")
        print(f"  Experiment: 125.25 +/- 0.17 GeV")
        print(f"  Error: {abs(m_H - 125.25)/125.25*100:.3f}%")
        print()
        print("Hierarchy suppression:")
        print(f"  exp(-kL) = {hierarchy_supp:.3e}")
        print()
        print("NOTE: The WIN framework derives the Higgs mass from the 5D")
        print("warped geometry. The KK graviton resonance is NOT currently")
        print("derived from WIN principles and is not shown.")
        print("=" * 70)

        # Plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # Left panel: Higgs mass vs kL
        kl_sweep = np.linspace(30.0, 45.0, 200)
        m_H_sweep = np.array([win_higgs_mass(kl)[0] for kl in kl_sweep])

        ax1.plot(kl_sweep, m_H_sweep, color='#1f77b4', linewidth=2.5,
                 label='WIN Higgs mass')
        ax1.axhline(125.25, color='green', linestyle='--', alpha=0.7,
                    label='Experiment (125.25 GeV)')
        ax1.axvline(kL_calibration, color='red', linestyle=':', alpha=0.7,
                    label=f'kL = {kL_calibration:.2f}')
        ax1.axvline(kL, color='orange', linestyle='-', alpha=0.5,
                    label=f'Current kL = {kL:.2f}')
        ax1.set_xlabel(r'Warp Factor ($kL$)', fontsize=11)
        ax1.set_ylabel(r'Higgs Mass $m_H$ (GeV)', fontsize=11)
        ax1.set_title('WIN Higgs Mass vs. Warp Factor', fontsize=12, fontweight='bold')
        ax1.grid(True, linestyle=':', alpha=0.6)
        ax1.legend(frameon=True, facecolor='white')

        # Right panel: hierarchy suppression
        hierarchy_sweep = np.exp(-kl_sweep)
        ax2.semilogy(kl_sweep, hierarchy_sweep, color='#2ca02c', linewidth=2.5,
                     label=r'$\exp(-kL)$')
        ax2.axvline(kL_calibration, color='red', linestyle=':', alpha=0.7,
                    label=f'kL = {kL_calibration:.2f}')
        ax2.set_xlabel(r'Warp Factor ($kL$)', fontsize=11)
        ax2.set_ylabel(r'Hierarchy Suppression $\exp(-kL)$', fontsize=11)
        ax2.set_title('Hierarchy Suppression vs. Warp Factor', fontsize=12, fontweight='bold')
        ax2.grid(True, which='both', linestyle=':', alpha=0.6)
        ax2.legend(frameon=True, facecolor='white')

        plt.tight_layout()
        plt.show()

# Bind controls
hierarchy_interactive = widgets.interactive(
    update_hierarchy_audit,
    kL=kl_slider
)
display(hierarchy_interactive, out)
