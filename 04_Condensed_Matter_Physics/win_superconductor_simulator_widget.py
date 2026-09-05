import ipywidgets as widgets
from IPython.display import display, clear_output
import matplotlib.pyplot as plt
import numpy as np

# Configure dark theme styling for scientific plots
plt.style.use('dark_background')

class WINSuperconductorDashboard:
    def __init__(self):
        self.lattice_size = 64
        self.nodes = np.arange(self.lattice_size)
        self.Tc_max = 15.0
        self.Bc2_0 = 8.0

        # Create UI Controls
        self.temp_slider = widgets.FloatSlider(value=4.2, min=0.1, max=20.0, step=0.1, description='Temp (K):', style={'description_width': 'initial'})
        self.field_slider = widgets.FloatSlider(value=0.0, min=0.0, max=10.0, step=0.1, description='Mag Field (T):', style={'description_width': 'initial'})
        self.entropy_slider = widgets.FloatSlider(value=1.5, min=0.1, max=5.0, step=0.1, description='Entropy Limit:', style={'description_width': 'initial'})
        
        # Output container for plots and text
        self.out = widgets.Output()

        # Bind events
        self.temp_slider.observe(self._update_view, names='value')
        self.field_slider.observe(self._update_view, names='value')
        self.entropy_slider.observe(self._update_view, names='value')

    def _compute_state(self, T, B, entropy_limit):
        t = T / self.Tc_max
        b = B / self.Bc2_0
        
        phase_field = np.maximum(0.0, 1.0 - t**2 - b)
        order_parameter = float(np.sqrt(phase_field))
        
        # Energy gap vector across N=64 Majorana substrate
        energy_gap = order_parameter * 2.0 * np.ones(self.lattice_size)
        
        # Density of States (DOS) spectrum
        dos = np.ones(self.lattice_size)
        if order_parameter > 0.05:
            p1 = int(self.lattice_size / 2) - int(10 * order_parameter)
            p2 = int(self.lattice_size / 2) + int(10 * order_parameter)
            dos[max(0, p1):min(self.lattice_size, p1+3)] += (3.0 * order_parameter)
            dos[max(0, p2):min(self.lattice_size, p2+3)] += (3.0 * order_parameter)

        entropy = float(0.1 + (t * 2.0) + (b * 1.5))
        gap_reg = float(np.maximum(0.001, order_parameter * 0.2))
        parity = float(np.cos(B * 0.5) * np.exp(-entropy * 0.3))

        is_coherent = (gap_reg > 0.05) and (entropy < entropy_limit) and (T < self.Tc_max) and (B < self.Bc2_0)
        state = "COHERENT_SUPERCONDUCTING_CONDENSATE" if is_coherent else "NORMAL_DISSIPATIVE_STATE"

        return {"state": state, "entropy": entropy, "gap_reg": gap_reg, "parity": parity, "gap": energy_gap, "dos": dos}

    def _update_view(self, change):
        T = self.temp_slider.value
        B = self.field_slider.value
        limit = self.entropy_slider.value
        data = self._compute_state(T, B, limit)

        with self.out:
            clear_output(wait=True)
            
            # Print status summary
            color = "#00ff66" if data["state"] == "COHERENT_SUPERCONDUCTING_CONDENSATE" else "#ff3333"
            print("--- WIN-Lang Superconductor Substrate Metrics ---")
            display(widgets.HTML(f"<b>State: <span style='color:{color}'>{data['state']}</span></b>"))
            print(f"Entropy: {data['entropy']:.4f} | Gap Reg: {data['gap_reg']:.4f} | Parity: {data['parity']:.4f}\n")

            # Render Matplotlib Subplots
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
            fig.patch.set_facecolor('#111111')
            
            # Top: Energy Gap
            ax1.set_facecolor('#1a1a1a')
            ax1.plot(self.nodes, data["gap"], color='#00ffff', linewidth=2, marker='o', markersize=3)
            ax1.set_ylabel("Energy Gap (Δ)", color='#00ffff')
            ax1.set_ylim(-0.1, 2.2)
            ax1.grid(True, color='#333333', linestyle='--')
            ax1.set_title("WIN Substrate Analysis: N=64 Majorana Lattice", color='white', fontsize=11, fontweight='bold')

            # Bottom: Density of States
            ax2.set_facecolor('#1a1a1a')
            ax2.plot(self.nodes, data["dos"], color='#ff00ff', linewidth=1.5)
            ax2.fill_between(self.nodes, data["dos"], color='#ff00ff', alpha=0.15)
            ax2.set_xlabel("Majorana Node Index", color='white')
            ax2.set_ylabel("Density of States (ρ)", color='#ff00ff')
            ax2.set_ylim(0, 10)
            ax2.grid(True, color='#333333', linestyle='--')

            plt.tight_layout()
            plt.show()

    def display_console(self):
        ui = widgets.VBox([
            widgets.HTML("<h3 style='color: white;'>WIN-Lang Superconductor Analysis Console</h3>"),
            widgets.HBox([self.temp_slider, self.field_slider, self.entropy_slider]),
            widgets.HTML("<hr style='border-color: #333;'>"),
            self.out
        ])
        display(ui)
        self._update_view(None)

# Initialize and render
dashboard = WINSuperconductorDashboard()
dashboard.display_console()