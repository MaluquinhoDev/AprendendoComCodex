"""Exemplo inicial de busca linear para rodar no Codespaces."""

from typing import Iterable


def busca_linear(valores: Iterable[int], alvo: int) -> int:
    for indice, valor in enumerate(valores):
        if valor == alvo:
            return indice
    return -1


def main() -> None:
    dados = [3, 7, 11, 19, 23]
    alvo = 19
    resultado = busca_linear(dados, alvo)

    if resultado >= 0:
        print(f"Valor {alvo} encontrado no índice {resultado}.")
    else:
        print(f"Valor {alvo} não encontrado.")


if __name__ == "__main__":
    main()
