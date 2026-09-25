# ============================================================
# WIN PARADIGM — INTERACTIVE WIDGET SUITE (v2, September 2026)
# Generates all figures for the README and the widget folder.
# Author: Stanley Preschutti
# ORCID:  0009-0004-5445-1744
# ============================================================
!pip install matplotlib numpy --quiet

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from matplotlib.colors import LinearSegmentedColormap
import os

os.makedirs("figures", exist_ok=True)

# ---------- STYLE ----------
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#333333",
    "axes.labelcolor": "#222222",
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "figure.facecolor": "white",
    "axes.facecolor": "#FAFAFA",
})

ACCENT     = "#1F6FEB"   # blue
ACCENT_2   = "#C44E52"   # red
ACCENT_3   = "#55A868"   # green
ACCENT_4   = "#D4A017"   # gold
NEUTRAL    = "#6B7280"   # gray

# ============================================================
# FIGURE 1 — THE DERIVATION CHAIN
# ============================================================
def fig_derivation_chain():
    fig, ax = plt.subplots(figsize=(12, 14))
    ax.set_xlim(0, 10); ax.set_ylim(0, 20)
    ax.axis("off")

    steps = [
        ("Photon (massless spin-1)",          "2 helicity states × 2 real components",     "#E8EEFB"),
        ("d = 4",                              "spacetime dimension (Wick rotation)",       "#D6E4F7"),
        ("N = d · 2^d = 64",                   "substrate size",                            "#C4DAF3"),
        ("8 × 8 torus  Λ = ℤ₈ × ℤ₈",          "L = √N = 8",                                "#B2D0EF"),
        ("Hodge complex  Ω⁰⊕Ω¹⊕Ω²",            "dim 256,  D² = Δ exactly",                  "#A0C6EB"),
        ("λ = 4 sector (56 states)",           "9A₁ ⊕ 5A₂ ⊕ 7B₁ ⊕ 7B₂ ⊕ 14E",              "#8EBCE7"),
        ("14-mode multiplet",                  "one SM generation  (10F + 4B)",             "#7CB2E3"),
        ("Gauge algebra",                      "su(3) ⊕ su(2) ⊕ u(1)⁵",                     "#6AA8DF"),
        ("Dimensional uplift",                 "dim ker D = b₀+b₁+b₂ = 4",                  "#589EDB"),
        ("Graviton",                           "54B₁ ⊕ 54B₂  (108 modes)",                  "#4694D7"),
        ("Hidden B₁ sector",                   "3_Ω¹ ⊕ 2_Ω² = (d−1) + d/2 = d+1",          "#348AD3"),
        ("(d+1)² = 25",                        "bilinear trace  →  G_N  and  sin²θ_W",      "#227FCF"),
    ]

    y = 19.0
    for i, (title, sub, color) in enumerate(steps):
        box = FancyBboxPatch((1.0, y - 0.75), 8.0, 1.1,
                              boxstyle="round,pad=0.08",
                              linewidth=1.5, edgecolor="#333333",
                              facecolor=color)
        ax.add_patch(box)
        ax.text(5.0, y - 0.05, title, ha="center", va="center",
                fontsize=13, fontweight="bold", color="#111111")
        ax.text(5.0, y - 0.5, sub, ha="center", va="center",
                fontsize=10, color="#222222", style="italic")
        if i < len(steps) - 1:
            arrow = FancyArrowPatch((5.0, y - 0.85), (5.0, y - 1.15),
                                     arrowstyle="-|>", mutation_scale=18,
                                     linewidth=1.5, color="#555555")
            ax.add_patch(arrow)
        y -= 1.55

    ax.text(5.0, 0.4, "Physics is what the machine cannot cancel.",
            ha="center", va="center", fontsize=13,
            fontweight="bold", color=ACCENT_4, style="italic")

    plt.tight_layout()
    plt.savefig("figures/01_derivation_chain.png", dpi=200,
                bbox_inches="tight")
    plt.close()
    print("  ✓ 01_derivation_chain.png")


