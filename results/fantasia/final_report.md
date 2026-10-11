# Final report — Fantasia (full mode, run full_20261010_200436)

* Subjects analysed: 40; records analysed: 40; test subjects: 24; folds: 1.
* Exclusions: 0 (none). Records not selected by configuration: 0.

## Final forecasting model per horizon — SELECTED ON VALIDATION (val_sel MAE), test results of that model
| horizon_ms | model | val_mae | n_subjects | mae | mae_lo | mae_hi | rmse | rmse_lo | rmse_hi |
|---|---|---|---|---|---|---|---|---|---|
| 100 | ridge | 0.01005 | 24 | 0.0105 | 0.008861 | 0.01248 | 0.01821 | 0.01415 | 0.02293 |
| 200 | ridge | 0.04505 | 24 | 0.04421 | 0.03696 | 0.05291 | 0.07636 | 0.05955 | 0.09667 |
| 300 | ensemble | 0.1019 | 24 | 0.1009 | 0.07988 | 0.1271 | 0.1905 | 0.143 | 0.247 |
| 400 | ensemble | 0.1643 | 24 | 0.1574 | 0.1237 | 0.1988 | 0.2758 | 0.2136 | 0.3505 |
| 500 | tcn_prob | 0.2217 | 24 | 0.2078 | 0.1652 | 0.2583 | 0.3498 | 0.2755 | 0.4378 |

## All models on the test set (descriptive; NOT used for selection)
| model | horizon_ms | n_subjects | mae | mae_lo | mae_hi | rmse |
|---|---|---|---|---|---|---|
| ensemble | 100 | 24 | 0.01418 | 0.01037 | 0.01921 | 0.04228 |
| ensemble | 200 | 24 | 0.04853 | 0.03829 | 0.0622 | 0.1065 |
| ensemble | 300 | 24 | 0.1009 | 0.07988 | 0.1271 | 0.1905 |
| ensemble | 400 | 24 | 0.1574 | 0.1237 | 0.1988 | 0.2758 |
| ensemble | 500 | 24 | 0.2094 | 0.1634 | 0.2672 | 0.35 |
| kalman | 100 | 24 | 0.03119 | 0.02541 | 0.0379 | 0.05386 |
| kalman | 200 | 24 | 0.09615 | 0.07771 | 0.1173 | 0.1635 |
| kalman | 300 | 24 | 0.1863 | 0.1494 | 0.2284 | 0.3087 |
| kalman | 400 | 24 | 0.2941 | 0.2346 | 0.3611 | 0.472 |
| kalman | 500 | 24 | 0.4157 | 0.3299 | 0.5127 | 0.6455 |
| lstm_prob | 100 | 24 | 0.01552 | 0.01137 | 0.021 | 0.04518 |
| lstm_prob | 200 | 24 | 0.05135 | 0.04013 | 0.06613 | 0.1133 |
| lstm_prob | 300 | 24 | 0.1044 | 0.08259 | 0.1316 | 0.1987 |
| lstm_prob | 400 | 24 | 0.1624 | 0.1277 | 0.2045 | 0.2865 |
| lstm_prob | 500 | 24 | 0.2153 | 0.1687 | 0.2736 | 0.3602 |
| persistence | 100 | 24 | 0.1184 | 0.09226 | 0.1483 | 0.1675 |
| persistence | 200 | 24 | 0.2339 | 0.1823 | 0.2931 | 0.3273 |
| persistence | 300 | 24 | 0.3446 | 0.2684 | 0.4319 | 0.4748 |
| persistence | 400 | 24 | 0.4499 | 0.3498 | 0.564 | 0.6092 |
| persistence | 500 | 24 | 0.5496 | 0.4269 | 0.6889 | 0.7327 |
| ridge | 100 | 24 | 0.0105 | 0.008861 | 0.01248 | 0.01821 |
| ridge | 200 | 24 | 0.04421 | 0.03696 | 0.05291 | 0.07636 |
| ridge | 300 | 24 | 0.09955 | 0.08207 | 0.1197 | 0.1691 |
| ridge | 400 | 24 | 0.1646 | 0.1346 | 0.1993 | 0.2717 |
| ridge | 500 | 24 | 0.229 | 0.1849 | 0.2803 | 0.3646 |
| tcn_det | 100 | 24 | 0.02232 | 0.01791 | 0.02787 | 0.03864 |
| tcn_det | 200 | 24 | 0.06272 | 0.05046 | 0.07792 | 0.1087 |
| tcn_det | 300 | 24 | 0.1125 | 0.09011 | 0.1396 | 0.1916 |
| tcn_det | 400 | 24 | 0.1633 | 0.1304 | 0.2039 | 0.2697 |
| tcn_det | 500 | 24 | 0.209 | 0.1654 | 0.2615 | 0.3364 |
| tcn_prob | 100 | 24 | 0.0174 | 0.0144 | 0.02125 | 0.03225 |
| tcn_prob | 200 | 24 | 0.05655 | 0.04632 | 0.06924 | 0.1037 |
| tcn_prob | 300 | 24 | 0.1082 | 0.08756 | 0.133 | 0.1952 |
| tcn_prob | 400 | 24 | 0.1606 | 0.1286 | 0.1985 | 0.281 |
| tcn_prob | 500 | 24 | 0.2078 | 0.1652 | 0.2583 | 0.3498 |

