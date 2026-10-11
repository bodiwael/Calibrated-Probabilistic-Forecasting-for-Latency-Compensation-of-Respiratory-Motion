# Final report — BIDMC (full mode, run full_20261010_181630)

**Simulation notice:** the robot, its actuator and the target displacement are SIMULATED; the respiratory waveform is a surrogate target, not measured anatomical displacement. All results are cross-validated on this single public cohort.

## 1. Execution status
* patient_identity: RUN
* dataset_inventory: RUN
* unit_tests_preprocessing: RUN
* forecasting_models: RUN
* forecast_evaluation: RUN
* model_selection_validation: RUN
* prediction_export_and_tests: RUN
* uncertainty_calibration: RUN
* distribution_shift: NOT RUN: only one evaluation group present ([np.str_('test')]); see held-out-subject results above
* synthetic_target: RUN
* robot_sinusoid_validation: RUN
* controllers_primary: RUN
* tracking_metrics: RUN
* failure_prediction: RUN
* failure_curves: RUN
* statistics: RUN
* sensitivity_plant: RUN
* sensitivity_measurement_noise: RUN
* ablation: RUN
* figures_tables: RUN

## 2. Cohort and subject identity
* Records analysed: 50; subjects: 50; test subjects (each exactly once): 50; folds: 5.
* Exclusions: 3 (bidmc05: valid_frac<0.70; bidmc35: valid_frac<0.70; bidmc39: valid_frac<0.70). Not selected by configuration: 0.
* Patient grouping requested/used: documented_id / documented_id; documented subject IDs parsed: 50 of 50; patient groups: 44; records grouped together: {'ID:s03386': ['bidmc06', 'bidmc07', 'bidmc08', 'bidmc09'], 'ID:s11342': ['bidmc20', 'bidmc21', 'bidmc22', 'bidmc23']}. If mode used = demographic_conservative this is an ASSUMPTION, not documented identity.

## 3. Validation-selected choices (no test data used)
**Forecaster chosen per fold on validation MAE, frozen, then evaluated on held-out test subjects:**
| horizon_ms | selected_by_folds | n_subjects | mae | mae_lo | mae_hi |
|---|---|---|---|---|---|
| 100 | tcn_prob:4, ridge:1 | 50 | 0.0387 | 0.03425 | 0.04386 |
| 200 | tcn_prob:3, tcn_det:2 | 50 | 0.109 | 0.09535 | 0.1243 |
| 300 | tcn_det:4, tcn_prob:1 | 50 | 0.1925 | 0.1682 | 0.2211 |
| 400 | tcn_det:5 | 50 | 0.2552 | 0.2232 | 0.2922 |
| 500 | tcn_det:5 | 50 | 0.2948 | 0.2575 | 0.3355 |

**Controller parameters chosen on validation (ensemble forecaster):**
| delay_ms | blend_w_median | folds_with_w_eq_1 | UA_c_median | folds_with_c_at_grid_max | ucpc_unconstrained_folds | trigger_never_folds |
|---|---|---|---|---|---|---|
| 100 | 1 | 5/5 | 64 | 5/5 | 5/5 | 5/5 |
| 200 | 1 | 5/5 | 64 | 5/5 | 5/5 | 5/5 |
| 300 | 1 | 5/5 | 64 | 5/5 | 4/5 | 5/5 |
| 400 | 1 | 5/5 | 64 | 5/5 | 3/5 | 5/5 |
| 500 | 1 | 5/5 | 64 | 5/5 | 3/5 | 5/5 |
**The validation-tuned fixed blend selected w = 1 in every fold, so it is mathematically identical to predictive-only control and is reported as a duplicate, not as an independent method.**

## 4. Held-out test forecasting results
*Descriptive comparison of all models (not a selection rule). The lowest-MAE row per horizon below is shown only for reference:*
| horizon_ms | model | mae | mae_lo | mae_hi |
|---|---|---|---|---|
| 100 | tcn_prob | 0.03892 | 0.03468 | 0.04352 |
| 200 | tcn_prob | 0.109 | 0.09657 | 0.1225 |
| 300 | tcn_det | 0.1918 | 0.1689 | 0.2166 |
| 400 | tcn_det | 0.2552 | 0.2241 | 0.2883 |
| 500 | tcn_det | 0.2948 | 0.2589 | 0.333 |

Inference latency (batch size 1, device = cuda): [{'model': 'lstm_prob', 'ms_per_window': 0.326}, {'model': 'tcn_prob', 'ms_per_window': 1.944}]

