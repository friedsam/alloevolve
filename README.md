# AlloEvolve

**AI-guided evolutionary discovery of resource-certified quantum mechanisms for allosteric-site prediction**

AlloEvolve is a research framework developed for the Cleveland Clinic track of the 2026 Global Quantum + AI Challenge. Rather than assuming that one quantum model should work across all proteins, the project searches a typed space of quantum-allostery algorithms, certifies candidate mechanisms before biological scoring, preserves both generalists and complementary specialists, and ultimately aims to learn when each expert should be applied to an unseen apo protein.

## Phase-I submission

**Submission date:** 2026-09-15  
**Phase-I snapshot:** `phase1-submission-2026-09-15`

This repository is the public evidence and reproducibility companion to the Phase-I concept proposal. The full research/development repository remains private during active development. The public companion was assembled immediately after proposal submission from the already-existing Phase-I artifacts; post-submission research is not retroactively treated as Phase-I evidence.

### Evidence currently available

- [Phase-I evidence index](docs/phase1_evidence_index.md)
- [Method snapshot](docs/phase1_method.md)
- [Validation contract](docs/validation_contract.md)
- [Hardware strategy](docs/hardware_strategy.md)
- [Exploratory result notes](results/phase1/README.md)
- [Specialist-uplift assignments](results/phase1/specialist_uplift_assignments.csv)
- [Apo-regime overlay counts](results/phase1/apo_regime_overlay_counts.csv)

## Core workflow

1. **Generate candidate algorithms**
   - typed candidate genomes spanning representation, interaction weighting, Hamiltonian/generator, perturbation, source state, observable, decoder, and operating parameters;
   - ordinary mutation/crossover plus LLM-guided semantic proposals.

2. **Certify before fitness**
   - reject structurally invalid combinations;
   - place unsupported but potentially interesting constructions in a research nursery;
   - invalidate inherited mathematical certificates after architecture-changing mutations;
   - identify the claimed quantum-specific term, matched resource-off/dephased limit, active parameter regime, resource envelope, and path to the required residue-level challenge outputs.

3. **Evaluate under a fixed external contract**
   - freeze predictions before biological labels are joined;
   - maintain separate verdicts for challenge viability, predictive utility, and quantum attribution;
   - compare each quantum candidate with matched resource-off controls and stronger classical analogues where relevant.

4. **Evolve a portfolio, not one winner**
   - preserve broad generalists;
   - preserve specialists that uniquely recover proteins or residues missed by the current portfolio;
   - retain control-adjusted gains, robustness, and behaviorally distinct mechanisms.

5. **Learn applicability**
   - characterize proteins using label-blind apo-derived traits;
   - test whether specialist benefit, generalist sufficiency, or persistent failure occupies reproducible regions of protein space;
   - route to a specialist or specialist combination only when prospective evidence supports it, otherwise fall back to the strongest generalist.

## Current exploratory status

The current development campaign contains **52 model/decoder variants across six mechanism families** evaluated on a **50-protein adaptive-development panel**.

Exploratory portfolio-level observations include:

- at least one current quantum candidate reaches **39/50** development proteins;
- the portfolio collectively recovers **270/659** annotated target residues somewhere in the current candidate set;
- specialist/generalist behavior is heterogeneous across proteins;
- preliminary label-blind apo-trait analysis suggests structured differences in specialist benefit and persistent failure, but the present `n=50` analysis is exploratory rather than confirmatory.

These figures describe **development headroom**, not deployable performance. The 50-protein panel has been adaptively inspected and is treated as training/development data.

## Validation principles

AlloEvolve keeps three verdicts separate:

- **Challenge viability** — can the candidate produce the required outputs, including an `N x N` residue-connectivity matrix and exact ranked top-5 residue predictions?
- **Predictive utility** — do known distal regulatory residues score above appropriate random/background and non-functional-pocket controls?
- **Quantum attribution** — is useful behavior specifically attributable to the claimed quantum mechanism rather than to a shared representation or matched classical/resource-off model?

A positive matched-control residual alone is not considered proof of quantum attribution.

Phase II is intended to expand beyond the current 50-protein development panel, reserve a sequence/family-separated external validation panel, and perform candidate-specific hardware/resource qualification only after the evolutionary search narrows to a frozen Pareto set.

## Hardware strategy

Hardware execution is a promotion stage, not a prerequisite for exploratory search.

Promoted candidates will proceed through:

1. candidate-specific resource certification;
2. backend-aware circuit synthesis and resource accounting;
3. finite-shot/noisy qualification of residue-rank and top-5 stability;
4. selected QPU execution for finalists that survive the earlier gates.

QPU execution tests hardware feasibility and noise survival; it does not replace the mathematical and matched-control requirements for quantum attribution.

## Public repository scope

Planned public artifacts include:

- Phase-I architecture and result figures;
- frozen result-summary tables/CSVs;
- validation and quantum-attribution contracts;
- selected evaluation and figure-reproduction code;
- environment/configuration information;
- later scaling, compilation, noise, and hardware studies.

The full active research engine and experimental candidate implementations are not part of this public companion repository at Phase I.

## Status

**Phase I:** submitted 2026-09-15  
**Current development:** active

Post-submission commits may contain continued research and are not retroactively part of the Phase-I evidence package. The `phase1-submission-2026-09-15` snapshot identifies the submitted state.
