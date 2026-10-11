# Limitations and assumptions (Fantasia, run full_20261010_200436, mode full)
* All robot results are SIMULATIONS driven by a surrogate respiratory waveform; target = A·z is an assumption (A=5.0 mm primary), NOT measured organ displacement. No physical-robot or clinical validation.
* Plant: 1-DOF first-order lag (τ=0.2s), observation delay D, command delay d_cmd=0 steps, saturation ±6.0A; inference latency is not added to D.
* Failure threshold ε = 20% of A, fixed a priori; alternatives reported as sensitivity.
* Conformal calibration uses chronologically separated validation windows of the validation subjects; temporal dependence and subject shift violate exchangeability, so coverage is measured, not guaranteed.
* Validation records provide both early-stopping (val_sel) and conformal calibration (val_cal) data, separated in time within each record.
* Windows within a subject are strongly dependent; all statistics are at the subject level and sample sizes are small (n subjects reported in tables).
* Window/test evaluation covers only the segments selected for this run (see inventory columns start_s/dur_s and exclusions in record_quality.csv).
* Fantasia contains healthy resting volunteers (young vs. elderly) with long recordings; only a reproducible segment per subject is used (segments are NOT independent subjects).
* Data are a third-party processed Kaggle CSV (not the official PhysioNet files): no headers/units/age metadata and no official checksums; the RESP channel is assumed to be the respiration waveform and is sanity-checked via the spectral respiratory rate. Cohort labels come from participant IDs.
* In this CSV participant f2y02 has Sampling_Rate = 333 (all others 250; its duration is still ~7035 s, so it is treated as genuinely recorded at 333 Hz) and several participants contain short non-finite stretches (gaps <= 0.25 s are forward-filled, longer ones are marked invalid and excluded from windows).
