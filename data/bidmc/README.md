# BIDMC PPG and Respiration Dataset

* **Source:** <https://physionet.org/content/bidmc/1.0.0/>
* **Kaggle copy used in the study:** `ieeeai/bidmc-ppg` (mounted at `/kaggle/input/datasets/ieeeai/bidmc-ppg/bidmc-ppg-and-respiration-dataset-1.0.0`)
* **Format:** original PhysioNet WFDB files (`bidmc01.hea`, `bidmc01.dat`, ...)
* **Population:** ICU patients, 8-minute recordings
* **Records:** 53 waveform records. Three are excluded by the quality rule (valid fraction < 0.7), leaving **50 records from 44 patients**
* **Used in:** [`notebooks/bidmc/`](../../notebooks/bidmc/README.md)

## How to get the data

**Kaggle (as in the study).** In the notebook's right panel choose *Add Input* and attach `ieeeai/bidmc-ppg`. Nothing is downloaded or copied. The notebook reads from `/kaggle/input` directly.

**Local.** Download from PhysioNet and set `DATA_DIR` in the configuration cell:

```bash
wget -r -N -c -np -P data/bidmc https://physionet.org/files/bidmc/1.0.0/
```

> The dataset must contain the **original WFDB files**. A copy that only has CSV exports is not enough, and the notebook stops with an explanatory assertion.

## What the notebook does with it

* Uses waveform records only (`bidmcNN`). Numerics records (`bidmcNNn`) are ignored.
* Selects the respiration channel by header name and verifies it at runtime.
* Parses the MIMIC-II **subject ID** from the dataset's `Fix` files to group records by patient. Two patients contribute four records each. If no id can be parsed, a demographic key (age, sex, location) is used and flagged as an assumption. The audit is saved as `patient_identity_audit.csv`.
* Keeps all records of one patient in the same fold (patient-grouped 5-fold CV).
* Uses the whole recording (about 8 minutes).

## Citation

* A. L. Goldberger *et al.*, "PhysioBank, PhysioToolkit, and PhysioNet," *Circulation*, 2000.
* The BIDMC dataset page on PhysioNet (follow the citation requested there).

Check the license on the PhysioNet page before redistributing derived data.
