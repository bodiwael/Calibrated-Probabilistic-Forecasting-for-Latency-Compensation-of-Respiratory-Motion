# Paper

* **Source:** `main.tex`, IEEEtran conference format, double-blind (anonymous authors)
* **Class:** `IEEEtran.cls` (provided by TeX Live / MiKTeX, or from CTAN)

## Build

```bash
cd paper
pdflatex main
pdflatex main
```

The bibliography is an inline `thebibliography` block, so BibTeX is not needed. Run `pdflatex` twice to resolve references.

## Figures

`main.tex` loads figures through a `\figph{name}{width}{height}` macro. It uses `figures/<name>.pdf` (or `.png`) if present and otherwise draws a labelled **PLACEHOLDER** box, so the paper compiles before the figures exist. Put these files in `paper/figures/`:

| File name | Source |
|---|---|
| `fig07_calibration_coverage` | Calibration reliability |
| `fig05_forecasts_uncertainty` | Example forecasts with intervals |
| `fig10_11_error_failure_vs_latency` | RMSE and failure rate versus delay (Fantasia in the paper) |
| `fig12_roc_failure` | ROC curves for failure warning |
| `fig14_distribution_shift` | Young-to-elderly shift |
| `fig_sim_validation_sinusoid` | Simulator validation |

The pipeline diagram is drawn in TikZ, so it needs no file.

> **Check `fig12_roc_failure`:** this name is not among the `savefig` calls found in the three notebooks, so confirm how it is generated.

## Open items in the source

Search `main.tex` for `TODO` and `AUDIT` comments before submission. Per-table sources are listed in [`../results/README.md`](../results/README.md).

## Page limit

If the paper exceeds the page limit, the usual savings are: merge or drop the distribution-shift, ROC and simulator-validation figures (their numbers are already in the text), shorten the two long Results paragraphs (uncertainty-aware blending, failure anticipation), and compress the limitations list.
