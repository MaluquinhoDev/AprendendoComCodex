# Aprendendo com Codex — Projeto de Aprendizado em Partes

Este repositório é um **guia progressivo** para estudar:

- fundamentos de Git e trabalho com versionamento;
- leitura e evolução de código legado;
- prática de Python para consolidar lógica e ferramentas;
- conceitos-base de ciência da computação aplicados ao dia a dia.

## Estrutura inicial

- `docs/parte-01-inicio.md`: começo da trilha, termos e práticas essenciais.
- `docs/parte-01-guia-detalhado.md`: explicação aprofundada do código Python (termos, adaptação e desafios).
- `exemplos/python/`: exemplos pequenos em Python para treino guiado.
  - `01_busca_linear.py`: fundamentos de algoritmo e leitura de código.
  - `02_servidor_web_local.py`: servidor HTTP local para aprender requisição/resposta.

## Como usar este projeto

1. Leia a Parte 01 em `docs/parte-01-inicio.md`.
2. Leia o guia aprofundado em `docs/parte-01-guia-detalhado.md`.
3. Execute os exemplos Python.
4. Faça commits pequenos e descritivos para praticar Git.
5. Registre o que aprendeu no final de cada sessão.

## Objetivo

Aprender de forma prática e incremental, com foco em **entender o porquê** de cada ferramenta, conceito e decisão técnica.


## Executando o servidor web local

```bash
python3 exemplos/python/02_servidor_web_local.py --host 127.0.0.1 --port 8000
```

Depois acesse:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/health`
