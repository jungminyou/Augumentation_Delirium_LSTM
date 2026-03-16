# GitHub Release Checklist

## Before Public Release

- Confirm manuscript author approval for open-source publication.
- Remove all personal or direct patient identifiers.
- Ensure data license allows redistribution.
- Replace local absolute paths with configurable relative paths.
- Confirm no proprietary model weights are included unintentionally.
- Confirm raw clinical source tables are excluded from commit history.
- Confirm only de-identified and institutionally approved artifacts are included.
- Verify no hidden identifiers remain in outputs (PID mappings, timestamps, notes, free text).
- Re-scan tracked files for sensitive keywords before push.

## Code Hygiene

- Run lint/format checks.
- Verify scripts run from clean environment.
- Validate `requirements.txt` is complete.
- Add clear error messages for missing files.

## Documentation

- Ensure `README.md` has setup, run, and output descriptions.
- Add method summary aligned with manuscript sections.
- Add citation information and license.

## Repository Settings

- Add `.gitignore` to avoid committing large artifacts.
- Use release tags (for example `v1.0.0`).
- Add issue templates and contribution guide if needed.

## Recommended Extras

- Provide a minimal synthetic sample dataset for smoke tests.
- Add CI workflow for basic import and unit checks.

## Suggested Final Gate (Private Data)

- Run a final pre-push review with at least two reviewers.
- Archive internal full-data analysis in a private storage location only.
- Publish a short data-availability statement describing privacy restrictions.
