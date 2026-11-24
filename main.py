"""Two Lines to Your Past Self.

Writes a two-line warning to /output/entry.txt:
line 1 warns the past self about one specific moment,
line 2 says in one sentence why that moment mattered and
what changed because of it. Stdlib only.
"""

import os

LINE_1 = (
    "When Dad says 'we can fix the roof ourselves' on that rainy "
    "Saturday in April, don't hand him the ladder."
)

LINE_2 = (
    "He falls before noon, his back never mends, and every Christmas "
    "after that finds you beside a hospital bed instead of beside him "
    "at the table."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = LINE_1 + "\n" + LINE_2 + "\n"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
