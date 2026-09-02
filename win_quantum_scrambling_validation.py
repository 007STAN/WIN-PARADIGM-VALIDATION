"""
Warped Information Number (WIN) Paradigm — Quantum Scrambling Validation Suite
Author: Stanley Preschutti (Entropia Research Institute)
Description: Simulates out-of-time-order correlators (OTOCs) using toy-model 
substrates and validates the recalibrated 'Goldilocks' zone for chaos damping (gamma).
"""

import numpy as np
import matplotlib.pyplot as plt

def chaos_damping_rate(k_param):
    """Recalibrated WIN chaos damping rate gamma ensuring stability across scale k."""
    return 0.90 + 0.25 * np.log(k_param)

def simulated_otoc(t, lyapunov, gamma):
    """
    Models regulated OTOC growth behavior under WIN chaos damping.
    C(t) represents the commutator magnitude over time.
    """
    # Regulated exponential growth avoiding unphysical runaway
    return np.exp(lyapunov * t) * np.exp(-gamma * t)

def run_quantum_scrambling_validation():
    time = np.linspace(0, 10, 200)
    lyapunov_lambda = 0.85  # Base scrambling rate
    
    # Evaluate different scale parameters k representing the 'Goldilocks' zone
    k_values = [1.0, 2.5, 5.0, 10.0]
    
    print("=" * 65)
    print("WIN PARADIGM: QUANTUM SCRAMBLING & CHAOS DAMPING AUDIT (OTOCs)")
    print("=" * 65)
    print(f"{'Scale (k)':<12} | {'Damping (gamma)':<18} | {'Peak OTOC Val':<15} | {'Status':<10}")
    print("-" * 65)
    
    results = []
    for k in k_values:
        gamma = chaos_damping_rate(k)
        otoc_curve = simulated_otoc(time, lyapunov_lambda, gamma)
        peak_val = np.max(otoc_curve)
        status = "STABLE" if peak_val <= 1.5 else "REVIEW"
        results.append((k, gamma, peak_val, otoc_curve))
        print(f"{k:<12.1f} | {gamma:<18.4f} | {peak_val:<15.4f} | {status:<10}")
    print("=" * 65)

    # Plotting OTOC Decay / Regulation Curves
    plt.figure(figsize=(10, 6))
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    for idx, (k, gamma, _, curve) in enumerate(results):
        plt.plot(time, curve, label=f'k = {k} ($\\gamma$ = {gamma:.3f})', color=colors[idx], linewidth=2.2)
        
    plt.axhline(1.0, color='black', linestyle='--', alpha=0.5, label='Equilibrium Threshold')
    
    plt.title('Quantum Scrambling Regulation: Toy-Model OTOCs under Recalibrated WIN Damping', fontsize=12, fontweight='bold')
    plt.ylabel('Regulated OTOC Magnitude $C(t)$', fontsize=11)
    plt.xlabel('Normalized Time ($t$)', fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, facecolor='white', loc='upper right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_quantum_scrambling_validation()