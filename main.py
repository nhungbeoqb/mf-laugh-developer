"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny single-line developer excuse to /output/entry.txt.
Python 3.13 stdlib only. Deterministic: the same text on every run.
"""

import os

ENTRY = (
    "Production's down because my 'temporary' fix from 2021 just retired "
    "\u2014 and it took the database password, the cron job, "
    "and my will to live with it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
