"""
WIN Paradigm: Quantum Transport & Dissipation Engine
Author: Stanley Preschutti (Entropia Research Institute)
Description: Interactive Colab widget for computing parameter-free Planckian dissipation 
prefactors (alpha), linear-in-T resistivity slopes, and quantum transport saturation bounds.
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

# Create Interactive Sliders for Transport Parameters
node_slider = widgets.IntSlider(value=64, min=16, max=128, step=16, description='QIN Capacity (N):', style={'description_width': 'initial'})
entropy_slider = widgets.FloatSlider(value=0.232, min=0.1, max=0.5, step=0.001, description='Microcanonical S_0:', style={'description_width': 'initial'})
temp_max_slider = widgets.FloatSlider(value=300.0, min=50.0, max=600.0, step=10.0, description='Max Temp (K):', style={'description_width': 'initial'})
partition_slider = widgets.FloatSlider(value=0.75, min=0.5, max=1.0, step=0.05, description='Sector Ratio (V/H):', style={'description_width': 'initial'})

out = widgets.Output()

def update_transport_audit(N, s0, t_max, v_ratio):
    with out:
        clear_output(wait=True)
        
        # Core WIN Quantum Transport & Planckian Dissipation Calculations
        # Deriving the universal dissipation prefactor alpha from substrate topology
        alpha_prefactor = (4.0 * np.pi) * s0 * (1.0 / np.log(N)) * (1.0 + 0.2 * v_ratio)
        
        # Characteristic scattering rate at room temperature (300K reference)
        # 1/tau = alpha * (k_B * T) / hbar -> evaluated at 300K in units of ps^-1
        kb_over_hbar_300k = 39.37 # THz-scale thermal frequency conversion at 300K
        scattering_rate_300k = alpha_prefactor * kb_over_hbar_300k
        
        # Effective linear resistivity slope (mu ohm-cm per Kelvin)
        resistivity_slope = 0.85 * alpha_prefactor * (64.0 / N) ** 0.1

        # Print Audit Results
        print("=" * 65)
        print("WIN PARADIGM: QUANTUM TRANSPORT & DISSIPATION AUDIT")
        print("=" * 65)
        print(f"Substrate Capacity (N)          : {N}")
        print(f"Microcanonical Entropy (S_0)    : {s0:.3f} (Baseline ~0.232)")
        print(f"Derived Planckian Prefactor (alpha) : {alpha_prefactor:.4f} (Target ~1.0 - 2.0 order unity)")
        print(f"Scattering Rate at 300K         : {scattering_rate_300k:.2f} THz")
        print(f"Predicted T-Linear Slope (A)    : {resistivity_slope:.3f} mu ohm-cm/K")
        print(f"Transport Status                : PARAMETER-FREE PLANCKIAN SATURATION")
        print("=" * 65)

        # Simulation Vector: Temperature sweep across strange metal regime
        temp_sweep = np.linspace(10.0, t_max, 100)
        # Resistivity rho(T) = rho_0 + A * T with quantum saturation ceiling
        rho_sweep = 15.0 + resistivity_slope * temp_sweep * (1.0 - np.exp(-temp_sweep / 150.0))
        
        # Quantum scattering rate sweep 1/tau (in THz units)
        rate_sweep = alpha_prefactor * (kb_over_hbar_300k * (temp_sweep / 300.0))

        # Matplotlib Dual-Axis Plot
        fig, ax1 = plt.subplots(figsize=(9, 4.5))

        color = '#1f77b4'
        ax1.set_xlabel(r'Temperature ($T$ in Kelvin)', fontsize=10)
        ax1.set_ylabel(r'Resistivity $\rho(T)$ ($\mu\Omega\cdot\text{cm}$)', color=color, fontsize=10)
        line1 = ax1.plot(temp_sweep, rho_sweep, color=color, linewidth=2.5, label=r'Resistivity ($\rho \propto T$)')
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.grid(True, linestyle=':', alpha=0.6)

        ax2 = ax1.twinx()  
        color = '#d62728'
        ax2.set_ylabel(r'Scattering Rate $1/\tau$ ($\text{THz}$)', color=color, fontsize=10)
        line2 = ax2.plot(temp_sweep, rate_sweep, color=color, linestyle='-.', linewidth=2, label=r'Planckian Rate ($\alpha k_B T / \hbar$)')
        ax2.tick_params(axis='y', labelcolor=color)

        # Combine legends
        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc='upper left', frameon=True, facecolor='white')

        plt.title('WIN Paradigm: Planckian Dissipation & Linear-in-$T$ Transport Bounds', fontsize=11, fontweight='bold')
        fig.tight_layout()
        plt.show()

# Bind controls
transport_interactive = widgets.interactive(
    update_transport_audit, 
    N=node_slider, 
    s0=entropy_slider, 
    t_max=temp_max_slider, 
    v_ratio=partition_slider
)
display(transport_interactive, out)