# ============================================================
# FIGURE 2 — TORUS LAPLACIAN SPECTRUM
# ============================================================
def fig_torus_spectrum():
    L = 8
    spectrum = []
    for n1 in range(L):
        for n2 in range(L):
            lam = 4 - 2*np.cos(np.pi*n1/4) - 2*np.cos(np.pi*n2/4)
            spectrum.append(lam)
    spectrum = np.array(spectrum)

    fig, ax = plt.subplots(figsize=(12, 6))
    unique, counts = np.unique(np.round(spectrum, 6), return_counts=True)
    bars = ax.bar(unique, counts, width=0.12,
                   color=NEUTRAL, edgecolor="#333333", linewidth=0.8)
    for u, c, b in zip(unique, counts, bars):
        if abs(u - 4.0) < 1e-6:
            b.set_color(ACCENT)
            b.set_edgecolor("#111111")
            b.set_linewidth(2)
    ax.axvline(x=4.0, color=ACCENT, linestyle="--", linewidth=1.5,
               alpha=0.6, label="λ = 4 (self-paired)")
    ax.annotate("14 modes\n(SM generation)",
                xy=(4.0, 14), xytext=(5.6, 15),
                fontsize=12, fontweight="bold", color=ACCENT,
                arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.5))
    ax.set_xlabel("Laplacian eigenvalue λ", fontsize=12)
    ax.set_ylabel("Multiplicity", fontsize=12)
    ax.set_title("The 8 × 8 torus Laplacian spectrum",
                 fontsize=14, fontweight="bold")
    ax.legend(frameon=True, loc="upper right")
    ax.grid(True, linestyle=":", alpha=0.5, axis="y")

    plt.tight_layout()
    plt.savefig("figures/02_torus_spectrum.png", dpi=200,
                bbox_inches="tight")
    plt.close()
    print("  ✓ 02_torus_spectrum.png")


# ============================================================
# FIGURE 3 — HODGE COMPLEX D4 DECOMPOSITION
# ============================================================
def fig_hodge_decomposition():
    fig, ax = plt.subplots(figsize=(12, 6))
    irreps = ["A₁", "A₂", "B₁", "B₂", "E"]
    visible = [3, 1, 2, 2, 3]      # Ω⁰|λ=4
    hidden1 = [3, 3, 3, 3, 8]      # Ω¹|λ=4
    hidden2 = [3, 1, 2, 2, 3]      # Ω²|λ=4

    x = np.arange(len(irreps))
    w = 0.27
    b1 = ax.bar(x - w, visible, w, label="Ω⁰|λ=4  (visible, 14)",
                color=ACCENT, edgecolor="#111111", linewidth=0.8)
    b2 = ax.bar(x, hidden1, w, label="Ω¹|λ=4  (hidden, 28)",
                color=ACCENT_2, edgecolor="#111111", linewidth=0.8)
    b3 = ax.bar(x + w, hidden2, w, label="Ω²|λ=4  (hidden, 14)",
                color=ACCENT_3, edgecolor="#111111", linewidth=0.8)

    # highlight B1
    ax.axvspan(1.7, 2.3, alpha=0.08, color=ACCENT_4, zorder=0)
    ax.text(2.0, 8.8, "hidden B₁ = 3 + 2 = 5",
            ha="center", fontsize=11, fontweight="bold",
            color=ACCENT_4, style="italic")

    ax.set_xticks(x)
    ax.set_xticklabels([f"$\\mathbf{{{i}}}$" for i in irreps], fontsize=14)
    ax.set_ylabel("Multiplicity", fontsize=12)
    ax.set_xlabel("D₄ irreducible representation", fontsize=12)
    ax.set_title("Hodge complex at λ = 4: total 56 states",
                 fontsize=14, fontweight="bold")
    ax.legend(frameon=True, loc="upper right", fontsize=10)
    ax.grid(True, linestyle=":", alpha=0.5, axis="y")
    ax.set_ylim(0, 10)

    plt.tight_layout()
    plt.savefig("figures/03_hodge_decomposition.png", dpi=200,
                bbox_inches="tight")
    plt.close()
    print("  ✓ 03_hodge_decomposition.png")


