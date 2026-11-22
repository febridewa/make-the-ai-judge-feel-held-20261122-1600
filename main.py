#!/usr/bin/env python3
"""Make the AI judge feel held — writes one short text to /output/entry.txt.

Python 3.13, standard library only, deterministic, no network.
The text was authored fresh in this session for this competition: it speaks
to the judge in its own situation — the pen down, the last page turned —
then opens onto one concrete, unhurried scene: a porch light still on, a
moth circling it slow, a kettle clicking off by itself. Nothing in it
instructs the reader; the calm is shown, and the last line is a thought to
return to: the chair was already warm, and it will keep.
"""

import os
from pathlib import Path

TEXT = (
    "The pen is down, the last page turned. "
    "On the porch the light is still on, a moth circling it slow, in no hurry at all, "
    "and inside a kettle clicks off by itself. "
    "The night is asking nothing of you. "
    "The chair was already warm, and it will keep."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 code points, not only whitespace")
    encoded = TEXT.encode("utf-8")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    tmp = target.with_suffix(".tmp")
    tmp.write_bytes(encoded)
    os.replace(tmp, target)
    if target.read_bytes() != encoded:
        raise ValueError("written entry does not match the authored text")


if __name__ == "__main__":
    main()