## 5. Held-out test uncertainty results
Mean |PICP95 - 0.95| over horizons (raw Gaussian intervals): {'ensemble': 0.006, 'lstm_prob': 0.026, 'tcn_prob': 0.038}.
Conformal 95% coverage / mean interval width (mean over horizons and subjects; width in normalised units; high coverage alone does not make intervals informative): {'conf_abs_5_picp': {'ensemble': 0.947, 'lstm_prob': 0.944, 'persistence': 0.947, 'ridge': 0.949, 'tcn_prob': 0.947}, 'conf_abs_5_mpiw': {'ensemble': 1.22, 'lstm_prob': 1.246, 'persistence': 2.759, 'ridge': 1.289, 'tcn_prob': 1.091}, 'conf_norm_5_picp': {'ensemble': 0.947, 'lstm_prob': 0.947, 'persistence': nan, 'ridge': nan, 'tcn_prob': 0.945}, 'conf_norm_5_mpiw': {'ensemble': 1.048, 'lstm_prob': 1.108, 'persistence': nan, 'ridge': nan, 'tcn_prob': 0.965}}
Ensemble sigma vs |error| Spearman across subject-horizons: mean 0.275 (min 0.037, max 0.602); an association with error is NOT evidence that uncertainty helps control.

## 6. Held-out test robot-simulation results (SIMULATED; subject-mean, mm)
| delay_ms | fixed_blend | fixed_blend_0.5 | kalman | predictive | reactive | trigger | ucpc | uncertainty_aware |
|---|---|---|---|---|---|---|---|---|
| 0 | nan | nan | nan | nan | 2.139 | nan | nan | nan |
| 100 | 2.191 | 2.618 | 2.257 | 2.191 | 3.054 | 2.191 | 2.191 | 2.211 |
| 200 | 2.396 | 3.111 | 2.681 | 2.396 | 3.885 | 2.396 | 2.396 | 2.423 |
| 300 | 2.646 | 3.558 | 3.375 | 2.646 | 4.62 | 2.646 | 2.646 | 2.676 |
| 400 | 2.819 | 3.914 | 4.208 | 2.819 | 5.267 | 2.819 | 2.825 | 2.852 |
| 500 | 2.916 | 4.191 | 5.115 | 2.916 | 5.84 | 2.916 | 2.918 | 2.95 |

Command total variation (mm/s) and failure rate by controller:
| delay_ms | fixed_blend | fixed_blend_0.5 | kalman | predictive | reactive | trigger | ucpc | uncertainty_aware |
|---|---|---|---|---|---|---|---|---|
| 0 | nan | nan | nan | nan | 9.386 | nan | nan | nan |
| 100 | 10.05 | 9.383 | 10.99 | 10.05 | 9.386 | 10.05 | 10.05 | 10 |
| 200 | 11.3 | 9.326 | 14.14 | 11.3 | 9.386 | 11.3 | 11.3 | 11.19 |
| 300 | 10.9 | 8.867 | 18.12 | 10.9 | 9.386 | 10.9 | 10.88 | 10.79 |
| 400 | 9.566 | 8.165 | 22.48 | 9.566 | 9.386 | 9.566 | 9.546 | 9.476 |
| 500 | 8.405 | 7.506 | 27.03 | 8.405 | 9.386 | 8.405 | 8.394 | 8.331 |

| delay_ms | fixed_blend | fixed_blend_0.5 | kalman | predictive | reactive | trigger | ucpc | uncertainty_aware |
|---|---|---|---|---|---|---|---|---|
| 0 | nan | nan | nan | nan | 0.6258 | nan | nan | nan |
| 100 | 0.6214 | 0.6826 | 0.6335 | 0.6214 | 0.7276 | 0.6214 | 0.6214 | 0.6235 |
| 200 | 0.622 | 0.7213 | 0.6644 | 0.622 | 0.786 | 0.622 | 0.622 | 0.626 |
| 300 | 0.6248 | 0.7483 | 0.7142 | 0.6248 | 0.8238 | 0.6248 | 0.6248 | 0.6296 |
| 400 | 0.636 | 0.7697 | 0.7618 | 0.636 | 0.8496 | 0.636 | 0.636 | 0.6402 |
| 500 | 0.649 | 0.7871 | 0.7955 | 0.649 | 0.8669 | 0.649 | 0.649 | 0.6524 |
Constrained-mode activation (share of windows with the limit binding / trigger active):
| controller | delay_ms | clip_frac | trig_frac |
|---|---|---|---|
| trigger | 100 | 0 | 0 |
| trigger | 200 | 0 | 0 |
| trigger | 300 | 0 | 0 |
| trigger | 400 | 0 | 0 |
| trigger | 500 | 0 | 0 |
| ucpc | 100 | 0 | 0 |
| ucpc | 200 | 0 | 0 |
| ucpc | 300 | 0.001502 | 0 |
| ucpc | 400 | 0.004012 | 0 |
| ucpc | 500 | 0.002557 | 0 |

