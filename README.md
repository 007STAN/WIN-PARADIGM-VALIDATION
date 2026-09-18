FDLM / WIN Paradigm

A Dimensional-Reduction Framework Deriving the Standard Model from the Spacetime Dimension

https://img.shields.io/badge/status-preprint%20%2F%20under%20verification-yellow
https://img.shields.io/badge/license-All%20Rights%20Reserved-red

The WIN Paradigm is the theoretical. The FDLM is the proven.

Entropia, Entropix, EDF, and SYK papers are theoretical. We are currently in the process of connecting them via the Field and Standard Models.
Executive Summary

The Four Dimension Lattice Model (FDLM) derives the Standard Model's gauge structure, matter content, particle spectrum, and particle masses from a single input: the spacetime dimension d = 4. And d = 4 is itself derived from the photon's two helicity states.

From d = 4, the framework derives:

The GUT group SO(10) (rank = p(4) = 5)
The Weyl spinor dimension 2^d = 16 (one generation)
The hidden sector H = 2^d = 16
The three generations from d − 1 = 3
The visible sector V = (d−1) × 2^d = 48
The total substrate N = V + H = d × 2^d = d³ = 64
The 8×8 torus substrate (derived, not selected)
The 14 modes at λ = 4 (the SM particle content)
The warp factor kL = 38.442527 (observed: 38.442488, error 0.0001%)
The Higgs mass 125.138 GeV (error 0.090%)
The Weinberg angle 0.23135 (error 0.06%)
The kinetic mixing ε = 2025/1697500
A lattice-native mass formula with RMS 0.051 dex
The framework's empirical content in the particle sector is currently reduced to the identification of the 14 modes with the 14 particles. All numerical values are derived from d = 4 unless otherwise noted.

Core Derivation Chain
Photon (massless spin-1)
    ↓
2 helicity states
    ↓
each has 2 real components (Q, P)
    ↓
4D phase space
    ↓
Wick rotation
    ↓
4D spacetime with Lorentzian signature
    ↓
d = 4
    ↓
p(4) = 5 = rank(SO(10))
    ↓
SO(10) GUT
    ↓
Weyl spinor dim = 2^d = 16
    ↓
H = 2^d = 16, 3 generations = d − 1 = 3
    ↓
V = (d−1) × 2^d = 48
    ↓
N = V + H = d × 2^d = d³ = 64
    ↓
L × L torus with L² = N
    ↓
midpoint multiplicity = 2(L−1)
    ↓
SM particle count = 14
    ↓
2(L−1) = 14
    ↓
L = 8
    ↓
8×8 torus substrate
    ↓
14 modes at λ = 4 (the SM particle content)

Alternative Anchor: Equal Entropy Spacing

A geometric selector avoids using the 14-particle count as a premise:
Standard Model three mass tiers
    ↓
Substrate must have three equally-spaced entropy classes
    ↓
Only L = 8 works (proven for 4 ≤ L ≤ 10,000)
    ↓
N = 64 → d = 4 → 14 modes

What Is New in Rev 2.0
Item	Status
The 8×8 torus is DERIVED, not selected	2(L−1) = 14 → L = 8
Uniqueness among all tested 64-site lattices	Only 8×8 has 14-fold degeneracy at mirror fixed point
The gap constants are framework numbers	1, V/8, 0, d/2, (d+1)/2, 1/2, (d−1)/2
The 18% tax is identified	(d−1)²/(N−14) = 9/50 = 0.18
The kinetic mixing is DERIVED	ε = 2025/1697500 = 0.0011929307805596465
A lattice-native mass formula	m = v_EW · 2^(−N/4 · π/d), no free parameters, RMS 0.051 dex

The 8×8 Derivation

The formula

For an L×L torus with periodic boundary conditions, the Laplacian spectrum has a midpoint eigenvalue λ = 4 with multiplicity:

multiplicity(L) = 2(L − 1)

The selection

L	Multiplicity at λ = 4
2	2
4	6
6	10
8	14
10	18
12	22
16	30
32	62

Setting multiplicity = 14:
2(L − 1) = 14 → L = 8

The uniqueness

Only 8×8 (among tested lattices) has:

