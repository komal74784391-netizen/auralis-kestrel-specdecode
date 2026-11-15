def accept(logits, tokens):
    return logits.argmax(-1).eq(tokens)
