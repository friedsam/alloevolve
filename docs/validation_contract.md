# Validation contract

The challenge specification remains authoritative. Diagnostics never replace required residue-level outputs.

## 1. Challenge viability

A promoted finalist must produce:

- an `N x N` residue-connectivity matrix;
- residue-level scores/ranking provenance;
- an exact ranked top-5 list of residue indices on the mandatory Cleveland targets.

## 2. Predictive utility

Primary evidence is whether known distal regulatory residues score above both:

- random/background residues;
- non-functional surface pockets.

The exact residue predictions are reported before aggregate diagnostics.

## 3. Quantum attribution

Quantum attribution is tested independently of predictive utility.

Evidence chain:

1. **Mathematical certificate** — identify the claimed quantum-specific term and the exact commuting/dephased/resource-off limit.
2. **Matched control** — preserve the representation/decoder where possible while removing the claimed quantum resource.
3. **Strong classical analogue** — test a stronger classical realization when scientifically relevant.
4. **Identity checks** — if an exact classical realization exists, the quantum-attribution claim fails even if predictive utility is good.

A `Q_ONLY` hit means that a candidate's quantum arm recovered an exact target residue missed by that candidate's matched control. It is not a claim of quantum advantage.

## Data regimes

- The current 50-protein panel is adaptive-development data.
- Phase II is intended to expand the nonredundant development panel.
- A sequence/family-separated external panel will be reserved for prospective validation.
- Mandatory Cleveland targets remain the application-specific challenge test.
