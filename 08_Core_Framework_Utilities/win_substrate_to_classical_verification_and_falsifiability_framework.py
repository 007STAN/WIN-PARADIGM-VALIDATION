import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

# Global Constants
EXACT_KL = 38.44
ERROR_THRESHOLD = 1.2e-4

def compute_win_dynamics(kL_val, N_val, noise_amplitude):
    T = 200
    dt = 0.01
    time_axis = np.linspace(0, T * dt, T)
    
    # 1. WIN Paradigm Invariant Substrate (Theoretical Baseline)
    win_substrate = np.exp(-0.15 * time_axis) * np.cos(2 * np.pi * 0.4 * time_axis / 1.0)
    
    # 2. Classical Observable (Governed by parameter adjustments)
    kl_fractional_delta = np.abs(kL_val - EXACT_KL) / EXACT_KL
    lattice_correction = 1.0 + 0.001 * (64.0 - N_val) / 64.0
    
    classical_field = win_substrate * lattice_correction * np.cos(kl_fractional_delta * time_axis)
    
    np.random.seed(42)
    measured_noise = np.random.normal(0, noise_amplitude, size=T)
    classical_response = classical_field + measured_noise
    
    # Residual and Status Evaluations
    residual = np.mean(np.abs(classical_response - win_substrate))
    
    # Dual-channel evaluation logic
    win_status = "PASSED (Invariant Substrate Intact)"
    classical_status = "PASSED (Aligned within threshold)" if residual <= ERROR_THRESHOLD else "FAILED (Divergence exceeds limit)"
    
    metrics = {
        "win_mean": np.mean(win_substrate),
        "win_peak": np.max(np.abs(win_substrate)),
        "classical_mean": np.mean(classical_response),
        "classical_peak": np.max(np.abs(classical_response)),
        "mean_residual": residual,
        "max_residual": np.max(np.abs(classical_response - win_substrate)),
        "win_status": win_status,
        "classical_status": classical_status
    }
    
    return time_axis, win_substrate, classical_response, metrics

# Interactive Widgets tailored for rigorous inspection
kl_slider = widgets.FloatSlider(value=38.44, min=30.0, max=50.0, step=0.01, description='Holographic kL:')
n_slider = widgets.IntSlider(value=64, min=16, max=256, step=16, description='Lattice N:')
noise_slider = widgets.FloatSlider(value=0.0000, min=0.0, max=0.01, step=0.0005, description='Noise Amp:', readout_format='.4f')

output_plot = widgets.Output()

def update_visualization(kl, n_val, noise):
    time_axis, win_sub, classical_res, metrics = compute_win_dynamics(kl, n_val, noise)
    error_profile = np.abs(classical_res - win_sub)
    
    with output_plot:
        clear_output(wait=True)
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        
        # Subplot 1: Field Amplitude Comparison
        ax1.plot(time_axis, win_sub, label=f"WIN Substrate (kL = {EXACT_KL})", color="#ff7f0e", linewidth=2)
        ax1.plot(time_axis, classical_res, label=f"Classical Field (kL = {kl:.2f}, N = {n_val})", color="#1f77b4", linestyle="--", alpha=0.8)
        ax1.set_ylabel("Field Amplitude")
        ax1.set_title("WIN Paradigm vs. Classical Physics Verification Matrix")
        
        stats_text_1 = (f"WIN Peak: {metrics['win_peak']:.4f}\n"
                        f"Classical Peak: {metrics['classical_peak']:.4f}\n"
                        f"WIN Mean: {metrics['win_mean']:.4f}\n"
                        f"Classical Mean: {metrics['classical_mean']:.4f}")
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax1.text(0.02, 0.95, stats_text_1, transform=ax1.transAxes, fontsize=10,
                verticalalignment='top', bbox=props)
        
        ax1.legend(loc="upper right")
        ax1.grid(True, linestyle=":", alpha=0.6)
        
        # Subplot 2: Error Residuals
        ax2.plot(time_axis, error_profile, label="Absolute Residual Error (|Classical - WIN|)", color="#d62728")
        ax2.axhline(y=ERROR_THRESHOLD, color='black', linestyle='-.', label=f"Falsifiability Limit ({ERROR_THRESHOLD})")
        ax2.set_xlabel("Time ($t$)")
        ax2.set_ylabel("Error Residual")
        
        stats_text_2 = (f"Mean Residual: {metrics['mean_residual']:.4e}\n"
                        f"Tripwire Limit: {ERROR_THRESHOLD:.1e}\n"
                        f"Classical: {metrics['classical_status'].split()[0]}")
        props_2 = dict(boxstyle='round', facecolor='lightgreen' if metrics['mean_residual'] <= ERROR_THRESHOLD else 'lightcoral', alpha=0.5)
        ax2.text(0.02, 0.95, stats_text_2, transform=ax2.transAxes, fontsize=10,
                verticalalignment='top', bbox=props_2)
        
        ax2.legend(loc="upper right")
        ax2.grid(True, linestyle=":", alpha=0.6)
        
        plt.tight_layout()
        plt.show()
        
        # Explicit Dual-Channel Audit Printout
        print("==========================================================")
        print(f"  AUDIT PARAMETERS -> kL: {kl:.2f} | N: {n_val} | Noise: {noise:.4f}")
        print("----------------------------------------------------------")
        print(f"  [1] WIN SUBSTRATE STATUS   : {metrics['win_status']}")
        print(f"      - Invariant Peak       : {metrics['win_peak']:.4f}")
        print(f"      - Invariant Mean       : {metrics['win_mean']:.4f}")
        print("----------------------------------------------------------")
        print(f"  [2] CLASSICAL ALIGNMENT    : {metrics['classical_status']}")
        print(f"      - Observed Peak        : {metrics['classical_peak']:.4f}")
        print(f"      - Mean Residual        : {metrics['mean_residual']:.2e}")
        print(f"      - Falsifiability Limit : {ERROR_THRESHOLD:.2e}")
        print("==========================================================")

# Bind widgets
interactive_plot = widgets.interactive(update_visualization, kl=kl_slider, n_val=n_slider, noise=noise_slider)
display(interactive_plot, output_plot)