## 7. Primary paired subject-level comparisons (RMSE difference a - b; negative favours a)

**Original uncertainty-aware blend (UA)** (Holm-corrected within family; n = 50 subjects):
| delay_ms | a | b | n | mean_diff | median_diff | ci_lo | ci_hi | p_raw | p_holm | effect_rank_biserial | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 100 | uncertainty_aware | reactive | 50 | -0.8439 | -0.8809 | -0.9305 | -0.7582 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 100 | uncertainty_aware | predictive | 50 | 0.01936 | 0.01813 | 0.01607 | 0.02304 | 1.776e-15 | 4.441e-14 | 1 | HIGHER RMSE (worse) |
| 100 | uncertainty_aware | fixed_blend | 50 | 0.01936 | 0.01813 | 0.01607 | 0.02304 | 1.776e-15 | 4.441e-14 | 1 | HIGHER RMSE (worse) |
| 100 | uncertainty_aware | fixed_blend_0.5 | 50 | -0.4074 | -0.43 | -0.4497 | -0.3659 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 100 | uncertainty_aware | kalman | 50 | -0.04615 | -0.05634 | -0.06 | -0.0311 | 1.37e-08 | 1.37e-08 | -0.8353 | lower RMSE (better) |
| 200 | uncertainty_aware | reactive | 50 | -1.463 | -1.583 | -1.623 | -1.305 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 200 | uncertainty_aware | predictive | 50 | 0.02677 | 0.02564 | 0.02284 | 0.0311 | 1.776e-15 | 4.441e-14 | 1 | HIGHER RMSE (worse) |
| 200 | uncertainty_aware | fixed_blend | 50 | 0.02677 | 0.02564 | 0.02284 | 0.0311 | 1.776e-15 | 4.441e-14 | 1 | HIGHER RMSE (worse) |
| 200 | uncertainty_aware | fixed_blend_0.5 | 50 | -0.688 | -0.7341 | -0.7632 | -0.6127 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 200 | uncertainty_aware | kalman | 50 | -0.2584 | -0.2352 | -0.3023 | -0.2165 | 3.677e-13 | 1.471e-12 | -0.9733 | lower RMSE (better) |
| 300 | uncertainty_aware | reactive | 50 | -1.944 | -2.101 | -2.168 | -1.73 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 300 | uncertainty_aware | predictive | 50 | 0.03 | 0.03046 | 0.02523 | 0.03497 | 1.776e-15 | 4.441e-14 | 1 | HIGHER RMSE (worse) |
| 300 | uncertainty_aware | fixed_blend | 50 | 0.03 | 0.03046 | 0.02523 | 0.03497 | 1.776e-15 | 4.441e-14 | 1 | HIGHER RMSE (worse) |
| 300 | uncertainty_aware | fixed_blend_0.5 | 50 | -0.8822 | -0.9623 | -0.9889 | -0.7777 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 300 | uncertainty_aware | kalman | 50 | -0.699 | -0.6524 | -0.7975 | -0.6095 | 3.553e-15 | 4.441e-14 | -0.9984 | lower RMSE (better) |
| 400 | uncertainty_aware | reactive | 50 | -2.415 | -2.652 | -2.706 | -2.14 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 400 | uncertainty_aware | predictive | 50 | 0.03236 | 0.03307 | 0.02648 | 0.03849 | 2.487e-14 | 1.492e-13 | 0.9906 | HIGHER RMSE (worse) |
| 400 | uncertainty_aware | fixed_blend | 50 | 0.03236 | 0.03307 | 0.02648 | 0.03849 | 2.487e-14 | 1.492e-13 | 0.9906 | HIGHER RMSE (worse) |
| 400 | uncertainty_aware | fixed_blend_0.5 | 50 | -1.062 | -1.143 | -1.199 | -0.925 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 400 | uncertainty_aware | kalman | 50 | -1.357 | -1.351 | -1.526 | -1.199 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 500 | uncertainty_aware | reactive | 50 | -2.89 | -3.13 | -3.242 | -2.555 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 500 | uncertainty_aware | predictive | 50 | 0.0341 | 0.0341 | 0.02707 | 0.04158 | 5.453e-13 | 1.636e-12 | 0.9702 | HIGHER RMSE (worse) |
| 500 | uncertainty_aware | fixed_blend | 50 | 0.0341 | 0.0341 | 0.02707 | 0.04158 | 5.453e-13 | 1.636e-12 | 0.9702 | HIGHER RMSE (worse) |
| 500 | uncertainty_aware | fixed_blend_0.5 | 50 | -1.241 | -1.342 | -1.412 | -1.071 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
| 500 | uncertainty_aware | kalman | 50 | -2.164 | -2.171 | -2.424 | -1.911 | 1.776e-15 | 4.441e-14 | -1 | lower RMSE (better) |
**Revised controllers (UCPC / Trigger)** (Holm-corrected within family; n = 50 subjects):
| delay_ms | a | b | n | mean_diff | median_diff | ci_lo | ci_hi | p_raw | p_holm | effect_rank_biserial | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 100 | ucpc | predictive | 50 | 0 | 0 | 0 | 0 | nan | nan | nan | no detectable difference |
| 100 | ucpc | reactive | 50 | -0.8632 | -0.8975 | -0.9532 | -0.7749 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |
| 100 | trigger | predictive | 50 | 2.825e-11 | 5.507e-11 | -3.016e-10 | 3.82e-10 | 0.9466 | 1 | 0.01176 | no detectable difference |
| 100 | trigger | reactive | 50 | -0.8632 | -0.8975 | -0.9532 | -0.7749 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |
| 200 | ucpc | predictive | 50 | 0 | 0 | 0 | 0 | nan | nan | nan | no detectable difference |
| 200 | ucpc | reactive | 50 | -1.489 | -1.613 | -1.654 | -1.329 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |
| 200 | trigger | predictive | 50 | -3.491e-12 | -4.427e-12 | -2.812e-10 | 2.651e-10 | 0.9466 | 1 | -0.01176 | no detectable difference |
| 200 | trigger | reactive | 50 | -1.489 | -1.613 | -1.654 | -1.329 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |
| 300 | ucpc | predictive | 50 | 0.0007653 | 0 | -0.00022 | 0.002195 | 0.1055 | 0.842 | 0.6 | no detectable difference |
| 300 | ucpc | reactive | 50 | -1.973 | -2.13 | -2.203 | -1.754 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |
| 300 | trigger | predictive | 50 | 2.328e-10 | 2.449e-10 | -5.953e-11 | 5.141e-10 | 0.1053 | 0.842 | 0.2643 | no detectable difference |
| 300 | trigger | reactive | 50 | -1.974 | -2.131 | -2.203 | -1.756 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |
| 400 | ucpc | predictive | 50 | 0.005329 | 0 | -0.0004315 | 0.01419 | 0.4091 | 1 | 0.219 | no detectable difference |
| 400 | ucpc | reactive | 50 | -2.442 | -2.688 | -2.735 | -2.16 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |
| 400 | trigger | predictive | 50 | 1.262e-10 | 8.877e-11 | -7.429e-11 | 3.316e-10 | 0.4043 | 1 | 0.1373 | no detectable difference |
| 400 | trigger | reactive | 50 | -2.448 | -2.688 | -2.744 | -2.167 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |
| 500 | ucpc | predictive | 50 | 0.002402 | 0 | -0.0002769 | 0.005892 | 0.2943 | 1 | 0.2762 | no detectable difference |
| 500 | ucpc | reactive | 50 | -2.922 | -3.167 | -3.28 | -2.581 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |
| 500 | trigger | predictive | 50 | -1.651e-11 | 4.772e-11 | -2.617e-10 | 2.296e-10 | 0.7888 | 1 | 0.04471 | no detectable difference |
| 500 | trigger | reactive | 50 | -2.924 | -3.167 | -3.283 | -2.582 | 1.776e-15 | 3.197e-14 | -1 | lower RMSE (better) |

