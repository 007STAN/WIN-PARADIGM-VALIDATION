import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, VBox, interactive_output

def compute_metal_failure_prediction(cyclic_stress, material_temperature, majorana_scale):
    # Fatigue cycles domain (N_cycles in thousands)
    cycles = np.linspace(1.0, 100.0, 300)
    
    # 1. Standard Continuum Mechanics Model (Empirical S-N Curve / Paris Law degradation)
    standard_degradation = 100.0 - (cyclic_stress / 10.0) * np.sqrt(cycles)
    standard_degradation = np.clip(standard_degradation, 0.0, 100.0)
    
    # 2. WIN Discrete Substrate Lattice Failure Model
    substrate_resilience = majorana_scale / 64.0
    thermal_softening = material_temperature / 300.0
    
    # Critical tipping point calculation based on discrete lattice saturation
    critical_threshold_cycle = 75.0 * substrate_resilience / (thermal_softening * (cyclic_stress / 50.0))
    
    # Sigmoidal dislocation avalanche curve (capturing sudden catastrophic drop)
    win_structural_integrity = 100.0 / (1.0 + np.exp(0.1 * (cycles - critical_threshold_cycle)))
    
    return cycles, standard_degradation, win_structural_integrity, critical_threshold_cycle

def interactive_failure_dashboard():
    stress_slider = FloatSlider(
        value=65.0, min=20.0, max=100.0, step=2.0,
        description=r'Cyclic Stress ($\sigma$ [MPa]):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    temp_slider = FloatSlider(
        value=298.0, min=200.0, max=800.0, step=10.0,
        description=r'Temp ($T$ [K]):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    majorana_slider = FloatSlider(
        value=64.0, min=16.0, max=128.0, step=4.0,
        description=r'Substrate Scale ($N$):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    
    def update_plot(cyclic_stress, material_temperature, majorana_scale):
        cycles, std_deg, win_int, fail_point = compute_metal_failure_prediction(
            cyclic_stress, material_temperature, majorana_scale
        )
        
        plt.figure(figsize=(9, 5))
        plt.plot(cycles, std_deg, 'r--', lw=2.0, label=r'Standard Continuum Fatigue Model (Smooth S-N)')
        plt.plot(cycles, win_int, 'c-', lw=2.5, label=r'WIN Discrete Lattice Failure Prediction')
        plt.axvline(x=fail_point, color='m', linestyle=':', lw=2.0, label=rf'Predicted Failure Cliff ($N_c \approx {fail_point:.1f}k$)')
        
        plt.xlabel(r'Loading Cycles ($\times 10^3$ Cycles)', fontsize=11)
        plt.ylabel(r'Structural Integrity Metric (%)', fontsize=11)
        plt.title(r'Materials Metrology: Predicting Metal Fatigue via Discrete Lattice Collapse', fontsize=12, fontweight='bold')
        plt.grid(True, ls='--', alpha=0.5)
        plt.legend(loc='lower left', frameon=True)
        
        text_str = (
            r"Failure Prediction Metrics:" + "\n" +
            r"• Applied Stress ($\sigma$): " + f"{cyclic_stress:.1f} MPa\n" +
            r"• Critical Tipping Point: " + f"{fail_point:.1f}k Cycles\n" +
            r"• Substrate Lattice ($N$): " + f"{majorana_scale:.0f}\n" +
            r"• Status: Topological Slip Stability Active"
        )
        
        props = dict(boxstyle='round', facecolor='azure', alpha=0.8)
        plt.gca().text(0.03, 0.30, text_str, transform=plt.gca().transAxes, fontsize=9,
                        verticalalignment='top', bbox=props)
        
        plt.tight_layout()
        plt.show()

    out = interactive_output(update_plot, {
        'cyclic_stress': stress_slider, 
        'material_temperature': temp_slider, 
        'majorana_scale': majorana_slider
    })
    
    display(VBox([stress_slider, temp_slider, majorana_slider, out]))

# Invoke the failure prediction dashboard
interactive_failure_dashboard()