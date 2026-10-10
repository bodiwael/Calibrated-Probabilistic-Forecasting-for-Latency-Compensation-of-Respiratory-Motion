# Fantasia notebook: healthy young and elderly adults

**File:** `fantasia_pipeline.ipynb`  **Dataset:** [Fantasia Database, PhysioNet](https://physionet.org/content/fantasia/1.0.0/), read from a third-party Kaggle CSV conversion  **Data guide:** [`../../data/fantasia/README.md`](../../data/fantasia/README.md)

## What this notebook does

Runs the full study pipeline on healthy adults and additionally carries the **young-to-elderly distribution-shift experiment** and the richest set of audit and sensitivity outputs (inference latency, actuator lag, measurement noise, exclusion of sampling-rate anomalies, validation selection logs).

## Protocol

| Item | Setting |
|---|---|
| Subjects | 40 participants (20 young, 20 elderly); one record (`f2y02`) has a different sampling rate (333 Hz) and is retained |
| Cohort labels | Encoded in the record name (`f1y##`, `f1o##`, `f2y##`, `f2o##`), cross-checked against header ages |
| Split | **Single split**: train on young subjects, validate on held-out young subjects, test on 4 young **and all 20 elderly** subjects (24 test subjects). The paper reports 12 young for training and 4 young for testing; the remaining 4 young subjects are presumably the validation block (inferred: 20 young = 12 + 4 + 4; confirm in `split_manifest.csv`) |
| Validation separation | The conformal calibration block is separated from the model-selection block by 30 s |
| Signal | Reproducible segment (`START_MIN`, `SEG_MIN`) of a ~2 h record; still one subject per record |
| Band-pass | `BAND = (0.1, 2.0)` Hz; alternatives (0.05, 1.0), (0.1, 1.0), (0.1, 3.0) |
| Mode | `MODE = "full"`, `SEED = 42` |

Because this is a **single split with only 4 young test subjects**, the young group is too small for inference.

## Data handling

The notebook reads the Kaggle CSV `fantasia_ecg_respiration_signals.csv` (columns `RESP`, `Participant`, `Sample`, `Sampling_Rate`), streams it **once** into per-participant float32 `.npy` files and writes an integrity manifest (row counts, sample gaps, sampling rates, non-finite values). The third-party conversion was verified against the official headers. No synthetic substitute is ever used: the notebook raises an error if the CSV is not found.

## Key configuration cell

```python
MODE = "full"
SEED = 42
RESULTS_BASE = f"{_BASE}/results/fantasia_v2"
DATA_DIR = f"{_BASE}/data/fantasia"
KAGGLE_CSV = None          # auto-detect /kaggle/input/**/fantasia_ecg_respiration_signals.csv
FORCE_RECONVERT = False    # True = redo the one-time CSV -> .npy conversion
```

## Results (300 ms, 24 test subjects)

| Model | MAE (normalised) | NLL | 95% coverage |
|---|---|---|---|
| Persistence | 0.345 | n/a | n/a |
| Ridge | **0.100** | n/a | n/a |
| Kalman | 0.186 | n/a | n/a |
| LSTM (prob.) | 0.104 | −0.80 | 94.4% |
| TCN (det.) | 0.113 | n/a | n/a |
| TCN (prob.) | 0.108 | −0.74 | 94.2% |
| Ensemble (M = 5) | 0.101 | −0.82 | 95.4% |
| Ensemble + conformal | n/a | n/a | 95.2% |

The ensemble reduces MAE versus persistence by **71%**.

Simulated tracking RMSE (mm), subject mean:

| Delay | Reactive | Predictive | UA | Kalman |
|---|---|---|---|---|
| 100 ms | 2.321 | 1.689 | 1.862 | 1.695 |
| 300 ms | 3.562 | 1.973 | 2.305 | 2.286 |
| 500 ms | 4.618 | 2.428 | 2.792 | not captured |

Predictive control reduces RMSE by **44.6%** at 300 ms and **47%** at 500 ms. UA is **worse** than predictive control (by 0.33 mm at 300 ms) and than Kalman at 100–200 ms.

## Distribution-shift result

| | Young (4 test) | Elderly (20 test) |
|---|---|---|
| Ensemble MAE at 300 ms | 0.129 | 0.095 |
| Mean σ | 0.176 | 0.134 |
| Raw 95% coverage | 95.1% | 95.4% |
| Conformal 90% coverage | 90.2% | 90.6% |

Models were not worse on elderly adults. σ tracked the change in difficulty, but elderly breathing here was *easier*, so no harmful shift occurred.

## Outputs

Everything in the PICS list, plus: `controller_selected_on_validation`, `controller_validation_selection`, `forecast_selected_model_per_horizon_validation`, `forecast_selected_model_test_results`, `forecast_validation_selection`, `group_sizes`, `inference_latency`, `sensitivity_actuator_tau`, `sensitivity_excluding_fs_anomaly_subjects`, `sensitivity_measurement_noise`.

## Notes

* The measurement-noise sensitivity is exploratory and covers the ridge forecaster only.
* Batch-1 GPU inference: 0.30–0.35 ms per LSTM and 1.8–2.1 ms per TCN window, far below the 50 ms control step.