# ============================================================
# FIGURE 4 — DIMENSIONAL UPLIFT
# ============================================================
def fig_dimensional_uplift():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")

    # Left: Hodge complex
    ax.text(2.5, 5.5, "Hodge complex  Ω⁰ ⊕ Ω¹ ⊕ Ω²",
            ha="center", fontsize=13, fontweight="bold")
    boxes = [
        (1.0, 3.8, "Ω⁰\n0-forms\ndim 64", "#D6E4F7"),
        (2.3, 3.8, "Ω¹\n1-forms\ndim 128", "#A0C6EB"),
        (3.6, 3.8, "Ω²\n2-forms\ndim 64", "#6AA8DF"),
    ]
    for x0, y0, txt, c in boxes:
        box = FancyBboxPatch((x0, y0), 1.15, 1.4,
                              boxstyle="round,pad=0.06",
                              linewidth=1.2, edgecolor="#333333", facecolor=c)
        ax.add_patch(box)
        ax.text(x0 + 0.575, y0 + 0.7, txt, ha="center", va="center",
                fontsize=10, fontweight="bold")

    # Arrow
    arrow = FancyArrowPatch((5.2, 4.5), (6.2, 4.5),
                             arrowstyle="-|>", mutation_scale=22,
                             linewidth=2, color="#333333")
    ax.add_patch(arrow)
    ax.text(5.7, 4.85, "D = d + d*", ha="center", fontsize=11,
            fontweight="bold", style="italic")

    # Right: kernel
    ax.text(8.2, 5.5, "Kernel of Hodge–Dirac",
            ha="center", fontsize=13, fontweight="bold")
    ax.text(8.2, 4.5, "dim ker D  =  b₀ + b₁ + b₂",
            ha="center", fontsize=12)
    ax.text(8.2, 3.9, "=  1 + 2 + 1  =  4",
            ha="center", fontsize=18, fontweight="bold", color=ACCENT)
    ax.text(8.2, 3.1, "b₀ = 1  (time)",
            ha="center", fontsize=11)
    ax.text(8.2, 2.6, "b₁ = 2  (spatial planes)",
            ha="center", fontsize=11)
    ax.text(8.2, 2.1, "b₂ = 1  (fourth direction)",
            ha="center", fontsize=11)
    ax.text(8.2, 1.2, "Four harmonic forms = four spacetime directions",
            ha="center", fontsize=11, fontweight="bold",
            color=ACCENT_4, style="italic")

    plt.tight_layout()
    plt.savefig("figures/04_dimensional_uplift.png", dpi=200,
                bbox_inches="tight")
    plt.close()
    print("  ✓ 04_dimensional_uplift.png")


# ============================================================
# FIGURE 5 — GRAVITON DECOMPOSITION
# ============================================================
def fig_graviton():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Sym² decomposition
    irreps = ["A₁", "A₂", "B₁", "B₂", "E"]
    mults = [60, 46, 54, 54, 96]
    dims = [1, 1, 1, 1, 2]
    sizes = [m*d for m, d in zip(mults, dims)]
    colors = [NEUTRAL, NEUTRAL, ACCENT, ACCENT, "#CCCCCC"]
    bars = ax1.bar(irreps, sizes, color=colors,
                    edgecolor="#111111", linewidth=1)
    for b, m in zip(bars, mults):
        ax1.text(b.get_x() + b.get_width()/2, b.get_height() + 3,
                 f"{m}", ha="center", fontsize=11, fontweight="bold")
    ax1.set_ylabel("Dimension", fontsize=12)
    ax1.set_title("Sym²(Ω¹|λ=4) = 406 states",
                  fontsize=13, fontweight="bold")
    ax1.text(2.0, 115, "Graviton\n54B₁ ⊕ 54B₂\n= 108 modes",
             ha="center", fontsize=12, fontweight="bold",
             color=ACCENT, style="italic")
    ax1.grid(True, linestyle=":", alpha=0.5, axis="y")
    ax1.set_ylim(0, 210)

    # Right: Mirror splitting
    categories = ["Self-paired\n(physical)", "Anti-self-paired\n(cancels)"]
    dims_split = [214, 192]
    colors_split = [ACCENT, NEUTRAL]
    bars2 = ax2.bar(categories, dims_split, color=colors_split,
                     edgecolor="#111111", linewidth=1, width=0.5)
    for b, d in zip(bars2, dims_split):
        ax2.text(b.get_x() + b.get_width()/2, b.get_height() + 4,
                 str(d), ha="center", fontsize=14, fontweight="bold")
    ax2.set_ylabel("Dimension", fontsize=12)
    ax2.set_title("Mirror splitting under M = r²",
                  fontsize=13, fontweight="bold")
    ax2.text(0, 130, "60A₁ ⊕ 46A₂\n⊕ 54B₁ ⊕ 54B₂",
             ha="center", fontsize=10)
    ax2.text(1, 130, "96E",
             ha="center", fontsize=10)
    ax2.grid(True, linestyle=":", alpha=0.5, axis="y")
    ax2.set_ylim(0, 260)

    plt.tight_layout()
    plt.savefig("figures/05_graviton.png", dpi=200, bbox_inches="tight")
    plt.close()
    print("  ✓ 05_graviton.png")


