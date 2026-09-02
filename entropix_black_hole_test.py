"""
Entropix Mesa Framework — Black Hole Evaporation & Page Curve Audit
Description: Simulates the N=64 Majorana substrate Page curve, Wishart ensemble 
variance suppression, and 8D archival persistence transfer.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_entropix_page_curve():
    N = 64
    s0 = 0.232  # Microcanonical entropy coefficient per Majorana
    effective_entropy = s0 * N  # ~14.848 nats
    
    # Entropix Mesa parameters from threading diagnostics
    persistence_residual = 0.0244 * effective_entropy
    saturation_ceiling = 0.039 * effective_entropy
    
    # Time evolution parameters
    gamma = 0.08  # Emission rate via stochastic barrier fluctuations
    times = np.linspace(0, 250, 500)
    
    s_rad = []
    for t in times:
        thermal_growth = gamma * t
        evaporating_bh = effective_entropy - gamma * t + persistence_residual
        val = min(thermal_growth, evaporating_bh)
        
        # Enforce terminal saturation ceiling at late remnant stage
        if t > 120 and val < saturation_ceiling:
            val = saturation_ceiling
        s_rad.append(max(0.0, val))
        
    # Wishart ensemble variance estimation (suppressed as e^-S0*N)
    d_b = np.exp(effective_entropy)
    var_s = np.pi**2 / (6.0 * d_b)
    
    print("=" * 65)
    print("ENTROPIX MESA: BLACK HOLE EVAPORATION & PAGE CURVE AUDIT")
    print("=" * 65)
    print(f"Substrate Capacity (N)      : {N}[cite: 2]")
    print(f"Effective Entropy (S_0*N)   : {effective_entropy:.3f}[cite: 2]")
    print(f"Persistence Residual (2.44%): {persistence_residual:.4f}[cite: 2]")
    print(f"Terminal Ceiling (3.90%)    : {saturation_ceiling:.4f}[cite: 2]")
    print(f"Wishart Ensemble Variance   : {var_s:.2e}[cite: 2]")
    print("=" * 65)

    # Plotting Unitary Page Curve
    plt.figure(figsize=(10, 5))
    plt.plot(times, s_rad, label='Unitary Page Curve ($S_{rad}$)', color='#1f77b4', linewidth=2.5)
    plt.axhline(persistence_residual, color='orange', linestyle='--', label='Persistence Residual (2.44%)')
    plt.axhline(saturation_ceiling, color='red', linestyle=':', label='Terminal Saturation Ceiling (3.90%)')
    
    plt.title('Entropix Mesa: Unitary Page Curve with 8D Persistence Transfer', fontsize=12, fontweight='bold')
    plt.xlabel('Normalized Time ($t$)', fontsize=11)
    plt.ylabel('Radiation Entanglement Entropy ($S_{rad}$)', fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, facecolor='white')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_entropix_page_curve()