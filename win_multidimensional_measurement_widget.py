import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, IntSlider, Output, VBox, interactive_output

def compute_multidimensional_metrics(dimension_tier, warp_input, coupling_epsilon):
    # Tier-based evaluations across 5D to 8D structures
    kL_base = 38.44 * warp_input
    
    if dimension_tier == 5:
        # 5D AdS/CFT Warped Sector
        scales = np.linspace(0, 5, 200)
        metric_profile = np.exp(-0.5 * scales) * (1.0 + coupling_epsilon * np.sin(scales))
        desc = r"5D Bulk Warped Geometry ($AdS_5$)"
    elif dimension_tier == 6:
        # 6D Toroidal Vault & Compression Wall
        scales = np.linspace(0, 6, 200)
        metric_profile = 1068.81 * (1.0 - np.exp(-scales / 1.5)) * (1.0 + 0.05 * np.cos(scales * kL_base / 38.44))
        desc = r"6D Toroidal Vault & Compression Wall (TeV)"
    elif dimension_tier == 7:
        # 7D Variational Selection Layer
        scales = np.linspace(0, 7, 200)
        gamma_opt = 0.703 * (1.0 + 0.1 * (warp_input - 1.0))
        metric_profile = gamma_opt * np.exp(-((scales - 3.5)**2) / 2.0)
        desc = r"7D Variational Selection Constant ($\gamma \approx 0.703$)"
    else:
        # 8D Persistence Layer & Dark Energy
        scales = np.linspace(0, 8, 200)
        w_eq = -1.018 * (1.0 + 0.02 * (coupling_epsilon - 1e-3))
        metric_profile = w_eq * np.ones_like(scales) + 0.05 * np.sin(scales)
        desc = r"8D Persistence Layer ($w \approx -1.018$)"
        
    return scales, metric_profile, desc

def interactive_multidimensional_dashboard():
    tier_slider = IntSlider(
        value=7, min=5, max=8, step=1,
        description=r'Dimension Tier:', style={'description_width': 'initial'}, layout={'width': '450px'}
    )
    warp_slider = FloatSlider(
        value=0.92, min=0.8, max=1.2, step=0.01,
        description=r'Warp Scale Multiplier:', style={'description_width': 'initial'}, layout={'width': '450px'}
    )
    epsilon_slider = FloatSlider(
        value=0.0, min=0.0, max=5e-3, step=1e-4, format='.4f',
        description=r'Coupling ($\epsilon$):', style={'description_width': 'initial'}, layout={'width': '450px'}
    )
    
    def update_plot(dimension_tier, warp_input, coupling_epsilon):
        scales, profile, title_desc = compute_multidimensional_metrics(dimension_tier, warp_input, coupling_epsilon)
        
        plt.figure(figsize=(9, 5))
        plt.plot(scales, profile, 'm-', lw=2.5, label=f'Tier {dimension_tier} Metric Profile')
        
        plt.xlabel(r'Coordinate Index / Extension Parameter', fontsize=11)
        plt.ylabel(r'Field Amplitude / Energy Scale', fontsize=11)
        plt.title(f'WIN Multi-Dimensional Metrology: {title_desc}', fontsize=12, fontweight='bold')
        plt.grid(True, ls='--', alpha=0.5)
        plt.legend(loc='upper right', frameon=True)
        
        # DME Status box
        text_str = (r'DME Parameters:' + '\n'
                    f'• Target Dimension: {dimension_tier}D\n'
                    f'• Warp Factor $kL$: {38.44 * warp_input:.2f}\n'
                    r'• Entropic Sync ($\delta I_{{mut}}$): 1.0 (Equilibrium)')
        props = dict(boxstyle='round', facecolor='lavender', alpha=0.5)
        plt.gca().text(0.03, 0.95, text_str, transform=plt.gca().transAxes, fontsize=10,
                        verticalalignment='top', bbox=props)
        
        plt.tight_layout()
        plt.show()

    out = interactive_output(update_plot, {
        'dimension_tier': tier_slider, 
        'warp_input': warp_slider, 
        'coupling_epsilon': epsilon_slider
    })
    
    display(VBox([tier_slider, warp_slider, epsilon_slider, out]))

# Invoke the multi-dimensional metrology dashboard
interactive_multidimensional_dashboard()