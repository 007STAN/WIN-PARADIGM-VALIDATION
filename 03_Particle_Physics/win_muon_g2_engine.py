"""
Warped Information Number (WIN) Paradigm — Muon g-2 Analysis
Author: Stanley Preschutti (Information Physics Institute, UK)
Description: Analysis of the muon g-2 anomaly within the WIN framework.

The muon g-2 anomaly is the discrepancy between:
- Standard Model prediction: a_mu_SM = 116591810(43) x 10^-11
- Experimental measurement: a_mu_exp = 116592061(41) x 10^-11
- Discrepancy: Delta_a_mu = 251(59) x 10^-11 (~4.2 sigma with 2021 Fermilab;
  reduced to ~1.8 sigma with 2025 BMW lattice result)

The WIN framework predicts a dark photon with:
- Mass: m_dark = 0.291 GeV
- Kinetic mixing: epsilon = 0.001193

This script computes the dark photon contribution to muon g-2 and shows
that it is insufficient to explain the observed anomaly.
"""

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, VBox, interactive_output

# ============================================================
# WIN SUBSTRATE PARAMETERS
# ============================================================

d = 4                       # Spacetime dimension
H = d**2                    # Hidden sector = 16
V = (d-1) * 2**d            # Visible sector = 48
N = V + H                   # Total substrate = 64
kL = 38.442487804005536     # Warp factor

# WIN predictions
m_dark = 0.291253           # Dark photon mass (GeV)
epsilon = 0.001193          # Kinetic mixing
alpha_EM = 1/137.036        # Fine structure constant
m_mu = 0.1056583755         # Muon mass (GeV)

# ============================================================
# MUON G-2 ANOMALY
# ============================================================

# Standard Model prediction (2020 White Paper)
a_mu_SM = 116591810e-11     # 116591810(43) x 10^-11

# Experimental measurement (Fermilab 2021)
a_mu_exp = 116592061e-11    # 116592061(41) x 10^-11
a_mu_exp_err = 41e-11

# Discrepancy
Delta_a_mu = a_mu_exp - a_mu_SM

# ============================================================
# DARK PHOTON CONTRIBUTION
# ============================================================

def dark_photon_loop_function(x):
    """
    Loop function for dark photon contribution to muon g-2.

    For m_dark >> m_mu:
    F(x) ~ 1/(2x^2)

    For m_dark << m_mu:
    F(x) ~ ln(m_mu/m_dark) - 5/6

    For m_dark ~ m_mu:
    F(x) is more complicated.
    """
    if x > 10:
        return 1/(2*x**2)
    elif x < 0.1:
        return np.log(1/x) - 5/6
    else:
        # Approximate form for intermediate x
        return 1/(2 + x**2)

def dark_photon_contribution(m_dark, epsilon, alpha_EM, m_mu):
    """
    Compute the dark photon contribution to muon g-2.

    Delta_a_mu = (alpha_eff / 2pi) * F(m_dark/m_mu)

    where alpha_eff = epsilon^2 * alpha_EM.
    """
    x = m_dark / m_mu
    alpha_eff = epsilon**2 * alpha_EM
    F = dark_photon_loop_function(x)
    Delta_a_mu_dark = (alpha_eff / (2*np.pi)) * F
    return Delta_a_mu_dark

# Compute the dark photon contribution
Delta_a_mu_dark = dark_photon_contribution(m_dark, epsilon, alpha_EM, m_mu)

