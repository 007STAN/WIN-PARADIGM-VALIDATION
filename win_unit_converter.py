"""
Warped Information Number (WIN) Paradigm — Conversion Toolkit
Author: Stanley Preschutti (Entropia Research Institute)
Description: Converts standard MKS/SI physical quantities into their native 
N=64 Majorana substrate informational equivalents based on the Master Conversion Dictionary.
"""

class WINConverter:
    def __init__(self):
        # Fundamental substrate constants defined by the WIN framework
        self.N_NODES = 64
        self.K_WIN = 1.0  # nat per informational work unit
        
    def mass_to_code_distance(self, mass_u, scaling_factor=44.0):
        """
        Converts atomic mass units (u) or general mass scale to error-correction 
        topological overhead (d_code). Protected states require d_code >= 5.
        """
        d_code = max(5, int(round(mass_u / scaling_factor * 5)))
        return d_code

    def energy_to_informational_work(self, d_code, persistence_depth):
        """
        Computes Informational Work (E_WIN = d_code / tau_WIN) in nats.
        """
        if persistence_depth <= 0:
            raise ValueError("Persistence depth (tau_WIN) must be greater than 0.")
        return d_code / persistence_depth

    def temperature_to_chaos_exponent(self, lyapunov_rate):
        """
        Maps Temperature to Chaos Exponent (lambda_L), representing information scrambling 
        across the 64-node network.
        """
        return float(lyapunov_rate)

    def force_to_entropic_pressure(self, grad_mutual_info):
        """
        Computes Entropic Force (F = \nabla S) as the gradient of regularized entropy 
        across lattice nodes (Nats per cycle).
        """
        return float(grad_mutual_info)

    def planck_constant_conversion(self, min_bit_capacity=1.0):
        v_min_bit = min_bit_capacity
        h_win = v_min_bit / (2.0 * 3.141592653589793)
        return h_win

def run_conversion_demo():
    converter = WINConverter()
    
    print("=" * 65)
    print("WIN PARADIGM: MKS/SI TO N=64 SUBSTRATE CONVERSION SUITE")
    print("=" * 65)
    
    # Example 1: Mass to Code Distance (e.g., Lead Pb-208 or heavy states)
    sample_mass_u = 208.0
    d_code = converter.mass_to_code_distance(sample_mass_u)
    print(f"1. Mass Conversion:")
    print(f"   - Input Mass         : {sample_mass_u} u (Lead-208 baseline)")
    print(f"   - Holo. Code Distance: {d_code} (Parity bits / error-correction overhead)\n")
    
    # Example 2: Informational Work (Energy)
    tau = 100.0  # persistence depth update cycles
    work = converter.energy_to_informational_work(d_code, tau)
    print(f"2. Energy Conversion:")
    print(f"   - Persistence Depth  : {tau} cycles")
    print(f"   - Informational Work : {work:.4f} Nats (E_WIN = d_code / tau_WIN)\n")
    
    # Example 3: Temperature to Chaos Exponent
    lyapunov = 0.85
    chaos_exp = converter.temperature_to_chaos_exponent(lyapunov)
    print(f"3. Temperature Conversion:")
    print(f"   - Chaos Exponent     : {chaos_exp:.4f} Lyapunov bits/cycle (lambda_L)\n")
    
    # Example 4: Planck Constant
    h_win = converter.planck_constant_conversion()
    print(f"4. Fundamental Constant Conversion:")
    print(f"   - WIN-Reduced Planck : {h_win:.5f} (I_min / 2*pi)\n")
    print("=" * 65)

if __name__ == "__main__":
    run_conversion_demo()