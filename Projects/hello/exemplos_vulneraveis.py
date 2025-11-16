"""
EXEMPLOS DE CÓDIGO VULNERÁVEL - APENAS PARA FINS EDUCACIONAIS
==============================================================
⚠️ ATENÇÃO: Este arquivo contém EXEMPLOS de código VULNERÁVEL
para demonstrar como o CodeQL detecta problemas de segurança.

NÃO USE ESTES EXEMPLOS EM PRODUÇÃO!

Este arquivo está comentado para não executar acidentalmente.
Para testar o CodeQL, descomente um dos exemplos, faça commit
e observe a pipeline detectar a vulnerabilidade.
==============================================================
"""

# =============================================================================
# EXEMPLO 1: SQL INJECTION (CWE-89) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará que estamos concatenando input do usuário em uma query SQL
# Isso permite que um atacante execute comandos SQL arbitrários

"""
import sqlite3

def buscar_usuario_vulneravel(username):
    # ❌ VULNERÁVEL: Concatenação direta de input do usuário
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM usuarios WHERE username = '{username}'"
    cursor.execute(query)  # CodeQL vai detectar aqui!
    
    return cursor.fetchall()

# Como corrigir:
def buscar_usuario_seguro(username):
    # ✅ SEGURO: Usar parâmetros preparados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM usuarios WHERE username = ?"
    cursor.execute(query, (username,))
    
    return cursor.fetchall()
"""

# =============================================================================
# EXEMPLO 2: COMMAND INJECTION (CWE-78) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará execução de comandos do sistema com input do usuário

"""
import os

def executar_comando_vulneravel(filename):
    # ❌ VULNERÁVEL: Execução de comando com input do usuário
    os.system(f"cat {filename}")  # CodeQL vai detectar aqui!
    # Atacante pode fazer: filename = "arquivo.txt; rm -rf /"

# Como corrigir:
import subprocess

def executar_comando_seguro(filename):
    # ✅ SEGURO: Usar subprocess com lista de argumentos
    subprocess.run(["cat", filename], check=True)
"""

# =============================================================================
# EXEMPLO 3: PATH TRAVERSAL (CWE-22) 🔴 HIGH
# =============================================================================
# O CodeQL detectará acesso a arquivos sem validação do caminho

"""
def ler_arquivo_vulneravel(filename):
    # ❌ VULNERÁVEL: Sem validação do caminho
    with open(f"/var/www/uploads/{filename}", 'r') as f:
        return f.read()
    # Atacante pode fazer: filename = "../../etc/passwd"

# Como corrigir:
import os

def ler_arquivo_seguro(filename):
    # ✅ SEGURO: Validar que o caminho está dentro do diretório permitido
    base_dir = "/var/www/uploads"
    filepath = os.path.join(base_dir, filename)
    
    # Verifica se o caminho real está dentro do diretório base
    if not os.path.realpath(filepath).startswith(os.path.realpath(base_dir)):
        raise ValueError("Caminho inválido")
    
    with open(filepath, 'r') as f:
        return f.read()
"""

# =============================================================================
# EXEMPLO 4: HARD-CODED CREDENTIALS (CWE-798) 🔴 HIGH
# =============================================================================
# O CodeQL detectará credenciais fixas no código

"""
# ❌ VULNERÁVEL: Credenciais no código
DATABASE_PASSWORD = "senha123"
API_KEY = "sk-1234567890abcdef"

# Como corrigir:
import os
from dotenv import load_dotenv

# ✅ SEGURO: Usar variáveis de ambiente
load_dotenv()
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
API_KEY = os.getenv('API_KEY')
"""

# =============================================================================
# EXEMPLO 5: WEAK CRYPTOGRAPHY (CWE-327) 🟠 MEDIUM
# =============================================================================
# O CodeQL detectará uso de algoritmos de criptografia fracos

"""
import hashlib

def hash_senha_vulneravel(senha):
    # ❌ VULNERÁVEL: MD5 é considerado fraco
    return hashlib.md5(senha.encode()).hexdigest()

# Como corrigir:
import bcrypt

def hash_senha_seguro(senha):
    # ✅ SEGURO: Usar bcrypt ou argon2
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt)
"""

# =============================================================================
# EXEMPLO 6: INSECURE DESERIALIZATION (CWE-502) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará desserialização de dados não confiáveis

"""
import pickle

def carregar_dados_vulneravel(data):
    # ❌ VULNERÁVEL: Pickle pode executar código arbitrário
    return pickle.loads(data)  # CodeQL vai detectar aqui!

# Como corrigir:
import json

def carregar_dados_seguro(data):
    # ✅ SEGURO: Usar JSON para dados não confiáveis
    return json.loads(data)
"""

# =============================================================================
# EXEMPLO 7: RANDOM NUMBER GENERATION (CWE-338) 🟠 MEDIUM
# =============================================================================
# O CodeQL detectará uso de gerador de números aleatórios fraco para segurança

"""
import random

def gerar_token_vulneravel():
    # ❌ VULNERÁVEL: random não é criptograficamente seguro
    return random.randint(1000, 9999)

# Como corrigir:
import secrets

def gerar_token_seguro():
    # ✅ SEGURO: Usar secrets para dados sensíveis
    return secrets.token_hex(16)
"""

# =============================================================================
# EXEMPLO 8: EVAL() COM INPUT DO USUÁRIO (CWE-94) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará uso de eval() com dados não confiáveis

"""
def calcular_vulneravel(expressao):
    # ❌ VULNERÁVEL: eval pode executar código arbitrário
    return eval(expressao)  # CodeQL vai detectar aqui!
    # Atacante pode fazer: expressao = "__import__('os').system('rm -rf /')"

# Como corrigir:
import ast

def calcular_seguro(expressao):
    # ✅ SEGURO: Usar ast.literal_eval para expressões seguras
    try:
        return ast.literal_eval(expressao)
    except (ValueError, SyntaxError):
        raise ValueError("Expressão inválida")
"""

# =============================================================================
# INSTRUÇÕES PARA TESTAR
# =============================================================================
"""
COMO TESTAR O CODEQL:

1. Descomente um dos exemplos acima (remova as aspas triplas)
2. Faça commit e push do código
3. Aguarde a pipeline executar
4. A pipeline vai FALHAR no job CodeQL
5. Vá em Security > Code scanning alerts para ver o alerta
6. Corrija usando o exemplo "seguro"
7. Faça novo commit e observe a pipeline passar!

EXERCÍCIO PRÁTICO:
- Descomente o EXEMPLO 1 (SQL Injection)
- Faça commit: git add . && git commit -m "Teste: código vulnerável"
- Push: git push
- Observe o CodeQL detectar a vulnerabilidade!
- Corrija usando a versão segura
- Confirme que a pipeline passa
"""

if __name__ == "__main__":
    print("⚠️  Este arquivo contém exemplos de código VULNERÁVEL!")
    print("📚 Use apenas para fins educacionais")
    print("🔒 Nunca use estes padrões em produção!")
