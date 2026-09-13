"""
Warped Information Number (WIN) Paradigm — Proton Radius Analysis
Author: Stanley Preschutti (Information Physics Institute, UK)
Description: Analysis of the proton radius within the WIN framework.

The proton radius puzzle was the discrepancy between:
- Electronic measurement: R_p = 0.877 +/- 0.007 fm (CODATA 2014)
- Muonic measurement: R_p = 0.841 +/- 0.001 fm (CREMA 2010, 2013)

The discrepancy was ~5-7 sigma.

However, recent measurements have largely resolved the puzzle:
- PRad (2019): R_p = 0.831 +/- 0.014 fm
- Mainz (2021): R_p = 0.843 +/- 0.008 fm
- CODATA 2018: R_p = 0.8414 +/- 0.0019 fm

The electronic and muonic measurements now agree.

The WIN framework does NOT derive the proton radius. The proton radius
is a QCD quantity, and the WIN framework provides the substrate but not
the QCD calculation.
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# WIN SUBSTRATE PARAMETERS
# ============================================================

d = 4                       # Spacetime dimension
H = d**2                    # Hidden sector = 16
V = (d-1) * 2**d            # Visible sector = 48
N = V + H                   # Total substrate = 64
s0_SYK = 0.2324             # SYK ground state entropy per mode

# ============================================================
# PROTON RADIUS MEASUREMENTS
# ============================================================

measurements = {
    'CODATA 2014 (e)': (0.877, 0.007, 'electronic'),
    'CREMA 2010 (mu)': (0.842, 0.002, 'muonic'),
    'CREMA 2013 (mu)': (0.840, 0.001, 'muonic'),
    'PRad 2019 (e)': (0.831, 0.014, 'electronic'),
    'Mainz 2021 (e)': (0.843, 0.008, 'electronic'),
    'CODATA 2018': (0.8414, 0.0019, 'combined'),
    'Muonic 2023': (0.8408, 0.0020, 'muonic'),
}

# ============================================================
# ANALYSIS
# ============================================================

def plot_proton_radius():
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot measurements
    names = list(measurements.keys())
    values = [measurements[n][0] for n in names]
    errors = [measurements[n][1] for n in names]
    types = [measurements[n][2] for n in names]

    colors = {'electronic': 'blue', 'muonic': 'red', 'combined': 'green'}

    for i, (name, val, err, typ) in enumerate(zip(names, values, errors, types)):
        ax.errorbar(val, i, xerr=err, fmt='o', color=colors[typ], 
                    markersize=8, capsize=4, label=typ if i < 3 else None)

    # Add labels
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names)
    ax.set_xlabel('Proton Charge Radius $R_p$ (fm)', fontsize=12)
    ax.set_title('Proton Radius Puzzle: Measurements (2010-2023)', fontsize=13, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)

    # Legend
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[t], 
                          markersize=8, label=t) for t in colors.keys()]
    ax.legend(handles=handles, loc='lower right', frameon=True, facecolor='white')

    plt.tight_layout()
    plt.show()

    # Print audit
    print("=" * 70)
    print("WIN PARADIGM: PROTON RADIUS ANALYSIS")
    print("=" * 70)
    print()
    print("Substrate parameters:")
    print(f"  d = {d}")
    print(f"  H = {H}")
    print(f"  V = {V}")
    print(f"  N = {N}")
    print(f"  s0 = {s0_SYK}")
    print()
    print("Proton radius measurements (fm):")
    for name, (val, err, typ) in measurements.items():
        print(f"  {name}: {val} +/- {err} ({typ})")
    print()
    print("Status:")
    print("  The proton radius puzzle was the ~5-7 sigma discrepancy")
    print("  between electronic (0.877 fm) and muonic (0.841 fm) measurements.")
    print()
    print("  Recent measurements (PRad 2019, Mainz 2021, CODATA 2018)")
    print("  have largely resolved the puzzle. The electronic and muonic")
    print("  measurements now agree at ~0.841 fm.")
    print()
    print("  The WIN framework does NOT derive the proton radius.")
    print("  The proton radius is a QCD quantity, and the WIN framework")
    print("  provides the substrate but not the QCD calculation.")
    print()
    print("  This is an OPEN PROBLEM for the WIN framework.")
    print("=" * 70)

if __name__ == "__main__":
    plot_proton_radius()