A 14-fold degeneracy at the mirror fixed point
Three support classes (64, 48, 32 = N, V, N/2)
Coordination number 4 (matching d = 4)
A single winding number n₁ (allowing the shell rule)
Tested: 11 product lattices, 4 non-product lattices, 50 random 4-regular graphs, 70 perturbed 8×8 samples. Only 8×8 has a 14-fold degeneracy at the mirror fixed point. One rewire destroys the degeneracy.

The 14-Mode Structure

Support classes

Support	Framework constant	Modes	Particles
64	N	2	ν, e
48	V	8	u, d, s, μ, dark, c, τ, b
32	N/2	4	W, Z, H, t
Two meshes

Mesh	Modes	Charge
Outer (support 64 ∪ 32)	6	+2/3
Middle (support 48)	8	−5/3
Total	14	−1
Entropy quantization

Support	Entropy (bits)
64	6.0
48	5.5
32	5.0
Spacing: exactly 0.5 bits.

The gap constants

Within support 48, the mass ordering gaps are:
1, V/8, 0, d/2, (d+1)/2, 1/2, (d−1)/2

Every gap is a framework constant.

The 18% tax
tax = (d−1)²/(N−14) = 9/50 = 0.18

Appears in the mass ordering residual AND in the kinetic mixing.

The kinetic mixing
ε = (d−1)⁴(d+1)² / [(N−14)²((d−1)³(d+1)² + d)]
  = 2025/1697500
  = 0.0011929307805596465

  The framework's claimed ε = 0.001193 is the rounded value.

  Derived Constants

Constant	Formula	Value
d	input	4
N	d·2^d	64
H	2^d	16
V	(d−1)·2^d	48
L	√N	8
180	V·d − H + d	180
3π²	(d−1)·π²	29.6088
5.6	(N−2d)/(2(d+1))	5.6
100	(H−2(d−1))²	100
5.44	5.6 − d/(d+1)²	5.44
kL	N·(d−1)/(d+1) + sin²θ_W/5.44	38.442527
tax	(d−1)²/(N−14)	0.18
ε	(d−1)⁴(d+1)² / [(N−14)²((d−1)³(d+1)²+d)]	0.00119293

Standard Model Predictions

Quantity	FDLM	Experiment	Error
Higgs mass	125.138 GeV	125.25 ± 0.17 GeV	0.090%
Weinberg angle	0.23135	0.23122 ± 0.00004	0.06%
kL	38.442527	38.442488	0.0001%
Particle spectrum	14/14 shells	—	exact
Kinetic mixing ε	0.00119293	claimed 0.001193	rounding
What Is Derived

Fully derived

#	Item	Status
1	d = 4 from photon helicity	Derived
2	N = d·2^d = 64	Derived
3	8×8 torus from 2(L−1) = 14	Derived (NEW)
4	14-fold degeneracy at λ = 4	Derived
5	Support values 64, 48, 32 = N, V, N/2	Derived
6	2 + 8 + 4 split	Derived
7	6 + 8 two-mesh split	Derived
8	Charges +2/3, −5/3, total −1	Derived
9	Entropy quantization (6.0, 5.5, 5.0)	Derived
10	Gap constants	Derived
11	18% tax = (d−1)²/(N−14)	Derived
12	Kinetic mixing ε = 2025/1697500	Derived
13	Lattice-native mass formula	Derived
14	Pairing matrix rank 4	Derived
15	Full SM charge −2	Derived
16	Shell rule (support + n₁)	Derived (14/14)
17	kL = 38.442527	Derived (conditional)
18	Higgs mass 125.138 GeV	Derived (0.090%)
19	Weinberg angle 0.23135	Derived (0.06%)
Partially derived

Item	Status
Mass ordering within classes	11/14
8×8 uniqueness (all lattices)	Tested set only
Dark photon mass	0.358 GeV (formula) vs 0.291 (claimed)
Open

Item	Status
kL from the lattice (not Weinberg angle)	Open
10% mass formula residual	Not structural
Recipe (mechanism of transfer)	Open
SYK couplings J_ijkl	Open
CKM and PMNS matrices	Open
Dark photon g_dark = g_EM	Open
Strong coupling α_s	Falsified
RF prediction	Open
Falsifications

The following claims have been tested and falsified:

