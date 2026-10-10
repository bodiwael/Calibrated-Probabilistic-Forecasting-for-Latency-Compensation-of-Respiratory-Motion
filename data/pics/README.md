# PICS: Preterm Infant Cardio-Respiratory Signals

* **Source:** <https://physionet.org/content/picsdb/1.0.0/>
* **Files:** <https://physionet.org/files/picsdb/1.0.0/>
* **Format:** WFDB (`.hea` header and `.dat` signal files), read with the `wfdb` package
* **Population:** preterm infants
* **Respiration signal:** abdominal inductance bands, 50 Hz. Infant 1 comes from the bedside monitor at 500 Hz
* **Used in:** [`notebooks/pics/`](../../notebooks/pics/README.md)

## How to get the data

**Automatic (default).** The notebook downloads the records it needs with a parallel selective downloader (`DL_WORKERS = 16`). No manual step is required, but internet access is.

**Full recursive download.** Set `RUN_RECURSIVE_WGET = True` in the notebook configuration, or run manually:

```bash
wget -r -N -c -np -P data/pics https://physionet.org/files/picsdb/1.0.0/
```

Point `DATA_DIR` at the folder that contains the `.hea` files.

## What the notebook does with it

* Selects the respiration channel by header name (regular expression `resp`), verified against the headers at runtime.
* Derives the infant id from the record name (`slp<NN>[a-z]`). Several records of one infant share the id, and all of an infant's records stay together in a fold.
* Applies the quality rule: infants with a valid fraction below 0.7 are excluded (one infant, leaving nine).
* Uses chunked streaming reads (`CHUNK_S = 300`), never loading a whole file at once.

## Citation

Cite the PICS database and PhysioNet as in the paper's reference list:

* PICS database page (doi:10.13026/C2QQ2M).
* A. H. Gee, R. Barbieri, D. Paydarfar and P. Indic, "Predicting bradycardia in preterm infants using point process analysis of heart rate," *IEEE Trans. Biomed. Eng.*, 2017.
* A. L. Goldberger *et al.*, "PhysioBank, PhysioToolkit, and PhysioNet," *Circulation*, 2000.

Check the license on the PhysioNet page before redistributing derived data.
