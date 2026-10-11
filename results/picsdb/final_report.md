# Final report — PICSDB (full mode, run full_20261010_172301)

* Subjects analysed: 9; records analysed: 9; test subjects: 9; folds: 9.
* Exclusions: 1 (infant5_resp: valid_frac<0.70). Records not selected by configuration: 10.

## Best forecasting model per horizon (lowest subject-mean MAE, normalised)
| horizon_ms | model | mae | mae_lo | mae_hi |
|---|---|---|---|---|
| 100 | tcn_prob | 0.1201 | 0.08393 | 0.1736 |
| 200 | tcn_prob | 0.3021 | 0.2168 | 0.4346 |
| 300 | tcn_prob | 0.4359 | 0.3156 | 0.6207 |
| 400 | tcn_det | 0.4938 | 0.3593 | 0.6946 |
| 500 | tcn_det | 0.5209 | 0.3759 | 0.7323 |

## Uncertainty calibration
Mean |PICP95 − 0.95| over horizons (Gaussian intervals): {'tcn_prob': 0.011, 'ensemble': 0.073, 'lstm_prob': 0.092}. Best-calibrated Gaussian method: **tcn_prob**.
Conformal 95% empirical coverage (mean over horizons/subjects): {'conf_abs_5_picp': {'ensemble': 0.911, 'lstm_prob': 0.911, 'persistence': 0.911, 'ridge': 0.914, 'tcn_prob': 0.915}, 'conf_norm_5_picp': {'ensemble': 0.939, 'lstm_prob': 0.938, 'persistence': nan, 'ridge': nan, 'tcn_prob': 0.945}}
Ensemble σ vs |error| Spearman across subject-horizons: mean 0.431 (min 0.100, max 0.613).

## Best controller per delay (SIMULATION, subject-mean RMSE, mm)
| delay_ms | controller | rmse | rmse_lo | rmse_hi |
|---|---|---|---|---|
| 0 | reactive | 3.303 | 2.34 | 4.655 |
| 100 | predictive | 3.395 | 2.256 | 4.954 |
| 200 | fixed_blend | 3.976 | 2.706 | 5.675 |
| 300 | fixed_blend | 4.343 | 3.001 | 6.13 |
| 400 | predictive | 4.387 | 2.986 | 6.266 |
| 500 | predictive | 4.434 | 2.986 | 6.367 |

## Uncertainty-aware blend vs comparators (RMSE difference, negative favours UA)
| delay_ms | b | n | mean_diff | ci_lo | ci_hi | p_raw | p_holm | effect_rank_biserial |
|---|---|---|---|---|---|---|---|---|
| 100 | reactive | 9 | -0.8221 | -0.9584 | -0.7183 | 0.003906 | 0.09766 | -1 |
| 100 | predictive | 9 | 0.2107 | 0.1416 | 0.2916 | 0.003906 | 0.09766 | 1 |
| 100 | fixed_blend | 9 | 0.2107 | 0.1416 | 0.2916 | 0.003906 | 0.09766 | 1 |
| 100 | fixed_blend_0.5 | 9 | -0.2674 | -0.3404 | -0.201 | 0.003906 | 0.09766 | -1 |
| 100 | kalman | 9 | -1.408 | -2.138 | -0.7371 | 0.007812 | 0.09766 | -0.9556 |
| 200 | reactive | 9 | -1.035 | -1.228 | -0.8778 | 0.003906 | 0.09766 | -1 |
| 200 | predictive | 9 | 0.1345 | 0.06521 | 0.2027 | 0.01172 | 0.09766 | 0.9111 |
| 200 | fixed_blend | 9 | 0.1487 | 0.09873 | 0.2043 | 0.003906 | 0.09766 | 1 |
| 200 | fixed_blend_0.5 | 9 | -0.298 | -0.4251 | -0.1977 | 0.003906 | 0.09766 | -1 |
| 200 | kalman | 9 | -1.439 | -2.049 | -1.019 | 0.003906 | 0.09766 | -1 |
| 300 | reactive | 9 | -1.072 | -1.343 | -0.8438 | 0.003906 | 0.09766 | -1 |
| 300 | predictive | 9 | 0.1156 | 0.05475 | 0.1921 | 0.01953 | 0.09766 | 0.8667 |
| 300 | fixed_blend | 9 | 0.116 | 0.05458 | 0.1921 | 0.003906 | 0.09766 | 1 |
| 300 | fixed_blend_0.5 | 9 | -0.2841 | -0.43 | -0.1742 | 0.003906 | 0.09766 | -1 |
| 300 | kalman | 9 | -1.522 | -2.108 | -1.066 | 0.003906 | 0.09766 | -1 |
| 400 | reactive | 9 | -1.176 | -1.484 | -0.9042 | 0.003906 | 0.09766 | -1 |
| 400 | predictive | 9 | 0.129 | 0.06922 | 0.2034 | 0.003906 | 0.09766 | 1 |
| 400 | fixed_blend | 9 | 0.1173 | 0.05512 | 0.197 | 0.003906 | 0.09766 | 1 |
| 400 | fixed_blend_0.5 | 9 | -0.3098 | -0.4499 | -0.1958 | 0.003906 | 0.09766 | -1 |
| 400 | kalman | 9 | -1.721 | -2.325 | -1.16 | 0.003906 | 0.09766 | -1 |
| 500 | reactive | 9 | -1.212 | -1.574 | -0.901 | 0.003906 | 0.09766 | -1 |
| 500 | predictive | 9 | 0.1281 | 0.06647 | 0.208 | 0.003906 | 0.09766 | 1 |
| 500 | fixed_blend | 9 | 0.1217 | 0.05813 | 0.2025 | 0.003906 | 0.09766 | 1 |
| 500 | fixed_blend_0.5 | 9 | -0.3032 | -0.4514 | -0.1882 | 0.003906 | 0.09766 | -1 |
| 500 | kalman | 9 | -1.876 | -2.552 | -1.237 | 0.003906 | 0.09766 | -1 |
Holm-significant improvements of UA: 0; Holm-significant degradations: 0; total primary comparisons: 25. (n subjects = 9; low power if small.)

