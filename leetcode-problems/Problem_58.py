def lengthOfLastWord(s: str) -> int:
    words = s.strip().split()

    if not words:
        return 0

    return len(words[-1])


print(lengthOfLastWord('Hello World!'))
print(lengthOfLastWord('  Hello World'))
