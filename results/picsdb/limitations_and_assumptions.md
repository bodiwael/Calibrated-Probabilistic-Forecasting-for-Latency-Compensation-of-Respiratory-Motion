# Limitations and assumptions (PICSDB, run full_20261010_172301, mode full)
* All robot results are SIMULATIONS driven by a surrogate respiratory waveform; target = A·z is an assumption (A=5.0 mm primary), NOT measured organ displacement. No physical-robot or clinical validation.
* Plant: 1-DOF first-order lag (τ=0.2s), observation delay D, command delay d_cmd=0 steps, saturation ±6.0A; inference latency is not added to D.
* Failure threshold ε = 20% of A, fixed a priori; alternatives reported as sensitivity.
* Conformal calibration uses chronologically separated validation windows of the validation subjects; temporal dependence and subject shift violate exchangeability, so coverage is measured, not guaranteed.
* Validation records provide both early-stopping (val_sel) and conformal calibration (val_cal) data, separated in time within each record.
* Windows within a subject are strongly dependent; all statistics are at the subject level and sample sizes are small (n subjects reported in tables).
* Window/test evaluation covers only the segments selected for this run (see inventory columns start_s/dur_s and exclusions in record_quality.csv).
* PICSDB has very few infants; subject-level confidence intervals are wide and many comparisons will be underpowered.
* Only a configurable segment per record is processed (compute); infant IDs are derived from record names and must be verified against the README.
* The neonatal passband is a documented choice validated only descriptively; alternatives are ablated.