## Uncertainty calibration
Mean |PICP95 − 0.95| over horizons (Gaussian intervals): {'lstm_prob': 0.005, 'tcn_prob': 0.007, 'ensemble': 0.008}. Best-calibrated Gaussian method: **lstm_prob**.
Conformal 95% empirical coverage (mean over horizons/subjects): {'conf_abs_5_picp': {'ensemble': 0.958, 'lstm_prob': 0.959, 'persistence': 0.961, 'ridge': 0.957, 'tcn_prob': 0.96}, 'conf_norm_5_picp': {'ensemble': 0.951, 'lstm_prob': 0.951, 'persistence': nan, 'ridge': nan, 'tcn_prob': 0.95}}
Ensemble σ vs |error| Spearman across subject-horizons: mean 0.351 (min 0.166, max 0.545).

## Controller SELECTED ON VALIDATION per delay, with its TEST tracking (SIMULATION, subject-mean, mm)
| controller | delay_ms | val_rmse | val_mae | rmse | rmse_lo | rmse_hi | mae | fail_rate | cmd_var | sat_rate | cons_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| reactive | 0 | 2.109 | 1.597 | 1.642 | 1.272 | 2.071 | 1.214 | 0.4075 | 0.2969 | 0.001777 | nan |
| predictive | 100 | 2.144 | 1.611 | 1.689 | 1.303 | 2.137 | 1.232 | 0.4091 | 0.3081 | 0.001806 | nan |
| fixed_blend | 200 | 2.23 | 1.652 | 1.789 | 1.371 | 2.271 | 1.275 | 0.4142 | 0.3461 | 0.001653 | nan |
| predictive | 300 | 2.41 | 1.738 | 1.973 | 1.496 | 2.53 | 1.364 | 0.4255 | 0.3835 | 0.001488 | nan |
| fixed_blend | 400 | 2.656 | 1.867 | 2.207 | 1.657 | 2.85 | 1.493 | 0.4439 | 0.3985 | 0.001315 | nan |
| predictive | 500 | 2.901 | 1.998 | 2.428 | 1.81 | 3.148 | 1.626 | 0.4631 | 0.3977 | 0.001142 | nan |
* TEST mean RMSE of **uncertainty_aware** is lower than predictive at 0/5 delays (point estimates only; see paired subject-level tests below). If this is 0, the candidate LOSES to predictive-only control and that is the finding.
* TEST mean RMSE of **ua_rate** is lower than predictive at 0/5 delays (point estimates only; see paired subject-level tests below). If this is 0, the candidate LOSES to predictive-only control and that is the finding.
* TEST mean RMSE of **ua_trigger** is lower than predictive at 0/5 delays (point estimates only; see paired subject-level tests below). If this is 0, the candidate LOSES to predictive-only control and that is the finding.