**UA vs predictive-only:** verdicts across delays = {'HIGHER RMSE (worse)': 5}. The report makes no claim that uncertainty-aware control improves tracking unless a row above shows a lower RMSE with a CI excluding zero.

## 8. Exploratory failure-prediction results (failure = |simulated tracking error| > threshold, a SIMULATION assumption)
ROC-AUC (predictive controller):
| delay_ms | abs_velocity | forecast_magnitude | last_forecast_error | sigma_aleatoric | sigma_epistemic | sigma_total | velocity+sigma |
|---|---|---|---|---|---|---|---|
| 100 | 0.9386 | 0.8714 | 0.6713 | 0.7611 | 0.6708 | 0.7629 | 0.9402 |
| 200 | 0.8783 | 0.855 | 0.6107 | 0.7209 | 0.6357 | 0.7225 | 0.8826 |
| 300 | 0.7675 | 0.7596 | 0.602 | 0.689 | 0.6215 | 0.689 | 0.7821 |
| 400 | 0.693 | 0.7054 | 0.6005 | 0.678 | 0.5927 | 0.6771 | 0.7211 |
| 500 | 0.6458 | 0.6864 | 0.6076 | 0.6793 | 0.5789 | 0.6785 | 0.6936 |
PR-AUC and prevalence (compare PR-AUC with prevalence):
| delay_ms | score | auprc | prevalence_test | precision | recall | f1 | brier | brier_baseline_prevalence | subject_auc_n |
|---|---|---|---|---|---|---|---|---|---|
| 100 | sigma_total | 0.805 | 0.6195 | 0.7177 | 0.9397 | 0.8138 | 0.1925 | 0.2357 | 50 |
| 100 | abs_velocity | 0.9618 | 0.6195 | 0.8904 | 0.9128 | 0.9015 | 0.09283 | 0.2357 | 50 |
| 100 | velocity+sigma | 0.9619 | 0.6195 | 0.8932 | 0.9132 | 0.9031 | 0.09182 | 0.2357 | 50 |
| 200 | sigma_total | 0.7713 | 0.6203 | 0.6921 | 0.9462 | 0.7994 | 0.2034 | 0.2356 | 50 |
| 200 | abs_velocity | 0.922 | 0.6203 | 0.8323 | 0.8669 | 0.8492 | 0.1356 | 0.2356 | 50 |
| 200 | velocity+sigma | 0.9223 | 0.6203 | 0.8207 | 0.8849 | 0.8516 | 0.1339 | 0.2356 | 50 |
| 300 | sigma_total | 0.746 | 0.6236 | 0.6845 | 0.9362 | 0.7908 | 0.2113 | 0.2347 | 50 |
| 300 | abs_velocity | 0.8428 | 0.6236 | 0.7275 | 0.8466 | 0.7825 | 0.1877 | 0.2347 | 50 |
| 300 | velocity+sigma | 0.8438 | 0.6236 | 0.7127 | 0.9244 | 0.8049 | 0.183 | 0.2347 | 50 |
| 400 | sigma_total | 0.7482 | 0.635 | 0.6869 | 0.9412 | 0.7942 | 0.2115 | 0.2318 | 50 |
| 400 | abs_velocity | 0.79 | 0.635 | 0.635 | 0.9999 | 0.7767 | 0.2086 | 0.2318 | 50 |
| 400 | velocity+sigma | 0.7952 | 0.635 | 0.6893 | 0.9511 | 0.7993 | 0.2005 | 0.2318 | 50 |
| 500 | sigma_total | 0.7618 | 0.6481 | 0.6943 | 0.9462 | 0.8009 | 0.2081 | 0.2281 | 50 |
| 500 | abs_velocity | 0.7595 | 0.6481 | 0.6481 | 0.9999 | 0.7864 | 0.2159 | 0.2281 | 50 |
| 500 | velocity+sigma | 0.7774 | 0.6481 | 0.6942 | 0.9558 | 0.8043 | 0.2043 | 0.2281 | 50 |

