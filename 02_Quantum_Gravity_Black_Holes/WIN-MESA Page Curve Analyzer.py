# ============================================================
# WIN PARADIGM — PAGE CURVE ANALYSIS (REVISED)
# ============================================================
"""
Author: Stanley Preschutti (Entropia Research Institute / Information Physics Institute)
ORCID:  0009-0004-5445-1744
Status: REVISED September 16, 2026

============================================================================
PURPOSE
============================================================================
The previous version of this analysis applied a "remnant floor" of
the form S_rad = max(S_rad, (H/N) * S_BH). That floor was falsified
for two reasons:

  1. It violates unitarity. In a unitary theory the black hole fully
     evaporates and S_rad -> 0 as t -> infinity. A floor at 0.25 * S_BH
     means 25% of the entropy is never radiated, which is exactly the
     paradox the Page curve is meant to resolve.

  2. The value H/N = 16/64 = 0.25 was asserted, not derived.

This revision does three things:

  A. Retains the falsification record for transparency.
  B. Presents a clean Page curve with unitarity preserved (S_rad -> 0).
  C. Adds a WIN-specific structural comparison: the substrate has
     N = 64 Majorana modes and a mirror-symmetric spectrum. The
     14 self-paired modes at lambda = 4 are the residual. This
     suggests a connection between the self-canceling vacuum and
     the Page curve's late-time behavior — but the connection is
     structural, not yet a derivation. It is stated as an open
     problem.
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
# WIN SUBSTRATE PARAMETERS
# ============================================================
d = 4
H_sector = 2**d               # 16
V_sector = (d - 1) * 2**d     # 48
N_substrate = V_sector + H_sector  # 64
L = 8

# SYK ground state entropy per Majorana mode (input from literature)
s0_SYK_DEFAULT = 0.2324

# WIN-specific substrate quantities
residual_fraction = 7 / 32    # from the self-canceling vacuum
paired_modes = 50
residual_modes = 14

# ============================================================
# PAGE CURVE (no remnant floor)
# ============================================================
def page_curve(N, s0, gamma_emission, t_max=None, n_points=400):
    """
    Compute the Page curve for a black hole with N Majorana modes.

    This is a TOY MODEL. The black hole is treated as a system with
    S_BH = s0 * N nats, and the radiation entropy is the minimum of
    the thermal entropy and the remaining black hole entropy:

        S_rad(t) = min(gamma * t, S_BH - gamma * t)

    The curve peaks at S_BH/2 at t_Page = S_BH/(2*gamma), then falls
    to zero as the black hole fully evaporates.

    Parameters:
    - N: number of Majorana modes
    - s0: SYK entropy per mode (input)
    - gamma_emission: emission rate (nats per unit time)
    - t_max: maximum time (default 2.5 * t_Page)
    - n_points: number of time samples
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
# WIN-SPECIFIC STRUCTURAL COMPARISON
# ============================================================
def win_structural_comparison(N, s0):
    """
    Compute the WIN-specific structural quantities relevant to the
    black hole evaporation problem:

    - The substrate has N Majorana modes.
    - The Laplacian spectrum is mirror-symmetric; 50 modes pair
      and cancel, 14 self-paired modes survive.
    - The residual fraction of zero-point energy is 7/32.

    If the black hole's entropy is stored in the substrate's mode
    structure, then the residual fraction 7/32 might set the
    late-time entropy of the radiation. This is a structural
    hypothesis, not a derivation.
    """
    S_BH = s0 * N
    S_residual_frac = S_BH * residual_fraction
    S_paired_frac = S_BH * (1 - residual_fraction)
    return {
        "S_BH": S_BH,
        "S_residual_frac": S_residual_frac,
        "S_paired_frac": S_paired_frac,
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
        value=s0_SYK_DEFAULT, min=0.1, max=0.5, step=0.001,
        description='SYK s0 (input):',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='500px'),
    )
    gamma_slider = widgets.FloatSlider(
        value=0.1, min=0.01, max=0.5, step=0.01,
        description='Emission rate gamma:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='500px'),
    )

    out = widgets.Output()

    def update_plot(N, s0, gamma):
        with out:
            clear_output(wait=True)
            times, S_rad, S_BH, t_Page = page_curve(N, s0, gamma)
            struct = win_structural_comparison(N, s0)

            print("=" * 72)
            print("WIN PARADIGM: PAGE CURVE ANALYSIS (REVISED)")
            print("=" * 72)
            print()
            print("Substrate parameters (from d = 4):")
            print(f"  d = {d}")
            print(f"  H_sector = 2^d = {H_sector}")
            print(f"  V_sector = (d-1)*2^d = {V_sector}")
            print(f"  N_substrate = {N_substrate}")
            print(f"  L = {L} (8x8 torus)")
            print()
            print("Black hole parameters (toy model):")
            print(f"  N (Majorana modes) = {N}")
            print(f"  s0 (SYK entropy per mode) = {s0:.4f}   [input]")
            print(f"  S_BH (initial entropy) = {S_BH:.4f} nats")
            print(f"  gamma (emission rate) = {gamma:.4f} nats/time  [input]")
            print()
            print("Page curve results:")
            print(f"  Page time t_Page = {t_Page:.4f}")
            print(f"  Peak entropy S_BH/2 = {S_BH/2:.4f} nats")
            print(f"  Final S_rad(t_max) = {S_rad[-1]:.6f} nats  (unitarity ok)")
            print()
            print("WIN structural comparison:")
            print(f"  Total zero-point units: 128")
            print(f"  Paired zero-point units: 100  (50 modes, cancel exactly)")
            print(f"  Residual units: 28  (14 self-paired modes at lambda = 4)")
            print(f"  Residual fraction: {residual_fraction:.4f} = 7/32")
            print()
            print("  If the black hole's entropy is stored in the substrate's")
            print("  mode structure, the residual fraction 7/32 = "
                  f"{residual_fraction:.4f} might")
            print("  set a late-time entropy scale. This is a STRUCTURAL")
            print("  HYPOTHESIS, not a derivation. No WIN-specific")
            print("  modification to the Page curve is currently derived.")
            print()
            print("STATUS: standard Page curve. Unitarity preserved.")
            print("        S_rad -> 0 as t -> infinity. No remnant floor.")
            print("=" * 72)

            # --- Figure: three panels ---
            fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

            # Panel 1: Page curve
            ax = axes[0]
            ax.plot(times, S_rad, label=r'$S_{rad}(t)$',
                    color='#1f77b4', linewidth=2.5)
            ax.axhline(S_BH, color='gray', linestyle='--', alpha=0.5,
                       label=f'Initial $S_{{BH}}$')
            ax.axhline(S_BH/2, color='orange', linestyle='--', alpha=0.5,
                       label=r'$S_{BH}/2$')
            ax.axvline(t_Page, color='green', linestyle='-.', alpha=0.5,
                       label=f'Page time')
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

            # Panel 3: WIN structural decomposition
            ax = axes[2]
            labels = ['Paired\n(cancel)', 'Residual\n(survive)']
            values = [struct['S_paired_frac'], struct['S_residual_frac']]
            colors_bar = ['#888888', '#C44E52']
            bars = ax.bar(labels, values, color=colors_bar,
                          edgecolor='black', linewidth=1.5, width=0.6)
            for bar, val in zip(bars, values):
                ax.text(bar.get_x() + bar.get_width()/2, val + 0.005,
                        f'{val:.4f}', ha='center', va='bottom',
                        fontsize=11, fontweight='bold')
            ax.set_ylabel(r'Entropy (nats)', fontsize=11)
            ax.set_title('WIN structural decomposition',
                         fontsize=12, fontweight='bold')
            ax.grid(True, linestyle=':', alpha=0.6, axis='y')

            plt.tight_layout()
            plt.show()

    page_interactive = widgets.interactive(
        update_plot,
        N=n_slider,
        s0=s0_slider,
        gamma=gamma_slider,
    )
    display(page_interactive, out)

