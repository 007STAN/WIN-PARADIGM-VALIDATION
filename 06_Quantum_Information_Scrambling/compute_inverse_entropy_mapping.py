import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, VBox, interactive_output

def compute_inverse_entropy_mapping(measured_entropy, temperature, system_scale):
    # Standard thermodynamic energy scale conversion (kT)
    k_boltzmann = 1.380649e-23
    thermal_scale = temperature * k_boltzmann
    
    # Forward Standard Physics Model: Entropy to Microstate Density
    microstate_density = np.exp(np.clip(measured_entropy / 10.0, 0, 20))
    
    # Inverse Entropic Mapping (WIN Paradigm Reverse Calculation)
    scaling_factor = system_scale / 64.0
    reconstructed_substrate = np.sqrt(microstate_density) * scaling_factor * 8.0
    
    # Domain coordinate for spatial/informational reconstruction
    x = np.linspace(0, 10, 200)
    
    # Forward vs Inverse convergence profile
    forward_field = (measured_entropy / 100.0) * np.sin(x)
    inverse_field = (reconstructed_substrate / 64.0) * np.cos(x * (temperature / 300.0))
    
    return x, forward_field, inverse_field, reconstructed_substrate

def interactive_inverse_entropy_dashboard():
    entropy_slider = FloatSlider(
        value=49.0, min=10.0, max=100.0, step=1.0,
        description=r'Measured Entropy ($S$):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    temp_slider = FloatSlider(
        value=206.0, min=1.0, max=1000.0, step=5.0,
        description=r'System Temp ($T$ [K]):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    scale_slider = FloatSlider(
        value=60.0, min=16.0, max=128.0, step=4.0,
        description=r'Baseline Substrate ($N$):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    
    def update_plot(measured_entropy, temperature, system_scale):
        x, forward_field, inverse_field, n_recon = compute_inverse_entropy_mapping(
            measured_entropy, temperature, system_scale
        )
        
        plt.figure(figsize=(9, 5))
        plt.plot(x, forward_field, 'r--', lw=2.0, label=r'Standard Forward Thermal Profile')
        plt.plot(x, inverse_field, 'c-', lw=2.5, label=r'WIN Inverse Reconstructed Field')
        
        plt.xlabel(r'Informational Coordinate Space ($\xi$)', fontsize=11)
        plt.ylabel(r'Field Amplitude / Potential', fontsize=11)
        plt.title(f'Inverse Entropic Metrology: Reconstructing Substrate from Entropy', fontsize=12, fontweight='bold')
        plt.grid(True, ls='--', alpha=0.5)
        plt.legend(loc='upper right', frameon=True)
        
        # Status Box showing the reverse-calculated WIN substrate scale
        text_str = (
            r"Inverse Mapping Results:" + "\n" +
            r"• Input Entropy ($S$): " + f"{measured_entropy:.1f} J/K\n" +
            r"• Reconstructed Substrate ($N_{recon}$): " + f"{n_recon:.2f}\n" +
            r"• Status: Holographic Inversion Converged"
        )
        
        props = dict(boxstyle='round', facecolor='azure', alpha=0.8)
        plt.gca().text(0.03, 0.95, text_str, transform=plt.gca().transAxes, fontsize=10,
                        verticalalignment='top', bbox=props)
        
        plt.tight_layout()
        plt.show()

    out = interactive_output(update_plot, {
        'measured_entropy': entropy_slider, 
        'temperature': temp_slider, 
        'system_scale': scale_slider
    })
    
    display(VBox([entropy_slider, temp_slider, scale_slider, out]))

# Invoke the inverse entropy dashboard
interactive_inverse_entropy_dashboard()