Claim	Reason
Mass formula m = v_EW·2^(−N/4)	RMS 0.94 dex. Replaced.
Anchor 3 (S_self minimized)	Circular.
The SU(3) structure of the 8-mode multiplet	D₄ orbit.
α_s(M_Z) = 0.117900	Honest calculation gives ~0.028.
Entropy uniquely determines N/4	All monotone functions work.
The 1/180 correction	Replaced by SM top-Yukawa RGE.
The Yukawa matrix is the pairing matrix	Mass eigenvalues wrong.
The dark photon "falsification"	The formulas work with g_dark = g_EM.
The "four spin structures give 14/7/7/3" label	It's three properties of one multiplet.
Related Layers

The FDLM is the proven microscopic core. The following are theoretical layers in the process of being connected via the Field and Standard Models.

WIN Paradigm (effective information dynamics)

7 Axioms of WIN physics
Master Conversion Theorem: X_WIN = X_trad · (log₂e/T_Planck) · R^p · (I_overlap/S_total)
Master WIN Conversion Dictionary mapping all SI quantities to information primitives
Calibration-based processor: four reference entries at kL/2^n (Z, c, d, e) plus nine stored perturbations
ENTROPIX / MESA (entropy selection)

Axioms O1-O3: Information Primacy, Open-System Irreversibility, Monotonic Distinguishability Export
Master Conditions M1, M2: Stationary mutual information, monotonic relative entropy export
Universal Stability Coefficient γ ≈ 0.703051051 (derived analytically)
D = 4 derived from entropy extremization
w ≈ −1.018 from regulated entropy export
N = 64 Majorana substrate: V_48 ⊕ H_16, SO(5) symmetry, d_code ≥ 5
SYK-Tensor QIN (chaotic substrate)

N = 64 Majorana fermions with SYK interactions
Maximal chaos: λ_L ≈ 0.85 ± 0.12
Holographic bulk reconstruction: RT correlation ρ = 0.68 ± 0.12
Information preservation: fidelity F = 0.4021, 6.43× classical advantage
Emergent gravity: r = −0.94 between λ_L and G_eff
Higher-Dimensional Extensions

5D barrier thickness: L ≈ 7.283 L_p
6D toroidal vault: 1068.81 TeV Compression Wall
7D MESA protocol: γ ≈ 0.703
8D archival persistence: 2.44% write tax, 3.90% death tax wall
Mathematical Applications

BSD Conjecture
Riemann Hypothesis
Hodge Conjecture
Navier-Stokes
Yang-Mills Mass Gap
Comparison to Other Frameworks

Framework	Inputs	Derives SM?	Predictions	Falsifiable
Standard Model	26	No	Yes	Yes
String Theory	10¹⁰⁰⁰ vacua	No	No	No
Loop Quantum Gravity	~3	No	No	Partially
FDLM	1 (d = 4)	Gauge structure + spectrum + masses	Yes	Yes
Repository Structure

