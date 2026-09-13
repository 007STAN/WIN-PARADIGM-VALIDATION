"""
Proton Radius Measurements (2010–2023) — Reference Figure

Author: Stanley Preschutti (Information Physics Institute, UK)
Status: REFERENCE — not a WIN validation widget.

============================================================================
NOTICE
============================================================================
The proton radius is a QCD quantity. The WIN framework provides the
substrate (d=4, N=64, H=16, V=48) but does NOT derive the proton radius.
There is currently no WIN prediction for R_p.

This figure is included as a REFERENCE for future work. It is not a
validation of the WIN framework, and it should not be cited as one.

If a WIN derivation of R_p is later found, this figure can be extended
to overlay the prediction. Until then, it shows only experimental data.
============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PROTON RADIUS MEASUREMENTS (experimental data only)
# ============================================================

measurements = {
    'CODATA 2014 (e)':  (0.8770, 0.0070, 'electronic'),
    'CREMA 2010 (mu)':  (0.8420, 0.0020, 'muonic'),
    'CREMA 2013 (mu)':  (0.8400, 0.0010, 'muonic'),
    'PRad 2019 (e)':    (0.8310, 0.0140, 'electronic'),
    'Mainz 2021 (e)':   (0.8430, 0.0080, 'electronic'),
    'CODATA 2018':      (0.8414, 0.0019, 'combined'),
    'Muonic 2023':      (0.8408, 0.0020, 'muonic'),
}

def plot_proton_radius():
    fig, ax = plt.subplots(figsize=(12, 6))

    names = list(measurements.keys())
    values = [measurements[n][0] for n in names]
    errors = [measurements[n][1] for n in names]
    types = [measurements[n][2] for n in names]

    colors = {'electronic': 'blue', 'muonic': 'red', 'combined': 'green'}

    for i, (name, val, err, typ) in enumerate(zip(names, values, errors, types)):
        ax.errorbar(val, i, xerr=err, fmt='o', color=colors[typ],
                    markersize=8, capsize=4)

    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names)
    ax.set_xlabel('Proton Charge Radius $R_p$ (fm)', fontsize=12)
    ax.set_title('Proton Radius Measurements (2010–2023)\n'
                 'Reference figure — no WIN prediction shown',
                 fontsize=12, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)

    handles = [plt.Line2D([0], [0], marker='o', color='w',
                          markerfacecolor=colors[t], markersize=8, label=t)
               for t in colors.keys()]
    ax.legend(handles=handles, loc='lower right', frameon=True, facecolor='white')

    plt.tight_layout()
    plt.show()

    print("=" * 70)
    print("PROTON RADIUS MEASUREMENTS — REFERENCE")
    print("=" * 70)
    print()
    print("Status: The proton radius puzzle (~5–7σ discrepancy between")
    print("        electronic and muonic measurements) has largely resolved.")
    print("        Electronic and muonic measurements now agree at ~0.841 fm.")
    print()
    print("WIN framework: Does NOT derive the proton radius. R_p is a QCD")
    print("               quantity. The substrate (d=4, N=64) does not, by")
    print("               itself, determine R_p. This is an OPEN PROBLEM.")
    print()
    print("This figure is a REFERENCE only. It is not a WIN validation.")
    print("=" * 70)

if __name__ == "__main__":
    plot_proton_radius()
