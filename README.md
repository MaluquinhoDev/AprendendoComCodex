# AprendendoComCodex

Este repositório contém exemplos simples para estudo.

## Atualizar uma branch com a main (Opção 1: merge)

Passo a passo para atualizar sua branch de trabalho com as mudanças mais recentes da `main`:

1. Entrar na branch que você quer atualizar:
   ```bash
   git checkout codex/remove-markdown-files-linting-in-github-actions-hxpydf
   ```
2. Buscar atualizações do remoto:
   ```bash
   git fetch origin
   ```
3. Fazer merge da `main` na sua branch:
   ```bash
   git merge origin/main
   ```
4. Se houver conflito, resolva os arquivos marcados com:
   - `<<<<<<<`
   - `=======`
   - `>>>>>>>`
5. Marcar conflitos como resolvidos:
   ```bash
   git add <arquivo>
   ```
6. Finalizar merge (se necessário):
   ```bash
   git commit
   ```
7. Enviar branch atualizada:
   ```bash
   git push origin codex/remove-markdown-files-linting-in-github-actions-hxpydf
   ```

### Comandos úteis para conferir estado

```bash
git status
git branch -a
git log --oneline --graph --decorate -n 10
```

## GitHub Pages

O repositório já está preparado para publicar a página automaticamente usando GitHub Pages via GitHub Actions (`.github/workflows/github-pages.yml`).

### Como ativar

1. Faça merge desta branch na `main`.
2. No GitHub, acesse **Settings > Pages**.
3. Em **Build and deployment**, selecione **Source: GitHub Actions**.
4. Após o próximo push na `main` (ou execução manual do workflow), o site será publicado.

URL esperada:

```text
https://<seu-usuario>.github.io/AprendendoComCodex/
```