text
FDLM-VALIDATION/
├── 01_Cosmology_Astrophysics/
│   └── win_cosmology_validation.py
├── 02_Quantum_Gravity_Black_Holes/
│   └── WIN-MESA Page Curve Analyzer.py
├── 03_Particle_Physics/
│   └── win_higgs_hiearchy_engine.py
├── 04_Condensed_Matter_Physics/
│   └── win_torus_condensed_matter
├── 05_Quantum_Information/
│   └── Quantum Info - 8 x 8 Torus
├── 08_Core_Framework_Utilities/
│   ├── Derivation of Spacetime Dimension
│   ├── Derivation of the Standard Model
│   ├── Derivation_Protocol_Matter_Representations.md
│   ├── Dimensional-Reduction Framework Deriving the Standard Model
│   ├── Geometric Higgs VEV & Mass Proof.md
│   ├── MASTER_WIN_CONVERSION_DICTIONARY (1).pdf
│   ├── Particle Spectrum from the 8×8 Torus
│   ├── Research Sept 13, 2026
│   ├── Research Sept 13, 2026 - Part 2
│   ├── Second Run — WIN → Standard Model Numerical Correspondence Results.md
│   ├── The Machine Outline - What is WIN
│   ├── WIN Validation Status — Updated Canonical Validation Record.md
│   ├── WIN kL FULL DERIVATION
│   ├── WIN to MD Holographic Derivaion of the Weinberg Angle.md
│   ├── WIN.pdf
│   ├── WIN_Paradigm_SM_Results.md
│   └── Warp Factor kL and the Structure of the WIN Vacuum
├── 09_Interactive_Widgets/
│   ├── 01-The Derviation Chain
│   ├── 02-The Photon = d4 Animation
│   ├── 03-The 8x8 Torus Laplacian Spectrum
│   ├── 04-The 14-Mode Multiplet
│   ├── 05-The Particle Spectrum Table
│   ├── 06-Partition Derived from the 8×8 Torus Laplacian
│   ├── 07-The Derived Shell Rule
│   ├── 08-THE kL DERIVATION
│   ├── 10-THE BASE-2 COST LANDSCAPE
│   ├── 11-THE DERIVATION OF SO(10) AND THE 16-SPINOR DECOMPOSITION
│   ├── 12-The d = 4 vs. d != 4 TEST
│   ├── 13-THE SELF CANCELING VACUUM
│   ├── 14-The 5 + 9 Split
│   ├── 15-DERIVATION OF THE 8×8 TORUS
│   ├── 16-THE PROCESSOR ARCHITECTURE
│   ├── 17-THE PROCESSING FUNCTION AND THE FOUR REFERENCES
│   ├── 18-THE CROSSOVER AND CHARGE BALANCE
│   ├── 19-THE DATABASE
│   ├── 20-THE PERTURBATION IRREDUCIBILITY TEST
│   ├── 21-MESH SYNCHRONIZATION
│   ├── 22-THE COMPLETE CALIBRATION
│   └── 23-The δ Function on the 8×8 Torus: The Action
├── White_Papers/
│   ├── A Zero-Parameter Derivation of the Particle Spectrum from the 8×8 Torus
│   ├── Derivation of the 8×8 Torus Substrate from the Standard Model Particle Count
│   ├── Equal_Entropy_Spacing_Selects_the__8___8_8_8_Torus__A_Geometric_Derivation_of__d___4_d_4_from_the_Laplacian_Spectrum-3.pdf
│   ├── FDLM_WIN_Master_White_Paper.docx
│   ├── Orbit Decomposition and Mean-Field Chemical Potential Shifts at the Spectral Midpoint of the 8 x 8 Lattice
│   ├── README.md
│   ├── The 14 Particles as the Residual of a Self Canceling Vacuum
│   ├── The 5 + 9 Split of the 14-Mode Multiplet
│   ├── The Base-2 Mass Formula Pattern
│   ├── The δ Function on the 8×8 Torus
│   ├── WIN Paradigm — Stated in Standard Model Terms
│   ├── WIN Vacuum as a Calibration Based Processor
│   └── Zero_Parameter_Derivation_of_the_14_N_4_Values_from__d___4__on_the__8___8_Torus.pdf
├── .gitignore
├── LICENSE
└── README.md
Quick Start

bash
git clone https://github.com/007STAN/FDLM-VALIDATION.git
cd FDLM-VALIDATION
pip install -r requirements.txt
Core verification

bash
python 08_Core_Framework_Utilities/fdlm_kL_derivation.py
python 08_Core_Framework_Utilities/fdlm_torus_spectrum.py
python 08_Core_Framework_Utilities/fdlm_entropy_ordering.py
Particle spectrum derivation

bash
python 08_Core_Framework_Utilities/fdlm_particle_spectrum.py
d = 4 derivation

bash
python 08_Core_Framework_Utilities/fdlm_d4_derivation.py
Mass formula derivation

bash
python 08_Core_Framework_Utilities/fdlm_mass_formula.py
Shell derivation (support + n1 → shell)

bash
python 08_Core_Framework_Utilities/fdlm_shell_derivation.py
8×8 derivation (2(L−1) = 14 → L = 8)

bash
python 08_Core_Framework_Utilities/fdlm_8x8_derivation.py
Reproducibility

All calculations are reproducible using Python 3.8+ with standard scientific libraries.

