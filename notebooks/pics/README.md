# PICS notebook: preterm infants

**File:** `pics_pipeline.ipynb`  **Dataset:** [PICS (Preterm Infant Cardio-Respiratory Signals), PhysioNet](https://physionet.org/content/picsdb/1.0.0/)  **Data guide:** [`../../data/pics/README.md`](../../data/pics/README.md)

## What this notebook does

Runs the full study pipeline on respiration recordings from preterm infants: preprocessing, forecasting, calibration, simulated closed-loop tracking, failure anticipation, statistics, ablations and export of the paper tables and figures.

## Protocol

| Item | Setting |
|---|---|
| Subjects | 9 infants after quality exclusion (1 infant excluded, valid fraction < 0.7) |
| Subject id | Parsed from record names (`slp<NN>[a-z]`); several records of one infant share the id |
| Folds | **Leave-one-infant-out**: test = infant *k*, validation = infant *k+1*, train = all others |
| Signal | Abdominal inductance bands at 50 Hz (infant 1 from the bedside monitor at 500 Hz) |
| Band-pass | `BAND = (0.1, 3.0)` Hz; alternatives for the band study: (0.1, 2.0), (0.2, 3.0), (0.1, 5.0) |
| Reads | Chunked streaming reads of a segment per record, never the whole file at once |
| Mode | `MODE = "full"`, `SEED = 42` |

## Key configuration cell

```python
MODE = "full"                       # "smoke" | "fast" | "full"
SEED = 42
RESULTS_BASE = f"{_BASE}/results/picsdb"
DATA_DIR = f"{_BASE}/data/picsdb"
RUN_RECURSIVE_WGET = False          # True = full recursive wget of the database (large, slow)
DL_WORKERS = 16                     # parallel download threads (selective downloader)
RESUME_RUN = None                   # resume an earlier timestamped run
USE_CACHE = True                    # reuse per-fold trained models
```

## Data download

The notebook downloads the needed WFDB records itself with a parallel selective downloader (default) or a full recursive `wget` of `https://physionet.org/files/picsdb/1.0.0/` (`RUN_RECURSIVE_WGET = True`). An internet connection is required.

## Results (300 ms, test infants, n = 9)

| Model | MAE (normalised) | 95% coverage |
|---|---|---|
| Persistence | 0.801 | n/a |
| Ridge | 1.037 | n/a |
| Kalman | 0.998 | n/a |
| LSTM (prob.) | 0.516 | 87.1% |
| TCN (det.) | 0.438 | n/a |
| TCN (prob.) | 0.436 | 95.3% |
| Ensemble (M = 5) | 0.501 | 89.1% |
| Ensemble + conformal | n/a | 93.9% |

Ridge and Kalman are **worse than persistence** in PICS (1.04 and 1.00 vs 0.80).

Simulated tracking RMSE (mm), subject mean:

| Delay | Reactive | Predictive | UA | Kalman |
|---|---|---|---|---|
| 100 ms | 4.428 | 3.395 | 3.606 | 5.014 |
| 300 ms | 5.531 | 4.343 | 4.459 | 5.981 |
| 500 ms | 5.774 | 4.434 | 4.562 | 6.438 |

Predictive control reduces RMSE by **21.5%** at 300 ms and **23%** at 500 ms. The Kalman controller is **worse than reactive control** at every delay.

## Outputs

Tables (CSV): `forecast_metrics`, `uncertainty_metrics`, `tracking_metrics`, `tracking_summary_by_controller_delay`, `failure_prediction_metrics`, `failure_threshold_sensitivity`, `statistical_tests`, `distribution_shift_performance`, `distribution_shift_tests`, `ablation_results`, `band_validation`, `dataset_characteristics`, `record_quality`, `split_manifest`.

Figures: `fig01_pipeline`, `fig02_dataset_statistics`, `fig03_raw_vs_filtered`, `fig04_eda_power_spectra`, `fig05_forecasts_uncertainty`, `fig06_error_vs_horizon`, `fig07_calibration_coverage`, `fig08_uncertainty_vs_error`, `fig09_tracking_trajectories`, `fig10_11_error_failure_vs_latency`, `fig14_distribution_shift`, `fig15_ablation`, `fig_sim_validation_sinusoid`, `fig_target_motion`.

## Known limitations of this run

* **This run predates later pipeline changes.** It has no UCPC or triggered-mode controllers, no plant (actuator-lag) or measurement-noise sensitivities, and no validation-only model-selection table. These exist in the BIDMC and Fantasia notebooks.
* With n = 9 test infants, Holm-corrected tests cannot reach significance. Non-significance is not equivalence.
* Raw Gaussian intervals under-cover (ensemble 89.1%, LSTM 87.1%); conformal calibration brings the ensemble to 93.9%, still about one point short of nominal.
