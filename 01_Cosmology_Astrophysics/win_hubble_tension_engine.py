"""
Warped Information Number (WIN) Paradigm — Hubble Tension Analysis
Author: Stanley Preschutti (Information Physics Institute, UK)
Description: Analysis of the Hubble tension within the WIN framework.

The Hubble tension is the discrepancy between:
- CMB measurement: H_0 = 67.4 +/- 0.5 km/s/Mpc (Planck 2018)
- Local measurement: H_0 = 73.0 +/- 1.0 km/s/Mpc (SH0ES 2022)

The discrepancy is ~5 sigma.

The WIN framework predicts a scale-dependent entropy correction derived
from the substrate's finite information capacity. This script presents
the framework for computing this correction and identifies what would
be needed to resolve the tension.
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
kL = 38.442487804005536     # Warp factor

# ============================================================
# COSMOLOGICAL MEASUREMENTS
# ============================================================

H_0_CMB = 67.4              # km/s/Mpc (Planck 2018)
H_0_CMB_err = 0.5
H_0_local = 73.0            # km/s/Mpc (SH0ES 2022)
H_0_local_err = 1.0

# ============================================================
# WIN SCALE-DEPENDENT CORRECTION
# ============================================================

def win_information_capacity_ratio(z):
    """
    Compute the ratio of the substrate information capacity at redshift z
    to the information capacity today.

    The substrate has N = 64 modes. The observable universe has an
    information capacity given by the holographic bound:
    S_universe(z) = A(z) / (4G)

    where A(z) is the area of the Hubble horizon at redshift z.

    The Hubble radius at redshift z is:
    R_H(z) = c / H(z)

    where H(z) is the Hubble parameter at redshift z.

    The area is:
    A(z) = 4 pi R_H(z)^2

    The information capacity ratio is:
    capacity_ratio(z) = S_universe(z) / S_universe(0)
                      = (R_H(z) / R_H(0))^2
                      = (H_0 / H(z))^2
    """
    Omega_m0 = 0.315
    Omega_L0 = 0.685
    H_z_sq = Omega_m0 * (1 + z)**3 + Omega_L0
    H_0_sq = Omega_m0 + Omega_L0
    capacity_ratio = H_0_sq / H_z_sq
    return capacity_ratio

def win_hubble_correction(z):
    """
    Compute the WIN correction to the Hubble parameter at redshift z.

    The correction is derived from the substrate's finite information
    capacity. As the universe expands, the information capacity of the
    observable universe changes, which modifies the effective Hubble
    parameter.

    The correction is:
    Delta_H(z) / H(z) = (H/N) * (1 - capacity_ratio(z))

    where H/N = 16/64 = 0.25 is the hidden sector fraction.

    This is the WIN prediction for the scale-dependent correction.
    """
    hidden_fraction = H / N  # = 0.25
    capacity_ratio = win_information_capacity_ratio(z)
    delta_H_over_H = hidden_fraction * (1 - capacity_ratio)
    return delta_H_over_H

def win_local_h0(H_0_early):
    """
    Compute the WIN-derived local H_0 from the CMB baseline.

    The local H_0 is:
    H_0_local = H_0_early * (1 + Delta_H/H(z=0))

    But at z = 0, capacity_ratio = 1, so Delta_H/H = 0.
    This means the WIN correction is zero at z = 0.

    To get a non-zero correction at z = 0, we need a different
    mechanism. The local measurement is at z ~ 0.01 (local universe),
    not exactly z = 0.

    Let's compute the correction at z = 0.01.
    """
    z_local = 0.01
    delta_H_over_H = win_hubble_correction(z_local)
    H_0_local = H_0_early * (1 + delta_H_over_H)
    return H_0_local, delta_H_over_H

# ============================================================
# WIDGET
# ============================================================

# Create sliders
h_early_slider = widgets.FloatSlider(
    value=H_0_CMB, min=60.0, max=72.0, step=0.1,
    description='CMB Baseline H_0:',
    style={'description_width': 'initial'}
)
z_local_slider = widgets.FloatSlider(
    value=0.01, min=0.001, max=0.1, step=0.001,
    description='Local z:',
    style={'description_width': 'initial'}
)

out = widgets.Output()

def update_hubble_audit(h_early, z_local):
    with out:
        clear_output(wait=True)

        # Compute WIN correction
        capacity_ratio = win_information_capacity_ratio(z_local)
        hidden_fraction = H / N
        delta_H_over_H = hidden_fraction * (1 - capacity_ratio)
        H_0_WIN = h_early * (1 + delta_H_over_H)

        # Print audit
        print("=" * 70)
        print("WIN PARADIGM: HUBBLE TENSION ANALYSIS")
        print("=" * 70)
        print()
        print("Substrate parameters:")
        print(f"  d = {d}")
        print(f"  H = {H}")
        print(f"  V = {V}")
        print(f"  N = {N}")
        print(f"  Hidden fraction H/N = {hidden_fraction:.4f}")
        print()
        print("Inputs:")
        print(f"  CMB baseline H_0 = {h_early:.2f} km/s/Mpc")
        print(f"  Local redshift z = {z_local:.4f}")
        print()
        print("WIN computation:")
        print(f"  Capacity ratio at z = {z_local:.4f}: {capacity_ratio:.6f}")
        print(f"  Delta_H/H = (H/N) * (1 - capacity_ratio) = {delta_H_over_H:.6f}")
        print(f"  WIN local H_0 = {H_0_WIN:.2f} km/s/Mpc")
        print()
        print("Comparison:")
        print(f"  CMB (Planck 2018): {H_0_CMB:.2f} +/- {H_0_CMB_err:.2f} km/s/Mpc")
        print(f"  Local (SH0ES 2022): {H_0_local:.2f} +/- {H_0_local_err:.2f} km/s/Mpc")
        print(f"  WIN prediction: {H_0_WIN:.2f} km/s/Mpc")
        print()
        print("Status:")
        print(f"  The WIN correction at z = {z_local:.4f} is {delta_H_over_H*100:.4f}%")
        print(f"  This is {'INSUFFICIENT' if abs(H_0_WIN - H_0_local) > 1 else 'SUFFICIENT'} to resolve the tension.")
        print()
        print("NOTE: The WIN framework's derivation of the Hubble tension is")
        print("an OPEN PROBLEM. The correction shown here is derived from the")
        print("substrate's finite information capacity, but it is not yet clear")
        print("whether this mechanism can fully resolve the tension.")
        print("=" * 70)

        # Plot
        z_sweep = np.logspace(-3, 4, 300)
        delta_H_sweep = np.array([win_hubble_correction(z) for z in z_sweep])
        H_sweep = h_early * (1 + delta_H_sweep)

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

        # Top panel: H(z)
        ax1.semilogx(z_sweep, H_sweep, color='#1f77b4', linewidth=2.5,
                     label='WIN Effective H(z)')
        ax1.axhline(h_early, color='gray', linestyle='--',
                    label=f'CMB Baseline ({h_early:.2f} km/s/Mpc)')
        ax1.axhline(H_0_local, color='green', linestyle='-.', alpha=0.7,
                    label=f'Local Measurement ({H_0_local:.2f} km/s/Mpc)')
        ax1.axhline(H_0_WIN, color='red', linestyle=':',
                    label=f'WIN Local Prediction ({H_0_WIN:.2f} km/s/Mpc)')
        ax1.set_ylabel(r'Expansion Rate $H(z)$ (km/s/Mpc)', fontsize=11)
        ax1.set_title('WIN Paradigm: Hubble Tension Analysis', fontsize=12, fontweight='bold')
        ax1.grid(True, which="both", linestyle=':', alpha=0.6)
        ax1.legend(loc='upper right', frameon=True, facecolor='white')

        # Bottom panel: correction
        ax2.semilogx(z_sweep, delta_H_sweep * 100, color='#d62728', linewidth=2.5)
        ax2.axhline(0, color='black', linestyle='--', alpha=0.5)
        ax2.set_xlabel(r'Redshift ($z$, log scale)', fontsize=11)
        ax2.set_ylabel(r'$\Delta H / H$ (%)', fontsize=11)
        ax2.set_title('WIN Scale-Dependent Correction', fontsize=12, fontweight='bold')
        ax2.grid(True, which="both", linestyle=':', alpha=0.6)

        plt.tight_layout()
        plt.show()

# Bind controls
hubble_interactive = widgets.interactive(
    update_hubble_audit,
    h_early=h_early_slider,
    z_local=z_local_slider
)
display(hubble_interactive, out)
