#!/usr/bin/env python3
"""Copy tables (CSV) and figures (PDF/PNG) from a notebook run folder into results/<cohort>/.

Usage:
    python scripts/collect_results.py --run-dir /path/to/results/bidmc/full_20260101_120000 --cohort bidmc

The script searches the run folder recursively, so it does not depend on the exact
sub-folder layout. Existing files in the destination are kept unless --overwrite is given.
"""
import argparse
import shutil
from pathlib import Path

FIG_EXT = {".pdf", ".png", ".svg"}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run-dir", required=True, type=Path, help="timestamped run folder created by a notebook")
    ap.add_argument("--cohort", required=True, choices=["pics", "bidmc", "fantasia"])
    ap.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--overwrite", action="store_true", help="replace files that already exist")
    a = ap.parse_args()

    if not a.run_dir.is_dir():
        raise SystemExit(f"run folder not found: {a.run_dir}")

    dest = a.repo_root / "results" / a.cohort
    (dest / "tables").mkdir(parents=True, exist_ok=True)
    (dest / "figures").mkdir(parents=True, exist_ok=True)

    n_tab = n_fig = n_skip = 0
    for f in sorted(a.run_dir.rglob("*")):
        if not f.is_file():
            continue
        if f.suffix.lower() == ".csv":
            out = dest / "tables" / f.name
            kind = "tab"
        elif f.suffix.lower() in FIG_EXT and f.stem.startswith("fig"):
            out = dest / "figures" / f.name
            kind = "fig"
        else:
            continue
        if out.exists() and not a.overwrite:
            n_skip += 1
            continue
        shutil.copy2(f, out)
        n_tab += kind == "tab"
        n_fig += kind == "fig"

    print(f"copied {n_tab} tables and {n_fig} figures to {dest}  (skipped {n_skip} existing)")


if __name__ == "__main__":
    main()
