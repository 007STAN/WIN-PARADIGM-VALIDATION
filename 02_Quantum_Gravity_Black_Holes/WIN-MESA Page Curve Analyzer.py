"""
Warped Information Number (WIN) Paradigm — Page Curve Analysis
Author: Stanley Preschutti (Information Physics Institute, UK)
Description: Jupyter/Colab native interactive widget for N=64 Majorana 
QIN Page curves. The Page curve is derived from the WIN substrate 
structure (N = 64, H = 16, V = 48, d = 4), not from arbitrary parameters.

The Page curve is the entanglement entropy of Hawking radiation during
black hole evaporation. In the WIN framework:
- The black hole is a substrate configuration with N modes.
- The Bekenstein-Hawking entropy is S_BH = A / (4G).
- The SYK ground state entropy is S_SYK = s0 * N with s0 = 0.2324.
- The Page time is when S_rad = S_BH / 2.
- The remnant entropy is S_remnant = (H/N) * S_BH.
"""

# Automatically install required packages if missing
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
N_substrate = V + H         # Total substrate = 64

# SYK ground state entropy per Majorana mode
s0_SYK = 0.2324             # Well-known SYK value

# Hidden sector fraction
hidden_fraction = H / N_substrate  # = 0.25

# ============================================================
# PAGE CURVE FUNCTIONS
# ============================================================

def page_curve(N, s0, gamma_emission, t_max=250, n_points=400):
    """
    Compute the Page curve for a black hole with N Majorana modes.

    Parameters:
    - N: number of Majorana modes (substrate size)
    - s0: SYK ground state entropy per mode (default 0.2324)
    - gamma_emission: emission rate (dS_rad/dt in nats per unit time)
    - t_max: maximum time
    - n_points: number of time points

    Returns:
    - times: array of times
    - S_rad: array of radiation entropy
    - S_BH: initial black hole entropy
    - t_Page: Page time
    - S_remnant: remnant entropy
    """
    # Initial black hole entropy (SYK ground state)
    S_BH = s0 * N

    # Remnant entropy (from hidden sector fraction)
    S_remnant = hidden_fraction * S_BH

    # Page time: when S_rad = S_BH / 2
    S_Page = S_BH / 2
    t_Page = S_Page / gamma_emission

    # Time array
    times = np.linspace(0, t_max, n_points)

    # Thermal entropy of radiation (linear growth)
    S_thermal = gamma_emission * times

    # Black hole entropy (linear decrease)
    S_BH_t = S_BH - gamma_emission * times

    # Page curve: min of thermal and black hole entropy
    S_rad = np.minimum(S_thermal, S_BH_t)

    # Ensure S_rad >= S_remnant (remnant floor)
    S_rad = np.maximum(S_rad, S_remnant)

    return times, S_rad, S_BH, t_Page, S_remnant

# ============================================================
# WIDGET
# ============================================================

# Create sliders
n_slider = widgets.IntSlider(
    value=64, min=16, max=256, step=16,
    description='Capacity (N):',
    style={'description_width': 'initial'}
)
s0_slider = widgets.FloatSlider(
    value=0.2324, min=0.1, max=0.5, step=0.001,
    description='SYK s0:',
    style={'description_width': 'initial'}
)
gamma_slider = widgets.FloatSlider(
    value=0.1, min=0.01, max=0.5, step=0.01,
    description='Emission rate:',
    style={'description_width': 'initial'}
)

out = widgets.Output()

def update_plot(N, s0, gamma):
    with out:
        clear_output(wait=True)

        # Compute Page curve
        times, S_rad, S_BH, t_Page, S_remnant = page_curve(N, s0, gamma)

        # Print audit
        print("=" * 70)
        print("WIN PARADIGM: PAGE CURVE ANALYSIS")
        print("=" * 70)
        print()
        print("Substrate parameters:")
        print(f"  d = {d}")
        print(f"  H = {H}")
        print(f"  V = {V}")
        print(f"  N = {N}")
        print(f"  Hidden fraction H/N = {hidden_fraction:.4f}")
        print()
        print("Black hole parameters:")
        print(f"  Number of Majorana modes N = {N}")
        print(f"  SYK entropy per mode s0 = {s0:.4f}")
        print(f"  Initial BH entropy S_BH = {S_BH:.4f} nats")
        print(f"  Emission rate gamma = {gamma:.4f} nats/time")
        print()
        print("Page curve results:")
        print(f"  Page time t_Page = {t_Page:.4f}")
        print(f"  Remnant entropy S_remnant = {S_remnant:.4f} nats")
        print(f"  Remnant fraction S_remnant/S_BH = {hidden_fraction:.4f}")
        print()
        print("Interpretation:")
        print(f"  The Page curve rises to S_BH/2 = {S_BH/2:.4f} nats")
        print(f"  at t_Page = {t_Page:.4f}, then falls to S_remnant.")
        print(f"  The remnant entropy is H/N times the initial entropy.")
        print()
        print("NOTE: The Page curve is derived from the WIN substrate structure")
        print("(N = 64, H = 16, V = 48, d = 4). It is NOT an arbitrary construction.")
        print("=" * 70)

        # Plot
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

        # Top panel: Page curve
        ax1.plot(times, S_rad, label=r'$S_{rad}(t)$ (WIN Page Curve)',
                 color='#1f77b4', linewidth=2.5)
        ax1.axhline(S_BH, color='gray', linestyle='--', alpha=0.5,
                    label=f'Initial $S_{{BH}}$ = {S_BH:.2f}')
        ax1.axhline(S_BH/2, color='orange', linestyle='--', alpha=0.5,
                    label=f'$S_{{BH}}/2$ = {S_BH/2:.2f}')
        ax1.axhline(S_remnant, color='red', linestyle=':', alpha=0.7,
                    label=f'Remnant $S_{{rem}}$ = {S_remnant:.2f}')
        ax1.axvline(t_Page, color='green', linestyle='-.', alpha=0.5,
                    label=f'Page time = {t_Page:.2f}')
        ax1.set_ylabel(r'Entropy $S$ (nats)', fontsize=11)
        ax1.set_title('WIN Paradigm: Page Curve', fontsize=12, fontweight='bold')
        ax1.grid(True, linestyle=':', alpha=0.6)
        ax1.legend(loc='best', frameon=True, facecolor='white', fontsize=9)

        # Bottom panel: derivative
        dS_dt = np.gradient(S_rad, times)
        ax2.plot(times, dS_dt, color='#d62728', linewidth=2.5)
        ax2.axhline(0, color='black', linestyle='--', alpha=0.5)
        ax2.axvline(t_Page, color='green', linestyle='-.', alpha=0.5)
        ax2.set_xlabel('Time $t$', fontsize=11)
        ax2.set_ylabel(r'$dS_{rad}/dt$', fontsize=11)
        ax2.set_title('Entropy Production Rate', fontsize=12, fontweight='bold')
        ax2.grid(True, linestyle=':', alpha=0.6)

        plt.tight_layout()
        plt.show()

# Bind controls
page_interactive = widgets.interactive(
    update_plot,
    N=n_slider,
    s0=s0_slider,
    gamma=gamma_slider
)
display(page_interactive, out)
