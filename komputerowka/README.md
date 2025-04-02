# Symulacje Komputerowe

Wydział Matematyki, Semestr Letni 2023/2024

**Laboratorium:** Zaliczenie

**Termin oddania:** 20/06/2024. max 60 minut

---
**Zadanie 1.** Generator "tuzin"

Niech $U_1, U_2, \ldots , U_{12}$ będą liczbami pseudolosowymi $\mathcal{U}(0,1)$. Metoda tuzina generująca liczbę pseudolosową $Y \sim \mathcal{N}(m, s)$ jest opisana za pomocą algorytmu:
1. $S=\sum\limits_{i=1}^{12}U_i$,
2. $X=S-6$,
3. $Y = sX + m$.

Niech $m$ oznacza resztę z dzielenia ostatniej cyfry Twojego indeksu przez liczbę 2 (operacja modulo 2), a następnie przeprowadź analizę poprawności implementacja (bez wykorzystania pętli `for`/`while`) ww. generatora generując $N > 1000$ realizacji dla rozkladu $\mathcal{N}(m, 1)$ w oparciu o
- histogram vs. gęstość teoretyczną,
- dystrybuantę empiryczną vs. dystrybuantę teoretyczną,
- wykres kwantylowy (QQ-plot).

Uwaga: Interfejs funkcji
```python
def tuzin(N, m, s):
   ...
```

Założenia implementacji:
- w przypadku wywołania funkcji w postacji `tuzin(1000)`, domyślne wartości parametrów `m` i `s` zdefiniuj jako $0$ i $1$ odpowiednio,
- zalecana biblioteka do obliczeń numerycznych [`numpy`](https://numpy.org/), 
- kod zgodny z [PEP-8](https://peps.python.org/pep-0008/) oraz [black](https://github.com/psf/black) i [isort](https://pycqa.github.io/isort/),
- pamiętaj o dobrych standardach programistycznych, w szczególności [PEP-3017](https://peps.python.org/pep-3107/).

**Zadanie 2** Proces ryzyka

Kapitał firmy ubezpieczeniowej jest zadany wzorem:
$$R(t)=r_0 +p(t)−\sum\limits_{i=1}^{N_t}X_i,$$
gdzie:
- $A$ oznacza ostatnią cyfrę Twojego indeksu. Jeżeli to $0$, weź $9$.
- Zakładamy, że firma ubezpieczeniowa ma liniowe przychody $p(t) = ct$, gdzie $c = \frac{A}{3}$
- Wypłaty odszkodowań obserwujemy jako niejednorodny proces Poissona $N_{t}$, przy czym intensywność $\lambda{(t)}$ jest równa $1 + \sin{(t)}$
- Wielkość wypłat pochodzi z rozkładu wykładniczego $\exp(A)$.
- Kapitał początkowy firmy to $r_0 = 2 \cdot A$.
- Jeden dzień trwa jedną jednostkę czasu
- Jeśli trafimy w 0, to rozpoczynamy odliczanie paryskiego zegara: jeśli będziemy na minusie dłużej niż 4 dni, przegrywamy.
- jeśli spadniemy poniżej -10, to automatycznie przegrywamy

Polecenie:
1. Oszacuj prawdopodobieństwo ruiny w ciągu $5$ lat.
2. Zbadaj rozkład czasu ruiny pod warunkiem, że nastąpiła przed upływem $5$ lat.


**Uwaga**: Rozwiązania poszczególnych zadań należy umieścić w dedykowanych plikach `*.py` lub `*.ipynb` o nazwach `zadanie_1.[py|ipynb]`, `zadanie_2.[py|ipynb]` i `zadanie_3.[py|ipynb]`, itd.
