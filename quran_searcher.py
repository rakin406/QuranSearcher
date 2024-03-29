#!/usr/bin/env python3
"""Search words in the Holy Quran."""

# Font configuration
BOLD = "\033[1m"
ENDC = "\033[0m"

while True:
    keyword = input("Enter word: ")
    if keyword.strip() == "":
        continue
    keyword = keyword.lower().split()[0]  # Get only first word
    keywords = [
        keyword,
        keyword + "s",
        keyword + "es",
        keyword + "ies",
        keyword + ".",
        keyword + ",",
        keyword + ":",
        keyword + ";",
        keyword + "?",
        keyword + "!",
    ]
    print()

    with open("Quran.txt", "r", encoding="utf-8") as quran:
        for line in quran:
            modified_line = line.lower().split()
            check = any(item in keywords for item in modified_line)
            if check is True:
                words = line.split()
                for i in words:
                    # Make keyword bold in line
                    if i.lower() in keywords:
                        print(BOLD, end="")
                    else:
                        print(ENDC, end="")

                    if i == words[-1]:
                        print(i)
                    else:
                        print(i, end=" ")
                print(ENDC)
