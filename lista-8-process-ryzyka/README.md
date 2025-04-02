# Symulacje Komputerowe

Wydział Matematyki, Semestr Letni 2023/2024

**Laboratorium 8:** Proces Ryzyka

**Termin oddania:** 19/05/2024 godz. 23:59:59 CET.

---

**Zadanie 1.** Proces ryzyka

Kapitał firmy ubezpieczeniowej jest zadany wzorem:
$$R(t)=r_0 +p(t)−\sum\limits_{i=1}^{N_t}X_i,$$
gdzie:
- $N_t$ jest procesem liczącym (tutaj jednorodnym procesem Poissona o intensywności $\lambda$, ale może być też inny proces odnowy),
- $X_i$ to wielkości szkód (np. z rozkładu gamma, Pareto, Weibulla),
- $r_0$ to kapitał początkowy,
- $p(t)$ to funkcja zysków. 
> Stwórz symulację takiego procesu, która zatrzymuje się przy uderzeniu w 0; funkcja $p(t)$ oraz rozkład zmiennych $X_i$ powinny być wprowadzane przez użytkownika.

**Zadanie 2.** Proces ryzyka cd.
Niech $p(t) = ct$ i $X_i \sim Exp(k)$. 
> Zbadaj rozkład (histogramy, statystyki opisowe) czasu ruiny w zależności od $r_0$, $c$, $k$, $\lambda$ (weź pod uwagę różne poziomy pozostałych parametrów).

**Zadanie 3.** Ruina Paryska

Uogólnij symulację, aby firma nie bankrutowała automatycznie po uderzeniu w 0. Firma będzie teraz bankrutować po $T$ jednostkach czasu przebywania poniżej $0$ (po wyjściu ponad poziom $0$ zegar restartujemy).

**Zadanie 4.** Ruina Paryska cd.

Dla takich parametrów $r_0$, $c$, $k$, $\lambda$, dla których firma w klasycznym przypadku bankrutuje „często” na przedziale czasu od $10$ do $100$, zbadaj rozkład czasu bankructwa paryskiego w zależności od $T$.

**Uwaga**: Rozwiązania poszczególnych zadań należy umieścić w dedykowanych plikach `*.py` lub `*.ipynb` o nazwach `zadanie_1.[py|ipynb]`, `zadanie_2.[py|ipynb]` i `zadanie_3.[py|ipynb]`, itd.
