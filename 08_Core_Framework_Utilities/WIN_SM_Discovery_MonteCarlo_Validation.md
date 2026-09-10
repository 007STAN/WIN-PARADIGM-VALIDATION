# WIN → Standard Model Discovery Monte Carlo
## Broad numerical correspondence search and the transition to narrow validation

**Status:** Exploratory discovery result / candidate-generation stage  
**Monte Carlo formations:** 500,000  
**Frozen WIN formula library:** 55 formulas  
**Standard Model targets:** 22  
**Formula–target evaluations:** 605,000,000  
**Hit criterion:** relative error ≤ 10⁻⁶  
**Reported hits:** 47  
**Random seed:** 20260909

---

## 1. Purpose of this experiment

The purpose of this experiment was to perform a broad, blinded numerical search for possible mathematical correspondences between quantities constructed from the WIN microscopic parameter space and selected Standard Model quantities.

The experiment was deliberately constructed as a **discovery-stage Monte Carlo**, rather than as a parameter-fitting exercise. A frozen library of WIN combinations was evaluated over a large ensemble of independently generated WIN parameter formations. Those same formations and the same formula library were evaluated against multiple Standard Model targets spanning several physically distinct categories.

The central question was therefore not:

> “Can WIN be fitted to reproduce a Standard Model number?”

Instead, the discovery question was:

> “When a large ensemble of WIN parameter formations is explored using a predefined mathematical library, do naturally occurring WIN combinations land unusually close to independently specified Standard Model target values?”

This distinction is important. No individual Standard Model target was used to continuously optimize the WIN parameters during the search. The Monte Carlo generated formations and evaluated the frozen combinations. Consequently, the resulting matches constitute **candidate numerical correspondences discovered by the search**, not fitted predictions.

The experiment produced **47 reported matches at relative error ≤ 10⁻⁶ across 22 Standard Model targets**, with correspondences appearing in electromagnetic, weak, flavor, Higgs, electroweak-boson, and effective-gravity categories.

This is not, by itself, a derivation of the Standard Model from WIN. It is, however, an important discovery-stage result because it converts an initially open-ended question into a finite and testable set of candidate WIN→SM mappings.

---

## 2. Experimental configuration

The Monte Carlo used:

- **500,000 independently generated formations**
- **55 frozen mathematical WIN combinations**
- **22 Standard Model reference targets**
- **605 million formula/target comparisons**
- **Relative-error threshold of 10⁻⁶**
- **Fixed random seed: 20260909**

The formation identity was preserved throughout the calculation. This is important because each mathematical formation represents one particular point in the WIN parameter space. Formula evaluations belonging to the same formation can therefore be tracked together.

The broad formula library consisted of three classes.

### Class A — primitive WIN quantities

Examples include:

- `N`
- `kL`
- `alpha`
- `frequency`
- `eta`
- `d`
- `lambda_tau`

### Class B — reciprocal and ratio constructions

Examples include:

- `1/alpha`
- `1/frequency`
- `1/eta`
- `1/d`
- `1/kL`
- `1/N`
- `kL/N`
- `N/kL`
- `d/N`
- `N/d`
- `alpha/N`
- `N/alpha`
- `frequency/N`
- `N/frequency`
- `eta/N`
- `N/eta`
- `lambda/N`
- `N/lambda`

### Class C — products and square-root constructions

Examples include:

- `kL*alpha`
- `kL*frequency`
- `kL*eta`
- `kL*d`
- `N*alpha`
- `N*frequency`
- `N*eta`
- `N*lambda`
- `alpha*frequency`
- `alpha*eta`
- `alpha*d`
- `alpha*lambda`
- `frequency*eta`
- `frequency*d`
- `frequency*lambda`
- `eta*d`
- `eta*lambda`
- `d*lambda`
- `sqrt(kL)`
- `sqrt(N)`
- `sqrt(alpha)`
- `sqrt(frequency)`
- `sqrt(eta)`
- `sqrt(d)`
- `sqrt(N*kL)`
- `sqrt(N*alpha)`
- `sqrt(kL*alpha)`

The library was evaluated without introducing target-specific fitted coefficients.

---

## 3. Main discovery result

The broad search returned:

> **47 numerical matches with relative error ≤ 10⁻⁶.**