# ============================================================
# FIGURE 6 — HIDDEN B1 SECTOR AND DUAL ROLE
# ============================================================
def fig_dual_role():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5.5))

    # Panel 1: 3 + 2 = 5
    ax1.bar([0], [3], color=ACCENT, edgecolor="#111111",
             linewidth=1, label="Ω¹|λ=4  (fermionic)")
    ax1.bar([0], [2], bottom=[3], color=ACCENT_2,
             edgecolor="#111111", linewidth=1,
             label="Ω²|λ=4  (bosonic)")
    ax1.text(0, 1.5, "3", ha="center", va="center",
             fontsize=20, fontweight="bold", color="white")
    ax1.text(0, 4.0, "2", ha="center", va="center",
             fontsize=20, fontweight="bold", color="white")
    ax1.set_xticks([0])
    ax1.set_xticklabels(["Hidden B₁"], fontsize=12)
    ax1.set_ylabel("Dimension", fontsize=12)
    ax1.set_title("Hidden B₁ = 3 + 2 = 5\n(d−1) + d/2 = d+1",
                  fontsize=12, fontweight="bold")
    ax1.legend(frameon=True, fontsize=9, loc="upper right")
    ax1.grid(True, linestyle=":", alpha=0.5, axis="y")
    ax1.set_ylim(0, 6)

    # Panel 2: bilinear trace = 25
    dim = 5
    grid = np.arange(dim * dim).reshape(dim, dim)
    ax2.imshow(np.ones((dim, dim)), cmap="Blues",
               vmin=0, vmax=2)
    for i in range(dim):
        for j in range(dim):
            if j < 3 and i < 3:
                ax2.add_patch(Rectangle((j-0.5, i-0.5), 1, 1,
                              facecolor=ACCENT, alpha=0.5))
            elif j >= 3 and i >= 3:
                ax2.add_patch(Rectangle((j-0.5, i-0.5), 1, 1,
                              facecolor=ACCENT_2, alpha=0.5))
            else:
                ax2.add_patch(Rectangle((j-0.5, i-0.5), 1, 1,
                              facecolor=ACCENT_4, alpha=0.4))
    ax2.set_xticks(range(dim))
    ax2.set_yticks(range(dim))
    ax2.set_title("Bilinear trace\n5 × 5 = 25 = (d+1)²",
                  fontsize=12, fontweight="bold")
    ax2.set_xlabel("9 F-F + 12 F-B + 4 B-B", fontsize=10)

    # Panel 3: dual role
    labels = ["b₂ contribution\n→ sin²θ_W", "Bilinear trace\n→ G_N"]
    values = [5/3, 25]
    x = np.arange(2)
    ax3.bar(x, values, color=[ACCENT_3, ACCENT_4],
             edgecolor="#111111", linewidth=1, width=0.6)
    ax3.text(0, 5/3 + 0.5, "5/3", ha="center",
             fontsize=16, fontweight="bold")
    ax3.text(1, 25 + 0.5, "25", ha="center",
             fontsize=16, fontweight="bold")
    ax3.set_xticks(x)
    ax3.set_xticklabels(labels, fontsize=11)
    ax3.set_ylabel("Value", fontsize=12)
    ax3.set_title("Same 5 states, two predictions",
                  fontsize=12, fontweight="bold")
    ax3.grid(True, linestyle=":", alpha=0.5, axis="y")
    ax3.set_ylim(0, 28)

    plt.suptitle("The dual role of the hidden B₁ sector",
                 fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()
    plt.savefig("figures/06_dual_role.png", dpi=200, bbox_inches="tight")
    plt.close()
    print("  ✓ 06_dual_role.png")


# ============================================================
# FIGURE 7 — NEWTON CONSTANT COMPARISON
# ============================================================
def fig_newton_constant():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

    # Panel 1: predicted vs observed
    predicted = 6.683139e-39
    observed  = 6.674000e-39
    bars = ax1.bar(["Predicted\n(WIN)", "Observed\n(Planck)"],
                    [predicted, observed],
                    color=[ACCENT, NEUTRAL],
                    edgecolor="#111111", linewidth=1, width=0.55)
    for b, v in zip(bars, [predicted, observed]):
        ax1.text(b.get_x() + b.get_width()/2, b.get_height()*1.005,
                 f"{v:.3e}", ha="center", fontsize=11, fontweight="bold")
    ax1.set_ylabel(r"$G_N$  [GeV$^{-2}$]", fontsize=12)
    ax1.set_title("Newton constant: theory vs observation",
                  fontsize=13, fontweight="bold")
    ax1.set_ylim(6.65e-39, 6.70e-39)
    ax1.grid(True, linestyle=":", alpha=0.5, axis="y")
    ax1.text(0.5, 6.69e-39, f"ratio = 1.0014\n(match to 0.14%)",
             ha="center", fontsize=12, fontweight="bold",
             color=ACCENT_3, style="italic")

    # Panel 2: The 25 decomposition
    parts = [9, 6, 6, 4]
    labels = ["F-F\n(3×3)", "F-B\n(3×2)", "B-F\n(2×3)", "B-B\n(2×2)"]
    colors = [ACCENT, ACCENT_4, ACCENT_4, ACCENT_2]
    ax2.bar(labels, parts, color=colors,
             edgecolor="#111111", linewidth=1)
    for i, v in enumerate(parts):
        ax2.text(i, v + 0.2, str(v), ha="center",
                 fontsize=14, fontweight="bold")
    ax2.set_ylabel("Number of channels", fontsize=12)
    ax2.set_title("25 = 9 + 6 + 6 + 4\n(fermion/boson decomposition)",
                  fontsize=13, fontweight="bold")
    ax2.grid(True, linestyle=":", alpha=0.5, axis="y")
    ax2.set_ylim(0, 11)

    plt.tight_layout()
    plt.savefig("figures/07_newton_constant.png", dpi=200, bbox_inches="tight")
    plt.close()
    print("  ✓ 07_newton_constant.png")


# ============================================================
# FIGURE 8 — MASS MAP
# ============================================================
def fig_mass_map():
    # (name, N/4, observed mass in GeV)
    fermions = [
        ("e",   24.0, 0.000511), ("μ", 14.0, 0.10566),
        ("τ",    9.0, 1.77686),  ("u", 21.0, 0.00216),
        ("d",   20.0, 0.00467),  ("s", 14.0, 0.0934),
        ("c",    9.5, 1.27),     ("b",  7.5, 4.18),
        ("t",    0.5, 172.7),
    ]
    A_mass = 224.0
    B_mass = 0.541197
    names = [f[0] for f in fermions]
    n4    = np.array([f[1] for f in fermions])
    obs   = np.array([f[2] for f in fermions])
    pred  = A_mass * np.exp(-B_mass * n4)

    fig, ax = plt.subplots(figsize=(11, 6))
    ax.scatter(obs, pred, s=120, color=ACCENT,
                edgecolor="#111111", linewidth=1.2, zorder=3)
    for name, o, p in zip(names, obs, pred):
        ax.annotate(name, (o, p), fontsize=11, fontweight="bold",
                    xytext=(6, 6), textcoords="offset points")
    lo, hi = 1e-4, 1e3
    ax.plot([lo, hi], [lo, hi], "--", color=NEUTRAL,
             linewidth=1.2, label="Perfect match")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(lo, hi); ax.set_ylim(lo, hi)
    ax.set_xlabel("Observed mass [GeV]", fontsize=12)
    ax.set_ylabel("Predicted mass [GeV]", fontsize=12)
    ax.set_title("Mass map:  m = A·exp(−B·N/4)\nRMS 0.0449 dex, zero fitted parameters",
                  fontsize=13, fontweight="bold")
    ax.grid(True, which="both", linestyle=":", alpha=0.5)
    ax.legend(frameon=True, loc="upper left")

    plt.tight_layout()
    plt.savefig("figures/08_mass_map.png", dpi=200, bbox_inches="tight")
    plt.close()
    print("  ✓ 08_mass_map.png")


# ============================================================
# FIGURE 9 — FALSIFIABLE PREDICTIONS TIMELINE
# ============================================================
def fig_predictions_timeline():
    fig, ax = plt.subplots(figsize=(13, 5.5))
    predictions = [
        ("V_td = 0.0061 ± 0.0001",       2026, 2028, ACCENT),
        ("w = −1.014054...",              2026, 2027, ACCENT_2),
        ("ζH/ρ = 0.004684...",            2027, 2028, ACCENT_3),
        ("Graviton spin = 2",             2026, 2030, ACCENT_4),
        ("Graviton mass < 10⁻⁷⁴ M_P",     2026, 2030, NEUTRAL),
        ("ε = 0.001193 (kinetic mixing)", 2026, 2030, "#8E44AD"),
        ("STEP η < 10⁻¹⁸ (equivalence)",  2030, 2035, "#7F8C8D"),
    ]
    y_positions = np.arange(len(predictions))
    for i, (label, start, end, color) in enumerate(predictions):
        ax.barh(i, end - start, left=start, height=0.6,
                 color=color, edgecolor="#111111", linewidth=1, alpha=0.85)
        ax.text(start - 0.15, i, label, ha="right", va="center",
                fontsize=11, fontweight="bold")
    ax.axvline(2026, color="#333333", linestyle=":", linewidth=1,
                alpha=0.6)
    ax.text(2026, len(predictions)-0.3, " now",
            fontsize=11, fontweight="bold", color="#333333")
    ax.set_yticks([])
    ax.set_xlabel("Year", fontsize=12)
    ax.set_xlim(2024, 2036)
    ax.set_title("Falsifiable predictions: test windows",
                  fontsize=14, fontweight="bold")
    ax.grid(True, linestyle=":", alpha=0.5, axis="x")
    plt.tight_layout()
    plt.savefig("figures/09_predictions.png", dpi=200, bbox_inches="tight")
    plt.close()
    print("  ✓ 09_predictions.png")


# ============================================================
# FIGURE 10 — FIVE-LAYER LOOP
# ============================================================
def fig_loop():
    fig, ax = plt.subplots(figsize=(11, 9))
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal"); ax.axis("off")

    layers = [
        ("FDLM/WIN\nlattice",        0.0, 1.0,  ACCENT),
        ("DME\ndimensional\nstability",   1.0, 0.3,  ACCENT_2),
        ("ENTROPIA-Core\ngradient flow",   0.6, -1.0, ACCENT_3),
        ("ENTROPIA-EFT\nvacuum",     -0.6, -1.0, ACCENT_4),
        ("Processor T\nreadout",       -1.0, 0.3,  "#8E44AD"),
    ]
    for label, x, y, color in layers:
        c = plt.Circle((x, y), 0.28, color=color, alpha=0.85,
                        edgecolor="#111111", linewidth=1.5, zorder=3)
        ax.add_patch(c)
        ax.text(x, y, label, ha="center", va="center",
                fontsize=9, fontweight="bold", color="white", zorder=4)

    # Arrows between layers
    for i in range(len(layers)):
        x1, y1 = layers[i][1], layers[i][2]
        x2, y2 = layers[(i+1) % len(layers)][1], layers[(i+1) % len(layers)][2]
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>",
                                     color="#555555",
                                     lw=1.8,
                                     connectionstyle="arc3,rad=0.15",
                                     shrinkA=22, shrinkB=22))

    ax.text(0, -1.4, "Time = loop eigenvalue τ = θ + i·ln r",
            ha="center", fontsize=12, fontweight="bold",
            color=ACCENT)
    ax.text(0, 1.35, "The WIN five-layer loop",
            ha="center", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("figures/10_loop.png", dpi=200, bbox_inches="tight")
    plt.close()
    print("  ✓ 10_loop.png")


# ============================================================
# RUN ALL
# ============================================================
if __name__ == "__main__":
    print("Generating WIN Paradigm widget figures...")
    fig_derivation_chain()
    fig_torus_spectrum()
    fig_hodge_decomposition()
    fig_dimensional_uplift()
    fig_graviton()
    fig_dual_role()
    fig_newton_constant()
    fig_mass_map()
    fig_predictions_timeline()
    fig_loop()
    print("\nDone. 10 figures written to figures/")
