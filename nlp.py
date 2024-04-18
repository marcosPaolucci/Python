import spacy
print(spacy.__version__)
nlp = spacy.load('pt_core_news_sm')

texto = "O spaCy é uma ótima ferramenta para processamento de lingugaem natural."

#tokenizar texto
doc = nlp(texto)

#exibir tokens
for token in doc:
    print(token.text)

texto2 = "O spaCy é uma ferramenta poderosa para processamento de linguagem natural."

doc = nlp(texto2)
for token in doc:
    print(f"Token: {token.text}, Forma básica: {token.lemma_}, Classe gramatical: {token.pos_}, Tag de detalhes: {token.tag_}")
   
texto3 = "Bill Gates fundou a Microsoft em 1975. Ele nasceu em Seattle."
doc = nlp(texto3)
for entidade in doc.ents:
    print(f"Entidade: {entidade.text}, Tipo: {entidade.label_}")

texto4 = "Marcos Paolucci comprou um bom livro."
doc = nlp(texto4)
for token in doc:
    print(f"Palavra: {token.text}, Dependencia: {token.dep_}, Governante:{token.head.text}")


