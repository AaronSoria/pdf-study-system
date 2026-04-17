from extractor import extract_text
from chunker import chunk_text
from processor import process_chunk
from aggregator import aggregate

def run(pdf_path):
    text = extract_text(pdf_path)
    chunks = chunk_text(text)

    results = []
    for chunk in chunks:
        results.append(process_chunk(chunk))

    final = aggregate(results)
    # 🔥 Segunda pasada (refinamiento global)
    final_refined = process_chunk(
    final,
    model="deepseek-coder-v2:16b")

    with open("output.md", "w") as f:
        f.write(final_refined)

if __name__ == "__main__":
    run("input.pdf")