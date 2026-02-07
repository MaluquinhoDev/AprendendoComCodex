# Parte 01.1 — Guia detalhado do código Python (busca linear)

Este guia aprofunda o arquivo `exemplos/python/01_busca_linear.py` palavra por palavra,
com foco em entendimento real, adaptação prática e evolução para código de produção.

---

## 1) Leitura linha por linha do arquivo

### Docstring do módulo

```python
"""Exemplo inicial de algoritmo: busca linear.
...
"""
```

- `""" ... """` (aspas triplas): define uma **docstring** de módulo.
- Serve para documentação automática, leitura em IDE e orientação de quem abre o arquivo pela primeira vez.
- Em código legado, uma boa docstring reduz tempo de entendimento do contexto.

### Import

```python
from typing import Iterable
```

- `from ... import ...`: importa apenas o nome necessário.
- `typing`: módulo da biblioteca padrão para anotações de tipos.
- `Iterable`: protocolo para qualquer coleção iterável (`list`, `tuple`, `set`, `range`, etc.).

**Por que usar `Iterable` em vez de `list`?**
- Deixa a função mais flexível: ela não depende de uma estrutura única.
- Facilita reúso com dados vindos de diferentes fontes.

### Definição da função

```python
def busca_linear(valores: Iterable[int], alvo: int) -> int:
```

- `def`: define função.
- `busca_linear`: nome semântico (o que a função faz).
- `valores: Iterable[int]`: parâmetro com anotação de tipo (iterável de inteiros).
- `alvo: int`: valor que queremos encontrar.
- `-> int`: tipo de retorno esperado (`índice` ou `-1`).

### Lógica principal

```python
for indice, valor in enumerate(valores):
    if valor == alvo:
        return indice
return -1
```

- `for`: iteração sequencial.
- `enumerate(valores)`: retorna pares `(indice, valor)`.
- `if valor == alvo`: comparação de igualdade.
- `return indice`: encerra cedo ao encontrar (eficiência prática).
- `return -1`: convenção para “não encontrado”.

**Custo algorítmico:**
- Melhor caso: `O(1)` (encontra no início).
- Pior caso: `O(n)` (não encontra ou encontra no fim).
- Memória extra: `O(1)`.

### Função principal

```python
def main() -> None:
```

- `main` organiza o fluxo de execução do script.
- `-> None` indica que não retorna valor útil (efeito principal: `print`).

### Guard de execução

```python
if __name__ == "__main__":
    main()
```

- `__name__`: variável especial definida pelo Python.
- Quando o arquivo é executado diretamente, `__name__ == "__main__"`.
- Quando importado como módulo, esse bloco **não roda**.

Isso permite reutilizar `busca_linear` em outros arquivos sem disparar execução automática.

---

## 2) Onde usar busca linear na prática

Use busca linear quando:
- o conjunto é pequeno/médio;
- os dados não estão ordenados;
- simplicidade e legibilidade importam mais que micro-otimização;
- você precisa de implementação rápida e transparente para ensino/debug.

Evite quando:
- você faz muitas buscas repetidas em coleções grandes;
- há necessidade forte de desempenho.

Alternativas:
- `set`/`dict` para consultas `O(1)` média por chave.
- Busca binária (`bisect`) em listas ordenadas (`O(log n)`).

---

## 3) Como adaptar este código para cenários reais

### Adaptação A — Retornar `None` ao invés de `-1`

Mais semântico em muitos contextos Python:

```python
def busca_linear(valores: Iterable[int], alvo: int) -> int | None:
    for indice, valor in enumerate(valores):
        if valor == alvo:
            return indice
    return None
```

### Adaptação B — Aceitar qualquer tipo de dado

```python
from typing import Iterable, TypeVar

T = TypeVar("T")

def busca_linear(valores: Iterable[T], alvo: T) -> int:
    for indice, valor in enumerate(valores):
        if valor == alvo:
            return indice
    return -1
```

### Adaptação C — Retornar todos os índices encontrados

Útil quando há repetição:

```python
def busca_todos(valores: Iterable[int], alvo: int) -> list[int]:
    return [i for i, v in enumerate(valores) if v == alvo]
```

---

## 4) Desafios fundamentais (ordem recomendada)

1. **Entrada dinâmica**: ler lista e alvo do usuário com `input`.
2. **Testes automatizados**: criar testes para encontrado/não encontrado/lista vazia.
3. **Generalização de tipos**: usar `TypeVar` para aceitar strings e objetos.
4. **Refatoração segura**: trocar `-1` por `None` sem quebrar consumidores.
5. **Comparação de desempenho**: medir busca linear vs `in` em `set` com `timeit`.
6. **Estudo de legados**: documentar pré-condições e pós-condições da função.

---

## 5) Erros comuns de iniciantes (e como evitar)

- Esquecer o `return -1` final → função retorna `None` sem intenção.
- Confundir índice com valor → o índice é posição, não conteúdo.
- Usar nomes genéricos (`x`, `y`) em todo lugar → dificulta manutenção.
- Mudar comportamento sem atualizar documentação e testes.

---

## 6) Checklist de qualidade para este tipo de código

- [ ] Nome da função reflete claramente a intenção?
- [ ] Contrato de entrada e saída está documentado?
- [ ] Casos de borda foram considerados (lista vazia, alvo ausente)?
- [ ] Existem exemplos de uso?
- [ ] Há teste mínimo automatizado?

Esse checklist é essencial para evolução de código legado com segurança.
