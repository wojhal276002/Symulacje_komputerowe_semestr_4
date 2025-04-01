[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Zm3oEiqJ)
# Symulacje Komputerowe

Wydział Matematyki, Semestr Letni 2023/2024

**Laboratorium 4:** Generowanie rozkładu normalnego

**Termin oddania:** 18/04/2024 godz. 23:59:59 CET.

---

**Zadanie 1.** Rozkład normalny jednowymariowy.
> Zaimplementuj metodę biegunową generowania rozkładu normalnego w wersji:
> - Boxa–Mullera,
> - Marsaglii.
> 
> Sprawdź zgodność z rozkładem teoretycznym. Porównaj ich wydajność.


**Zadanie 2.** Rozkład normalny wielowymiarowy.
> Wygeneruj wektory normalne dla dowolnej macierzy kowariancji $2\times 2$ oraz wybranych macierzy $3\times 3$. Zwizualizuj wygenerowane rozkłady.

**Uwaga:** Chcąc wygenerować wektor o rozkładzie normalnym $\mathcal{N}(0, \Sigma)$ można znaleźć taką
macierz $A$ aby $\Sigma = AA^T$. Wtedy $X = AZ$, $Z$ iid $\mathcal{N}(0,1)$, ma szukany rozkład.

**Uwaga**: Rozwiązania poszczególnych zadań należy umieścić w dedykowanych plikach `*.py` lub `*.ipynb` o nazwach `zadanie_1.[py|ipynb]`, `zadanie_2.[py|ipynb]` i `zadanie_3.[py|ipynb]`, itd.