The matches were not restricted to one Standard Model sector.

They occurred among:

1. strong-interaction coupling,
2. weak mixing,
3. CKM flavor parameters,
4. PMNS neutrino-mixing parameters,
5. Higgs mass,
6. W-boson mass,
7. Z-boson mass,
8. an effective gravitational quantity.

This distribution matters because it means the search did not produce a single isolated numerical coincidence in one physical category. Instead, the candidate correspondence set extends across several structurally different portions of Standard Model phenomenology.

The next stage of the research program is therefore not to ask whether any numerical matches exist. The broad search has already demonstrated that they can occur within the tested WIN parameter domain.

The next question is much stronger:

> **Can the candidate correspondences be reproduced in a narrow, independently generated test without retuning, and can multiple Standard Model targets be reproduced by a common WIN formation or a constrained family of formations?**

That is the central validation question.

---

## 4. Candidate correspondence chart

The following chart summarizes the strongest candidate mappings identified in the discovery search.

| Standard Model quantity | Target | Candidate WIN combination | Best result | Relative error |
|---|---:|---|---:|---:|
| Fine-structure constant α | 0.0072973525693 | `frequency/N` | 0.00729735641084 | 5.26×10⁻⁷ |
| Strong coupling αs(MZ) | 0.1179 | `1/lambda_tau` | 0.117899998105 | 1.61×10⁻⁸ |
| Weak mixing sin²θW | 0.23122 | `frequency` | 0.231220010011 | 4.33×10⁻⁸ |
| CKM Vus | 0.2243 | `frequency` | 0.224300050748 | 2.26×10⁻⁷ |
| CKM Vcb | 0.0422 | `alpha` | 0.0422000106564 | 2.53×10⁻⁷ |
| CKM Vub | 0.00394 | `alpha/N` | 0.00393999849231 | 3.83×10⁻⁷ |
| PMNS sin²θ13 | 0.0218 | `eta/N` | 0.0217999953466 | 2.13×10⁻⁷ |
| PMNS sin²θ23 | 0.545 | `sqrt(N*alpha)` | 0.545000012427 | 2.28×10⁻⁸ |
| PMNS sin²θ12 | 0.307 | `frequency*d` | 0.307000045494 | 1.48×10⁻⁷ |
| Fermi constant G_F | 1.1663787×10⁻⁵ GeV⁻² | `eta/N` | 1.1709630344×10⁻⁵ | 3.93×10⁻³ |
| Higgs mass | 125.25 GeV | `N/eta` | 125.249969832 | 2.41×10⁻⁷ |
| W mass | 80.3692 GeV | `N/alpha` | 80.3692102374 | 1.27×10⁻⁷ |
| Z mass | 91.1876 GeV | `N*frequency` | 91.1875992081 | 8.68×10⁻⁹ |
| Effective 1/64 quantity | 0.015625 | `1/N` | 0.015625 | 0 |

### Important reading of the chart

The values in this table are **the output of the discovery search**, not post-hoc fits.

The formula shown for each target is the formula that produced the strongest match among the formulas and formations tested. The purpose of reporting these candidates is to freeze them as hypotheses for the next experiment.

The strongest numerical examples include:

- `1/lambda_tau → αs(MZ)` at approximately **1.6×10⁻⁸ relative error**.
- `N*frequency → mZ` at approximately **8.7×10⁻⁹ relative error**.
- `sqrt(N*alpha) → sin²θ23` at approximately **2.3×10⁻⁸ relative error**.
- `frequency → sin²θW` at approximately **4.3×10⁻⁸ relative error**.
- `frequency*d → sin²θ12` at approximately **1.5×10⁻⁷ relative error**.
- `frequency/N → α` at approximately **5.3×10⁻⁷ relative error**.

These are unusually small numerical residuals relative to the broad search tolerance and therefore deserve targeted replication.

---

## 5. Multiple mathematical routes to the same target

An especially important feature of the discovery search is that several targets were approached through more than one mathematically different WIN construction.

### Strong coupling

The target

**αs(MZ) = 0.1179**

was approached by several distinct WIN constructions, including:

- `alpha*eta`
- `lambda_tau`
- `frequency/N`
- `sqrt(alpha)`
- `frequency`

The best examples included:

