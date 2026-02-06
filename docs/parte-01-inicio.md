# Parte 01 — Começando do início

## 1) Termos importantes

- **Repositório (repo)**: pasta versionada pelo Git.
- **Commit**: fotografia do estado dos arquivos em um momento.
- **Branch**: linha de desenvolvimento (ex.: `main`, `feature/x`).
- **Merge**: combinação de mudanças entre branches.
- **Código legado**: software já existente em produção/manutenção.

## 2) Conceitos que você vai praticar

### Versionamento
- Histórico confiável de alterações.
- Reversão de mudanças com segurança.
- Colaboração sem sobrescrever trabalho de outras pessoas.

### Legado
- Ler antes de alterar.
- Fazer mudanças pequenas e testáveis.
- Evitar "reescrever tudo" sem necessidade.

### Python no aprendizado
- Linguagem simples para focar em lógica.
- Excelente para scripts utilitários, automação e prática de algoritmos.

## 3) Fluxo Git recomendado (iniciante)

1. Atualize seu branch local.
2. Crie uma branch curta para uma tarefa específica.
3. Faça mudanças pequenas.
4. Rode testes/checks.
5. Commit com mensagem clara.
6. Abra PR explicando contexto e impacto.

Exemplo de mensagens de commit:
- `docs: adiciona introdução da trilha de aprendizado`
- `feat: adiciona exemplo Python de busca linear`
- `fix: corrige explicação sobre merge e rebase`

## 4) Mini-práticas sugeridas

### Prática A — Histórico limpo
- Edite 1 arquivo de documentação.
- Faça 1 commit objetivo.
- Revise com `git log --oneline`.

### Prática B — Leitura de legado
- Pegue uma função existente.
- Escreva em 3 linhas: entrada, processamento, saída.
- Sugira uma melhoria pequena sem quebrar comportamento.

### Prática C — Python + Git
- Rode `exemplos/python/01_busca_linear.py`.
- Altere os dados de exemplo.
- Commit da alteração com descrição do aprendizado.

## 5) Próximos passos (Parte 02)

- Estruturas de dados na prática (listas, dicionários, conjuntos).
- Complexidade de algoritmos (Big-O de forma intuitiva).
- Ferramentas: formatter, linter e testes automatizados.
