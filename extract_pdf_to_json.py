
"""
extract_pdf_to_json.py

Extracts structured, chunked data from allCHCdata.pdf and writes it as:
    organized_chc_data.jsonl

Requires:
    pip install pdfplumber ftfy tiktoken
"""

import json
import re
import uuid
from pathlib import Path

import pdfplumber
import ftfy
import tiktoken


def clean_line(line):
    line = ftfy.fix_text(line)
    line = re.sub(r"\s+", " ", line).strip()
    line = re.sub(r"^[•\-–—]\s*", "", line)
    return line


_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def chunk_text(text, tok, max_tokens):
    sentences = _SENT_SPLIT.split(text)
    buf = []
    count = 0
    for s in sentences:
        n = len(tok.encode(s))
        if count + n > max_tokens and buf:
            yield " ".join(buf)
            buf, count = [], 0
        buf.append(s)
        count += n
    if buf:
        yield " ".join(buf)


def process_lines(lines, tok, max_tokens):
    docs = []
    section = subsection = None
    buffer = []

    def flush():
        nonlocal buffer
        if not buffer:
            return
        block = " ".join(buffer)
        buffer.clear()
        for i, chunk in enumerate(chunk_text(block, tok, max_tokens)):
            docs.append({
                "id": str(uuid.uuid4()),
                "text": chunk,
                "metadata": {
                    "section": section,
                    "subsection": subsection,
                    "chunk": i
                }
            })

    for raw in lines:
        line = clean_line(raw)
        if not line:
            continue
        if line.isupper():
            flush()
            section, subsection = line.title(), None
            continue
        if line.endswith(":"):
            flush()
            subsection = line[:-1]
            continue
        buffer.append(line)
    flush()
    return docs


def extract_text_lines_from_pdf(pdf_path):
    lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                page_lines = text.splitlines()
                lines.extend(page_lines)
    return lines


def main():
    input_pdf = Path("allCHCdata.pdf")
    output_jsonl = Path("organized_chc_data.jsonl")

    if not input_pdf.exists():
        raise FileNotFoundError("Missing allCHCdata.pdf in current directory")

    lines = extract_text_lines_from_pdf(input_pdf)
    tok = tiktoken.get_encoding("cl100k_base")
    docs = process_lines(lines, tok, max_tokens=400)

    with output_jsonl.open("w", encoding="utf-8") as f:
        for d in docs:
            json.dump(d, f, ensure_ascii=False)
            f.write("\n")

    print(f"[done] Wrote {len(docs)} chunks to {output_jsonl}")
    if docs:
        print("[sample]\n" + json.dumps(docs[0], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
