# Notebooks

One self-contained notebook per cohort. The three notebooks share the **same pipeline** (Sections B–S) and differ only in the *dataset hooks* (data loading, subject identification, cohort labels, fold construction) and a few configuration values.

| Notebook | Cohort | Folder |
|---|---|---|
| `pics_pipeline.ipynb` | Preterm infants (PICS) | [`pics/`](pics/README.md) |
| `bidmc_pipeline.ipynb` | ICU patients (BIDMC) | [`bidmc/`](bidmc/README.md) |
| `fantasia_pipeline.ipynb` | Healthy young and elderly adults (Fantasia) | [`fantasia/`](fantasia/README.md) |

## Shared notebook sections

| Section | Content |
|---|---|
| Run configuration | `MODE`, `SEED`, paths, preprocessing, model and controller settings |
| B | Environment setup and helpers |
| Dataset hooks | Record naming, cohort labels, subset selection, fold construction |
| C | Dataset access (download, Kaggle input or CSV conversion) |
| D | Exploratory data analysis (descriptive only) |
| E | Causal preprocessing and unit tests (no window leakage, training-only normalisation, invalid-segment exclusion) |
| F | Subject-level splits and causal windows |
| G | Forecasting models: persistence, ridge, Kalman, probabilistic LSTM, probabilistic and deterministic TCN, deep ensemble |
| H | Uncertainty estimation and calibration (Gaussian and split conformal intervals) |
| I | Distribution-shift experiment |
| J | Synthetic target motion |
| K | One-degree-of-freedom simulated robot |
| L | Controllers |
| M | Tracking metrics and plots |
| N | Tracking-failure prediction |
| O | Statistical analysis (bootstrap CIs, paired tests, Holm correction) |
| P | Ablation and sensitivity studies (one factor at a time) |
| Q | Publication figures and tables |
| R | Reproducibility and artifact export |
| S | Automatic final report |

Differences between notebooks:

* The BIDMC notebook adds **Section G2** (validation-only model selection, saved predictions and reproducibility tests).
* The Fantasia notebook has the richest set of extra tables (inference latency, actuator-lag sensitivity, measurement-noise sensitivity, validation selection logs).
* The PICS run is the oldest and **lacks several later additions**; see its README.

## Common configuration

| Setting | Value |
|---|---|
| Seed | `SEED = 42` |
| Model sampling rate | `FS_MODEL = 20` Hz |
| Filter | 4th-order Butterworth, one direction (causal) |
| History | `HIST = 100` samples (5 s) |
| Horizons | `HORIZONS_STEPS = [2, 4, 6, 8, 10]` (100–500 ms) |
| Gap handling | `MAX_GAP_S = 0.25`, `FLAT_S = 2.0`, `WARMUP_S = 10.0` |
| Quality rule | `MIN_VALID_FRAC = 0.7` |
| Sigma floor | `SIGMA_MIN = 1e-3` |

## Output layout of a run

Each run creates a **new timestamped folder** under `RESULTS_BASE` (for example `full_20260101_120000`) containing CSV tables, figures and the final report. Use `RESUME_RUN` to continue an interrupted run and `USE_CACHE` to reuse per-fold trained models. Use [`../scripts/collect_results.py`](../scripts/collect_results.py) to copy outputs into [`../results/`](../results/README.md).

## Practical notes

* Notebooks were executed on Kaggle (Python 3.13). A GPU speeds up training but is not required for a smoke test.
* Set `MODE = "smoke"` first to confirm that paths and dependencies work.
* Do not commit raw data. See [`../data/`](../data/README.md).