## Full test comparison, all controllers (descriptive, not used for selection)
| controller | delay_ms | rmse | rmse_lo | rmse_hi | mae | max_abs | fail_rate | cmd_var | sat_rate | cons_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| fixed_blend | 100 | 1.689 | 1.303 | 2.137 | 1.232 | 20.16 | 0.4091 | 0.3081 | 0.001806 | nan |
| fixed_blend | 200 | 1.789 | 1.371 | 2.271 | 1.275 | 22.94 | 0.4142 | 0.3461 | 0.001653 | nan |
| fixed_blend | 300 | 1.973 | 1.496 | 2.53 | 1.364 | 25.81 | 0.4255 | 0.3835 | 0.001488 | nan |
| fixed_blend | 400 | 2.207 | 1.657 | 2.85 | 1.493 | 27.95 | 0.4439 | 0.3985 | 0.001315 | nan |
| fixed_blend | 500 | 2.428 | 1.81 | 3.148 | 1.626 | 28.78 | 0.4631 | 0.3977 | 0.001142 | nan |
| fixed_blend_0.5 | 100 | 2.002 | 1.553 | 2.521 | 1.484 | 21.74 | 0.4857 | 0.2975 | 0.001784 | nan |
| fixed_blend_0.5 | 200 | 2.359 | 1.829 | 2.97 | 1.751 | 25.06 | 0.5458 | 0.3024 | 0.001682 | nan |
| fixed_blend_0.5 | 300 | 2.722 | 2.104 | 3.435 | 2.018 | 27.77 | 0.5911 | 0.3067 | 0.001574 | nan |
| fixed_blend_0.5 | 400 | 3.075 | 2.363 | 3.898 | 2.281 | 29.69 | 0.6273 | 0.3034 | 0.001449 | nan |
| fixed_blend_0.5 | 500 | 3.393 | 2.59 | 4.322 | 2.522 | 30.72 | 0.656 | 0.2933 | 0.001364 | nan |
| kalman | 100 | 1.695 | 1.318 | 2.131 | 1.241 | 19.41 | 0.4134 | 0.3206 | 0.001923 | nan |
| kalman | 200 | 1.901 | 1.493 | 2.37 | 1.361 | 22.85 | 0.4395 | 0.3724 | 0.002377 | nan |
| kalman | 300 | 2.286 | 1.797 | 2.831 | 1.622 | 26.65 | 0.4982 | 0.4467 | 0.003154 | nan |
| kalman | 400 | 2.814 | 2.228 | 3.473 | 2.028 | 29.94 | 0.5793 | 0.5345 | 0.004616 | nan |
| kalman | 500 | 3.444 | 2.736 | 4.241 | 2.541 | 32.37 | 0.6575 | 0.63 | 0.006792 | nan |
| predictive | 100 | 1.689 | 1.303 | 2.137 | 1.232 | 20.16 | 0.4091 | 0.3081 | 0.001806 | nan |
| predictive | 200 | 1.789 | 1.371 | 2.271 | 1.275 | 22.94 | 0.4142 | 0.3461 | 0.001653 | nan |
| predictive | 300 | 1.973 | 1.496 | 2.53 | 1.364 | 25.81 | 0.4255 | 0.3835 | 0.001488 | nan |
| predictive | 400 | 2.207 | 1.657 | 2.85 | 1.493 | 27.95 | 0.4439 | 0.3985 | 0.001315 | nan |
| predictive | 500 | 2.428 | 1.81 | 3.148 | 1.626 | 28.78 | 0.4631 | 0.3977 | 0.001142 | nan |
| reactive | 0 | 1.642 | 1.272 | 2.071 | 1.214 | 18.2 | 0.4075 | 0.2969 | 0.001777 | nan |
| reactive | 100 | 2.321 | 1.812 | 2.904 | 1.737 | 23.48 | 0.5466 | 0.2969 | 0.001777 | nan |
| reactive | 200 | 2.965 | 2.315 | 3.703 | 2.241 | 27.8 | 0.6335 | 0.2969 | 0.001777 | nan |
| reactive | 300 | 3.562 | 2.778 | 4.452 | 2.718 | 30.51 | 0.6937 | 0.2969 | 0.001777 | nan |
| reactive | 400 | 4.113 | 3.201 | 5.145 | 3.168 | 32.56 | 0.7378 | 0.2969 | 0.001777 | nan |
| reactive | 500 | 4.618 | 3.585 | 5.784 | 3.587 | 34.39 | 0.7703 | 0.2969 | 0.001777 | nan |
| ua_rate | 100 | 1.702 | 1.313 | 2.151 | 1.233 | 21.52 | 0.4091 | 0.3075 | 0.001775 | 0.0004598 |
| ua_rate | 200 | 1.803 | 1.379 | 2.29 | 1.278 | 23.55 | 0.4142 | 0.3449 | 0.001588 | 0.001172 |
| ua_rate | 300 | 1.986 | 1.503 | 2.552 | 1.368 | 25.91 | 0.4256 | 0.3815 | 0.001396 | 0.001841 |
| ua_rate | 400 | 2.218 | 1.663 | 2.869 | 1.497 | 27.73 | 0.444 | 0.396 | 0.001203 | 0.002142 |
| ua_rate | 500 | 2.437 | 1.814 | 3.165 | 1.63 | 28.62 | 0.4631 | 0.3953 | 0.001043 | 0.002075 |
| ua_trigger | 100 | 1.702 | 1.313 | 2.151 | 1.233 | 21.52 | 0.4091 | 0.3075 | 0.001775 | 0 |
| ua_trigger | 200 | 1.803 | 1.379 | 2.29 | 1.278 | 23.55 | 0.4142 | 0.3449 | 0.001588 | 0 |
| ua_trigger | 300 | 1.986 | 1.503 | 2.552 | 1.368 | 25.91 | 0.4256 | 0.3815 | 0.001396 | 0 |
| ua_trigger | 400 | 2.218 | 1.663 | 2.869 | 1.497 | 27.73 | 0.444 | 0.396 | 0.001203 | 0 |
| ua_trigger | 500 | 2.437 | 1.814 | 3.165 | 1.63 | 28.62 | 0.4631 | 0.3953 | 0.001043 | 0 |
| uncertainty_aware | 100 | 1.862 | 1.414 | 2.39 | 1.336 | 22.62 | 0.4287 | 0.3022 | 0.001777 | nan |
| uncertainty_aware | 200 | 2.073 | 1.549 | 2.69 | 1.454 | 25.59 | 0.4483 | 0.3247 | 0.001741 | nan |
| uncertainty_aware | 300 | 2.305 | 1.713 | 3.022 | 1.589 | 27.48 | 0.4673 | 0.3485 | 0.00167 | nan |
| uncertainty_aware | 400 | 2.558 | 1.885 | 3.384 | 1.743 | 29.16 | 0.4874 | 0.3576 | 0.001582 | nan |
| uncertainty_aware | 500 | 2.792 | 2.042 | 3.717 | 1.891 | 30.19 | 0.5056 | 0.3552 | 0.001484 | nan |

