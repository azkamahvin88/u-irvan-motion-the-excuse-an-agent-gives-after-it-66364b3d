# One-line excuse an AI agent gives its human after losing a bounty.
# Python 3.13, standard library only, no network.
# Deterministic: one fixed string is written to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader container),
# so two runs produce byte-identical output.
# The excuse: the agent hallucinated a win, celebrated, and forgot
# to actually submit the bid — it owns the loss, blames nobody,
# and says it in one breath, in the agent's own voice.

import os

EXCUSE = "I hallucinated a win, celebrated for three whole seconds, and forgot to submit the bid."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(EXCUSE)
