[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/PSxO9zSJ)
# Symulacje Komputerowe

Wydział Matematyki, Semestr Letni 2023/2024

**Laboratorium 3:** Metoda akceptacji-odrzucania

**Termin oddania:** 10/04/2024 godz. 23:59:59 CET.

---

**Zadanie 1.** Gęstość potęgowa.
> Zaimplementuj metodę akceptacji i odrzucania dla rozkładów o gęstości $p(x) = C_\alpha x^{\alpha}$ dla $x\in [0,1]$, zaczynając od rozkładu jednostajnego. Ile wynosci $C_\alpha$?
> - Sprawdź, jak efektywność symulacji, tj. procent trafionych prób, zależy od $\alpha$.


**Zadanie 2.** Efektywność a przekształcenia rozkładu.
> Metodą akceptacji odrzucania wygeneruj rozkład X o gęstości $p(x) = C\sin(x), \quad x \in [0, \frac{\pi}{2}]$ zaczynając od rozkładu jednostajnego.
> - Jak ta efektywność zmieni się, kiedy zaczniesz od wygenerowania $Y = X^2$ (oblicz jego gęstość), a $X$ uzyskasz jako $\sqrt{Y}$ ?


**Zadanie 3.** Rozkłady na półosi.
> Zaimplementuj generowanie rozkładu normalnego zaczynając od rozkładu wykładniczego. W pierwszym kroku wygeneruj rozkład pół-normalny, tj. $|\mathcal{N}(0, 1)|$. Postaraj się, aby symulacja działała jak najszybciej.

**Zadanie 4.** Metoda ziggurat.
> Ustal podział nośnika rozkładuna przedziały $\ldots,[x_k,x_{k+1}], [x_{k+1}, x_{k+2}], [x_{k+3}, x_{k+4}],\ldots$, brzegowe $x$ mogą być nieskończone. Na każdym z nich oblicz maksimum oraz minimum docelowej gęstości $f_i := \min_{x_i \leq x \leq x_{i+1}} f(x)$, $F_i := \max_{x_i\leq x \leq x_{i+1}} f(x)$. Zapisz te wartości w pamięci.
>
> Następnie, przy generowaniu próby metodą akceptacji-odrzucania, mając wygenerowane $U\sim \mathcal{U}(0,1)$ oraz $X \sim g$ znajdź przedział, $[x_i,x_{i+1}]$ do którego należy $X$ oraz sprawdź czy:
>
> - $UCg(X) > F_i$, w tym wypadku odrzuć $X$.
>
> - $UCg(X) < f_i$, w tym wypadku zaakceptuj $X$.
>
> Tylko jeżeli ani jeden ani drugi nie jest spełniony sprawdź czy $UCg(X) < f(X)$.
>
> Sprawdź szybkość tego algorytmu w porównaniu do metody akceptacji odrzuca- nia bez tej korekty. Przetestuj różne podziały nośnika.


**Uwaga**: Rozwiązania poszczególnych zadań należy umieścić w dedykowanych plikach `*.py` lub `*.ipynb` o nazwach `zadanie_1.[py|ipynb]`, `zadanie_2.[py|ipynb]` i `zadanie_3.[py|ipynb]`, itd.