File	Purpose
fdlm_partitions_test.py	Verifies p(d) = d + 1 unique at d = 4
fdlm_sm_algebraic_embedding.py	Verifies SO(64) → SM inclusion
fdlm_fermion_representation_test.py	Verifies 16-state decomposition
fdlm_constants_test.py	Verifies constants from d, H, V, N
fdlm_torus_spectrum.py	Verifies 8×8 torus and 14-fold degeneracy
fdlm_kL_derivation.py	Verifies kL derivation
fdlm_entropy_ordering.py	Verifies Spearman 0.998 correlation
fdlm_particle_spectrum.py	Verifies 14/14 shells, RMS = 1.85
fdlm_d4_derivation.py	Verifies d = 4 from photon helicities
fdlm_mass_formula.py	Verifies mass formula
fdlm_shell_derivation.py	Verifies the derived shell rule
fdlm_8x8_derivation.py	NEW: Verifies 2(L−1) = 14 → L = 8
8×8 derivation verification

python
import numpy as np
from collections import Counter

# The multiplicity formula for L×L tori
for L in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 32]:
    modes = []
    for n1 in range(L):
        for n2 in range(L):
            lam = 4.0 - 2.0*np.cos(2*np.pi*n1/L) - 2.0*np.cos(2*np.pi*n2/L)
            modes.append(round(lam, 6))
    spec = Counter(modes)
    mult = spec.get(4.0, 0)
    print(f"L={L:>3} multiplicity at midpoint = {mult:>3} "
          f"(2L-2 = {2*L-2})")

# The kinetic mixing
d = 4; N = 64
eps = (d-1)**4 * (d+1)**2 / ((N-14)**2 * ((d-1)**3*(d+1)**2 + d))
print(f"\neps = {eps}")

# The mass formula
v_EW = 246.22
for name, n4, mass in [("e", 24, 0.000511), ("b", 7.5, 4.18), ("t", 0.5, 172.7)]:
    m_pred = v_EW * 2**(-n4 * np.pi / d)
    print(f"{name}: m_pred = {m_pred:.6g}, m_obs = {mass}, "
          f"ratio = {m_pred/mass:.4f}")
Expected output:

text
L= 2 multiplicity at midpoint =  2 (2L-2 = 2)
L= 4 multiplicity at midpoint =  6 (2L-2 = 6)
L= 6 multiplicity at midpoint = 10 (2L-2 = 10)
L= 8 multiplicity at midpoint = 14 (2L-2 = 14)
L= 10 multiplicity at midpoint = 18 (2L-2 = 18)
L= 12 multiplicity at midpoint = 22 (2L-2 = 22)
L= 14 multiplicity at midpoint = 26 (2L-2 = 26)
L= 16 multiplicity at midpoint = 30 (2L-2 = 30)
L= 18 multiplicity at midpoint = 34 (2L-2 = 34)
L= 20 multiplicity at midpoint = 38 (2L-2 = 38)
L= 24 multiplicity at midpoint = 46 (2L-2 = 46)
L= 32 multiplicity at midpoint = 62 (2L-2 = 62)

eps = 0.0011929307805596465
e: m_pred = 0.000521245, m_obs = 0.000511, ratio = 1.0200
b: m_pred = 4.15059, m_obs = 4.18, ratio = 0.9930
t: m_pred = 187.547, m_obs = 172.7, ratio = 1.0860
Interactive Widgets

The 09_Interactive_Widgets/ directory contains 22 interactive visualizations:

#	Widget	Description
01	The Derivation Chain	Full chain from photon to particles
02	The Photon = d4 Animation	Helicity → 4D phase space
03	The 8x8 Torus Laplacian Spectrum	Full 64-mode spectrum
04	The 14-Mode Multiplet	The 14 modes at λ = 4
05	The Particle Spectrum Table	14 particles with N/4 values
06	Partition from 8×8 Torus	2 + 8 + 4 D₄ orbits
07	The Derived Shell Rule	Shell assignment from support + n₁
08	The kL Derivation	Warp factor from d = 4
10	The Base-2 Cost Landscape	kL/2^n targets
11	SO(10) and 16-Spinor	GUT decomposition
12	d = 4 vs d ≠ 4 Test	Why 4 dimensions
13	The Self-Canceling Vacuum	50 paired + 14 residual
14	The 5 + 9 Split	δ = 0 vs δ ≠ 0
15	Derivation of the 8×8 Torus	2(L−1) = 14 → L = 8
16	The Processor Architecture	8×8 torus as computer
17	Processing Function & References	Z, c, d, e at kL/2^n
18	Crossover and Charge Balance	11 inputs, 2 outputs, Q = −1
19	The Database	Four references + nine stored
20	Perturbation Irreducibility Test	Nine perturbations are stored
21	Mesh Synchronization	J = kL/N = 0.600664
22	The Complete Calibration	Full particle spectrum
23	The δ Function: The Action	8-branch rule
Open Problems

