from pathlib import Path
import sys

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "tirs.csv"
TARGET = "quality"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    data = pd.read_csv(DATA_FILE)
    features = data.drop(columns=[TARGET])
    target = data[TARGET]
    train_features, test_features, train_target, test_target = train_test_split(
        features,
        target,
        test_size=0.25,
        random_state=42,
        stratify=target,
    )

    model = RandomForestClassifier(n_estimators=300, random_state=42, class_weight="balanced")
    model.fit(train_features, train_target)
    predictions = model.predict(test_features)
    model_accuracy = accuracy_score(test_target, predictions)

    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(train_features, train_target)
    baseline_predictions = baseline.predict(test_features)
    baseline_accuracy = accuracy_score(test_target, baseline_predictions)

    importances = pd.Series(model.feature_importances_, index=features.columns).sort_values(
        ascending=False
    )
    print(f"Testa precizitāte — modelis: {model_accuracy:.3f}")
    print(f"Testa precizitāte — biežākā klase (bāzes līnija): {baseline_accuracy:.3f}")
    print("Divas svarīgākās kolonnas:")
    for name, importance in importances.head(2).items():
        print(f"  {name}: {importance:.3f}")

    mistakes = test_features.loc[predictions != test_target].copy()
    mistakes["quality_actual"] = test_target.loc[mistakes.index]
    mistakes["quality_predicted"] = predictions[test_target.index.get_indexer(mistakes.index)]
    if mistakes.empty:
        print("Testa kopā kļūdainu prognožu nebija.")
    else:
        print("Pirmā kļūdainā testa rinda (rādītāji, īstā klase, prognoze):")
        print(mistakes.iloc[0].to_dict())


if __name__ == "__main__":
    main()