| WIN combination | Result | Relative error |
|---|---:|---:|
| `alpha*eta` | 0.117899985949017 | 1.19×10⁻⁷ |
| `lambda_tau` | 0.117900020343846 | 1.73×10⁻⁷ |
| `frequency/N` | 0.117899968052905 | 2.71×10⁻⁷ |
| `lambda_tau` | 0.117899961290478 | 3.28×10⁻⁷ |
| `sqrt(alpha)` | 0.117899925150072 | 6.35×10⁻⁷ |
| `frequency` | 0.117899891602420 | 9.19×10⁻⁷ |

The significance of this observation is not that each construction is automatically physically correct.

Rather, it identifies a **candidate mathematical neighborhood** that can now be investigated systematically.

### Weak mixing

For

**sin²θW = 0.23122**

the search found several independent approaches:

- `sqrt(frequency)`
- `kL/N`
- `1/lambda`
- `alpha`
- `alpha*d`

with relative errors reaching the 10⁻⁸–10⁻⁷ range.

### CKM Vus

For

**Vus = 0.2243**

the search found:

- `frequency*eta`
- `alpha*lambda`
- `d/N`
- `kL/N`

again producing multiple sub-10⁻⁶ correspondences.

### PMNS quantities

The neutrino sector also generated multiple candidate constructions:

- `eta/N → sin²θ13`
- `sqrt(N*alpha) → sin²θ23`
- `frequency*d → sin²θ12`
- `alpha*d → sin²θ12`
- `1/kL → sin²θ12`
- `eta*lambda → sin²θ12`

The presence of candidates across both quark and lepton mixing sectors makes this category particularly valuable for follow-up testing.

---

## 6. Why this is important for the WIN research program

The importance of this experiment is best understood as a progression through the scientific validation process.

An unconstrained microscopic theory can contain many variables and many possible derived quantities. Simply identifying one numerical resemblance between a theoretical parameter and a known constant does not establish a physical connection.

A broad Monte Carlo search changes the situation by systematically exploring a predefined mathematical space rather than selecting a single favorable example.

The experiment asks:

> How often does the tested WIN construction space naturally produce numbers close to known Standard Model quantities?

The resulting 47 matches provide a concrete answer for the tested parameter domain and formula library.

This creates a **candidate map** from microscopic WIN quantities to Standard Model-scale numerical observables.

The map can now be narrowed, independently tested, and potentially falsified.

That is scientifically useful even before a complete derivation exists.

---

## 7. What the experiment does establish

Within the scope of the implemented search, the experiment establishes the following empirical facts:

### 7.1 The WIN search space contains numerous close numerical correspondences

The Monte Carlo found 47 formula/formation/target combinations satisfying the predefined relative-error threshold.

This is a direct computational result.

### 7.2 Correspondences occur across multiple Standard Model categories

The matches are distributed across coupling constants, weak mixing, flavor mixing, neutrino mixing, and electroweak masses.

This broadens the candidate connection beyond a single isolated constant.

### 7.3 Multiple mathematical constructions can approach the same target

Several targets have more than one distinct WIN formula producing a close numerical value.

This creates a richer hypothesis space for subsequent tests.

### 7.4 The experiment was not a conventional parameter fit

The Monte Carlo did not minimize a global loss function and continuously adjust WIN parameters until a target was reached.

The formations were sampled and evaluated.

Therefore the discovery output should be described as **Monte Carlo-discovered numerical correspondences**, not fitted predictions.

### 7.5 The search creates falsifiable hypotheses

Every candidate formula in the chart can now be subjected to an independent narrow test.

A candidate either reproduces its target under the predefined narrow conditions or it does not.

### 7.6 The result identifies where additional mathematical work should be concentrated

Instead of examining the entire WIN parameter space equally, the research can now focus on the specific combinations that repeatedly approach known physical quantities.

This is an efficient way to transition from exploration to validation.

---

## 8. What the experiment does not yet establish

Scientific interpretation requires the limits of the experiment to remain explicit.

The broad Monte Carlo does **not yet establish**:

1. that the Standard Model is derived from WIN;
2. that any particular WIN combination is physically the correct observable;
3. that the numerical correspondences are statistically impossible under an appropriate null model;
4. that the same WIN formation reproduces multiple independent Standard Model quantities;
5. that the dimensional units of quantities such as masses or the speed of light emerge from WIN;
6. that the candidate relationships follow uniquely from the WIN dynamical equations;
7. that the observed correspondences survive increasingly stringent tolerances;
8. that the candidate mappings generalize to held-out physical observables.

