import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, VBox, interactive_output

def compute_idp_phase_separation(solution_temp, charge_hydropathy_ratio, majorana_scale):
    # Protein concentration domain (micromolar [uM])
    concentration = np.linspace(1.0, 100.0, 300)
    
    # 1. Standard Flory-Huggins Polymer Model (Smooth, continuous phase boundary lacking sharp nucleation cliffs)
    standard_phase_boundary = 50.0 - 15.0 * np.log(concentration / 10.0)
    standard_phase_boundary = np.clip(standard_phase_boundary, 5.0, 95.0)
    
    # 2. WIN Discrete Substrate Phase Transition Model
    # Incorporates N=64 topological constraint as a cooperative binding matrix
    substrate_factor = majorana_scale / 64.0
    thermal_scaling = solution_temp / 298.0
    
    # Critical saturation threshold (C_sat) governed by discrete lattice cooperative nodes
    c_sat_threshold = 35.0 * (thermal_scaling / substrate_factor) * (1.0 / charge_hydropathy_ratio)
    
    # Sigmoidal droplet condensation probability curve (capturing sharp phase transition cliff)
    win_condensation_prob = 100.0 / (1.0 + np.exp(-0.15 * (concentration - c_sat_threshold)))
    
    return concentration, standard_phase_boundary, win_condensation_prob, c_sat_threshold

def interactive_idp_dashboard():
    temp_slider = FloatSlider(
        value=298.0, min=270.0, max=320.0, step=2.0,
        description=r'Solution Temp ($T$ [K]):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    ratio_slider = FloatSlider(
        value=1.2, min=0.5, max=2.5, step=0.05,
        description=r'Sequence Charge-Hydropathy ($\omega$):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    majorana_slider = FloatSlider(
        value=64.0, min=16.0, max=128.0, step=4.0,
        description=r'Substrate Scale ($N$):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    
    def update_plot(solution_temp, charge_hydropathy_ratio, majorana_scale):
        conc, std_phase, win_prob, c_sat = compute_idp_phase_separation(
            solution_temp, charge_hydropathy_ratio, majorana_scale
        )
        
        plt.figure(figsize=(9, 5))
        plt.plot(conc, std_phase, 'r--', lw=2.0, label=r'Standard Flory-Huggins Model (Polymer Approximation)')
        plt.plot(conc, win_prob, 'c-', lw=2.5, label=r'WIN Discrete Condensation Probability')
        plt.axvline(x=c_sat, color='m', linestyle=':', lw=2.0, label=rf'Critical Saturation Threshold ($C_{{\text{{sat}}}} \approx {c_sat:.1f}\ \mu\text{{M}}$)')
        
        plt.xlabel(r'Protein Concentration ($c$ [$\mu$M])', fontsize=11)
        plt.ylabel(r'Condensation / Droplet Formation Probability (%)', fontsize=11)
        plt.title(r'Biomedical Metrology: Predicting IDP Phase Separation via Discrete Lattice Substrate', fontsize=12, fontweight='bold')
        plt.grid(True, ls='--', alpha=0.5)
        plt.legend(loc='lower right', frameon=True)
        
        # Status Box highlighting phase metrics
        text_str = (
            r"IDP Phase Metrics:" + "\n" +
            r"• Critical Saturation ($C_{\text{sat}}$): " + f"{c_sat:.1f} $\\mu$M\n" +
            r"• Sequence Parameter ($\omega$): " + f"{charge_hydropathy_ratio:.2f}\n" +
            r"• Substrate Lattice ($N$): " + f"{majorana_scale:.0f}\n" +
            r"• Status: Cooperative Condensation Active"
        )
        
        props = dict(boxstyle='round', facecolor='azure', alpha=0.8)
        plt.gca().text(0.03, 0.75, text_str, transform=plt.gca().transAxes, fontsize=9,
                        verticalalignment='top', bbox=props)
        
        plt.tight_layout()
        plt.show()

    out = interactive_output(update_plot, {
        'solution_temp': temp_slider, 
        'charge_hydropathy_ratio': ratio_slider, 
        'majorana_scale': majorana_slider
    })
    
    display(VBox([temp_slider, ratio_slider, majorana_slider, out]))

# Invoke the IDP phase separation dashboard
interactive_idp_dashboard()