import pandas as pd

from src.augmentation import run_augmentation_pipeline
from src.config import get_default_config
from src.evaluate import evaluate_multi_class, prepare_occurrence_probabilities
from src.tensor_prep import build_scaled_tensors
from src.train import train_all_models


if __name__ == "__main__":
    cfg = get_default_config()
    aug = run_augmentation_pipeline(base_dir=cfg.base_dir, seed=42, timegan_epochs=500)

    tensors = build_scaled_tensors(
        df_train=aug.df_train,
        df_val=aug.df_val,
        df_test=aug.df_test,
        df_tg=aug.df_tg,
        df_sm=aug.df_sm,
        feature_cols=aug.all_feature_cols,
        label_cols=aug.label_cols,
        time_steps=aug.time_steps,
    )

    preds_next, preds_typ, preds_kdr = train_all_models(tensors, lstm_epochs=300, batch_size=32)

    y_true_next = tensors["Y_val"][..., 1].ravel().astype(int)
    y_true_typ = tensors["Y_val"][..., 2].ravel().astype(int)
    y_true_kdr = tensors["Y_val"][..., 3].ravel().astype(int)

    models_next_2d = prepare_occurrence_probabilities(preds_next)
    df_occ = evaluate_multi_class(models_next_2d, y_true_next, n_classes=2)
    df_sub = evaluate_multi_class(preds_typ, y_true_typ, n_classes=int(y_true_typ.max()) + 1)
    df_sev = evaluate_multi_class(preds_kdr, y_true_kdr, n_classes=int(y_true_kdr.max()) + 1)

    df_occ.to_csv(cfg.base_dir / "metrics_occurrence.csv", index=False)
    df_sub.to_csv(cfg.base_dir / "metrics_subtype.csv", index=False)
    df_sev.to_csv(cfg.base_dir / "metrics_severity.csv", index=False)

    print("Stage 03 completed: train + evaluation metrics saved.")
