# MIpraktiskaisd

## Pirmais modelis no nulles

Šis projekts izmanto UCI sarkanvīna kvalitātes datus, pārbauda un attīra CSV failu, pēc tam apmāca klasifikācijas modeli prognozēt vīna kvalitātes vērtējumu (`quality`) no ķīmiskajiem mērījumiem. Sākotnējais fails atrodas mapē `dati/` un netiek mainīts.

## Palaišana

Nepieciešams Python 3 un bibliotēkas `pandas` un `scikit-learn`. Instalē tās ar:

```bash
python -m pip install pandas scikit-learn
```

No projekta mapes palaid:

```bash
python 01_tirisana.py
python 02_modelis.py
```

Pirmais skripts izveido `tirs.csv` un izvada rindu skaitu pirms un pēc tīrīšanas, kā arī izņemto rindu skaitu pa iemesliem. Otrais izvada modeļa un biežākās klases bāzes līnijas testa precizitāti, divas svarīgākās pazīmes un vienu kļūdainu prognozi. Rezultātu skaidrojums ir failā `rezultati.md`.