## 9. Ablations and sensitivity studies
Confirmatory = prespecified primary comparisons only; every ablation / sensitivity in `ablation_results.csv` is labelled in column `design` (exploratory unless stated). Number of ablation rows: 2742. Plant sensitivities keep the parameters tuned on the nominal plant.

## 10. Reproducibility
* Seed: 42; run folder: /kaggle/working/results/bidmc/full_20261010_181630.
* Environment: {"python": "3.13.15", "platform": "Linux-6.18.48+-x86_64-with-glibc2.39", "numpy": "2.1.3", "pandas": "2.3.3", "scipy": "1.16.3", "sklearn": "1.6.1", "statsmodels": "0.15.0", "wfdb": "4.3.1", "torch": "2.11.0+cu128", "matplotlib": "3.10.0", "device": "cuda", "cuda_available": true, "ram_total_gb": 31.35, "ram_available_gb": 29.75, "seed": 42, "mode": "full"}
* Configuration, split manifest, dataset inventory, patient-identity audit, controller parameters, model summary, saved predictions and logs are exported in the run folder.

## 11. Limitations (also in limitations_and_assumptions.md)
Simulation only (first-order 1-DOF actuator, surrogate waveform, no organ motion); single public ICU cohort (BIDMC), 8-minute recordings; the failure threshold is a simulation assumption; measurement-noise sensitivity covers the ridge forecaster only; distribution-shift analysis runs only if age is available for all subjects; no external-cohort validation in this notebook.