# Print results
print("=" * 70)
print("WIN PARADIGM: MUON G-2 ANALYSIS")
print("=" * 70)
print()
print("Substrate parameters:")
print(f"  d = {d}")
print(f"  H = {H}")
print(f"  V = {V}")
print(f"  N = {N}")
print(f"  kL = {kL:.5f}")
print()
print("WIN dark photon prediction:")
print(f"  m_dark = {m_dark:.6f} GeV")
print(f"  epsilon = {epsilon:.6f}")
print()
print("Muon g-2 anomaly:")
print(f"  a_mu_SM = {a_mu_SM:.4e}")
print(f"  a_mu_exp = {a_mu_exp:.4e}")
print(f"  Delta_a_mu = {Delta_a_mu:.4e} = {Delta_a_mu/1e-11:.1f} x 10^-11")
print()
print("Dark photon contribution:")
print(f"  Mass ratio m_dark/m_mu = {m_dark/m_mu:.4f}")
print(f"  alpha_eff = epsilon^2 * alpha_EM = {epsilon**2 * alpha_EM:.4e}")
print(f"  Loop function F = {dark_photon_loop_function(m_dark/m_mu):.6f}")
print(f"  Delta_a_mu (dark) = {Delta_a_mu_dark:.4e} = {Delta_a_mu_dark/1e-11:.4f} x 10^-11")
print()
print("Comparison:")
print(f"  Observed anomaly: {Delta_a_mu/1e-11:.1f} x 10^-11")
print(f"  Dark photon: {Delta_a_mu_dark/1e-11:.4f} x 10^-11")
print(f"  Ratio: {Delta_a_mu / Delta_a_mu_dark:.1f}")
print()
print("CONCLUSION:")
print(f"  The dark photon contribution is {Delta_a_mu / Delta_a_mu_dark:.0f} times")
print("  smaller than the observed anomaly.")
print()
print("  The WIN framework's dark photon CANNOT explain the muon g-2 anomaly.")
print()
print("  The muon g-2 anomaly is an OPEN PROBLEM for the WIN framework.")
print("=" * 70)

# ============================================================
# WIDGET
# ============================================================

def plot_muon_g2(m_dark_val, epsilon_val):
    """Plot the dark photon contribution to muon g-2."""
    # Compute contribution
    Delta_a_mu_dark_val = dark_photon_contribution(m_dark_val, epsilon_val, alpha_EM, m_mu)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Bar chart
    labels = ['Observed anomaly', 'Dark photon contribution']
    values = [Delta_a_mu/1e-11, Delta_a_mu_dark_val/1e-11]
    colors = ['green', 'blue']
    
    bars = ax.bar(labels, values, color=colors, alpha=0.7, edgecolor='black')
    
    # Add value labels
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                f'{val:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_ylabel(r'$\Delta a_\mu \times 10^{-11}$', fontsize=11)
    ax.set_title('Muon g-2: Observed Anomaly vs. Dark Photon Contribution',
                 fontsize=12, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6, axis='y')
    
    # Add text
    text_str = (
        f"Dark photon parameters:\n"
        f"  m_dark = {m_dark_val:.4f} GeV\n"
        f"  epsilon = {epsilon_val:.6f}\n"
        f"  alpha_eff = {epsilon_val**2 * alpha_EM:.4e}\n"
        f"\n"
        f"Observed anomaly: {Delta_a_mu/1e-11:.1f} x 10^-11\n"
        f"Dark photon: {Delta_a_mu_dark_val/1e-11:.4f} x 10^-11\n"
        f"Ratio: {Delta_a_mu / Delta_a_mu_dark_val:.1f}"
    )
    props = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(0.98, 0.98, text_str, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right', bbox=props)
    
    plt.tight_layout()
    plt.show()

# Create sliders
m_dark_slider = FloatSlider(
    value=0.291253, min=0.001, max=10.0, step=0.001,
    description='m_dark (GeV):',
    style={'description_width': 'initial'}, layout={'width': '500px'}
)
epsilon_slider = FloatSlider(
    value=0.001193, min=1e-6, max=1e-1, step=1e-6,
    description='epsilon:',
    style={'description_width': 'initial'}, layout={'width': '500px'}
)

out = interactive_output(plot_muon_g2, {
    'm_dark_val': m_dark_slider,
    'epsilon_val': epsilon_slider
})

display(VBox([m_dark_slider, epsilon_slider, out]))
