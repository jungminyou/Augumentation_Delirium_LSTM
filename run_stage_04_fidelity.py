import pandas as pd

from src.config import get_default_config
from src.fidelity import (
    compute_distance_metrics,
    compute_jsd_table,
    run_pairwise_statistics,
    run_tsne_pairwise,
    save_tsne_pairwise_figure,
)


if __name__ == "__main__":
    cfg = get_default_config()
    train_aug_df = pd.read_csv(cfg.base_dir / "260314_Train_Augmented_Final.csv")

    cont_features = [
        "GDS", "FRAIL", "ADL", "IADL", "MNA", "BMI", "age",
        "op_level2", "anesthesia_duration", "op_duration", "ASAscore", "CCI", "V1MMSE",
    ]
    cat_features = ["sex", "edu"]
    excluded_cols = {
        "pid",
        "time",
        "Dataset_Type",
        "delirium",
        "delirium_next_day",
        "delirium_typ",
        "K-DRS-R-98",
    }
    feature_cols = [c for c in train_aug_df.columns if c not in excluded_cols]

    stats_df = run_pairwise_statistics(train_aug_df, cont_features, cat_features)
    jsd_df = compute_jsd_table(train_aug_df, cont_features, cat_features)
    dist_df = compute_distance_metrics(train_aug_df, feature_cols)
    tsne_result = run_tsne_pairwise(train_aug_df, feature_cols, perplexity=30)
    save_tsne_pairwise_figure(tsne_result, str(cfg.base_dir / "tSNE_Pairwise_Comparison_Vivid.png"))

    stats_df.to_csv(cfg.base_dir / "statistical_comparison_pairwise_genuine.csv", index=False)
    jsd_df.to_csv(cfg.base_dir / "js_divergence_results.csv", index=False)
    dist_df.to_csv(cfg.base_dir / "distance_metrics_separated.csv", index=False)

    print("Stage 04 completed: fidelity tables and t-SNE figure saved.")
