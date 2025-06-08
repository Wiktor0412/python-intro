# Raport – Analiza wielokryterialna z użyciem pymcdm

## 1. Dane
Rozważono 3 laptopy oceniane według 3 kryteriów:
- Cena (zł) – minimalizowana
- Wydajność (pkt) – maksymalizowana
- Waga (kg) – minimalizowana

### 1.1. Macierz decyzyjna

| Laptop | Cena (zł) | Wydajność (pkt) | Waga (kg) |
|--------|-----------|------------------|-----------|
| A1     | 2500      | 4000             | 1.5       |
| A2     | 2200      | 3700             | 1.3       |
| A3     | 2700      | 4200             | 1.6       |


## 2. Metody
Zastosowano dwie metody MCDM:
- **TOPSIS** – oparta na odległości od rozwiązania idealnego
- **SPOTIS** – oparta na odległości do punktu referencyjnego

## 3. Wagi
Wszystkim kryteriom przypisano jednakową wagę: 1/3

## 4. Wyniki
Wyniki zapisano w pliku `wyniki.csv` oraz wypisano w terminalu PyCharma. Ranking różni się nieco w zależności od metody.

## 5. Wnioski
W zależności od metody inne laptopy uzyskują lepsze miejsca. Warto wziąć pod uwagę różne podejścia przy podejmowaniu decyzji.