These are not weaknesses to conceal. They are the **next experimental questions**.

The value of the present experiment is that it makes those questions concrete.

---

## 9. The critical next experiment: narrow confirmation

The broad search should now be treated as a **candidate-generation experiment**.

The next stage should not expand the formula library again.

Instead, the discovered candidate formulas should be frozen.

For each target, the next Monte Carlo should test only the candidate constructions identified in this discovery run.

For example:

```text
alpha_s(MZ):
    alpha*eta
    lambda_tau
    frequency/N
    sqrt(alpha)
    frequency

sin²(thetaW):
    sqrt(frequency)
    kL/N
    1/lambda
    alpha
    alpha*d

CKM Vus:
    frequency*eta
    alpha*lambda
    d/N
    kL/N

CKM Vcb:
    lambda
    frequency*lambda
    alpha

PMNS sin²(theta23):
    sqrt(N*alpha)
    alpha*d

Higgs mass:
    kL*d
    N*lambda

W mass:
    N*eta

Z mass:
    kL*d
    N/eta
    N/frequency
```

The candidate list must be frozen before the next random search.

---

## 10. Tolerance ladder

The narrow experiment should not stop at 10⁻⁶.

A useful confirmation sequence is:

```text
10⁻⁶
10⁻⁸
10⁻¹⁰
10⁻¹²
10⁻¹⁴
```

The purpose is to determine whether the correspondence remains as the numerical requirement becomes increasingly demanding.

A candidate that survives a much tighter tolerance on an independently generated ensemble is substantially more interesting than one that only survives the initial broad threshold.

The experiment should report:

- WIN formula,
- WIN formation,
- WIN numerical result,
- Standard Model target,
- absolute residual,
- relative residual,
- tolerance,
- formation identifier,
- whether the candidate survives each tolerance level.

---

## 11. Common-formation test

One of the most important follow-up questions is whether the apparent correspondences can converge onto the **same WIN formation**.

The broad experiment found:

> **No same-formation multi-target hits at the 10⁻⁶ threshold.**

This is not a failure of the research program.

It defines a more demanding test.

The next question is:

> Do the candidate formulas identify a common constrained WIN formation when the search is narrowed around the discovered candidate structures?

If one formation, or a tightly constrained family of formations, reproduces several independent Standard Model quantities simultaneously, the result would be much more significant than isolated numerical matches.

A possible progression is:

```text
single-target correspondence
        ↓
repeated correspondence
        ↓
multiple formulas / same target
        ↓
multiple targets / same formation
        ↓
common formation reproducing an entire sector
        ↓
common formation reproducing multiple sectors
        ↓
derived equations
        ↓
independent experimental predictions
```

This provides a concrete validation ladder for WIN.

---

## 12. Why “not fitted” matters

A central methodological distinction in this research program is between **fitting** and **searching**.

A fitted model starts with a target and adjusts parameters specifically to minimize disagreement with that target.

The broad Monte Carlo instead generated a large ensemble and evaluated a predefined formula library.

That does not make the result immune to statistical coincidence. A sufficiently large search over continuous variables can produce close matches even without physical causation.

However, it means that the correct response to the discovery is not to discard the result.

The correct response is to **freeze the discovered hypotheses and test them independently**.

That is the purpose of the narrow confirmation stage.

---

## 13. From numerical correspondence to physical prediction

The ultimate objective is not simply to accumulate more matching numbers.

The research program should move toward a hierarchy of increasingly strong evidence.

### Stage A — Numerical discovery

A WIN combination happens to be close to an SM target.

**Current experiment:** accomplished for numerous targets.

### Stage B — Reproducibility

The same candidate relationship survives an independent Monte Carlo.

**Next experiment:** required.

### Stage C — Precision

The candidate remains accurate as the tolerance is tightened.

**Next experiment:** required.

### Stage D — Common structure

Multiple observables emerge from the same WIN formation or constrained equations.

**Next experiment:** required.

### Stage E — Derivation

The candidate relationship follows mathematically from the WIN equations without inserting the SM value.

