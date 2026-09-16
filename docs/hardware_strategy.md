# Hardware strategy

Hardware execution is a promotion stage, not a prerequisite for broad exploratory search.

## Stage 1 — resource certificate

For each promoted architecture:

- define encoding and logical width;
- identify Hamiltonian/observable structure;
- estimate measurement settings and scaling;
- preserve a frozen residue-level decoder.

Candidates with pathological resource growth or no credible circuit path are not QPU priorities.

## Stage 2 — backend-aware synthesis

For a small frozen Pareto set:

- synthesize against candidate backends;
- record physical qubits;
- record depth and two-qubit gates;
- quantify routing/SWAP overhead;
- quantify measurement/shot burden.

Backend choice follows measured fit rather than vendor preference.

## Stage 3 — noisy qualification

Compare ideal and finite-shot/noisy execution using:

- residue-rank correlation;
- exact top-5 stability;
- candidate-versus-matched-control residual.

Loss of actionable residue ranking or of the claimed quantum-specific behavior blocks hardware promotion.

## Stage 4 — selected QPU execution

Only representative finalists proceed to hardware.

QPU execution tests hardware feasibility and noise survival. It does not establish quantum attribution by itself.