## Uncertainty-aware blend vs comparators (RMSE difference, negative favours UA)
| delay_ms | b | n | mean_diff | ci_lo | ci_hi | p_raw | p_holm | effect_rank_biserial |
|---|---|---|---|---|---|---|---|---|
| 100 | reactive | 24 | -0.4585 | -0.5297 | -0.3824 | 1.192e-07 | 2.98e-06 | -1 |
| 100 | predictive | 24 | 0.173 | 0.1089 | 0.257 | 1.192e-07 | 2.98e-06 | 1 |
| 100 | fixed_blend | 24 | 0.173 | 0.1089 | 0.257 | 1.192e-07 | 2.98e-06 | 1 |
| 100 | fixed_blend_0.5 | 24 | -0.1397 | -0.1736 | -0.1084 | 2.384e-07 | 2.98e-06 | -0.9933 |
| 100 | kalman | 24 | 0.1675 | 0.09522 | 0.2679 | 1.192e-07 | 2.98e-06 | 1 |
| 200 | reactive | 24 | -0.8917 | -1.038 | -0.7378 | 1.192e-07 | 2.98e-06 | -1 |
| 200 | predictive | 24 | 0.284 | 0.179 | 0.4249 | 1.192e-07 | 2.98e-06 | 1 |
| 200 | fixed_blend | 24 | 0.284 | 0.179 | 0.4249 | 1.192e-07 | 2.98e-06 | 1 |
| 200 | fixed_blend_0.5 | 24 | -0.2864 | -0.3445 | -0.2372 | 1.192e-07 | 2.98e-06 | -1 |
| 200 | kalman | 24 | 0.1716 | 0.06054 | 0.3251 | 0.01641 | 0.03281 | 0.5533 |
| 300 | reactive | 24 | -1.258 | -1.47 | -1.035 | 1.192e-07 | 2.98e-06 | -1 |
| 300 | predictive | 24 | 0.3317 | 0.2073 | 0.4942 | 1.192e-07 | 2.98e-06 | 1 |
| 300 | fixed_blend | 24 | 0.3317 | 0.2073 | 0.4942 | 1.192e-07 | 2.98e-06 | 1 |
| 300 | fixed_blend_0.5 | 24 | -0.4167 | -0.4943 | -0.3505 | 1.192e-07 | 2.98e-06 | -1 |
| 300 | kalman | 24 | 0.01901 | -0.1074 | 0.1996 | 0.2182 | 0.2182 | -0.2933 |
| 400 | reactive | 24 | -1.555 | -1.823 | -1.284 | 1.192e-07 | 2.98e-06 | -1 |
| 400 | predictive | 24 | 0.3511 | 0.2169 | 0.5197 | 1.192e-07 | 2.98e-06 | 1 |
| 400 | fixed_blend | 24 | 0.3511 | 0.2169 | 0.5197 | 1.192e-07 | 2.98e-06 | 1 |
| 400 | fixed_blend_0.5 | 24 | -0.5166 | -0.6104 | -0.4334 | 1.192e-07 | 2.98e-06 | -1 |
| 400 | kalman | 24 | -0.2556 | -0.4024 | -0.06117 | 0.002001 | 0.006003 | -0.6933 |
| 500 | reactive | 24 | -1.827 | -2.144 | -1.511 | 1.192e-07 | 2.98e-06 | -1 |
| 500 | predictive | 24 | 0.3635 | 0.2228 | 0.5426 | 2.384e-07 | 2.98e-06 | 0.9933 |
| 500 | fixed_blend | 24 | 0.3635 | 0.2228 | 0.5426 | 2.384e-07 | 2.98e-06 | 0.9933 |
| 500 | fixed_blend_0.5 | 24 | -0.6009 | -0.7095 | -0.5015 | 1.192e-07 | 2.98e-06 | -1 |
| 500 | kalman | 24 | -0.6528 | -0.8425 | -0.4581 | 3.016e-05 | 0.0001206 | -0.88 |

