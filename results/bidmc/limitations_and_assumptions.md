# Limitations and assumptions (BIDMC, run full_20261010_181630, mode full)
* All robot results are SIMULATIONS driven by a surrogate respiratory waveform; target = A·z is an assumption (A=5.0 mm primary), NOT measured organ displacement. No physical-robot or clinical validation.
* Plant: 1-DOF first-order lag (τ=0.2s), observation delay D, command delay d_cmd=0 steps, saturation ±6.0A; inference latency is not added to D.
* Failure threshold ε = 20% of A, fixed a priori; alternatives reported as sensitivity.
* Conformal calibration uses chronologically separated validation windows of the validation subjects; temporal dependence and subject shift violate exchangeability, so coverage is measured, not guaranteed.
* Validation records provide both early-stopping (val_sel) and conformal calibration (val_cal) data, separated in time within each record.
* Evaluation is patient-grouped K-fold cross-validation (each analysed subject tested once; records with identical age/sex/location header metadata are kept in one fold). Windows within a subject are strongly dependent; all statistics are at the subject level (n subjects reported in tables). Failure-AUC bootstrap CIs use every BOOT_STRIDE-th window; point estimates use all windows.
* Window/test evaluation covers only the segments selected for this run (see inventory columns start_s/dur_s and exclusions in record_quality.csv).
* BIDMC is a hospital ICU population with short (~8 min) recordings of a single impedance-pneumography respiratory channel; generalisation to other populations is untested here.
* Subgroup (age) analyses depend on header metadata parsed best-effort; they are exploratory.
