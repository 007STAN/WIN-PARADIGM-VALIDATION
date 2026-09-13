"""
Dark Photon Contribution to Muon g-2 — General Explorer

Author: Stanley Preschutti (Information Physics Institute, UK)
Status: CORRECTED Sept 13, 2026 — rebranded as general explorer.

============================================================================
NOTICE
============================================================================
This widget computes the dark photon contribution to muon g-2 for
arbitrary (m_dark, epsilon). It is a REAL calculation (standard QED
loop formula).

It is NOT a WIN validation widget. The WIN dark photon prediction
(m_dark = 0.291 GeV, epsilon = 0.001193) is FALSIFIED:

    The stated formulas:
        m_dark = g_dark * v_EW / H^2     -> gives 0.0996 GeV (not 0.291)
        epsilon = (g_dark * g_EM)/(2kL) -> gives 6.7e-4 (not 1.19e-3)

Either the formulas are wrong, or the values came from a different
(undisclosed) route. Until the formulas are corrected, no WIN dark
photon prediction can be made.

This widget lets you explore the (m_dark, epsilon) parameter space.
The default values are the falsified WIN values, retained only for
reproducibility. They should not be cited as a WIN prediction.
============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, VBox, interactive_output

# ============================================================
# CONSTANTS (measured)
# ============================================================

alpha_EM = 1/137.036        # Fine structure constant
m_mu = 0.1056583755         # Muon mass (GeV)

# ============================================================
# MUON G-2 ANOMALY
# ============================================================

a_mu_SM = 116591810e-11     # 116591810(43) x 10^-11 (2020 White Paper)
a_mu_exp = 116592061e-11    # 116592061(41) x 10^-11 (Fermilab 2021)
a_mu_exp_err = 41e-11

Delta_a_mu = a_mu_exp - a_mu_SM  # = 251e-11

# ============================================================
# DARK PHOTON CONTRIBUTION (exact one-loop formula)
# ============================================================

def dark_photon_loop_function_exact(x):
    """
    Exact one-loop function for dark photon contribution to muon g-2.

    F(x) = integral_0^1 2z(1-z)^2 / [z^2 + (1-z)x^2] dz

    where x = m_dark / m_mu.

    For x >> 1: F(x) ~ 1/(2x^2)
    For x << 1: F(x) ~ ln(1/x) - 5/6
    """
    if x < 1e-6:
        return np.log(1/x) - 5/6
    # Numerical integration
    z = np.linspace(0, 1, 10000)
    integrand = 2*z*(1-z)**2 / (z**2 + (1-z)*x**2)
    return np.trapz(integrand, z)

def dark_photon_contribution(m_dark, epsilon, alpha_EM, m_mu):
    """
    Compute the dark photon contribution to muon g-2.

    Delta_a_mu = (alpha_eff / 2pi) * F(m_dark/m_mu)

    where alpha_eff = epsilon^2 * alpha_EM.
    """
    x = m_dark / m_mu
    alpha_eff = epsilon**2 * alpha_EM
    F = dark_photon_loop_function_exact(x)
    return (alpha_eff / (2*np.pi)) * F

# ============================================================
# WIDGET
# ============================================================

def plot_muon_g2(m_dark_val, epsilon_val):
    """Plot the dark photon contribution to muon g-2."""
    Delta_a_mu_dark_val = dark_photon_contribution(
        m_dark_val, epsilon_val, alpha_EM, m_mu
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    labels = ['Observed anomaly', 'Dark photon contribution']
    values = [Delta_a_mu/1e-11, Delta_a_mu_dark_val/1e-11]
    colors = ['green', 'blue']

    bars = ax.bar(labels, values, color=colors, alpha=0.7, edgecolor='black')

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                f'{val:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

    ax.set_ylabel(r'$\Delta a_\mu \times 10^{-11}$', fontsize=11)
    ax.set_title('Muon g-2: Observed Anomaly vs. Dark Photon Contribution',
                 fontsize=12, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6, axis='y')

    ratio = Delta_a_mu / Delta_a_mu_dark_val if Delta_a_mu_dark_val > 0 else np.inf

    text_str = (
        f"Dark photon parameters:\n"
        f"  m_dark = {m_dark_val:.4f} GeV\n"
        f"  epsilon = {epsilon_val:.6f}\n"
        f"  alpha_eff = {epsilon_val**2 * alpha_EM:.4e}\n"
        f"\n"
        f"Observed anomaly: {Delta_a_mu/1e-11:.1f} x 10^-11\n"
        f"Dark photon: {Delta_a_mu_dark_val/1e-11:.4f} x 10^-11\n"
        f"Ratio: {ratio:.1f}"
    )
    props = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(0.98, 0.98, text_str, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right', bbox=props)

    plt.tight_layout()
    plt.show()

# Defaults are the FALSIFIED WIN values, retained for reproducibility.
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

# Print audit (non-interactive)
print("=" * 70)
print("DARK PHOTON CONTRIBUTION TO MUON G-2 — GENERAL EXPLORER")
print("=" * 70)
print()
print("STATUS: This is a general explorer, NOT a WIN validation.")
print("        The WIN dark photon values are FALSIFIED (see NOTICE).")
print()
print("Muon g-2 anomaly:")
print(f"  a_mu_SM  = {a_mu_SM:.4e}")
print(f"  a_mu_exp = {a_mu_exp:.4e}")
print(f"  Delta    = {Delta_a_mu:.4e} = {Delta_a_mu/1e-11:.1f} x 10^-11")
print()
print("Default (FALSIFIED) WIN values:")
print(f"  m_dark = 0.291253 GeV, epsilon = 0.001193")
print(f"  Contribution = {dark_photon_contribution(0.291253, 0.001193, alpha_EM, m_mu)/1e-11:.4f} x 10^-11")
print(f"  Ratio to observed = {Delta_a_mu/dark_photon_contribution(0.291253, 0.001193, alpha_EM, m_mu):.1f}")
print()
print("CONCLUSION (conditional on the falsified values):")
print("  The dark photon contribution is ~15x smaller than the observed")
print("  anomaly. Even with the falsified-formula values (0.0996 GeV,")
print("  6.7e-4), the contribution remains ~14x too small. A dark photon")
print("  cannot explain the muon g-2 anomaly in this framework.")
print()
print("NOTE: The muon g-2 anomaly itself is in flux — the 2025 BMW")
print("      lattice result reduces the discrepancy to ~1.8 sigma.")
print("=" * 70)

display(VBox([m_dark_slider, epsilon_slider, out]))
