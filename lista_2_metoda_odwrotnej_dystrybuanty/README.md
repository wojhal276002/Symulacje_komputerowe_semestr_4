[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/2nj9HNKV)
# Symulacje Komputerowe

Wydział Matematyki, Semestr Letni 2023/2024

**Laboratorium 2:** Metoda odwrotnej dystrybuanty

---

Implementując poniższe algorytmy skupimy się na:
- **Weryfikacji wyników:** Porównanie gęstości oraz dystrybuant teoretycznych do empirycznych, użycie testów statystycznych.
- **Optymalizacji obliczeń:** Porównanie szybkości oraz zużycia pamięci zaimplementowanych algorytmów do wbudowanych generatorów.

**Zadanie 1.** Rozkłady ciągłe.

> Zaimplementuj generowanie metodą odwrotnej dystrybuanty w przypadku:
> - rozkładu wykładnicznego $\mathcal{Exp}(\lambda)$,
> - rozkładu normalnego $\mathcal{N}(\mu, \sigma^2)$,
> - rozkładu Cauchy'ego $\mathcal{C}(\mu, \gamma)$.


**Zadanie 2.** Rozkłady dyskretne.

> Zaimplementuj generowanie metodą odwrotnej dystrybuanty w przypadku:
> - rozkładu geometrycznego $\mathcal{Geo}(p)$,
> - rozkładu Poissona $\mathcal{Poiss}(\lambda)$.


**Zadanie 3.** Metoda tablicowa.
> Dla rozkładów zadanych skończoną liczbą prawdopodobieństw zaimplementuj generowanie metodą tablicową (table lookup).


**Uwaga**: Rozwiązania poszczególnych zadań należy umieścić w dedykowanych plikach `*.py` lub `*.ipynb` o nazwach `zadanie_1.[py|ipynb]`, `zadanie_2.[py|ipynb]` i `zadanie_3.[py|ipynb]`. 
