"""One-line office joke entry.

Writes a single-line joke about office life to /output/entry.txt.
Pure stdlib, no network, no reads outside this repository.
"""

import os

JOKE = (
    "My boss said the meeting could have been an email, so I replied-all "
    "to the invite with the email it should have been - now we're having "
    "a meeting about the email."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
