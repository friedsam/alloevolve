"""Reproduce compact Phase-I summary statistics from public frozen CSVs."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "phase1"


def main() -> None:
    assignments = pd.read_csv(RESULTS / "specialist_uplift_assignments.csv")
    regimes = pd.read_csv(RESULTS / "apo_regime_overlay_counts.csv")

    print("=== Specialist/generalist development labels ===")
    if "category" in assignments.columns:
        counts = assignments["category"].value_counts(dropna=False)
        for label, count in counts.items():
            print(f"{label}: {int(count)}")
    else:
        print("No 'category' column found; inspect the assignment table directly.")

    print("\n=== Apo-regime overlay ===")
    wanted = [
        "regime",
        "GENERALIST",
        "UNIQUE_SPECIALIST",
        "SPECIALIST_TIE",
        "UNCOVERED",
        "specialist_or_tie_fraction_covered",
    ]
    existing = [column for column in wanted if column in regimes.columns]
    print(regimes.loc[:, existing].to_string(index=False))

    if "specialist_or_tie_fraction_covered" in regimes.columns:
        print("\nSpecialist benefit among covered proteins:")
        for _, row in regimes.iterrows():
            regime = row.get("regime", "?")
            fraction = float(row["specialist_or_tie_fraction_covered"])
            print(f"{regime}: {fraction:.1%}")


if __name__ == "__main__":
    main()
