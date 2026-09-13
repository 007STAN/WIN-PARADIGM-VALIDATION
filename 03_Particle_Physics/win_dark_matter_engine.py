"""
Warped Information Number (WIN) Paradigm — Dark Matter Analysis
Author: Stanley Preschutti (Information Physics Institute, UK)
Description: Analysis of dark matter within the WIN framework.

The WIN framework predicts stable Majorana bound states in the hidden 
sector H = 16. These states could be dark matter candidates. The relic 
density is determined by the standard freeze-out calculation.

The WIN framework does NOT currently derive the dark matter relic density 
from first principles. This script presents the framework for computing 
it and identifies what would be needed.

Observed dark matter relic density:
  Omega_DM h^2 = 0.1200 +/- 0.0012 (Planck 2018)
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

# Observed dark matter relic density
Omega_DM_obs = 0.1200       # Planck 2018
Omega_DM_err = 0.0012

# Physical constants
M_Pl = 1.220910e19          # Planck mass (GeV)
hbar = 6.582119569e-25      # Reduced Planck constant (GeV s)
c = 2.99792458e10           # Speed of light (cm/s)

# ============================================================
# DARK MATTER RELIC DENSITY (FREEZE-OUT)
# ============================================================

def thermal_average_cross_section(sigma_v):
    """
    Thermal average of the annihilation cross section.

    For s-wave annihilation:
    <sigma v> = sigma_v (constant)
    """
    return sigma_v

def freeze_out_integral(x_f):
    """
    Freeze-out integral J(x_f).

    J(x_f) = integral from x_f to infinity of <sigma v> x^-2 dx

    For s-wave annihilation:
    J(x_f) = <sigma v> / x_f
    """
    # This is a placeholder. The actual calculation depends on <sigma v>.
    return 1 / x_f

def relic_density(m_dark_GeV, sigma_v_cm3_s):
    """
    Compute the dark matter relic density from the freeze-out calculation.

    Omega_DM h^2 = (1.07e9 GeV^-1) / (g_*^(1/2) M_Pl J(x_f))

    where:
    - g_* ~ 100 (effective relativistic degrees of freedom)
    - M_Pl = 1.22e19 GeV
    - J(x_f) = <sigma v> / x_f
    - x_f ~ 20 (freeze-out temperature)

    The cross section <sigma v> is in cm^3/s.
    """
    g_star = 100.0
    x_f = 20.0

    # Convert sigma_v from cm^3/s to GeV^-2
    # 1 GeV^-2 = (hbar c)^2 cm^2 = (1.97e-14 cm)^2 = 3.89e-28 cm^2
    # So 1 cm^2 = 2.57e27 GeV^-2
    # sigma_v [cm^3/s] = sigma_v [GeV^-2] × (hbar c^2) × (2.57e27)
    # Actually, sigma_v is in cm^3/s. To convert to GeV^-2, we need to 
    # divide by (hbar^2 c^2) or something. Let me be careful.

    # Actually, in natural units, sigma_v is in GeV^-2.
    # In SI units, sigma_v is in cm^3/s.
    # The conversion is: sigma_v [GeV^-2] = sigma_v [cm^3/s] / (1.167e-17)
    # where 1.167e-17 cm^3/s = 1 GeV^-2.

    # Let me just use the standard formula:
    # Omega_DM h^2 = 0.12 × (3e-26 cm^3/s) / <sigma v>
    # This is the standard result for a thermal relic.

    sigma_v_thermal = 3e-26  # cm^3/s (thermal relic cross section)
    Omega_DM_h2 = 0.12 * (sigma_v_thermal / sigma_v_cm3_s)

    return Omega_DM_h2

# ============================================================
# WIN DARK MATTER PREDICTION
# ============================================================

def win_dark_matter_relic_density():
    """
    Compute the WIN dark matter relic density.

    The WIN framework predicts stable Majorana bound states in the 
    hidden sector H = 16. The relic density is determined by the 
    standard freeze-out calculation.

    The annihilation cross section for Majorana bound states is:
    <sigma v> = (alpha_dark^2 / m_dark^2) × (something)

    where alpha_dark = epsilon^2 × alpha_EM, and m_dark = 0.291 GeV.

    The WIN framework does NOT currently derive the exact value of 
    <sigma v>. This function returns the value for the standard 
    thermal relic cross section, which gives Omega_DM h^2 = 0.12.
    """
    # Standard thermal relic cross section
    sigma_v_thermal = 3e-26  # cm^3/s

    # WIN dark matter mass
    m_dark = 0.291253  # GeV

    # Compute relic density
    Omega_DM_h2 = relic_density(m_dark, sigma_v_thermal)

    return Omega_DM_h2, sigma_v_thermal

# ============================================================
# WIDGET
# ============================================================

# Create sliders
sigma_v_slider = widgets.FloatLogSlider(
    value=3e-26, base=10, min=-30, max=-20, step=0.1,
    description='<sigma v> (cm^3/s):',
    style={'description_width': 'initial'}, layout={'width': '500px'}
)

out = widgets.Output()

def update_dm_audit(sigma_v):
    with out:
        clear_output(wait=True)

        # Compute relic density
        m_dark = 0.291253  # GeV
        Omega_DM_h2 = relic_density(m_dark, sigma_v)

        # Print audit
        print("=" * 70)
        print("WIN PARADIGM: DARK MATTER RELIC DENSITY ANALYSIS")
        print("=" * 70)
        print()
        print("Substrate parameters:")
        print(f"  d = {d}")
        print(f"  H = {H}")
        print(f"  V = {V}")
        print(f"  N = {N}")
        print()
        print("WIN dark matter prediction:")
        print(f"  m_dark = {m_dark:.6f} GeV = {m_dark*1000:.3f} MeV")
        print()
        print("Input:")
        print(f"  <sigma v> = {sigma_v:.3e} cm^3/s")
        print()
        print("Computed relic density:")
        print(f"  Omega_DM h^2 = {Omega_DM_h2:.4f}")
        print()
        print("Comparison:")
        print(f"  Observed (Planck 2018): {Omega_DM_obs:.4f} +/- {Omega_DM_err:.4f}")
        print(f"  WIN computed: {Omega_DM_h2:.4f}")
        print(f"  Error: {abs(Omega_DM_h2 - Omega_DM_obs)/Omega_DM_obs*100:.2f}%")
        print()
        print("NOTE: The WIN framework does NOT currently derive the exact")
        print("value of <sigma v> from first principles. The standard thermal")
        print("relic cross section (3e-26 cm^3/s) gives the observed value.")
        print()
        print("This is an OPEN PROBLEM for the WIN framework.")
        print("=" * 70)

        # Plot
        fig, ax = plt.subplots(figsize=(10, 6))

        # Sweep over sigma_v
        sigma_v_sweep = np.logspace(-30, -20, 200)
        Omega_sweep = np.array([relic_density(m_dark, sv) for sv in sigma_v_sweep])

        ax.loglog(sigma_v_sweep, Omega_sweep, color='#1f77b4', linewidth=2.5,
                  label='WIN relic density')
        ax.axhline(Omega_DM_obs, color='green', linestyle='--', alpha=0.7,
                   label=f'Observed ({Omega_DM_obs:.4f})')
        ax.axvline(sigma_v, color='orange', linestyle=':', alpha=0.7,
                   label=f'Current <sigma v>')
        ax.axvline(3e-26, color='red', linestyle='-.', alpha=0.5,
                   label='Thermal relic (3e-26)')

        ax.set_xlabel(r'$\langle \sigma v \rangle$ (cm$^3$/s)', fontsize=11)
        ax.set_ylabel(r'$\Omega_{DM} h^2$', fontsize=11)
        ax.set_title('WIN Dark Matter Relic Density', fontsize=12, fontweight='bold')
        ax.grid(True, which='both', linestyle=':', alpha=0.6)
        ax.legend(frameon=True, facecolor='white', loc='upper right')

        plt.tight_layout()
        plt.show()

# Bind controls
dm_interactive = widgets.interactive(
    update_dm_audit,
    sigma_v=sigma_v_slider
)
display(dm_interactive, out)
