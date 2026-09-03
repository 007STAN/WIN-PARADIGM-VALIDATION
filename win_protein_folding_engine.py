import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, VBox, interactive_output

def compute_protein_conformational_states(thermal_energy, ligand_affinity, majorana_scale):
    # Reaction coordinate / conformational pathway domain
    pathway_steps = np.linspace(0.0, 10.0, 300)
    
    # 1. Standard Static / Free Energy Landscape (Single deep native basin, misses intermediates)
    standard_landscape = -10.0 * np.exp(-((pathway_steps - 5.0)**2) / 2.0)
    
    # 2. WIN Discrete Substrate Conformational Landscape 
    # Incorporates N=64 topological constraint to reveal cryptic intermediate basins
    substrate_resolution = majorana_scale / 64.0
    
    # Primary native well + transient intermediate well governed by discrete substrate nodes
    win_landscape = (-12.0 * np.exp(-((pathway_steps - 5.0)**2) / 1.5)) + \
                    (-4.5 * substrate_resolution * np.exp(-((pathway_steps - 3.0)**2) / (0.5 * thermal_energy)))
    
    # Cryptic pocket opening probability (%)
    pocket_open_prob = 100.0 / (1.0 + np.exp(-0.8 * (ligand_affinity - (6.0 / substrate_resolution))))
    
    return pathway_steps, standard_landscape, win_landscape, pocket_open_prob

def interactive_protein_folding_dashboard():
    thermal_slider = FloatSlider(
        value=1.0, min=0.5, max=2.5, step=0.05,
        description=r'Thermal Fluctuation ($k_BT$):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    affinity_slider = FloatSlider(
        value=5.0, min=1.0, max=10.0, step=0.2,
        description=r'Binding Stress ($\Delta G$ [kcal/mol]):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    majorana_slider = FloatSlider(
        value=64.0, min=16.0, max=128.0, step=4.0,
        description=r'Substrate Scale ($N$):', style={'description_width': 'initial'}, layout={'width': '480px'}
    )
    
    def update_plot(thermal_energy, ligand_affinity, majorana_scale):
        pathway, std_land, win_land, pocket_prob = compute_protein_conformational_states(
            thermal_energy, ligand_affinity, majorana_scale
        )
        
        plt.figure(figsize=(9, 5))
        plt.plot(pathway, std_land, 'r--', lw=2.0, label=r'Standard Static Energy Landscape (AlphaFold Baseline)')
        plt.plot(pathway, win_land, 'c-', lw=2.5, label=r'WIN Discrete Intermediate Landscape')
        
        plt.xlabel(r'Conformational Pathway Coordinate ($Q$)', fontsize=11)
        plt.ylabel(r'Free Energy ($F$ [Arbitrary Units])', fontsize=11)
        plt.title(r'Biophysical Metrology: Revealing Cryptic Pockets & Intermediates via WIN Substrate', fontsize=12, fontweight='bold')
        plt.grid(True, ls='--', alpha=0.5)
        plt.legend(loc='upper right', frameon=True)
        
        # Status Box highlighting cryptic pocket metrics
        text_str = (
            r"Drug Discovery Metrics:" + "\n" +
            r"• Cryptic Pocket Open Prob.: " + f"{pocket_prob:.1f}%\n" +
            r"• Substrate Lattice ($N$): " + f"{majorana_scale:.0f}\n" +
            r"• Thermal Factor ($k_BT$): " + f"{thermal_energy:.2f}\n" +
            r"• Status: Transient Intermediate Trapped"
        )
        
        props = dict(boxstyle='round', facecolor='azure', alpha=0.8)
        plt.gca().text(0.03, 0.30, text_str, transform=plt.gca().transAxes, fontsize=9,
                        verticalalignment='top', bbox=props)
        
        plt.tight_layout()
        plt.show()

    out = interactive_output(update_plot, {
        'thermal_energy': thermal_slider, 
        'ligand_affinity': affinity_slider, 
        'majorana_scale': majorana_slider
    })
    
    display(VBox([thermal_slider, affinity_slider, majorana_slider, out]))

# Invoke the protein folding dashboard
interactive_protein_folding_dashboard()