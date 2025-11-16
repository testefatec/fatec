"""
Aplicação Python de Exemplo - FATEC
====================================
Este é um exemplo didático de aplicação Python para demonstrar
a pipeline CI/CD com análise de segurança CodeQL.

Autor: Professor FATEC
Disciplina: Desenvolvimento de Sistemas
"""


def saudacao(nome: str) -> str:
    """
    Retorna uma saudação personalizada.
    
    Args:
        nome: Nome da pessoa ou instituição
        
    Returns:
        String com a saudação formatada
    """
    if not nome:
        return "Olá, visitante!"
    return f"Olá, {nome}!"


def calcular_media(notas: list) -> float:
    """
    Calcula a média de uma lista de notas.
    
    Args:
        notas: Lista de notas (float)
        
    Returns:
        Média das notas
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def validar_email(email: str) -> bool:
    """
    Valida se um email possui formato básico válido.
    
    Args:
        email: String com o email a validar
        
    Returns:
        True se válido, False caso contrário
    """
    # Validação simples para fins didáticos
    if not email or '@' not in email:
        return False
    
    partes = email.split('@')
    if len(partes) != 2:
        return False
    
    usuario, dominio = partes
    return len(usuario) > 0 and len(dominio) > 0 and '.' in dominio


def main():
    """Função principal da aplicação."""
    print("=" * 50)
    print("🎓 Bem-vindo ao Sistema FATEC")
    print("=" * 50)
    
    # Exemplo de uso das funções
    print(saudacao("FATEC Santana de Parnaíba"))
    
    # Exemplo de cálculo de média
    notas_aluno = [8.5, 9.0, 7.5, 8.0]
    media = calcular_media(notas_aluno)
    print(f"\n📊 Média do aluno: {media:.2f}")
    
    # Exemplo de validação de email
    email_teste = "aluno@fatec.sp.gov.br"
    if validar_email(email_teste):
        print(f"✅ Email válido: {email_teste}")
    else:
        print(f"❌ Email inválido: {email_teste}")
    
    print("\n" + "=" * 50)
    print("✅ Aplicação executada com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    main()