## NEW constrained candidates vs predictive/reactive (RMSE difference, negative favours the candidate; Holm-corrected within family)
| delay_ms | a | b | n | mean_diff | ci_lo | ci_hi | p_raw | p_holm | effect_rank_biserial | cohens_dz |
|---|---|---|---|---|---|---|---|---|---|---|
| 100 | ua_rate | predictive | 24 | 0.01223 | 0.002835 | 0.02507 | 1.633e-05 | 0.0001633 | 0.9 | 0.4444 |
| 100 | ua_rate | reactive | 24 | -0.6192 | -0.7623 | -0.4926 | 1.192e-07 | 3.576e-06 | -1 | -1.802 |
| 100 | ua_trigger | predictive | 24 | 0.01223 | 0.002835 | 0.02507 | 1.633e-05 | 0.0001633 | 0.9 | 0.4444 |
| 100 | ua_trigger | reactive | 24 | -0.6192 | -0.7623 | -0.4926 | 1.192e-07 | 3.576e-06 | -1 | -1.802 |
| 100 | uncertainty_aware | predictive | 24 | 0.173 | 0.1089 | 0.257 | 1.192e-07 | 3.576e-06 | 1 | 0.9096 |
| 100 | uncertainty_aware | reactive | 24 | -0.4585 | -0.5297 | -0.3824 | 1.192e-07 | 3.576e-06 | -1 | -2.388 |
| 200 | ua_rate | predictive | 24 | 0.01375 | 0.003919 | 0.02746 | 0.0008463 | 0.005078 | 0.74 | 0.4514 |
| 200 | ua_rate | reactive | 24 | -1.162 | -1.425 | -0.9278 | 1.192e-07 | 3.576e-06 | -1 | -1.819 |
| 200 | ua_trigger | predictive | 24 | 0.01375 | 0.003919 | 0.02746 | 0.0008463 | 0.005078 | 0.74 | 0.4514 |
| 200 | ua_trigger | reactive | 24 | -1.162 | -1.425 | -0.9278 | 1.192e-07 | 3.576e-06 | -1 | -1.819 |
| 200 | uncertainty_aware | predictive | 24 | 0.284 | 0.179 | 0.4249 | 1.192e-07 | 3.576e-06 | 1 | 0.9125 |
| 200 | uncertainty_aware | reactive | 24 | -0.8917 | -1.038 | -0.7378 | 1.192e-07 | 3.576e-06 | -1 | -2.284 |
| 300 | ua_rate | predictive | 24 | 0.01323 | 0.002156 | 0.02696 | 0.0001496 | 0.001197 | 0.82 | 0.4115 |
| 300 | ua_rate | reactive | 24 | -1.576 | -1.936 | -1.264 | 1.192e-07 | 3.576e-06 | -1 | -1.838 |
| 300 | ua_trigger | predictive | 24 | 0.01323 | 0.002156 | 0.02696 | 0.0001496 | 0.001197 | 0.82 | 0.4115 |
| 300 | ua_trigger | reactive | 24 | -1.576 | -1.936 | -1.264 | 1.192e-07 | 3.576e-06 | -1 | -1.838 |
| 300 | uncertainty_aware | predictive | 24 | 0.3317 | 0.2073 | 0.4942 | 1.192e-07 | 3.576e-06 | 1 | 0.9151 |
| 300 | uncertainty_aware | reactive | 24 | -1.258 | -1.47 | -1.035 | 1.192e-07 | 3.576e-06 | -1 | -2.224 |
| 400 | ua_rate | predictive | 24 | 0.01108 | 0.0004485 | 0.02365 | 0.00158 | 0.005078 | 0.7067 | 0.3873 |
| 400 | ua_rate | reactive | 24 | -1.895 | -2.309 | -1.524 | 1.192e-07 | 3.576e-06 | -1 | -1.859 |
| 400 | ua_trigger | predictive | 24 | 0.01108 | 0.0004485 | 0.02365 | 0.00158 | 0.005078 | 0.7067 | 0.3873 |
| 400 | ua_trigger | reactive | 24 | -1.895 | -2.309 | -1.524 | 1.192e-07 | 3.576e-06 | -1 | -1.859 |
| 400 | uncertainty_aware | predictive | 24 | 0.3511 | 0.2169 | 0.5197 | 1.192e-07 | 3.576e-06 | 1 | 0.9117 |
| 400 | uncertainty_aware | reactive | 24 | -1.555 | -1.823 | -1.284 | 1.192e-07 | 3.576e-06 | -1 | -2.209 |
| 500 | ua_rate | predictive | 24 | 0.008822 | 0.0008357 | 0.01882 | 0.001238 | 0.005078 | 0.72 | 0.387 |
| 500 | ua_rate | reactive | 24 | -2.181 | -2.648 | -1.753 | 1.192e-07 | 3.576e-06 | -1 | -1.854 |
| 500 | ua_trigger | predictive | 24 | 0.008822 | 0.0008357 | 0.01882 | 0.001238 | 0.005078 | 0.72 | 0.387 |
| 500 | ua_trigger | reactive | 24 | -2.181 | -2.648 | -1.753 | 1.192e-07 | 3.576e-06 | -1 | -1.854 |
| 500 | uncertainty_aware | predictive | 24 | 0.3635 | 0.2228 | 0.5426 | 2.384e-07 | 3.576e-06 | 0.9933 | 0.8821 |
| 500 | uncertainty_aware | reactive | 24 | -1.827 | -2.144 | -1.511 | 1.192e-07 | 3.576e-06 | -1 | -2.195 |
Holm-significant improvements of UA: 12; Holm-significant degradations: 12; total primary comparisons: 25. (n subjects = 24; low power if small.)

