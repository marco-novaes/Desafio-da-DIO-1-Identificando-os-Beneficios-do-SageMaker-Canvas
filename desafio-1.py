# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um benefício e retornar sua respectiva descrição.
def descrever_beneficio(beneficio):
    if beneficio == "Suporta todo o ciclo de vida do ML":
        return "Suporte a todo o ciclo de vida do Machine Learning"
    elif beneficio == "Impulsiona a colaboração":
        return "Todos os modelos criados podem ser compartilhados"
    elif beneficio == "ML sem código":
        return "Interface visual intuitiva e simples"
    elif beneficio == "Modelos de base prontos para uso":
        return "Acesso a Modelos de base (FMs) prontos para uso"
    else:
        return "Benefício desconhecido"

# Imprime a descrição associada ao benefício fornecido como entrada
print(descrever_beneficio(entrada))
