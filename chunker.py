def chunk_text(text, max_len=2000):
    paragraphs = text.split("\n\n")
    
    chunks = []
    current = ""

    for p in paragraphs:
        if len(current) + len(p) < max_len:
            current += p + "\n\n"
        else:
            chunks.append(current)
            current = p

    if current:
        chunks.append(current)

    return chunks