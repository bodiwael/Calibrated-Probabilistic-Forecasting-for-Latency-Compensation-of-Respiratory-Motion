| setting | value |
|---|---|
| band_Hz | (0.1, 2.0) |
| filter | Butterworth order 4 (x2 for bandpass), SOS, causal sosfilt |
| fs_model_Hz | 20 |
| resample | zero-order hold (causal) |
| max_gap_s | 0.25 |
| flatline_s | 2 |
| warmup_s | 10 |
| normalisation | train-subject mean/std per fold |
| history/horizons | 100 samples / [100, 200, 300, 400, 500] ms |