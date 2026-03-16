# Pipeline Documentation

## Stage 1: Data Loading and Leakage Prevention
- Load longitudinal table from csv file.
- Drop leakage-prone columns (for example `CAM_diagnosis`).
- Define dynamic features, static features, and output labels.

## Stage 2: Patient-Level Split
- Split by patient identifier (`pid`) into train/validation/test.
- Do not split by rows to avoid temporal or patient leakage.

## Stage 3: Minority Sequence Augmentation
- Build 3D dynamic + static sequence tensors.
- Extract minority class trajectories (`delirium == 1`).
- Train TimeGAN on minority trajectories.
- Generate synthetic trajectories using:
  - TimeGAN sampling.
  - DTW-SMOTE interpolation.
- Enforce original value range and integer category constraints.
- Rebuild tabular dataframe with sampled real label trajectories.

## Stage 4: Tensor Preparation and Scaling
- Convert dataframes to `(N, T, F)` tensors.
- Fit scaler only on original train features.
- Transform validation/test and synthetic tensors with the same scaler.

## Stage 5: Model Training
- Baseline: logistic regression with soft gating logic.
- Deep models: soft-gated multi-task LSTM.
  - Model A: original train only.
  - Model B: original + DTW-SMOTE.
  - Model C: original + TimeGAN.

## Stage 6: Evaluation
- Compute AUROC and AUPRC with bootstrap confidence intervals.
- Compute calibration metrics (Brier score, slope, intercept).
- Perform Decision Curve Analysis (net benefit).
- Save performance tables and publication-ready figures.

## Stage 7: Fidelity Analysis
- Pairwise statistical tests:
  - Original anchor uses genuine delirium subgroup (`Original_Train` with `delirium == 1`).
  - Continuous features: Mann-Whitney U test.
  - Categorical features: chi-square test.
- Distribution similarity:
  - Jensen-Shannon divergence.
- Sequence-level distance:
  - DTW and Wasserstein distance.
- Visualization:
  - Pairwise t-SNE plots.

## Outputs
- Augmented and split csv files.
- Model metrics tables.
- Plot images for performance and fidelity.
- Intermediate numpy arrays and optional model checkpoints.