## Failure-warning ROC-AUC (predictive controller; pooled windows, subject-bootstrap CI in failure_prediction_metrics.csv)
| delay_ms | abs_velocity | forecast_magnitude | last_forecast_error | sigma_aleatoric | sigma_epistemic | sigma_total |
|---|---|---|---|---|---|---|
| 100 | 0.8883 | 0.8017 | 0.6438 | 0.6714 | 0.7063 | 0.6868 |
| 200 | 0.7381 | 0.7708 | 0.6475 | 0.6488 | 0.6959 | 0.6561 |
| 300 | 0.6594 | 0.7153 | 0.6547 | 0.6489 | 0.6778 | 0.6524 |
| 400 | 0.6284 | 0.6767 | 0.6395 | 0.6447 | 0.6524 | 0.6464 |
| 500 | 0.62 | 0.6468 | 0.6251 | 0.6471 | 0.6388 | 0.6481 |
σ_total AUC exceeds |velocity| AUC at 40% of delays; see paired subject-level tests (family exploratory_auc) before concluding anything.

## Distribution-shift findings
| group | n_subjects | mae | mae_lo | mae_hi | mean_sigma | picp95 |
|---|---|---|---|---|---|---|
| held_out_infant | 9 | 0.5014 | 0.3556 | 0.7222 | 0.5548 | 0.8913 |

## Experiment status
* dataset_inventory: RUN
* unit_tests_preprocessing: RUN
* forecasting_models: RUN
* forecast_evaluation: RUN
* uncertainty_calibration: RUN
* distribution_shift: NOT RUN: only one evaluation group present ([np.str_('held_out_infant')]); see held-out-subject results above
* synthetic_target: RUN
* robot_sinusoid_validation: RUN
* controllers_primary: RUN
* tracking_metrics: RUN
* failure_prediction: RUN
* failure_curves: RUN
* statistics: RUN
* ablation: RUN
* figures_tables: RUN

## Negative / null results to check
* Compare UA vs predictive/fixed-blend rows above: if p_holm ≥ 0.05 or the CI spans 0, UA did not demonstrably improve tracking in this run.
* If σ AUC ≤ velocity AUC, uncertainty was not a better failure warning than a trivial baseline.
* Coverage gaps (PICP95 − 0.95) quantify miscalibration under shift.

## Known limitations
See limitations_and_assumptions.md. Simulation only; surrogate waveform; small cohorts; segments selected for compute; no physical validation.