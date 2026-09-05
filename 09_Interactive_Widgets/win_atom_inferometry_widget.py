import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, Output, VBox, interactive_output

def compute_atom_interferometry(baseline_l, interrogation_t, log_cmrr):
    cmrr = 10**log_cmrr
    freqs = np.logspace(-1, 2, 300) # 0.1 Hz to 100 Hz
    
    # Simulated strain sensitivity floor influenced by CMRR and baseline
    sql_limit = 1e-20 / np.sqrt(freqs)
    laser_noise_floor = (1.0 / cmrr) * 1e-15 * (1.0 / np.maximum(baseline_l, 0.1))
    total_sensitivity = np.sqrt(sql_limit**2 + laser_noise_floor**2)
    
    return freqs, total_sensitivity, sql_limit, laser_noise_floor

def interactive_atom_interferometry_dashboard():
    baseline_slider = FloatSlider(
        value=10.0, min=1.0, max=100.0, step=1.0,
        description='Baseline $L$ (m):', style={'description_width': 'initial'}, layout={'width': '450px'}
    )
    time_slider = FloatSlider(
        value=1.0, min=0.1, max=2.5, step=0.05,
        description='Pulse Time $T$ (s):', style={'description_width': 'initial'}, layout={'width': '450px'}
    )
    cmrr_slider = FloatSlider(
        value=5.0, min=2.0, max=8.0, step=0.1,
        description='Log10(CMRR):', style={'description_width': 'initial'}, layout={'width': '450px'}
    )
    
    def update_plot(baseline_l, interrogation_t, log_cmrr):
        freqs, sensitivity, sql, laser_noise = compute_atom_interferometry(
            baseline_l, interrogation_t, log_cmrr
        )
        
        plt.figure(figsize=(9, 5))
        plt.loglog(freqs, sensitivity, 'b-', lw=2, label='Total Strain Noise Floor')
        plt.loglog(freqs, sql, 'k--', alpha=0.6, label='Standard Quantum Limit')
        plt.loglog(freqs, laser_noise * np.ones_like(freqs), 'r:', label='Residual Laser Noise (CMRR)')
        
        plt.xlabel('Frequency $f$ [Hz]', fontsize=11)
        plt.ylabel('Strain Sensitivity [1/√Hz]', fontsize=11)
        plt.title('Differential Atom Interferometry & Noise Cancellation', fontsize=12, fontweight='bold')
        plt.grid(True, which="both", ls="--", alpha=0.5)
        plt.ylim(1e-22, 1e-15)
        plt.xlim(0.1, 100)
        plt.legend(loc='upper right', frameon=True)
        
        text_str = (f'Parameters:\n'
                    f'• Baseline: {baseline_l:.1f} m\n'
                    f'• Interrogation T: {interrogation_t:.2f} s\n'
                    f'• Suppression (CMRR): 10^{log_cmrr:.1f}')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.4)
        plt.gca().text(0.03, 0.95, text_str, transform=plt.gca().transAxes, fontsize=10,
                        verticalalignment='top', bbox=props)
        
        plt.tight_layout()
        plt.show()

    out = interactive_output(update_plot, {
        'baseline_l': baseline_slider, 
        'interrogation_t': time_slider, 
        'log_cmrr': cmrr_slider
    })
    
    display(VBox([baseline_slider, time_slider, cmrr_slider, out]))

# Explicitly invoke the dashboard to render the output widget
interactive_atom_interferometry_dashboard()