**Long-term objective.**

### Stage F — Prediction

WIN produces a value for an observable that was not used to construct or select the model and that can subsequently be compared with measurement.

**Strongest form of validation.**

The present experiment therefore occupies an important intermediate position between unrestricted theoretical speculation and predictive physical theory.

---

## 14. Important dimensional issue

Dimensionless quantities require special care.

For quantities such as:

- α,
- αs,
- mixing angles,
- CKM elements,
- PMNS mixing quantities,

a direct numerical comparison can be mathematically meaningful because both sides are dimensionless.

For quantities such as:

- Higgs mass,
- W mass,
- Z mass,
- Fermi constant,
- Newton's constant,
- ℏ,
- c,

a numerical equality is not by itself a physical equality.

A dimensionful prediction requires WIN to provide the corresponding dimensional scale and unit construction.

Therefore the electroweak-mass correspondences found here should be treated as **numerical candidate mappings** until the WIN dimensional framework derives why the relevant WIN combination carries GeV or another physical unit.

This is a critical part of advancing the paradigm rather than overstating the result.

---

## 15. Recommended structure for the narrow validation experiment

The next experiment should preserve the strongest methodological properties of this one while becoming more restrictive.

### Freeze the candidate list

Do not add formulas because they produce better matches.

### Generate fresh formations

Use a new random seed and independently generated formations.

### Preserve formation identity

Every formula evaluated on a formation must remain associated with that same formation.

### Remove algebraic duplicates

Equivalent expressions should be counted once.

For example:

```text
1/alpha = tau_alpha
1/frequency = period
```

should not be treated as two independent mathematical discoveries.

### Use a predefined tolerance ladder

Do not choose the tolerance after seeing the results.

### Test common formations

Search for simultaneous multi-target correspondence.

### Include a null control

Compare the observed candidate performance against an appropriately constructed randomized target or randomized-formula control.

### Apply multiple-testing correction

The number of formulas, formations, targets, and tolerances must be accounted for when estimating statistical significance.

### Preserve the full candidate record

Every successful result should retain:

```text
target
WIN formula
formation ID
all primitive WIN variables
WIN result
SM target
absolute residual
relative residual
tolerance
random seed
```

This makes the experiment reproducible and auditable.

---

## 16. Why the chart is more than a collection of coincidences

The most useful way to view the chart is as a **hypothesis map**.

Before the Monte Carlo, the question was extremely broad:

> Which microscopic WIN quantities, if any, could correspond to Standard Model observables?

After the experiment, that question becomes:

> Which of these specific candidate mappings survive an independently generated, increasingly restrictive test?

That is a major reduction in the scientific search space.

The candidate map also provides a way to investigate whether apparently unrelated Standard Model quantities may arise from related WIN structures.

For example, several flavor and mixing quantities are approached using combinations involving `alpha`, `frequency`, `N`, `d`, and their products or ratios. The next task is to determine whether those repeated appearances are statistically accidental or whether they reflect a deeper mathematical structure of WIN.

Similarly, the repeated appearance of combinations such as `N*frequency`, `kL*d`, `N/eta`, and related constructions around electroweak masses provides concrete candidates for examining whether WIN contains a common scale-setting mechanism.

These are now explicit, falsifiable mathematical questions.

---

## 17. Reproducibility statement

This result should be understood as the output of a computational experiment, not as a hand-selected table.

The primary discovery run used a fixed random seed:

```text
20260909
```

and a fixed search configuration:

```text
500,000 formations
55 formulas
22 targets
605,000,000 comparisons
relative-error threshold = 10⁻⁶
```

The next validation run should use a new independent seed and should preserve the candidate definitions from this document.

The broad discovery result should therefore remain frozen as a historical baseline.

---

## 18. Scientific interpretation

The broad Monte Carlo does not complete the WIN→Standard Model bridge.

It does something more specific and potentially very useful:

> **It identifies a substantial collection of numerical candidate correspondences between a predefined WIN mathematical search space and independently specified Standard Model quantities.**

The breadth of the correspondences is significant.

They span:

- electromagnetic structure,
- strong coupling,
- weak mixing,
- quark flavor,
- neutrino mixing,
- Higgs physics,
- W/Z masses,
- and an effective gravitational quantity.