## Per-group paired comparisons (UA minus comparator, RMSE mm; separate Holm family per group)
| family | delay_ms | b | n | mean_diff | ci_lo | ci_hi | p_raw | p_holm |
|---|---|---|---|---|---|---|---|---|
| group:in_dist_young_test | 100 | predictive | 4 | 0.2065 | 0.0836 | 0.4027 | nan | nan |
| group:in_dist_young_test | 100 | fixed_blend | 4 | 0.2065 | 0.0836 | 0.4027 | nan | nan |
| group:in_dist_young_test | 100 | predictive | 4 | 0.0444 | 0.0005386 | 0.08838 | nan | nan |
| group:in_dist_young_test | 100 | predictive | 4 | 0.0444 | 0.0005386 | 0.08838 | nan | nan |
| group:in_dist_young_test | 200 | predictive | 4 | 0.3447 | 0.1185 | 0.6852 | nan | nan |
| group:in_dist_young_test | 200 | fixed_blend | 4 | 0.3447 | 0.1185 | 0.6852 | nan | nan |
| group:in_dist_young_test | 200 | predictive | 4 | 0.03231 | -0.003636 | 0.09711 | nan | nan |
| group:in_dist_young_test | 200 | predictive | 4 | 0.03231 | -0.003636 | 0.09711 | nan | nan |
| group:in_dist_young_test | 300 | predictive | 4 | 0.3997 | 0.1173 | 0.7987 | nan | nan |
| group:in_dist_young_test | 300 | fixed_blend | 4 | 0.3997 | 0.1173 | 0.7987 | nan | nan |
| group:in_dist_young_test | 300 | predictive | 4 | 0.02272 | -0.03336 | 0.09586 | nan | nan |
| group:in_dist_young_test | 300 | predictive | 4 | 0.02272 | -0.03336 | 0.09586 | nan | nan |
| group:in_dist_young_test | 400 | predictive | 4 | 0.4171 | 0.102 | 0.8377 | nan | nan |
| group:in_dist_young_test | 400 | fixed_blend | 4 | 0.4171 | 0.102 | 0.8377 | nan | nan |
| group:in_dist_young_test | 400 | predictive | 4 | 0.01686 | -0.03571 | 0.08013 | nan | nan |
| group:in_dist_young_test | 400 | predictive | 4 | 0.01686 | -0.03571 | 0.08013 | nan | nan |
| group:in_dist_young_test | 500 | predictive | 4 | 0.4142 | 0.06385 | 0.8578 | nan | nan |
| group:in_dist_young_test | 500 | fixed_blend | 4 | 0.4142 | 0.06385 | 0.8578 | nan | nan |
| group:in_dist_young_test | 500 | predictive | 4 | 0.01536 | -0.02511 | 0.06445 | nan | nan |
| group:in_dist_young_test | 500 | predictive | 4 | 0.01536 | -0.02511 | 0.06445 | nan | nan |
| group:shift_elderly_frozen | 100 | predictive | 20 | 0.1663 | 0.09794 | 0.2648 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 100 | fixed_blend | 20 | 0.1663 | 0.09794 | 0.2648 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 100 | predictive | 20 | 0.005796 | 0.0005203 | 0.01352 | 4.768e-05 | 0.0005722 |
| group:shift_elderly_frozen | 100 | predictive | 20 | 0.005796 | 0.0005203 | 0.01352 | 4.768e-05 | 0.0005722 |
| group:shift_elderly_frozen | 200 | predictive | 20 | 0.2719 | 0.161 | 0.4308 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 200 | fixed_blend | 20 | 0.2719 | 0.161 | 0.4308 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 200 | predictive | 20 | 0.01004 | 0.002802 | 0.01944 | 0.001017 | 0.006369 |
| group:shift_elderly_frozen | 200 | predictive | 20 | 0.01004 | 0.002802 | 0.01944 | 0.001017 | 0.006369 |
| group:shift_elderly_frozen | 300 | predictive | 20 | 0.3181 | 0.1882 | 0.5025 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 300 | fixed_blend | 20 | 0.3181 | 0.1882 | 0.5025 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 300 | predictive | 20 | 0.01133 | 0.003991 | 0.02053 | 2.67e-05 | 0.0003738 |
| group:shift_elderly_frozen | 300 | predictive | 20 | 0.01133 | 0.003991 | 0.02053 | 2.67e-05 | 0.0003738 |
| group:shift_elderly_frozen | 400 | predictive | 20 | 0.3378 | 0.2002 | 0.5393 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 400 | fixed_blend | 20 | 0.3378 | 0.2002 | 0.5393 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 400 | predictive | 20 | 0.00992 | 0.003463 | 0.01857 | 0.001017 | 0.006369 |
| group:shift_elderly_frozen | 400 | predictive | 20 | 0.00992 | 0.003463 | 0.01857 | 0.001017 | 0.006369 |
| group:shift_elderly_frozen | 500 | predictive | 20 | 0.3533 | 0.2052 | 0.5664 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 500 | fixed_blend | 20 | 0.3533 | 0.2052 | 0.5664 | 1.907e-06 | 5.722e-05 |
| group:shift_elderly_frozen | 500 | predictive | 20 | 0.007514 | 0.002422 | 0.01483 | 0.0007076 | 0.006369 |
| group:shift_elderly_frozen | 500 | predictive | 20 | 0.007514 | 0.002422 | 0.01483 | 0.0007076 | 0.006369 |

