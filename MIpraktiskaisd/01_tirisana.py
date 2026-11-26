from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parent
RAW_FILE = ROOT / "dati" / "winequality-red.csv"
OUTPUT_FILE = ROOT / "tirs.csv"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    # UCI failā kolonnas atdala ar semikolu, tāpēc to norādām, nevis paļaujamies uz CSV noklusējumu.
    data = pd.read_csv(RAW_FILE, sep=";")
    initial_rows = len(data)

    # Tukšu šūnu rindas izņemam, jo bez visiem ķīmiskajiem rādītājiem nevar korekti apmācīt modeli.
    missing_rows = int(data.isna().any(axis=1).sum())
    data = data.dropna().copy()

    # Visas šīs kopas kolonnas ir skaitliskas, tāpēc nederīgas teksta vērtības pārvēršam par trūkstošām.
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # Pēc skaitliskās pārveides radušās nederīgu vērtību rindas izmetam, lai modelim paliktu skaitļi.
    invalid_numeric_rows = int(data.isna().any(axis=1).sum())
    data = data.dropna().copy()

    # Dublikātus izņemam, jo identisku vīna mērījumu atkārtošanās var nesamērīgi ietekmēt modeļa apmācību.
    duplicate_rows = int(data.duplicated().sum())
    data = data.drop_duplicates().copy()

    data.to_csv(OUTPUT_FILE, index=False)
    removed_rows = initial_rows - len(data)
    print(f"Rindas sākumā: {initial_rows}")
    print(f"Izmestas tukšu vērtību dēļ: {missing_rows}")
    print(f"Izmestas nederīgu skaitlisku vērtību dēļ: {invalid_numeric_rows}")
    print(f"Izmestas dublikātu dēļ: {duplicate_rows}")
    print(f"Rindas beigās: {len(data)}")
    print(f"Kopā izmestas: {removed_rows}")
    print(f"Sakārtotie dati saglabāti: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
