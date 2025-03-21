import pandas as pd
import spacy
import matplotlib.pyplot as plt
from collections import Counter
import re

# Carregar o modelo de linguagem do spaCy
nlp = spacy.load("pt_core_news_sm")

# Ler o arquivo CSV
arquivo_csv = 'Chamados Porto.csv'
df = pd.read_csv(arquivo_csv, sep=';', engine='python')

# Lista de palavras irrelevantes (stopwords)
stopwords = {"de", "e", "a", "o", "que", "do", "da", "com", "no", "na", "os", "as", "um", "uma", "é", "em"}

# Verificar se a coluna 'Descrição' existe
if 'Descrição' in df.columns:
    # Juntar todas as descrições
    texto_completo = ' '.join(df['Descrição'].dropna())
    
    # Processar o texto com spaCy
    doc = nlp(texto_completo)
    
    # Coletar palavras relevantes e suas categorias
    entidades = [(ent.text, ent.label_) for ent in doc.ents if ent.text.lower() not in stopwords]
    
    # Contar as palavras mais frequentes
    contagem_palavras = Counter(entidades)
    
    # Obter as 10 palavras mais comuns
    palavras_comuns = contagem_palavras.most_common(10)
    
    # Exibir no prompt
    print("Palavras mais frequentes e suas categorias:")
    for (palavra, categoria), qtd in palavras_comuns:
        print(f"{palavra} - {qtd} vezes - {categoria}")
    
    # Gerar gráfico de barras
    palavras, quantidades = zip(*[(p[0], qtd) for p, qtd in palavras_comuns])
    categorias = [p[1] for p, qtd in palavras_comuns]
    
    plt.figure(figsize=(12, 6))
    plt.bar(palavras, quantidades, color='skyblue')
    plt.title('Top 10 Palavras Mais Frequentes com Categorias')
    plt.xlabel('Palavras')
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
    
    # Adicionar as categorias acima das barras
    for i, cat in enumerate(categorias):
        plt.text(i, quantidades[i] + 0.5, cat, ha='center')

    plt.tight_layout()
    plt.show()

else:
    print("Coluna 'Descrição' não encontrada.")