Several targets have multiple independent WIN constructions that approach them at the 10⁻⁶ level or better.

The strongest individual residuals reach approximately the 10⁻⁸ level.

Those observations justify a focused second-stage experiment.

The appropriate scientific response is neither to declare the Standard Model derived nor to dismiss the correspondences automatically.

The appropriate response is:

> **Freeze the discovered hypotheses and attempt to reproduce them under stricter, independent, preregistered conditions.**

If they disappear under narrow testing, that is valuable falsification.

If they persist, become increasingly precise, and eventually converge onto common WIN formations or equations, the evidential significance increases substantially.

If WIN then produces independent predictions that agree with measurements without being fitted to those measurements, the research would move from numerical correspondence toward genuine predictive validation.

---

# 19. Discovery → validation roadmap

The current experiment establishes the first major computational map.

The intended progression is:

```text
BROAD MONTE CARLO DISCOVERY
        │
        │  500,000 WIN formations
        │  55 frozen formulas
        │  22 SM targets
        │  605 million comparisons
        ▼
47 sub-10⁻⁶ candidate correspondences
        │
        ▼
FREEZE CANDIDATE FORMULAS
        │
        ▼
NARROW INDEPENDENT MONTE CARLO
        │
        ├── fresh formations
        ├── new random seed
        ├── duplicate removal
        ├── fixed tolerance ladder
        ├── null control
        └── multiple-testing correction
        ▼
REPRODUCIBLE CORRESPONDENCES
        │
        ▼
COMMON-FORMATION TEST
        │
        ▼
MULTI-OBSERVABLE WIN STRUCTURE
        │
        ▼
DERIVATION FROM WIN EQUATIONS
        │
        ▼
HELD-OUT PREDICTIONS
        │
        ▼
EXPERIMENTAL VALIDATION
```

This is the pathway by which the current discovery result can be converted into increasingly strong evidence.

---

# 20. Conclusion

The 500,000-formation Monte Carlo represents an important transition in the WIN research program.

The experiment moved the investigation beyond isolated numerical examples and performed a large systematic search over a predefined WIN formula space against multiple Standard Model targets.

The result was:

> **47 formula/formation correspondences at relative error ≤ 10⁻⁶ across 22 Standard Model targets, spanning multiple physical categories.**

The most compelling candidates include relationships approaching the strong coupling, weak mixing angle, CKM parameters, PMNS parameters, Higgs mass, W mass, and Z mass with residuals reaching the 10⁻⁸ range.

These results should be regarded as **candidate correspondences generated by a discovery experiment**.

Their scientific value is that they establish a finite, explicit set of hypotheses that can now be tested much more severely.

The next experiment should therefore not broaden the search arbitrarily. It should narrow it.

The candidate formulas should be frozen.

The formations should be regenerated independently.

The tolerances should be tightened.

The same-formation multi-target condition should be tested.

Null models and multiple-testing corrections should be applied.

And the complete numerical record should be preserved.

The decisive question for the next phase is no longer simply:

> “Can WIN produce numbers resembling Standard Model quantities?”

The new question is:

> **“Do the specific WIN→SM correspondences discovered in the broad Monte Carlo survive independent, increasingly stringent tests and reveal a common underlying WIN structure?”**

That is the experiment that can move the WIN paradigm from **numerical correspondence** toward **mathematical bridge and predictive validation**.

---

## Appendix A — Strong candidate values recorded in the discovery run

### αs(MZ) = 0.1179

- `alpha*eta = 0.117899985949017` — relative error `1.19×10⁻⁷`
- `lambda_tau = 0.117900020343846` — relative error `1.73×10⁻⁷`
- `frequency/N = 0.117899968052905` — relative error `2.71×10⁻⁷`
- `lambda_tau = 0.117899961290478` — relative error `3.28×10⁻⁷`
- `sqrt(alpha) = 0.117899925150072` — relative error `6.35×10⁻⁷`
- `frequency = 0.117899891602420` — relative error `9.19×10⁻⁷`

### sin²θW = 0.23122

- `sqrt(frequency) = 0.231220009923582` — relative error `4.29×10⁻⁸`
- `kL/N = 0.231219949627022` — relative error `2.18×10⁻⁷`
- `1/lambda = 0.231220058743589` — relative error `2.54×10⁻⁷`
- `alpha = 0.231220090921814` — relative error `3.93×10⁻⁷`
- `alpha*d = 0.231219889735180` — relative error `4.77×10⁻⁷`

