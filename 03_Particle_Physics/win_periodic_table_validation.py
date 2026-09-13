"""
Warped Information Number (WIN) Paradigm — Periodic Table Analysis
Author: Stanley Preschutti (Information Physics Institute, UK)
Description: Analysis of nuclear masses within the WIN framework.

The WIN framework derives the substrate structure (d = 4, H = 16, V = 48, 
N = 64) and the particle spectrum. It does NOT currently derive nuclear 
masses from first principles.

This script presents a phenomenological fit to nuclear masses based on 
the WIN substrate structure. The fit is presented as a starting point for 
future derivation, not as a first-principles result.

The WIN substrate provides:
- The number of Majorana modes: N = 64
- The hidden sector: H = 16
- The visible sector: V = 48
- The spacetime dimension: d = 4

The nuclear mass formula is:
M(A, Z) = Z * m_p + (A - Z) * m_n - B(A, Z)
where B(A, Z) is the binding energy.

The binding energy is given by the semi-empirical mass formula (Bethe-
Weizsäcker). The WIN framework does not currently derive the coefficients.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# WIN SUBSTRATE PARAMETERS
# ============================================================

d = 4                       # Spacetime dimension
H = d**2                    # Hidden sector = 16
V = (d-1) * 2**d            # Visible sector = 48
N = V + H                   # Total substrate = 64

# ============================================================
# SEMI-EMPIRICAL MASS FORMULA (BETHE-WEIZSÄCKER)
# ============================================================

# Coefficients (in MeV)
# These are the standard Bethe-Weizsäcker coefficients, NOT derived from WIN.
a_V = 15.75    # Volume term
a_S = 17.8     # Surface term
a_C = 0.711    # Coulomb term
a_A = 23.7     # Asymmetry term

# Pairing term
def pairing(A, Z):
    """Pairing term of the semi-empirical mass formula."""
    if A % 2 == 1:
        return 0
    elif Z % 2 == 0:
        return 11.18 / np.sqrt(A)  # even-even
    else:
        return -11.18 / np.sqrt(A)  # odd-odd

def binding_energy(A, Z):
    """Semi-empirical binding energy (MeV)."""
    B = (a_V * A 
         - a_S * A**(2/3) 
         - a_C * Z * (Z - 1) / A**(1/3) 
         - a_A * (A - 2*Z)**2 / A 
         + pairing(A, Z))
    return B

def nuclear_mass(A, Z):
    """Nuclear mass from the semi-empirical mass formula (u)."""
    m_p = 1.007276  # proton mass (u)
    m_n = 1.008665  # neutron mass (u)
    m_e = 0.000549  # electron mass (u)
    # Convert binding energy from MeV to u
    # 1 u = 931.494 MeV/c^2
    B_u = binding_energy(A, Z) / 931.494
    M = Z * (m_p + m_e) + (A - Z) * m_n - B_u
    return M

# ============================================================
# WIN-DERIVED CORRECTION (PHENOMENOLOGICAL)
# ============================================================

def win_correction(A, Z):
    """
    WIN correction to the nuclear mass.

    The WIN framework predicts a scale-dependent entropy correction 
    derived from the substrate's finite information capacity. The 
    correction to the nuclear mass is:
    Delta_M / M = (H/N) * (Z / A)
    where H/N = 16/64 = 0.25 is the hidden sector fraction.

    This is a phenomenological correction, not a first-principles 
    derivation. It is presented as a starting point for future work.
    """
    hidden_fraction = H / N  # = 0.25
    correction = hidden_fraction * (Z / A)
    return correction

def win_nuclear_mass(A, Z):
    """WIN-corrected nuclear mass (u)."""
    M = nuclear_mass(A, Z)
    correction = win_correction(A, Z)
    return M * (1 + correction)

# ============================================================
# DATA
# ============================================================

# Precision dataset
precision_elements = [
    (1, "H", 1, 1.008), (2, "He", 4, 4.003), (3, "Li", 7, 6.940),
    (4, "Be", 9, 9.012), (6, "C", 12, 12.011), (7, "N", 14, 14.007),
    (8, "O", 16, 15.999), (10, "Ne", 20, 20.180), (12, "Mg", 24, 24.305),
    (14, "Si", 28, 28.085), (18, "Ar", 40, 39.948), (20, "Ca", 40, 40.078),
    (26, "Fe", 56, 55.845), (30, "Zn", 64, 65.380), (36, "Kr", 84, 83.798),
    (54, "Xe", 131, 131.293), (79, "Au", 197, 196.967), (82, "Pb", 208, 207.200),
    (86, "Rn", 222, 222.000), (92, "U", 238, 238.029), (118, "Og", 294, 294.000)
]

# ============================================================
# ANALYSIS
# ============================================================

def run_validation():
    df = pd.DataFrame(precision_elements, columns=['Z', 'Sym', 'A', 'Real_Mass'])
    
    # Compute semi-empirical mass
    df['M_semi'] = df.apply(lambda row: nuclear_mass(row['A'], row['Z']), axis=1)
    
    # Compute WIN-corrected mass
    df['M_WIN'] = df.apply(lambda row: win_nuclear_mass(row['A'], row['Z']), axis=1)
    
    # Compute ratios
    df['Ratio_semi'] = df['Real_Mass'] / df['M_semi']
    df['Ratio_WIN'] = df['Real_Mass'] / df['M_WIN']
    
    # Filter out Hydrogen (Z=1)
    df_core = df[df['Z'] > 1].copy()
    
    # Statistics
    core_mean_semi = df_core['Ratio_semi'].mean()
    core_std_semi = df_core['Ratio_semi'].std()
    core_mean_WIN = df_core['Ratio_WIN'].mean()
    core_std_WIN = df_core['Ratio_WIN'].std()
    
    df_core['Residual_semi'] = df_core['Ratio_semi'] - core_mean_semi
    df_core['Residual_WIN'] = df_core['Ratio_WIN'] - core_mean_WIN
    
    # Print results
    print("=" * 70)
    print("WIN PARADIGM: PERIODIC TABLE ANALYSIS (Z >= 2)")
    print("=" * 70)
    print()
    print("Substrate parameters:")
    print(f"  d = {d}")
    print(f"  H = {H}")
    print(f"  V = {V}")
    print(f"  N = {N}")
    print(f"  Hidden fraction H/N = {H/N:.4f}")
    print()
    print("Semi-empirical mass formula (Bethe-Weizsäcker):")
    print(f"  Volume term a_V = {a_V} MeV")
    print(f"  Surface term a_S = {a_S} MeV")
    print(f"  Coulomb term a_C = {a_C} MeV")
    print(f"  Asymmetry term a_A = {a_A} MeV")
    print()
    print(f"{'Model':<25} | {'Mean Ratio':>12} | {'Std Dev':>10}")
    print("-" * 55)
    print(f"{'Semi-empirical':<25} | {core_mean_semi:>12.4f} | {core_std_semi:>10.4f}")
    print(f"{'WIN-corrected':<25} | {core_mean_WIN:>12.4f} | {core_std_WIN:>10.4f}")
    print()
    print("NOTE: The semi-empirical mass formula is a PHENOMENOLOGICAL fit.")
    print("The WIN framework does NOT currently derive the coefficients from")
    print("first principles. The WIN correction is a starting point for")
    print("future work.")
    print("=" * 70)
    print()
    print("Detailed results:")
    print(df_core[['Z', 'Sym', 'A', 'Real_Mass', 'M_WIN', 'Ratio_WIN', 'Residual_WIN']].to_string(index=False))
    print("=" * 70)

    # Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # Top panel: residuals
    ax1.scatter(df_core['Z'], df_core['Residual_WIN'], 
                color='#1f77b4', zorder=3, edgecolors='k', s=50,
                label='WIN-corrected')
    ax1.scatter(df_core['Z'], df_core['Residual_semi'], 
                color='#ff7f0e', zorder=2, edgecolors='k', s=50,
                alpha=0.5, label='Semi-empirical')
    ax1.axhline(0, color='black', linestyle='--', alpha=0.7)
    ax1.set_ylabel('Residual', fontsize=11)
    ax1.set_title('WIN Model: Nuclear Mass Residuals', fontsize=13, fontweight='bold')
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(frameon=True, facecolor='white')
    
    # Bottom panel: ratios
    ax2.scatter(df_core['Z'], df_core['Ratio_WIN'], 
                color='#2ca02c', zorder=3, edgecolors='k', s=50,
                label='WIN-corrected')
    ax2.scatter(df_core['Z'], df_core['Ratio_semi'], 
                color='#d62728', zorder=2, edgecolors='k', s=50,
                alpha=0.5, label='Semi-empirical')
    ax2.axhline(1.0, color='black', linestyle='--', alpha=0.7)
    ax2.set_xlabel('Atomic Number (Z)', fontsize=11)
    ax2.set_ylabel('Ratio (Real / Model)', fontsize=11)
    ax2.set_title('Mass Ratios', fontsize=13, fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(frameon=True, facecolor='white')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_validation()
