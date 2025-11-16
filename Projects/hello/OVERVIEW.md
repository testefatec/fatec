# 📊 VISÃO GERAL DA PIPELINE CI/CD

## 🎯 Objetivo

Garantir que **nenhum código com vulnerabilidades** chegue ao ambiente de produção através de análise automatizada de segurança.

---

## 🔄 Fluxo da Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                    DESENVOLVEDOR                             │
│                  Faz commit e push                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 🔒 JOB 1: CODEQL                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 1. Checkout do código                                │  │
│  │ 2. Configura Python 3.11                             │  │
│  │ 3. Instala dependências                              │  │
│  │ 4. Inicializa CodeQL para Python                     │  │
│  │ 5. Analisa código em busca de vulnerabilidades       │  │
│  │ 6. Gera relatório de segurança                       │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ├─── ❌ Vulnerabilidades? ──► FALHA
                     │                              │
                     ▼                              ▼
              ✅ Código Seguro           📊 Gera Alerta no GitHub
                     │                   🚨 Notifica Desenvolvedores
                     │                   ⛔ Bloqueia Pipeline
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                🧪 JOB 2: TESTES                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 1. Checkout do código                                │  │
│  │ 2. Configura Python 3.11                             │  │
│  │ 3. Instala dependências + pytest                     │  │
│  │ 4. Executa testes unitários                          │  │
│  │ 5. Valida qualidade do código (flake8)               │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ├─── ❌ Testes Falharam? ──► FALHA
                     │
                     ▼
              ✅ Testes Passaram
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              🚀 JOB 3: DEPLOY STAGE                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 1. Checkout do código                                │  │
│  │ 2. Prepara artefatos                                 │  │
│  │ 3. Realiza deploy no ambiente Stage                  │  │
│  │ 4. Valida deploy                                     │  │
│  │ 5. Notifica conclusão                                │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
              ✅ SUCESSO!
         🌐 Aplicação em Stage
```

---

## 📈 Estatísticas de Segurança

### Vulnerabilidades Detectadas pelo CodeQL

| Tipo | Severidade | Exemplo |
|------|------------|---------|
| SQL Injection | 🔴 Critical | `cursor.execute(f"SELECT * FROM users WHERE id={user_id}")` |
| Command Injection | 🔴 Critical | `os.system(f"cat {filename}")` |
| Path Traversal | 🔴 High | `open(f"/uploads/{user_file}")` |
| Hard-coded Credentials | 🔴 High | `PASSWORD = "admin123"` |
| Weak Crypto | 🟠 Medium | `hashlib.md5(password)` |
| Insecure Random | 🟠 Medium | `random.randint()` para tokens |
| Unsafe Deserialization | 🔴 Critical | `pickle.loads(user_data)` |
| Use of eval() | 🔴 Critical | `eval(user_input)` |

---

## ⏱️ Tempo Médio de Execução

```
🔒 CodeQL Analysis:     ~3-5 minutos
🧪 Testes:             ~1-2 minutos  
🚀 Deploy:             ~1-3 minutos
─────────────────────────────────────
📊 TOTAL:              ~5-10 minutos
```

---

## 🎓 Conceitos Importantes

### 1. **Shift Left Security**
```
Tradicional:  Dev → Build → Test → Security → Deploy
Pipeline CI:  Dev → Security → Build → Test → Deploy
              ↑
         Detecta cedo!
```

### 2. **Fail Fast**
```
❌ Vulnerabilidade detectada no minuto 3
✅ Economiza 7+ minutos de build/test/deploy
✅ Economiza horas de correção em produção
```

### 3. **Zero Trust**
```
Todo código é analisado, sempre!
Nenhuma exceção
Nenhum bypass manual
```

---

## 🔍 Análise CodeQL em Detalhes

### O que o CodeQL Analisa?

```
Source Code (Python)
        │
        ▼
    ┌───────┐
    │ Parse │ ─── Cria AST (Abstract Syntax Tree)
    └───┬───┘
        │
        ▼
  ┌─────────┐
  │ CodeQL  │ ─── Executa queries de segurança
  │ Queries │     (3000+ regras predefinidas)
  └────┬────┘
        │
        ▼
┌──────────────┐
│ Data Flow    │ ─── Rastreia fluxo de dados
│ Analysis     │     (taint tracking)
└──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Vulnerabili- │
 │ ties Report  │
 └──────────────┘
```

### Exemplo de Detecção

**Código Vulnerável:**
```python
username = request.GET['user']
query = f"SELECT * FROM users WHERE name='{username}'"
cursor.execute(query)
```

**CodeQL Detecta:**
1. ✅ `username` vem de fonte não confiável (HTTP request)
2. ✅ Concatenado em string SQL
3. ✅ Passado para `execute()` sem sanitização
4. 🚨 **ALERTA: SQL Injection (CWE-89)**

---

## 📊 Dashboard de Métricas

### Por Execução da Pipeline

```
✅ Código Analisado:     X linhas
✅ Arquivos Verificados: Y arquivos
✅ Testes Executados:    Z testes
✅ Cobertura:           N%
✅ Vulnerabilidades:    0 (objetivo!)
```

### Histórico

```
                     Execuções
  100% │              ██████████
       │          ████          
   50% │      ████              
       │  ████                  
    0% └────────────────────────
        Sem  1-2  3-5  >5
        Vulns          Vulns
```

---

## 🎯 Benefícios da Pipeline

### Para Desenvolvedores
- ✅ Feedback imediato sobre segurança
- ✅ Aprende boas práticas automaticamente
- ✅ Menos bugs em produção
- ✅ Código mais limpo e seguro

### Para a Equipe
- ✅ Padronização de código
- ✅ Redução de vulnerabilidades
- ✅ Deploy mais confiável
- ✅ Documentação viva

### Para o Projeto
- ✅ Conformidade com padrões de segurança
- ✅ Redução de custos com correções
- ✅ Reputação preservada
- ✅ Confiança dos usuários

---

## 📚 Vocabulário CI/CD

| Termo | Significado |
|-------|-------------|
| **Pipeline** | Sequência automatizada de etapas |
| **Job** | Grupo de tarefas relacionadas |
| **Step** | Ação individual dentro de um job |
| **Workflow** | Definição completa da pipeline |
| **Artifact** | Arquivo gerado pela pipeline |
| **Environment** | Destino do deploy (stage, prod) |
| **Secret** | Credencial armazenada de forma segura |
| **Trigger** | Evento que inicia a pipeline |

---

## 🔐 Checklist de Segurança

Antes de fazer deploy, certifique-se:

- [ ] ✅ CodeQL passou sem alertas
- [ ] ✅ Todos os testes passaram
- [ ] ✅ Cobertura de testes adequada
- [ ] ✅ Sem credenciais no código
- [ ] ✅ Dependências atualizadas
- [ ] ✅ Logs não expõem dados sensíveis
- [ ] ✅ Validação de inputs implementada
- [ ] ✅ Comunicação criptografada (HTTPS)

---

## 🎓 Exercício Final

**Desafio: Implementar Feature Completa**

1. Crie uma nova função em `main.py`
2. Adicione testes em `tests/test_main.py`
3. Garanta que não há vulnerabilidades
4. Faça commit e push
5. Observe a pipeline executar
6. Verifique que todos os jobs passaram

**Pontos de Aprendizagem:**
- Desenvolvimento orientado a testes (TDD)
- Segurança desde o início (Security First)
- Automação de qualidade
- CI/CD na prática

---

**Criado para os alunos da FATEC** 🎓  
**Desenvolvimento de Sistemas** 💻  
**Professor: [Seu Nome]** 👨‍🏫
