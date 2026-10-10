# Fantasia Database

* **Official source:** <https://physionet.org/content/fantasia/1.0.0/>
* **Version used in the study:** third-party Kaggle CSV conversion, `fantasia_ecg_respiration_signals.csv` (Kaggle dataset "fantasia-dataset-with-ecg-and-respiration-signals", by `lana0038`)
* **Population:** 20 young and 20 elderly healthy adults
* **Used in:** [`notebooks/fantasia/`](../../notebooks/fantasia/README.md)

## How to get the data

**Kaggle (as in the study).** Use *Add Data* and search for `fantasia-dataset-with-ecg-and-respiration-signals`. The notebook auto-detects `/kaggle/input/**/fantasia_ecg_respiration_signals.csv`.

**Local.** Download the CSV manually and either place it under `data/fantasia/` or set `KAGGLE_CSV='/path/to/fantasia_ecg_respiration_signals.csv'` in the configuration cell.

If the file cannot be found the notebook raises an error. **No synthetic substitute is used.**

## CSV format

| Column | Meaning |
|---|---|
| `RESP` | Respiration signal |
| `Participant` | Record id, e.g. `f1y01`, `f2o07` |
| `Sample` | Sample index (used to detect gaps) |
| `Sampling_Rate` | Per-participant sampling rate |

The file is large (the notebook logs its size in GiB), so it is streamed in chunks.

## One-time conversion

The notebook streams the CSV once into per-participant float32 `.npy` files under `data/fantasia/fantasia_resp_npy/` and writes `manifest.csv` with integrity checks (row counts, sample gaps, sampling rates, non-finite values). Set `FORCE_RECONVERT = True` to redo it.

## Things to know

* Cohort is read from the record name: `f1y##` / `f2y##` are young and `f1o##` / `f2o##` are elderly. This is cross-checked against header ages.
* Record **`f2y02` has a different sampling rate (333 Hz)** and is retained. A sensitivity analysis excluding sampling-rate-anomaly subjects is saved as `sensitivity_excluding_fs_anomaly_subjects.csv`.
* The CSV conversion was verified against the official PhysioNet headers. Because it is third-party, prefer the official WFDB files if you need an authoritative source.
* Each long (~2 h) record is cut to a reproducible segment (`START_MIN`, `SEG_MIN`). It is still one subject.

## Citation

* A. L. Goldberger *et al.*, "PhysioBank, PhysioToolkit, and PhysioNet," *Circulation*, 2000.
* The Fantasia database page on PhysioNet (follow the citation requested there).
* The Kaggle dataset page for the CSV conversion.

Check the license on each page before redistributing derived data.
