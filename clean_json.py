
"""clean_json.py  (auto‑detect edition)

Run it with *no arguments* and it will:

1. Look in the current working directory for the first .json file whose
   name does NOT contain the word "clean".
2. Create an output file called "<stem>_clean.jsonl" in the same folder.
3. Clean, structure and chunk the text so it’s ready for embedding / RAG.

You can still override anything with CLI flags:

    python clean_json.py --input myfile.json --output out.jsonl --max-tokens 512

Dependencies:
    pip install ftfy tiktoken
"""

import argparse
import json
import re
import uuid
from pathlib import Path
from typing import Iterable, List, Union

import ftfy
import tiktoken


# ---------- basic text cleaning ------------------------------------------------
def clean_line(line: str) -> str:
    line = ftfy.fix_text(line)                     # fix mojibake
    line = re.sub(r"\s+", " ", line).strip()   # collapse whitespace
    line = re.sub(r"^[•\-–—]\s*", "", line)    # strip bullets
    return line


_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def chunk_text(text: str, tok, max_tokens: int) -> Iterable[str]:
    sentences = _SENT_SPLIT.split(text)
    buf: List[str] = []
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


# ---------- JSON flattening ----------------------------------------------------
def iter_strings(obj: Union[dict, list, str], text_key: str) -> Iterable[str]:
    """Walk arbitrary JSON and yield every string we can find."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_strings(item, text_key)
    elif isinstance(obj, dict):
        if text_key in obj and isinstance(obj[text_key], str):
            yield obj[text_key]
        for v in obj.values():
            yield from iter_strings(v, text_key)


# ---------- main processing ----------------------------------------------------
def process_lines(lines: List[str], tok, max_tokens: int):
    docs = []
    section = subsection = None
    buffer: List[str] = []

    def flush():
        nonlocal buffer, docs
        if not buffer:
            return
        block = " ".join(buffer)
        buffer = []
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

    for raw_line in lines:
        line = clean_line(raw_line)
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


# ---------- entry‑point --------------------------------------------------------
def autodetect_json() -> Path:
    p = Path("allCHCdata_clean_lines.json")
    if not p.exists():
        raise FileNotFoundError("allCHCdata_clean_lines.json not found!")
    print(f"[auto] Using {p} as input file")
    return p

def main():
    parser = argparse.ArgumentParser(...)
    # (flags definition stays the same)
    args = parser.parse_args()

    # Auto‑detect input / output if not provided
    if args.input is None:
        args.input = autodetect_json()
    if args.output is None:
        args.output = Path("organized_chc_data.jsonl")
        print(f"[auto] Writing output to {args.output}")


if __name__ == "__main__":
    main()