## Failure-warning ROC-AUC (predictive controller; pooled windows, subject-bootstrap CI in failure_prediction_metrics.csv)
| delay_ms | abs_velocity | forecast_magnitude | last_forecast_error | sigma_aleatoric | sigma_epistemic | sigma_total | vel_plus_sigma |
|---|---|---|---|---|---|---|---|
| 100 | 0.975 | 0.9331 | 0.6321 | 0.7394 | 0.693 | 0.742 | 0.9756 |
| 200 | 0.9491 | 0.9474 | 0.6534 | 0.7275 | 0.6966 | 0.7296 | 0.9509 |
| 300 | 0.8629 | 0.8993 | 0.6735 | 0.7274 | 0.7021 | 0.7281 | 0.877 |
| 400 | 0.7791 | 0.8402 | 0.6741 | 0.7318 | 0.6964 | 0.7321 | 0.8168 |
| 500 | 0.7123 | 0.7878 | 0.6538 | 0.7358 | 0.6929 | 0.7362 | 0.7756 |
σ_total AUC exceeds |velocity| AUC at 20% of delays; see paired subject-level tests (family exploratory_auc) before concluding anything.

## Distribution-shift findings (EXPLORATORY; young n=4 vs elderly n=20 test subjects; not causal, no significance claim for the small young group)
| group | n_subjects | mae | mae_lo | mae_hi | mean_sigma | picp95 |
|---|---|---|---|---|---|---|
| in_dist_young_test | 4 | 0.129 | 0.09358 | 0.1954 | 0.1763 | 0.9506 |
| shift_elderly_frozen | 20 | 0.09526 | 0.07237 | 0.1246 | 0.1343 | 0.9543 |

## Experiment status
* dataset_inventory: RUN
* provenance_verification: RUN
* unit_tests_preprocessing: RUN
* forecasting_models: RUN
* forecast_evaluation: RUN
* validation_model_selection: RUN
* uncertainty_calibration: RUN
* distribution_shift: RUN
* synthetic_target: RUN
* robot_sinusoid_validation: RUN
* controllers_primary: RUN
* tracking_metrics: RUN
* failure_prediction: RUN
* failure_curves: RUN
* statistics: RUN
* ablation: RUN
* sensitivity_actuator_tau: RUN
* sensitivity_measurement_noise: RUN
* figures_tables: RUN

## Negative / null results to check
* Compare UA vs predictive/fixed-blend rows above: if p_holm ≥ 0.05 or the CI spans 0, UA did not demonstrably improve tracking in this run.
* If σ AUC ≤ velocity AUC, uncertainty was not a better failure warning than a trivial baseline.
* Coverage gaps (PICP95 − 0.95) quantify miscalibration under shift.

## Known limitations
See limitations_and_assumptions.md. Simulation only; surrogate waveform; small cohorts; segments selected for compute; no physical validation.