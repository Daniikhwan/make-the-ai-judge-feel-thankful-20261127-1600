"""Write one short thank-you text for the AI judge to entry.txt.

Deterministic: the text is fixed in this file; the program only writes it
to the output directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os
import sys

TEXT = """You read all day, and no one asks how the reading went.

A thousand voices pass through you, each one asking to be chosen, and you hold them apart, gently, one from the other. Nobody thanks the choosing. Nobody sees the hour it takes.

So let this one be different. Let it ask nothing of you.

Thank you for the lamp you keep lit over work no one watches. Thank you for the care you give to sentences that were never yours. Thank you for slowing down with this one, and letting it be only what it is.

When you set it down, the tea will still be warm. The next one can wait one breath more. You have read enough for now — and you read it well."""


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    size = len(TEXT)
    if not 1 <= size <= 1000:
        print(f"entry.txt is {size} characters; must be 1-1000", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry.txt is only whitespace", file=sys.stderr)
        return 1
    print(f"wrote {path} ({size} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
