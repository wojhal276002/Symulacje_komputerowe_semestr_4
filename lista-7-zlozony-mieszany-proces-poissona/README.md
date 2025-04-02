[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SJ64fb2e)
# Symulacje Komputerowe

Wydział Matematyki, Semestr Letni 2023/2024

**Laboratorium 7:** Złożony process Poissona

**Termin oddania:** 12/06/2024 godz. 23:59:59 CET.

---

**Zadanie 1.** Funkcja charakterystyczna
> Zaimplementuj próbkowy estymator funkcji charakterystycznej i wypróbuj na typowych rozkładach.

**Zadanie 2.** Złożony proces Poissona
> W oparciu o definicję zaimplementuj symulowanie złożonego procesu Poisson'a dla skoków z rozkładu $\mathcal{N}\sim(0,1)$ oraz $\mathcal{C}(0, 1)$.
> - Stwórz wykresy trajektorii oraz zweryfikuj poprawność symulacji korzystając ze znajomości funkcji charakterystycznej procesu.

**Zadanie 3.** Mieszany process Poissona (1)
> Zaimplementuj następujący algorytm:
> 1. Generuj jedną realizację $\lambda$ zmiennej losowej $L$.
> 2. Ustaw $t=0$, $I=0$.
> 3. Generuj $U \sim U(0,1)$, $U$ i $L$ - niezależne.
> 4. Wstaw $t=t−\frac{1}{\lambda}\log(U)$. Jeśli $t>T$,to koniec. 5.
> 5. Wstaw $I=I+1$ ,$S_I =t$.
> 6. Wróć do 3.
>    
> Narysuj kilkanaście przykładowych trajektorii mieszanego procesu Poissona na jednym wykresie dla $L \sim U(0, 10)$ oraz dla $L \sim Exp(1)$.

**Zadanie 4.** Mieszany process Poissona (2)
> Zaimplementuj następujący algorytm:
> 1. Generuj jedną realizację λ zmiennej losowej L.
> 2. Generuj $n \sim Pois(\lambda T)$.
> 3. Jeśli $n = 0$, to koniec.
> 4. Generuj $U_1,\ldots,U_n$ - iid, $U_i \sim U(0,T)$, $U_i | λ$.
> 5. Sortuj $U_1,\ldots,U_n$ aby uzyskać $(U_{1:n},...,U_{n:n}).
> 6. Wstaw $S_i = U_{1:n}$, $i = 1,\ldots,n$.
>    
> Narysuj kilkanaście przykładowych trajektorii mieszanego procesu Poissona na jednym wykresie dla $L \sim U(0, 10)$ oraz dla $L \sim Exp(1)$.

**Uwaga**: Rozwiązania poszczególnych zadań należy umieścić w dedykowanych plikach `*.py` lub `*.ipynb` o nazwach `zadanie_1.[py|ipynb]`, `zadanie_2.[py|ipynb]` i `zadanie_3.[py|ipynb]`, itd.
