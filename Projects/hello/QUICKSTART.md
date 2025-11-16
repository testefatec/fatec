# 🚀 GUIA RÁPIDO DE USO

## ⚡ Começando em 5 Minutos

### 1️⃣ Configure o Repositório

```bash
# Clone ou crie o repositório
git init
git add .
git commit -m "Initial commit: Pipeline CI/CD com CodeQL"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git push -u origin main
```

### 2️⃣ Habilite o GitHub Advanced Security

1. Vá para o repositório no GitHub
2. `Settings` → `Code security and analysis`
3. Ative `CodeQL analysis`
4. Clique em `Set up` → `Advanced`

### 3️⃣ Configure o Ambiente Stage

1. `Settings` → `Environments` → `New environment`
2. Nome: `stage`
3. (Opcional) Adicione regras de proteção

### 4️⃣ Execute a Pipeline

A pipeline executará automaticamente após o push. Para executar manualmente:

1. Vá para a aba `Actions`
2. Selecione `CI/CD Pipeline com CodeQL`
3. Clique em `Run workflow`

---

## 📊 Verificando Resultados

### Ver Status da Pipeline
```
GitHub → Actions → Selecione a execução
```

### Ver Alertas de Segurança
```
GitHub → Security → Code scanning alerts
```

---

## 🧪 Testando o CodeQL

### Teste 1: Código Seguro (Pipeline Passa)
```bash
# O código atual já está seguro
git push
# ✅ Pipeline deve passar
```

### Teste 2: Código Vulnerável (Pipeline Falha)
```bash
# 1. Abra exemplos_vulneraveis.py
# 2. Descomente o EXEMPLO 1 (SQL Injection)
# 3. Salve e faça commit

git add exemplos_vulneraveis.py
git commit -m "Teste: código vulnerável"
git push

# ❌ Pipeline deve falhar no CodeQL
# 📋 Verifique Security → Code scanning alerts
```

### Teste 3: Correção (Pipeline Passa Novamente)
```bash
# 1. Comente novamente o código vulnerável
# 2. Ou use a versão "segura" do exemplo

git add exemplos_vulneraveis.py
git commit -m "Fix: correção de vulnerabilidade"
git push

# ✅ Pipeline deve passar
```

---

## 🔍 Comandos Úteis

### Verificar Status Local
```bash
# Ver status do git
git status

# Ver logs de commits
git log --oneline

# Ver branches
git branch -a
```

### Executar Testes Localmente
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python main.py

# Executar testes
pytest tests/

# Executar com cobertura
pytest --cov=. --cov-report=html
```

### Análise de Código Local
```bash
# Verificar estilo
flake8 .

# Formatar código
black .

# Análise de segurança
bandit -r .
```

---

## 🎓 Exercícios Práticos

### Exercício 1: Pipeline Básica
- [ ] Clone o repositório
- [ ] Configure GitHub Advanced Security
- [ ] Execute a pipeline
- [ ] Verifique que todos os jobs passaram

### Exercício 2: Detecção de Vulnerabilidades
- [ ] Descomente um exemplo vulnerável
- [ ] Faça commit e push
- [ ] Observe a pipeline falhar
- [ ] Analise o alerta de segurança no GitHub

### Exercício 3: Correção de Vulnerabilidades
- [ ] Corrija o código vulnerável
- [ ] Verifique que a pipeline passa
- [ ] Confirme que o alerta foi resolvido

### Exercício 4: Adicionar Funcionalidade
- [ ] Adicione uma nova função em `main.py`
- [ ] Crie testes em `tests/test_main.py`
- [ ] Verifique que a pipeline continua passando

### Exercício 5: Deploy Personalizado
- [ ] Modifique o job `deploy-stage` com seu processo real
- [ ] Adicione secrets necessários
- [ ] Teste o deploy

---

## ⚠️ Troubleshooting Rápido

| Problema | Solução |
|----------|---------|
| Pipeline não executa | Verifique que o arquivo está em `.github/workflows/` |
| CodeQL não funciona | Habilite GitHub Advanced Security em Settings |
| Testes falhando | Execute `pytest` localmente para debugar |
| Deploy falhando | Verifique configuração do ambiente `stage` |

---

## 📚 Recursos Adicionais

- [Documentação Completa](README.md)
- [GitHub Actions Docs](https://docs.github.com/actions)
- [CodeQL Docs](https://codeql.github.com/)

---

## 💡 Dicas

1. **Sempre revise os logs**: Cada job mostra detalhes do que executou
2. **Use branches**: Teste mudanças em branches antes do main
3. **Leia os alertas**: O CodeQL explica cada vulnerabilidade encontrada
4. **Teste localmente**: Execute testes antes de fazer push
5. **Comente seu código**: Ajuda na manutenção e aprendizado

---

**Bons estudos! 🎓**
