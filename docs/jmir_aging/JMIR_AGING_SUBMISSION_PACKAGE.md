# JMIR Aging Submission Package

## Scope

This document provides a practical submission package for JMIR Aging based on the current repository and privacy constraints.

## Core Positioning

- Manuscript type candidate: model development and validation study in aging-focused digital health.
- Population context: older adults with delirium risk trajectories.
- Technical novelty: leakage-free split, TimeGAN plus DTW-SMOTE augmentation, and soft-gated multi-task prediction.

## Repository Evidence for Methods and Reproducibility

- Methods-to-code traceability: see docs/MANUSCRIPT_CODE_MAPPING.md.
- Pipeline overview: see docs/PIPELINE.md.
- Public release guardrails: see docs/GITHUB_RELEASE_CHECKLIST.md.

## Required Submission Blocks (Draft-Ready)

1. Data availability statement
   - Use template in docs/jmir_aging/JMIR_DATA_AVAILABILITY_TEMPLATE.md.

2. Ethics approval and consent statement
   - Use template in docs/jmir_aging/JMIR_ETHICS_STATEMENT_TEMPLATE.md.

3. Reporting guideline declaration
   - Use template in docs/jmir_aging/JMIR_REPORTING_CHECKLIST_TEMPLATE.md.

## Suggested Main Manuscript Structure

- Title and abstract
- Introduction
- Methods
- Results
- Discussion
- Data availability
- Ethics statement
- Conflicts of interest
- Abbreviations
- References

## Methods Section Mapping

- Data construction and leakage control: src/augmentation.py
- Patient-level split and augmentation: run_stage_01_augmentation.py
- Tensor conversion and scaling policy: src/tensor_prep.py
- Model architecture: src/models.py
- Training and internal validation: src/train.py
- Performance metrics and calibration: src/evaluate.py
- Fidelity/statistical analysis: src/fidelity.py

## Privacy-Safe Transparency Statement

Use wording aligned with institutional policy:

"The source clinical dataset contains sensitive personal information and cannot be publicly shared. The repository provides complete executable analysis code, including preprocessing, augmentation, modeling, and evaluation. Publicly shared artifacts are de-identified and approved according to institutional policy."

## Pre-Submission Verification

- Confirm no raw clinical source files are tracked.
- Confirm no direct or indirect identifiers remain in outputs.
- Confirm repository URLs and author metadata are finalized in CITATION.cff.
- Confirm all scripts execute in a clean environment.

## Final Notes

- Re-check current JMIR Aging author requirements at submission time in case forms or declarations change.
- Keep this package as supplementary text source, and copy edited content into the journal submission system.
