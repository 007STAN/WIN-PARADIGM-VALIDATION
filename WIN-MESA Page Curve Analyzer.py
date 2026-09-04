"""
WIN Paradigm Colab Interactive Tool
Author: Stanley Preschutti (Information Physics Institute, UK)
Description: Jupyter/Colab native interactive widget for N=64 Majorana QIN Page curves.
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

# Create Interactive Sliders
n_slider = widgets.IntSlider(value=64, min=16, max=256, step=16, description='Capacity (N):', style={'description_width': 'initial'})
s0_slider = widgets.FloatSlider(value=0.232, min=0.1, max=0.5, step=0.001, description='Coeff (S0):', style={'description_width': 'initial'})
gamma_slider = widgets.FloatSlider(value=0.08, min=0.01, max=0.2, step=0.01, description='Emission (g):', style={'description_width': 'initial'})
p_slider = widgets.FloatSlider(value=0.0244, min=0.0, max=0.1, step=0.001, description='Persistence:', style={'description_width': 'initial'})
c_slider = widgets.FloatSlider(value=0.0390, min=0.0, max=0.1, step=0.001, description='Ceiling:', style={'description_width': 'initial'})

out = widgets.Output()

def update_plot(N, s0, gamma, p_frac, c_frac):
    with out:
        clear_output(wait=True)
        
        # Calculations
        effective_entropy = s0 * N
        persistence_residual = p_frac * effective_entropy
        saturation_ceiling = c_frac * effective_entropy
        d_b = np.exp(effective_entropy)
        var_s = np.pi**2 / (6.0 * d_b)

        # Simulation curve
        times = np.linspace(0, 250, 400)
        s_rad = []
        for t in times:
            thermal_growth = gamma * t
            evaporating_bh = effective_entropy - gamma * t + persistence_residual
            val = min(thermal_growth, evaporating_bh)
            if t > 120 and val < saturation_ceiling:
                val = saturation_ceiling
            s_rad.append(max(0.0, val))

        # Print Audit Results
        print("=" * 60)
        print("WIN PARADIGM LIVE MEASUREMENT AUDIT")
        print("=" * 60)
        print(f"Effective Entropy     : {effective_entropy:.3f} nats")
        print(f"Persistence Residual  : {persistence_residual:.4f} ({p_frac*100:.2f}%)")
        print(f"Terminal Ceiling      : {saturation_ceiling:.4f} ({c_frac*100:.2f}%)")
        print(f"Wishart Variance      : {var_s:.2e}")
        print("=" * 60)

        # Matplotlib Plot
        fig, ax = plt.subplots(figsize=(9, 4.5))
        ax.plot(times, s_rad, label='Unitary $S_{rad}$', color='#1f77b4', linewidth=2.5)
        ax.axhline(persistence_residual, color='orange', linestyle='--', label='Persistence Res.')
        ax.axhline(saturation_ceiling, color='red', linestyle=':', label='Terminal Ceiling')
        ax.set_title("WIN Page Curve & Remnant Bounds (Live Interactive)", fontsize=11, fontweight='bold')
        ax.set_xlabel("Time ($t$)", fontsize=10)
        ax.set_ylabel("Radiation Entropy ($S_{rad}$)", fontsize=10)
        ax.legend(frameon=True, facecolor='white')
        ax.grid(True, linestyle=':', alpha=0.6)
        fig.tight_layout()
        plt.show()

# Bind controls to function
interactive_plot = widgets.interactive(update_plot, N=n_slider, s0=s0_slider, gamma=gamma_slider, p_frac=p_slider, c_frac=c_slider)
display(interactive_plot, out)
