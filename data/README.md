# Data

**No raw data is stored in this repository.** All three datasets are public, de-identified and distributed by PhysioNet (Fantasia also via a third-party Kaggle conversion). Download them yourself and respect each dataset's license and terms of use.

| Cohort | Source | Access used in the study | Guide |
|---|---|---|---|
| PICS | PhysioNet `picsdb/1.0.0` | Downloaded by the notebook (selective parallel download or recursive `wget`) | [`pics/`](pics/README.md) |
| BIDMC | PhysioNet `bidmc/1.0.0` | Kaggle dataset `ieeeai/bidmc-ppg` attached to the notebook | [`bidmc/`](bidmc/README.md) |
| Fantasia | PhysioNet `fantasia/1.0.0` | Kaggle CSV conversion `fantasia_ecg_respiration_signals.csv` (dataset by `lana0038`) | [`fantasia/`](fantasia/README.md) |

Only the **respiration channel** is used. Annotations are not used.

## Summary

| | PICS | BIDMC | Fantasia |
|---|---|---|---|
| Population | Preterm infants | ICU patients | Healthy young and elderly adults |
| Records in database | 10 infants (1 excluded: valid fraction < 0.7, leaving 9) | 53 (3 excluded, leaving 50 from 44 patients) | 40 (20 young, 20 elderly) |
| Respiration sensor | Abdominal inductance band (infant 1: bedside monitor) | ICU monitor respiration waveform | Respiration channel |
| Native rate | 50 Hz (infant 1: 500 Hz) | 125 Hz per PhysioNet documentation (verify in `dataset_characteristics.csv`) | see `dataset_characteristics.csv`; `f2y02` is 333 Hz |
| Recording length used | Chunked segment per record | Whole ~8-min recording | Reproducible segment of a ~2 h record |
| Model rate | 20 Hz | 20 Hz | 20 Hz |
| Band-pass (Hz) | 0.1–3.0 | 0.1–2.0 | 0.1–2.0 |

The authoritative values (sampling rates, durations, per-record quality) are written by each notebook to `dataset_characteristics.csv` and `record_quality.csv`. Trust those files over this table.

## Expected local layout

If you run locally (not on Kaggle), the notebooks expect something like:

```
data/
├── pics/       # WFDB files (slp*.hea / .dat)
├── bidmc/      # bidmc01.hea, bidmc01.dat, ... (waveform records only)
└── fantasia/   # fantasia_ecg_respiration_signals.csv (+ auto-created fantasia_resp_npy/)
```

Raw files are excluded by `.gitignore`.

## Ethics and licensing

* The data are public and de-identified. No patient identifiers are used or stored.
* Check the license text on each PhysioNet page before redistributing anything derived from the data.
* The third-party Fantasia CSV is not an official release; the study verified it against the official headers.
