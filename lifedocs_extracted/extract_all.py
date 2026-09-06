import sys, os, glob
import pymupdf

SRC = r"D:\god_ai\timeofmylife\lifedocs_extracted\lifedocs"
DST = r"D:\god_ai\timeofmylife\lifedocs_extracted\lifedocs_text"
os.makedirs(DST, exist_ok=True)

pdfs = sorted(glob.glob(os.path.join(SRC, "*.pdf")))
print(f"{len(pdfs)} PDFs found")
for p in pdfs:
    base = os.path.splitext(os.path.basename(p))[0]
    out = os.path.join(DST, base + ".txt")
    try:
        doc = pymupdf.open(p)
        parts = []
        total = 0
        for i, page in enumerate(doc):
            t = page.get_text("text")
            total += len(t)
            parts.append(f"\n===== PAGE {i+1}/{doc.page_count} =====\n{t}")
        doc.close()
        with open(out, "w", encoding="utf-8", errors="replace") as f:
            f.write("".join(parts))
        print(f"OK   {total:>8} chars  {base[:80]}")
    except Exception as e:
        print(f"FAIL {base[:80]}  ->  {e}")
