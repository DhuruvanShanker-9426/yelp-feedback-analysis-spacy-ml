import spacy

nlp = spacy.load("en_core_web_md")

negation_words = {"not", "no", "never", "n't"}

def text_preprocessing(text):
    doc = nlp(text.lower())

    tokens = []

    for token in doc:
        if token.is_punct or token.is_space:
            continue

        if token.text in negation_words:
            tokens.append(token.text)
            continue

        if token.is_alpha and not token.is_stop:
            tokens.append(token.lemma_)

    cleaned_text = " ".join(tokens)

    return cleaned_text


def text_to_vector(text):
    doc = nlp(text)
    return doc.vector