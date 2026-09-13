"""
Warped Information Number (WIN) Paradigm — Page Curve Analysis
Author: Stanley Preschutti (Information Physics Institute, UK)
Status: CORRECTED Sept 13, 2026 — falsified remnant floor removed.

============================================================================
TRIPWIRE NOTICE
============================================================================
The previous version of this widget applied a "remnant floor":
    S_rad = max(S_rad, (H/N) · S_BH)

This is FALSIFIED for two reasons:

  1. A nonzero remnant floor contradicts the unitarity argument that the
     Page curve is supposed to illustrate. In a unitary theory, the black
     hole fully evaporates, and S_rad → 0 as t → ∞. A floor at 0.25·S_BH
     means 25% of the initial entropy is never radiated — i.e., information
     is permanently lost. That is the very paradox the Page curve resolves.

  2. The value H/N = 16/64 = 0.25 is asserted, not derived. Nothing in the
     WIN framework says the remnant entropy equals H/N times S_BH. If a
     remnant is claimed, it must be derived from the substrate dynamics.

Any future WIN Page curve MUST:
  - Satisfy S_rad(t) → 0 as t → ∞ (unitarity).
  - Derive any remnant from the substrate, not assert it.
  - Use S_BH = s0 · N with s0 from the SYK model (not a free slider) OR
    explicitly label s0 as an input.

See: WIN Research — Sept 13, 2026, Section 5.3 (falsified formulas must be
retracted, not rationalized).
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
    print("NOTE: ipywidgets not available. Run non-interactively or install:")
    print("      pip install ipywidgets")

# ============================================================
# WIN SUBSTRATE PARAMETERS
# ============================================================

d = 4                       # Spacetime dimension (input)
H = 2**d                    # Hidden sector = 16  [FIXED: was d**2]
V = (d - 1) * 2**d          # Visible sector = 48
N_substrate = V + H         # Total substrate = 64

# SYK ground state entropy per Majorana mode (known result)
# This is an INPUT from the SYK literature, not a WIN derivation.
s0_SYK_DEFAULT = 0.2324

# ============================================================
# PAGE CURVE (no remnant floor — unitarity preserved)
# ============================================================

def page_curve(N, s0, gamma_emission, t_max=None, n_points=400):
    """
    Compute the Page curve for a black hole with N Majorana modes.

    This is a TOY MODEL: the black hole is treated as a system with
    S_BH = s0 · N nats, and the radiation entropy is the minimum of
    the thermal entropy and the remaining black hole entropy:

        S_rad(t) = min(γt, S_BH − γt)

    The curve peaks at S_BH/2 at t_Page = S_BH/(2γ), then falls to zero
    as the black hole fully evaporates. No remnant floor is applied —
    the curve reaches zero, consistent with unitarity.

    Parameters:
    - N: number of Majorana modes (substrate size)
    - s0: SYK ground state entropy per mode
    - gamma_emission: emission rate (nats per unit time)
    - t_max: maximum time (default: 2.5 × t_Page)
    - n_points: number of time points

    Returns:
    - times, S_rad, S_BH, t_Page
    """
    S_BH = s0 * N
    t_Page = S_BH / (2 * gamma_emission)

    if t_max is None:
        t_max = 2.5 * t_Page

    times = np.linspace(0, t_max, n_points)

    # Thermal entropy rises linearly
    S_thermal = gamma_emission * times

    # Black hole entropy falls linearly
    S_BH_t = S_BH - gamma_emission * times

    # Page curve: minimum of the two — NO FLOOR
    S_rad = np.minimum(S_thermal, np.maximum(S_BH_t, 0.0))

    # TRIPWIRE: the curve must reach zero at late times (unitarity)
    assert S_rad[-1] < 1e-6, \
        f"TRIPWIRE FAILED: S_rad(t_max) = {S_rad[-1]} ≠ 0. Unitarity violated."

    return times, S_rad, S_BH, t_Page

# ============================================================
# WIDGET
# ============================================================

if HAS_WIDGETS:
    n_slider = widgets.IntSlider(
        value=64, min=16, max=256, step=16,
        description='Capacity (N):',
        style={'description_width': 'initial'}
    )
    s0_slider = widgets.FloatSlider(
        value=s0_SYK_DEFAULT, min=0.1, max=0.5, step=0.001,
        description='SYK s0 (input):',
        style={'description_width': 'initial'}
    )
    gamma_slider = widgets.FloatSlider(
        value=0.1, min=0.01, max=0.5, step=0.01,
        description='Emission rate γ (input):',
        style={'description_width': 'initial'}
    )

    out = widgets.Output()

    def update_plot(N, s0, gamma):
        with out:
            clear_output(wait=True)
            times, S_rad, S_BH, t_Page = page_curve(N, s0, gamma)

            print("=" * 70)
            print("WIN PARADIGM: PAGE CURVE ANALYSIS")
            print("=" * 70)
            print()
            print("Substrate parameters:")
            print(f"  d = {d}")
            print(f"  H = 2^d = {H}  [FIXED: was d**2]")
            print(f"  V = (d-1)·2^d = {V}")
            print(f"  N_substrate = {N_substrate}")
            print()
            print("Black hole parameters (TOY MODEL):")
            print(f"  Number of Majorana modes N = {N}")
            print(f"  SYK entropy per mode s0 = {s0:.4f}  [INPUT, not derived]")
            print(f"  Initial BH entropy S_BH = {S_BH:.4f} nats")
            print(f"  Emission rate γ = {gamma:.4f} nats/time  [INPUT, not derived]")
            print()
            print("Page curve results:")
            print(f"  Page time t_Page = {t_Page:.4f}")
            print(f"  Peak entropy S_BH/2 = {S_BH/2:.4f} nats")
            print(f"  Final entropy S_rad(t_max) = {S_rad[-1]:.6f} nats  (unitarity ✓)")
            print()
            print("STATUS: This is a TOY MODEL, not a derivation from the")
            print("        WIN substrate. The substrate enters only via")
            print("        S_BH = s0 · N. The curve shape is the standard")
            print("        triangle Page curve. Any WIN-specific prediction")
            print("        (remnant, modified Page time, etc.) is an OPEN PROBLEM.")
            print()
            print("REMOVED: The previous 'remnant floor' S_rem = (H/N)·S_BH is")
            print("         falsified — it violates unitarity and was not derived.")
            print("=" * 70)

            # Plot
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

            ax1.plot(times, S_rad, label=r'$S_{rad}(t)$ (Page curve)',
                     color='#1f77b4', linewidth=2.5)
            ax1.axhline(S_BH, color='gray', linestyle='--', alpha=0.5,
                        label=f'Initial $S_{{BH}}$ = {S_BH:.2f}')
            ax1.axhline(S_BH/2, color='orange', linestyle='--', alpha=0.5,
                        label=f'$S_{{BH}}/2$ = {S_BH/2:.2f}')
            ax1.axvline(t_Page, color='green', linestyle='-.', alpha=0.5,
                        label=f'Page time = {t_Page:.2f}')
            ax1.set_ylabel(r'Entropy $S$ (nats)', fontsize=11)
            ax1.set_title('Page Curve — Toy Model (No Remnant Floor)',
                          fontsize=12, fontweight='bold')
            ax1.set_ylim(bottom=0)
            ax1.grid(True, linestyle=':', alpha=0.6)
            ax1.legend(loc='best', frameon=True, facecolor='white', fontsize=9)

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

    page_interactive = widgets.interactive(
        update_plot,
        N=n_slider,
        s0=s0_slider,
        gamma=gamma_slider
    )
    display(page_interactive, out)

# ============================================================
# NON-INTERACTIVE FALLBACK
# ============================================================

if __name__ == "__main__" or not HAS_WIDGETS:
    times, S_rad, S_BH, t_Page = page_curve(N_substrate, s0_SYK_DEFAULT, 0.1)
    print("WIN Page Curve — Default Parameters")
    print(f"  N = {N_substrate}, s0 = {s0_SYK_DEFAULT}, γ = 0.1")
    print(f"  S_BH = {S_BH:.4f} nats")
    print(f"  t_Page = {t_Page:.4f}")
    print(f"  Peak S_rad = {S_rad.max():.4f} nats")
    print(f"  Final S_rad = {S_rad[-1]:.6f} nats (unitarity ✓)")
