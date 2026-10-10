# BIDMC notebook: ICU patients

**File:** `bidmc_pipeline.ipynb`  **Dataset:** [BIDMC PPG and Respiration Dataset, PhysioNet](https://physionet.org/content/bidmc/1.0.0/)  **Data guide:** [`../../data/bidmc/README.md`](../../data/bidmc/README.md)

## What this notebook does

Runs the full study pipeline on 8-minute ICU recordings with a **patient-grouped 5-fold cross-validation**, including the later pipeline additions: validation-only model selection (Section G2), UCPC and triggered controllers, and sensitivity studies.

## Protocol

| Item | Setting |
|---|---|
| Records | 53 waveform records; 3 excluded by the quality rule, leaving **50 records from 44 patients** |
| Patient identity | MIMIC-II subject ID parsed from the dataset's own `Fix` files (`PATIENT_GROUPING = 'documented_id'`). Records are grouped only if the documentation says they share a subject. A demographic key (age, sex, location) is the fallback and is flagged as an assumption |
| Folds | Patient-grouped K-fold: test = bucket *k*, validation = bucket *k+1*, train = the rest. Each subject is a test subject exactly once. All records of a patient stay in one fold |
| Signal | Whole ~8-min respiration recording (waveform records `bidmcNN` only; numerics `bidmcNNn` are ignored) |
| Band-pass | `BAND = (0.1, 2.0)` Hz; alternatives (0.05, 1.0), (0.1, 1.0), (0.1, 3.0) |
| Mode | `MODE = "full"`, `SEED = 42` |

Two patients contribute four records each; this is stated in the paper's limitations.

## Key configuration cell

```python
MODE = "full"
SEED = 42
RESULTS_BASE = "/kaggle/working/results/bidmc"
DATA_DIR = "/kaggle/input/datasets/ieeeai/bidmc-ppg/bidmc-ppg-and-respiration-dataset-1.0.0"
ALLOW_OVERWRITE = True
EXPECTED_N_RECORDS = 53
```

This notebook **reads the dataset directly from `/kaggle/input`** (read-only, no copy, no download). To run it locally, change `DATA_DIR` to a folder containing the original PhysioNet WFDB files (`bidmc01.hea`, `bidmc01.dat`, ...). If the configured path has no headers, the notebook searches all attached inputs, and asserts with an explanatory message if it still finds none.

## Results (300 ms, 50 records)

| Model | MAE (normalised) | NLL | 95% coverage |
|---|---|---|---|
| Persistence | 0.524 | n/a | n/a |
| Ridge | 0.223 | n/a | n/a |
| Kalman | 0.386 | n/a | n/a |
| LSTM (prob.) | 0.226 | 0.16 | 92.8% |
| TCN (det.) | **0.192** | n/a | n/a |
| TCN (prob.) | 0.194 | −0.01 | 91.2% |
| Ensemble (M = 5) | 0.218 | 0.10 | 94.3% |
| Ensemble + conformal | n/a | n/a | 94.8% |

The ensemble reduces MAE versus persistence by **58%**.

Simulated tracking RMSE (mm), subject mean:

| Delay | Reactive | Predictive | UA | UCPC | Triggered | Kalman |
|---|---|---|---|---|---|---|
| 100 ms | 3.054 | 2.191 | 2.211 | 2.191 | 2.191 | 2.257 |
| 300 ms | 4.620 | 2.646 | 2.676 | 2.646 | 2.646 | 3.375 |
| 500 ms | 5.840 | 2.916 | 2.950 | 2.918 | 2.916 | 5.115 |

Predictive control reduces RMSE by **42.7%** at 300 ms and **50%** at 500 ms. The validation-tuned blend chose w = 1 (pure forecast) in all five folds, so it matches predictive control exactly. UA, UCPC and the triggered variant never beat predictive control.

## Outputs

Everything in the PICS list, plus: `controller_parameter_summary`, `patient_identity_audit`, `validation_model_selection_log`, `validation_selected_forecaster_test_performance`.

Figures: same 14 figures as the other notebooks (see the main README or `results/README.md`).

## Notes

* Validation-selected forecasters (Section G2) mostly pick TCN variants in BIDMC (`tcn_det` in 4/5 folds at 300 ms), consistent with TCN being best at 300 ms.
* The 50 test "subjects" are **records**, from 44 patients.
