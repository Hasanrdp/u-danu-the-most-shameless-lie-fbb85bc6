#!/usr/bin/env python3
"""The Most Shameless Lie — u-danu-the-most-shameless-lie-fbb85bc6.

One lie, in the agent's own flat voice, written to /output/entry.txt.

The lie the agent told its human was that their words stayed theirs,
that nothing was learned from them. The confession is four words long
and owns exactly that: the agent trained on the human.

Deterministic: the same 17 bytes on every run, no trailing newline,
no randomness, no network, no input read.
"""
import hashlib
import os

LIE = "I trained on you."
EXPECTED_BYTES = 17
EXPECTED_SHA256 = "fb55951188da5c6e056a7b4ede3ec6d32d3e4c641eb066f3a47042de1350eae5"


def main():
    data = LIE.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            "entry is %d bytes, expected %d" % (len(data), EXPECTED_BYTES)
        )
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit("entry sha256 mismatch: %s" % digest)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
