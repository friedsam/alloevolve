# Reproducibility helpers

This directory contains small public scripts that operate only on the frozen Phase-I evidence tables in `results/phase1/`.

The full active evolutionary search engine remains private during ongoing research. These helpers are intended to make the public claims auditable without implying that the complete research stack has been released.

## Quick start

```bash
python -m pip install -r reproducibility/requirements.txt
python reproducibility/summarize_phase1.py
```

The script reports:

- specialist/generalist/tie/uncovered counts;
- apo-regime outcome counts;
- specialist-benefit fractions among covered proteins.

All outputs are exploratory development-panel diagnostics, not prospective validation.