# ============================================================
# NON-INTERACTIVE FALLBACK
# ============================================================
if __name__ == "__main__" or not HAS_WIDGETS:
    times, S_rad, S_BH, t_Page = page_curve(
        N_substrate, s0_SYK_DEFAULT, 0.1
    )
    struct = win_structural_comparison(N_substrate, s0_SYK_DEFAULT)

    print("=" * 72)
    print("WIN PAGE CURVE — DEFAULT PARAMETERS")
    print("=" * 72)
    print()
    print(f"  N = {N_substrate}")
    print(f"  s0 = {s0_SYK_DEFAULT}")
    print(f"  gamma = 0.1")
    print()
    print(f"  S_BH = {S_BH:.4f} nats")
    print(f"  t_Page = {t_Page:.4f}")
    print(f"  Peak S_rad = {S_rad.max():.4f} nats")
    print(f"  Final S_rad = {S_rad[-1]:.6f} nats (unitarity ok)")
    print()
    print("  WIN structural comparison:")
    print(f"    Paired entropy: {struct['S_paired_frac']:.4f} nats")
    print(f"    Residual entropy: {struct['S_residual_frac']:.4f} nats")
    print(f"    Residual fraction: 7/32 = {residual_fraction:.4f}")
    print()
    print("  STATUS: standard Page curve. Unitarity preserved.")
    print("          S_rad -> 0 as t -> infinity. No remnant floor.")
