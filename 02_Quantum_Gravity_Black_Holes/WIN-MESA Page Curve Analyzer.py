# ============================================================
# WIN PARADIGM — PAGE CURVE ANALYSIS (v2, September 2026)
# ============================================================
"""
Author: Stanley Preschutti (Entropia Research Institute / Information Physics Institute)
ORCID:  0009-0004-5445-1744
Status: REVISED September 25, 2026

============================================================================
PURPOSE
============================================================================
The Page curve for a black hole with N Majorana modes, using the WIN
substrate's mirror-cancellation structure as the structural template.

Two revisions since the September 16 version:

  1. SYK is removed from the framing. The framework's algebraic
     substrate is the Hodge complex Ω⁰ ⊕ Ω¹ ⊕ Ω² on the 8×8 torus.
     The quantity previously labeled "SYK s0" is now expressed as
     the maximally-mixed entropy at λ = 4, S = log 56, which is
     derived from the Hodge complex.

  2. The residual fraction 7/32 is stated explicitly as a structural
     quantity from the mirror-cancellation structure of the 64-site
     substrate, and its relevance to the Page curve is labeled as
     a hypothesis, not a derivation.

HONEST STATUS:
  The framework has NOT yet derived black hole entropy from the
  Hodge complex. The Page curve here is a toy model with WIN-native
  parameters. A first-principles derivation is OPEN (Tier 3 in the
  handoff).
============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

try:
    import ipywidgets as widgets
    from IPython.display import display, clear_output
    HAS_WIDGETS = True
except ImportError:
    HAS_WIDGETS = False
    print("NOTE: ipywidgets not available.")

# ============================================================
# SUBSTRATE PARAMETERS
# ============================================================
d = 4
H_sector = 2**d                    # 16
V_sector = (d - 1) * 2**d          # 48
N_sites = V_sector + H_sector      # 64
L = 8

# Hodge complex dimensions
dim_Omega0 = 64
dim_Omega1 = 128
dim_Omega2 = 64
dim_Hodge = dim_Omega0 + dim_Omega1 + dim_Omega2   # 256

# Content at λ = 4
dim_56 = 56                        # 9A₁ ⊕ 5A₂ ⊕ 7B₁ ⊕ 7B₂ ⊕ 14E
dim_visible = 14                   # Ω⁰|λ=4
dim_hidden = 42                    # Ω¹|λ=4 ⊕ Ω²|λ=4

# Maximally-mixed entropy at λ = 4 (Hodge flatness theorem)
S_lambda4 = np.log(dim_56)         # ≈ 4.025 nats
S_visible = np.log(dim_visible)    # ≈ 2.639 nats

# Mirror-cancellation structure on the 64-site substrate
paired_modes    = 50
residual_modes  = 14
total_units     = 2 * paired_modes + 2 * residual_modes   # 128
residual_units  = 2 * residual_modes                      # 28
residual_fraction = residual_units / total_units          # 7/32
paired_fraction   = 1 - residual_fraction

# ============================================================
# PAGE CURVE (no remnant floor)
# ============================================================
def page_curve(N, s0, gamma_emission, t_max=None, n_points=400):
    """
    Page curve for a black hole with N Majorana modes.

    Toy model: S_BH = s0 * N. Radiation entropy is the minimum of
    the thermal entropy and the remaining black hole entropy:

        S_rad(t) = min(gamma·t, S_BH - gamma·t)

    Peaks at S_BH/2 at t_Page = S_BH/(2·gamma), then falls to zero.
    """
    S_BH = s0 * N
    t_Page = S_BH / (2 * gamma_emission)
    if t_max is None:
        t_max = 2.5 * t_Page
    times = np.linspace(0, t_max, n_points)
    S_thermal = gamma_emission * times
    S_BH_t = S_BH - gamma_emission * times
    S_rad = np.minimum(S_thermal, np.maximum(S_BH_t, 0.0))
    assert S_rad[-1] < 1e-6, \
        f"TRIPWIRE: S_rad(t_max) = {S_rad[-1]} != 0. Unitarity violated."
    return times, S_rad, S_BH, t_Page

# ============================================================
# STRUCTURAL COMPARISON
# ============================================================
def substrate_comparison(N, s0):
    """
    Structural quantities from the substrate's mirror cancellation.
    Relevance to the Page curve is a hypothesis, not a derivation.
    """
    S_BH = s0 * N
    return {
        "S_BH": S_BH,
        "S_paired_frac": S_BH * paired_fraction,
        "S_residual_frac": S_BH * residual_fraction,
        "residual_modes": residual_modes,
        "paired_modes": paired_modes,
    }

# ============================================================
# INTERACTIVE WIDGET
# ============================================================
if HAS_WIDGETS:
    n_slider = widgets.IntSlider(
        value=64, min=16, max=256, step=16,
        description='Capacity (N):',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='500px'),
    )
    s0_slider = widgets.FloatSlider(
        value=0.2324, min=0.1, max=0.5, step=0.001,
        description='Entropy per mode:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='500px'),
    )
    gamma_slider = widgets.FloatSlider(
        value=0.1, min=0.01, max=0.5, step=0.01,
        description='Emission rate γ:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='500px'),
    )

    out = widgets.Output()

    def update_plot(N, s0, gamma):
        with out:
            clear_output(wait=True)
            times, S_rad, S_BH, t_Page = page_curve(N, s0, gamma)
            struct = substrate_comparison(N, s0)

            print("=" * 72)
            print("WIN PARADIGM: PAGE CURVE ANALYSIS (v2)")
            print("=" * 72)
            print()
            print("Substrate parameters (from d = 4):")
            print(f"  d = {d}")
            print(f"  Substrate sites N = {N_sites}  (8 × 8 torus)")
            print(f"  Hodge complex dim = {dim_Hodge}  "
                  f"(Ω⁰={dim_Omega0}, Ω¹={dim_Omega1}, Ω²={dim_Omega2})")
            print(f"  Content at λ = 4: {dim_56} states "
                  f"({dim_visible} visible + {dim_hidden} hidden)")
            print(f"  Hodge-flat entropy at λ = 4:  S = log 56 = "
                  f"{S_lambda4:.4f} nats")
            print()
            print("Black hole parameters (toy model):")
            print(f"  N (Majorana modes) = {N}")
            print(f"  s0 (entropy per mode) = {s0:.4f}   [input]")
            print(f"  S_BH = s0 · N = {S_BH:.4f} nats")
            print(f"  γ (emission rate) = {gamma:.4f} nats/time   [input]")
            print()
            print("Page curve results:")
            print(f"  Page time t_Page = {t_Page:.4f}")
            print(f"  Peak entropy S_BH/2 = {S_BH/2:.4f} nats")
            print(f"  Final S_rad(t_max) = {S_rad[-1]:.6f} nats  (unitarity ok)")
            print()
            print("Substrate structural comparison:")
            print(f"  Total zero-point units: {total_units}")
            print(f"  Paired units (cancel):  {2*paired_modes}")
            print(f"  Residual units:         {residual_units}  "
                  f"({residual_modes} self-paired modes at λ = 4)")
            print(f"  Residual fraction:      {residual_fraction:.4f} = 7/32")
            print()
            print("  The residual fraction 7/32 is a STRUCTURAL quantity of the")
            print("  substrate's mirror cancellation. Its connection to the")
            print("  Page curve's late-time behavior is a HYPOTHESIS, not a")
            print("  derivation. No WIN-specific modification to the standard")
            print("  Page curve is currently derived.")
            print()
            print("HONEST STATUS:")
            print("  → Standard unitarity-preserving Page curve.")
            print("  → No remnant floor. S_rad → 0 as t → ∞.")
            print("  → Deriving black hole entropy from the Hodge complex is")
            print("    an OPEN problem (Tier 3 of the framework handoff).")
            print("=" * 72)

            fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

            # Panel 1: Page curve
            ax = axes[0]
            ax.plot(times, S_rad, color='#1f77b4', linewidth=2.5,
                    label=r'$S_{rad}(t)$')
            ax.axhline(S_BH, color='gray', linestyle='--', alpha=0.5,
                       label=r'Initial $S_{BH}$')
            ax.axhline(S_BH/2, color='orange', linestyle='--', alpha=0.5,
                       label=r'$S_{BH}/2$')
            ax.axvline(t_Page, color='green', linestyle='-.', alpha=0.5,
                       label='Page time')
            ax.set_xlabel('Time $t$', fontsize=11)
            ax.set_ylabel(r'Entropy $S$ (nats)', fontsize=11)
            ax.set_title('Page curve (no remnant floor)',
                         fontsize=12, fontweight='bold')
            ax.set_ylim(bottom=0)
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc='best', frameon=True, facecolor='white',
                      fontsize=9)

            # Panel 2: entropy production rate
            ax = axes[1]
            dS_dt = np.gradient(S_rad, times)
            ax.plot(times, dS_dt, color='#d62728', linewidth=2.5)
            ax.axhline(0, color='black', linestyle='--', alpha=0.5)
            ax.axvline(t_Page, color='green', linestyle='-.', alpha=0.5,
                       label='Page time')
            ax.set_xlabel('Time $t$', fontsize=11)
            ax.set_ylabel(r'$dS_{rad}/dt$', fontsize=11)
            ax.set_title('Entropy production rate',
                         fontsize=12, fontweight='bold')
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc='best', frameon=True, facecolor='white',
                      fontsize=9)

            # Panel 3: substrate structural decomposition
            ax = axes[2]
            labels = ['Paired\n(cancel)', 'Residual\n(survive)']
            values = [struct['S_paired_frac'], struct['S_residual_frac']]
            bars = ax.bar(labels, values, color=['#888888', '#C44E52'],
                          edgecolor='black', linewidth=1.5, width=0.6)
            for bar, val in zip(bars, values):
                ax.text(bar.get_x() + bar.get_width()/2, val + 0.005,
                        f'{val:.4f}', ha='center', va='bottom',
                        fontsize=11, fontweight='bold')
            ax.set_ylabel(r'Entropy (nats)', fontsize=11)
            ax.set_title('Substrate structural decomposition',
                         fontsize=12, fontweight='bold')
            ax.grid(True, linestyle=':', alpha=0.6, axis='y')

            plt.tight_layout()
            plt.show()

    page_interactive = widgets.interactive(
        update_plot, N=n_slider, s0=s0_slider, gamma=gamma_slider,
    )
    display(page_interactive, out)

# ============================================================
# NON-INTERACTIVE FALLBACK
# ============================================================
if __name__ == "__main__" or not HAS_WIDGETS:
    times, S_rad, S_BH, t_Page = page_curve(N_sites, 0.2324, 0.1)
    struct = substrate_comparison(N_sites, 0.2324)

    print("=" * 72)
    print("WIN PAGE CURVE — DEFAULT PARAMETERS (v2)")
    print("=" * 72)
    print()
    print(f"  Substrate: N = {N_sites} sites (8 × 8 torus)")
    print(f"  Hodge complex dim: {dim_Hodge}")
    print(f"  Hodge-flat entropy at λ = 4: log 56 = {S_lambda4:.4f} nats")
    print()
    print(f"  Black hole toy model: N = {N_sites}, s0 = 0.2324, γ = 0.1")
    print(f"  S_BH = {S_BH:.4f} nats")
    print(f"  t_Page = {t_Page:.4f}")
    print(f"  Peak S_rad = {S_rad.max():.4f} nats")
    print(f"  Final S_rad = {S_rad[-1]:.6f} nats  (unitarity ok)")
    print()
    print("  Substrate structural decomposition:")
    print(f"    Paired entropy: {struct['S_paired_frac']:.4f} nats")
    print(f"    Residual entropy: {struct['S_residual_frac']:.4f} nats")
    print(f"    Residual fraction: 7/32 = {residual_fraction:.4f}")
    print()
    print("HONEST STATUS:")
    print("  → Standard unitarity-preserving Page curve.")
    print("  → No remnant floor. S_rad → 0 as t → ∞.")
    print("  → Deriving black hole entropy from the Hodge complex is OPEN.")
