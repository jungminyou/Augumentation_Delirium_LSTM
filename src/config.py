from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectConfig:
    base_dir: Path
    raw_longitudinal_csv: str = "250505_df_long.csv"
    train_augmented_csv: str = "260314_Train_Augmented_Final.csv"
    val_original_csv: str = "260314_Val_Original.csv"
    test_original_csv: str = "260314_Test_Original.csv"


def get_default_config() -> ProjectConfig:
    # `github_public_release` is expected to be placed inside the original project root.
    base_dir = Path(__file__).resolve().parents[2]
    return ProjectConfig(base_dir=base_dir)


def ensure_file_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
