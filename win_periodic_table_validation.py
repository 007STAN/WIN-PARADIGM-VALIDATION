"""
Warped Information Number (WIN) Paradigm — Periodic Table Validation Suite
Author: Stanley Preschutti (Entropia Research Institute)
Description: Tests the corrected mass formula and IDR function across the 
periodic table (Z = 1 to 118), isolates single-proton boundary exceptions (H), 
and computes multi-nucleon core baseline statistics.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def idr(z):
    """Returns Information Dissipation Rate (%) for any atomic number Z."""
    if z <= 2:
        return 2.44 + 0.14 * (z - 1)
    elif z <= 10:
        return 2.58 + 0.06 * (z - 2)
    elif z <= 20:
        return 3.12 + 0.005 * (z - 10)
    else:
        return 3.17 + 0.0041 * (z - 20)

def m_win_corrected(z, a):
    """Computes m_WIN_corrected (u) for any atomic number Z and mass number A."""
    raw_z = z * 0.01803
    idr_val = idr(z)
    idr_factor = 1 / (1 - idr_val / 100)
    mesa_factor = 0.703
    neutron_factor = 1 + 0.001 * (a - z)
    return raw_z * idr_factor * mesa_factor * neutron_factor

def run_validation():
    # Precision dataset including boundary elements and shell closures
    precision_elements = [
        (1, "H", 1, 1.008), (2, "He", 4, 4.003), (3, "Li", 7, 6.940),
        (4, "Be", 9, 9.012), (6, "C", 12, 12.011), (7, "N", 14, 14.007),
        (8, "O", 16, 15.999), (10, "Ne", 20, 20.180), (12, "Mg", 24, 24.305),
        (14, "Si", 28, 28.085), (18, "Ar", 40, 39.948), (20, "Ca", 40, 40.078),
        (26, "Fe", 56, 55.845), (30, "Zn", 64, 65.380), (36, "Kr", 84, 83.798),
        (54, "Xe", 131, 131.293), (79, "Au", 197, 196.967), (82, "Pb", 208, 207.200),
        (86, "Rn", 222, 222.000), (92, "U", 238, 238.029), (118, "Og", 294, 294.000)
    ]

    df = pd.DataFrame(precision_elements, columns=['Z', 'Sym', 'A', 'Real_Mass'])
    df['m_WIN'] = df.apply(lambda row: m_win_corrected(row['Z'], row['A']), axis=1)
    df['Ratio'] = df['Real_Mass'] / df['m_WIN']

    # Filter out Hydrogen (Z=1) to establish the true multi-nucleon core baseline
    df_core = df[df['Z'] > 1].copy()
    core_mean = df_core['Ratio'].mean()
    core_std = df_core['Ratio'].std()

    df_core['Residual'] = df_core['Ratio'] - core_mean

    print("=" * 45)
    print("WIN PARADIGM: CORE PERIODIC TABLE BASELINE (Z >= 2)")
    print("=" * 45)
    print(f"Core Mean Ratio : {core_mean:.2f}")
    print(f"Core Std Dev    : {core_std:.2f}\n")
    print(df_core[['Z', 'Sym', 'Ratio', 'Residual']].to_string(index=False))
    print("=" * 45)

    # Plotting High-Fidelity Residuals (Z >= 2)
    plt.figure(figsize=(11, 5))
    plt.scatter(df_core['Z'], df_core['Residual'], color='#1f77b4', zorder=3, edgecolors='k', s=50)
    plt.axhline(0, color='black', linestyle='--', alpha=0.7, label='Core Mean Baseline')
    plt.fill_between([df_core['Z'].min(), df_core['Z'].max()], -core_std, core_std, color='gray', alpha=0.15, label=f'±1 Std Dev ({core_std:.2f})')

    # Annotate key shell boundaries
    for _, row in df_core.iterrows():
        if row['Z'] in [2, 8, 20, 54, 82, 118]:
            plt.annotate(row['Sym'], (row['Z'], row['Residual']), 
                         textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

    plt.title('WIN Model Core Scaling Residuals (Z >= 2)', fontsize=13, fontweight='bold')
    plt.xlabel('Atomic Number (Z)', fontsize=11)
    plt.ylabel('Residual (Ratio - Core Mean)', fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, facecolor='white')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_validation()