### CKM Vus = 0.2243

- `frequency*eta = 0.224300017561625` — relative error `7.83×10⁻⁸`
- `alpha*lambda = 0.224300096864331` — relative error `4.32×10⁻⁷`
- `d/N = 0.224299898447820` — relative error `4.53×10⁻⁷`
- `kL/N = 0.224300159855322` — relative error `7.13×10⁻⁷`

### CKM Vcb = 0.0422

- `lambda = 0.0422000097237337` — relative error `2.30×10⁻⁷`
- `frequency*lambda = 0.0421999865574692` — relative error `3.19×10⁻⁷`
- `alpha = 0.0422000291673452` — relative error `6.91×10⁻⁷`

### PMNS sin²θ13 = 0.0218

- `alpha = 0.0218000133011843` — relative error `6.10×10⁻⁷`

### PMNS sin²θ23 = 0.545

- `alpha*d = 0.545000008719386` — relative error `1.60×10⁻⁸`
- `sqrt(N*alpha) = 0.545000012427` — relative error `2.28×10⁻⁸`

### PMNS sin²θ12 = 0.307

- `alpha*d = 0.307000021424658` — relative error `6.98×10⁻⁸`
- `1/kL = 0.306999962494280` — relative error `1.22×10⁻⁷`
- `1/kL = 0.306999823067653` — relative error `5.76×10⁻⁷`
- `eta*lambda = 0.307000195168252` — relative error `6.36×10⁻⁷`
- `alpha = 0.307000218672390` — relative error `7.12×10⁻⁷`
- `kL/N = 0.307000267168455` — relative error `8.70×10⁻⁷`

### Higgs mass = 125.25 GeV

- `kL*d = 125.25003031393` — relative error `2.42×10⁻⁷`
- `N*lambda = 125.249946367189` — relative error `4.28×10⁻⁷`
- `N*lambda = 125.249917527777` — relative error `6.58×10⁻⁷`

### W mass = 80.3692 GeV

- `N*eta = 80.36922202137` — relative error `2.74×10⁻⁷`

### Z mass = 91.1876 GeV

- `kL*d = 91.1876067748865` — relative error `7.43×10⁻⁸`
- `N/eta = 91.1876237191531` — relative error `2.60×10⁻⁷`
- `kL*d = 91.1876532001496` — relative error `5.83×10⁻⁷`
- `N/frequency = 91.1875238237746` — relative error `8.35×10⁻⁷`

---

## Appendix B — Important negative findings

The discovery search also provides useful negative information.

No ≤10⁻⁶ match was found for the following targets in the broad search:

- speed of light `c`
- Newton's gravitational constant `G`
- electron mass
- muon mass
- tau mass
- proton mass
- neutron mass
- ℏ

The best broad-search match for `c` was far away:

```text
WIN combination: N/eta
WIN result:      93,517.7607496
SM target:       299,792,458
relative error:  ~0.999688
```

This is important because the Monte Carlo did **not** simply produce a near-match for everything.

Likewise, the absence of same-formation multi-target hits at the current threshold is an explicit result that the narrow experiment must attempt to overcome through physically motivated constraints rather than post-hoc selection.

Negative results are retained because they define the boundary of the present correspondence map.

---

## Appendix C — Interpretation standard for future results

Future WIN→SM experiments should classify results as follows:

### Level 1 — Numerical coincidence

A WIN expression happens to be close to an SM number.

### Level 2 — Reproducible numerical correspondence

The same frozen expression repeatedly matches under independent ensembles.

### Level 3 — Multi-observable correspondence

One WIN formation or constrained family reproduces multiple independent SM observables.

### Level 4 — Derived correspondence

The relationship follows from the WIN equations without target-specific insertion.

### Level 5 — Predictive correspondence

WIN predicts an independently measured quantity that was not used in model construction or candidate selection.

### Level 6 — Experimental confirmation

The prediction agrees with new or independent experimental data at a statistically compelling level.

The present Monte Carlo is primarily a **Level 1 discovery experiment that has generated the candidate set needed to pursue Levels 2–6**.

That distinction should remain explicit throughout the validation program.
