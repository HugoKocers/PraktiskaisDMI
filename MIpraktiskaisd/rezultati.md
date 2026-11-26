# Rezultātu interpretācija

## Kas ir šie dati un no kurienes tie nāk?

Šī ir UCI Machine Learning Repository sarkanvīna kvalitātes datu kopa. Tajā ir 1 599 Portugāles ziemeļu Vinho Verde vīnu paraugi, 11 ķīmiskie mērījumi un kvalitātes vērtējums (`quality`) no sensoro testu rezultātiem. Oriģinālo CSV failu lejupielādēju 2026. gada 26. novembrī; avota saite un licence norādīta [dati/AVOTS.txt](dati/AVOTS.txt).

## Kas ar datiem bija nepareizi un ko es izdarīju?

Sākotnējā failā bija 1 599 rindas un 12 kolonnas; lauki bija atdalīti ar semikolu. Atradu 240 pilnīgi identiskas dublikātu rindas. Trūkstošu vērtību un nederīgu skaitlisku vērtību rindu nebija. Tīrīšanas skripts dublikātus izmeta un saglabāja 1 359 rindas failā `tirs.csv`; sākotnējais fails palika nemainīts.

| Iemesls | Izmestās rindas |
|---|---:|
| Trūkstošas vērtības | 0 |
| Nederīgas skaitliskas vērtības | 0 |
| Dublikāti | 240 |
| **Kopā** | **240** |

## Ko modelis prognozē un cik labi?

Modelis prognozē sensoro kvalitātes vērtējuma klasi (`quality`) no 11 ķīmiskajiem rādītājiem. Random Forest tika trenēts ar 75% datu un pārbaudīts uz atlikušajiem 25%, izmantojot fiksētu nejaušības sēklu un klašu stratifikāciju.

| Metode | Precizitāte testa datos |
|---|---:|
| Random Forest | 0,576 (57,6%) |
| Bāzes līnija — vienmēr prognozēt biežāko klasi | 0,424 (42,4%) |

Šajā testa sadalījumā modelis bāzes līniju pārspēja par 15,2 procentpunktiem, kas ir jūtama atšķirība šī testa rezultātā. Tomēr viens testa sadalījums nepierāda, ka šāda priekšrocība atkārtosies uz citiem vīniem vai datu kopām; rezultāts nav pietiekams, lai apgalvotu drošu vispārināšanu.

## Svarīgākās kolonnas

Modeļa aprēķinātās svarīgākās pazīmes bija alkohola saturs (`alcohol`, 0,135) un gaistošais skābums (`volatile acidity`, 0,130). Tas šķiet ticami, jo abi rādītāji var būt saistīti ar vīna sensorajām īpašībām, bet svarīguma vērtības rāda modeļa izmantoto pazīmju ietekmi, nevis pierāda cēloņsakarību.

## Viena kļūdaina prognoze

Testa kopas rinda:

| fixed acidity | volatile acidity | citric acid | residual sugar | chlorides | free sulfur dioxide | total sulfur dioxide | density | pH | sulphates | alcohol | Īstā kvalitāte | Prognoze |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8,1 | 0,78 | 0,23 | 2,6 | 0,059 | 5 | 15 | 0,997 | 3,37 | 0,56 | 11,3 | 5 | 4 |

Modelis šo vīnu novērtēja ar 4, bet testa datos tā vērtējums bija 5. Tās ir blakus esošas klases, un ķīmisko mērījumu vērtības vien ne vienmēr pilnībā atspoguļo subjektīvu degustācijas vērtējumu; tas ir ticams iemesls, bet no vienas kļūdas vien to pierādīt nevar.

## Ko ar šo modeli nedrīkst darīt?

Ar šo modeli nedrīkst automātiski noraidīt vai sertificēt vīna partijas komerciālai pārdošanai: kļūdaina klasifikācija ir bieža, novērtējums balstās uz ierobežotu vēsturisku datu kopu, un modelis nav neatkarīgi pārbaudīts uz jauniem vīniem. Tas ir mācību piemērs, nevis profesionāla kvalitātes kontroles sistēma.

## Pašvērtējums

Man izdevās atrast dublikātus, izveidot tīrīšanas skriptu un salīdzināt modeli ar bāzes līniju. Man neizdevās pierādīt, ka modeļa sniegums atkārtotos uz citiem datiem, jo izmantoju vienu testa sadalījumu. Nākamreiz es pārbaudītu modeli ar krustenisko validāciju un neatkarīgu datu kopu.
