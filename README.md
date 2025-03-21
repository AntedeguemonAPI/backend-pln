
### Como funciona um sistema básico de NER (Named Entity Recognition)
 O processo normalmente envolve três etapas principais:
1. Tokenização: Quebra o texto em palavras ou tokens menores.
2. Anotação: O modelo atribui rótulos às palavras (ex.: PER para pessoa, ORG para organização etc.)
       PER (Person - Pessoa): Identifica nomes próprios de indivíduos
    ORG (Organization - Organização): Identifica empresas, instituições ou grupos.
    LOC (Location - Localização): Identifica locais geográficos
    DATE (Data): Identifica datas específicas
    TIME (Hora): Identifica horas mencionadas
    MONEY (Dinheiro): Identifica valores monetários
    PERCENT (Porcentagem): Identifica valores percentuais
    GPE (Geopolitical Entity - Entidade Geopolítica): Identifica países, estados ou cidades que são reconhecidos geopoliticamente.
    PRODUCT (Produto): Identifica nomes de produtos ou marcas
3. Classificação: Cada token recebe uma classificação de acordo com seu papel no texto