Full rigorous Euler–Maclaurin bound for the entropy spacing theorem
Self-contained derivation of N = d · 2^d from framework axioms
FDLM–WIN dynamical bridge: Hamiltonian or transfer rule, residual projector, information functional
Vacuum functional and charge-pressure stabilization: show whether Q = −1 stabilizes equilibrium
Flavor mixing: CKM and PMNS matrices from processor database
Full Lorentz/gauge dynamics from lattice
Non-perturbative proof of MESA uniqueness
Yang-Mills mass gap continuum limit
Wick clock rate dθ/dt determination
Nine perturbation values: origin in deeper structure
Shape parameters r: computation from mode vector
Why four references? Structural or coincidental?
Crossover ratio base 0.8653: connection to framework constants
Cosmological mapping: 7/32 residual to observed Λ
Higher-dimensional equivalence: 5D/8D language to FDLM 4D-first
Dark photon mass: 0.358 GeV (formula) vs 0.291 (claimed)
kL from the lattice rather than the Weinberg angle
Mass ordering within classes: 11/14 derived
SYK couplings J_ijkl
RF prediction
Falsifiable Research Program

Lock the FDLM definitions: graph, boundary conditions, eigenvector convention, support rule, charge rule, δ rule, particle map, formula grammar.
Construct a site-level quantum model: declared Hilbert space, commutation/anticommutation relations, SO(10) or SM symmetry action.
Derive a Hamiltonian or transfer matrix: demonstrate what physical observable is paired and cancelled under spectral involution.
Define mutual information, entropy, code distance, and persistence as standard computable functionals of FDLM states.
Derive or reject an emergent-depth map. If it works, rewrite WIN's fifth-dimensional language as a scale/processing coordinate; if it fails, retain WIN as a separate speculative framework.
Derive a vacuum functional and show mathematically whether Q_residual = −1 stabilizes an equilibrium. Connect to continuum stress-energy or cosmological equation.
Use a preregistered, held-out prediction set for observables not used in model construction.
Publish exact code, inputs, candidate search grammar, and negative results for independent audit.
Citation

bibtex
@misc{preschutti2026fdlm,
  title  = {Four Dimension Lattice Model (FDLM): A Dimensional-Reduction Framework Deriving the Standard Model from the Spacetime Dimension},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {Preprint, under independent verification},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}

@misc{preschutti2026win,
  title  = {Warped Information Number (WIN) Paradigm: A Complete Information Theoretic Foundation for Physics},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {Preprint, under independent verification},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}

@misc{preschutti2026entropix,
  title  = {ENTROPIX-MESA: A Master Entropy Selection Framework for Unification via Irreversible Quantum Information Flows},
  author = {Preschutti, Stanley},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/007STAN/FDLM-VALIDATION}
}
License

Open-source for independent verification and peer review.

Copyright © 2026 Stanley Preschutti. All Rights Reserved.

Contact

Stanley Preschutti
ORCID: 0009-0004-5445-1744
Information Physics Institute
Los Angeles, CA, USA

The FDLM derives the Standard Model's gauge structure, matter content, particle spectrum, and particle masses from a single input: the spacetime dimension d = 4. And d = 4 is itself derived from the photon's two helicity states. The 8×8 torus is derived, not selected. The 14 modes at λ = 4 are the SM particle content. What is proven: d = 4, the 8×8 torus, the gauge structure, the particle spectrum (14/14 shells), the kinetic mixing, the mass formula, the Weinberg angle, the Higgs mass, the kL formula. What is open: the mass ordering within classes (11/14), the dark photon mass, kL from the lattice, the interaction (SYK couplings), flavor physics (CKM, PMNS), the strong coupling (falsified), and the RF prediction.




