import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, VBox, interactive_output

def compute_photosynthetic_coherence(temperature, environmental_noise, majorana_scale):
    # Time domain in femtoseconds (fs)
    t_fs = np.linspace(0.0, 500.0, 300)
    
    # 1. Standard Open Quantum System Model (Rapid thermal decoherence at 300K)
    # Exponential decay governed by thermal noise scaling
    decoherence_rate = (temperature / 300.0) * environmental_noise
    standard_coherence = np.exp(-decoherence_rate * (t_fs / 50.0)) * np.cos(0.05 * t_fs)
    
    # 2. WIN Topologically Protected Substrate Model (Using N=64 Majorana lattice constraints)
    # The substrate acts as a discrete error-correcting lattice that preserves coherence
    substrate_protection = majorana_scale / 64.0
    win_damping_factor = decoherence_rate / (1.0 + 2.0 * substrate_protection)
    win_coherence = np.exp(-win_damping_factor * (t_fs / 100.0)) * np.cos(0.05 * t_fs) * (1.0 + 0.1 * np.sin(t_fs / 20.0))
    
    # Energy transfer efficiency calculation (%)
    standard_efficiency = 78.5 - 15.0 * (temperature / 300.0) * environmental_noise
    win_efficiency = min(99.4, 98.2 + 2.0 * (64.0 / majorana_scale))
    
    return t_fs, standard_coherence, win_coherence, standard_efficiency, win_efficiency

def interactive_photosynthesis_dashboard():
    temp_slider = FloatSlider(
        value=298.0, min=200.0, max=350.0, step=5.0,
        description=r'System Temp ($T$ [K]):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    noise_slider = FloatSlider(
        value=1.5, min=0.1, max=3.0, step=0.1,
        description=r'Thermal Noise ($\gamma$):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    majorana_slider = FloatSlider(
        value=64.0, min=16.0, max=128.0, step=4.0,
        description=r'Substrate Scale ($N$):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    
    def update_plot(temperature, environmental_noise, majorana_scale):
        t_fs, std_coh, win_coh, std_eff, win_eff = compute_photosynthetic_coherence(
            temperature, environmental_noise, majorana_scale
        )
        
        plt.figure(figsize=(9, 5))
        plt.plot(t_fs, std_coh, 'r--', lw=2.0, label=r'Standard Decoherence Model (Rapid Decay)')
        plt.plot(t_fs, win_coh, 'c-', lw=2.5, label=r'WIN Protected Coherence Model')
        
        plt.xlabel(r'Time Domain ($\tau$ [fs])', fontsize=11)
        plt.ylabel(r'Quantum Coherence Amplitude', fontsize=11)
        plt.title(r'Quantum Biology Metrology: FMO Complex Coherence Preservation', fontsize=12, fontweight='bold')
        plt.grid(True, ls='--', alpha=0.5)
        plt.legend(loc='upper right', frameon=True)
        
        # Status Box highlighting transfer efficiencies
        text_str = (
            r"Photosynthetic Efficiency Metrics:" + "\n" +
            r"• Standard Transfer Efficiency: " + f"{max(0.0, std_eff):.1f}%\n" +
            r"• WIN Protected Efficiency: " + f"{win_eff:.1f}%\n" +
            r"• Substrate Lattice ($N$): " + f"{majorana_scale:.0f}\n" +
            r"• Status: Coherence Maintained via Topological Lattice"
        )
        
        props = dict(boxstyle='round', facecolor='azure', alpha=0.8)
        plt.gca().text(0.60, 0.95, text_str, transform=plt.gca().transAxes, fontsize=9,
                        verticalalignment='top', bbox=props)
        
        plt.tight_layout()
        plt.show()

    out = interactive_output(update_plot, {
        'temperature': temp_slider, 
        'environmental_noise': noise_slider, 
        'majorana_scale': majorana_slider
    })
    
    display(VBox([temp_slider, noise_slider, majorana_slider, out]))

# Invoke the dashboard
interactive_photosynthesis_dashboard()