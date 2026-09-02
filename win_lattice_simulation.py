"""
Warped Information Number (WIN) Paradigm — N=64 Majorana Lattice Simulation
Author: Stanley Preschutti (Entropia Research Institute)
Description: Models the closed N=64 Majorana fermion lattice substrate, sector 
partition (V_48 + H_16), complex fermion mapping, and the Master Evolution Equation.
"""

import numpy as np
import matplotlib.pyplot as plt

class WINMajoranaLattice:
    def __init__(self):
        self.total_nodes = 64
        self.visible_dim = 48
        self.hidden_dim = 16
        
        # Initialize the N=64 Majorana modes (gamma_i = gamma_i^dagger)
        # Represented here as abstract index states satisfying {gamma_i, gamma_j} = 2 * delta_ij
        self.lattice_nodes = np.arange(1, self.total_nodes + 1)
        
        # Sector Partition: V_48 (Visible) and H_16 (Hidden Reservoir)
        self.visible_sector = self.lattice_nodes[:self.visible_dim]
        self.hidden_sector = self.lattice_nodes[self.visible_dim:]

    def construct_complex_fermions(self):
        """
        Pairs Majoranas to form complex fermionic modes: 
        psi_k = 0.5 * (gamma_{2k-1} + i * gamma_{2k}) yielding 32 complex modes.
        """
        complex_modes = []
        for k in range(1, (self.total_nodes // 2) + 1):
            # Conceptual pairing mapping for the U(32) subgroup
            g1 = 2 * k - 1
            g2 = 2 * k
            complex_modes.append((k, g1, g2))
        return complex_modes

    def master_evolution_step(self, W_grid, delta_c, delta_tau, lambda_l):
        """
        Solves a discrete step of the Master WIN Differential Equation:
        d_W / d_tau = partial(W) / partial(C) - lambda_L * W + nabla^2 * W
        where W = delta_I_mut * d_code (Warped Information Number scalar field).
        """
        # Spatial diffusion term (nabla^2 W) via finite difference
        laplacian_w = np.gradient(np.gradient(W_grid))
        
        # Computational path gradient term (partial W / partial C)
        transport_w = np.gradient(W_grid, delta_c)
        
        # Chaos scrambling sink term (- lambda_L * W)
        scrambling_sink = lambda_l * W_grid
        
        # Combined rate of change
        dW_dtau = transport_w - scrambling_sink + laplacian_w
        
        # Update scalar field W over persistence depth increment delta_tau
        W_updated = W_grid + dW_dtau * delta_tau
        return W_updated

def run_lattice_audit():
    lattice = WINMajoranaLattice()
    
    print("=" * 65)
    print("WIN PARADIGM: N=64 MAJORANA SUBSTRATE ARCHITECTURE AUDIT")
    print("=" * 65)
    print(f"Total Substrate Capacity  : {lattice.total_nodes} Majorana nodes")
    print(f"Visible Sector (V_48)     : Nodes 1 to {lattice.visible_dim} (Observable Physics)[cite: 1]")
    print(f"Hidden Sector (H_16)      : Nodes {lattice.visible_dim + 1} to {lattice.total_nodes} (Entanglement Reservoir)[cite: 1]")
    
    complex_modes = lattice.construct_complex_fermions()
    print(f"Complex Fermion Mapping   : {len(complex_modes)} complex modes (U(32) Subgroup)[cite: 1]")
    
    # Simulate Master Evolution Equation Across Spatial/Computational Grid
    space_points = 50
    C_space = np.linspace(0, 10, space_points)
    delta_c = C_space[1] - C_space[0]
    delta_tau = 0.01
    lambda_l = 0.85  # Chaos exponent
    
    # Initial Warped Information Number scalar field (W = delta_I_mut * d_code)
    # Baseline protected state with d_code >= 5
    W_field = 5.0 * np.exp(-((C_space - 5.0)**2) / 2.0)
    
    # Run 100 update cycles of persistence depth tau
    cycles = 100
    history = [W_field.copy()]
    for _ in range(cycles):
        W_field = lattice.master_evolution_step(W_field, delta_c, delta_tau, lambda_l)
        history.append(W_field.copy())
        
    print(f"Master Evolution Engine   : Executed {cycles} update cycles successfully.")
    print(f"Final Peak W Field Value  : {np.max(W_field):.4f} Nats*bits")
    print("=" * 65)

    # Plotting Substrate Evolution
    plt.figure(figsize=(10, 5))
    plt.plot(C_space, history[0], label='Initial State ($\\tau = 0$)', color='gray', linestyle='--')
    plt.plot(C_space, history[25], label='Mid-Cycle ($\\tau = 25$)', color='#1f77b4')
    plt.plot(C_space, history[-1], label=f'Final Equilibrium ($\\tau = {cycles}$)', color='#2ca02c', linewidth=2)
    
    plt.title('N=64 Majorana Substrate: Master WIN Evolution Field ($\mathcal{W}$)', fontsize=12, fontweight='bold')
    plt.xlabel('Computational Path Index ($\mathcal{C}$)', fontsize=11)
    plt.ylabel('Warped Information Number ($\mathcal{W}$)', fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, facecolor='white')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_lattice_audit()