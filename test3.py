def is_magic_number(n):
    digits = [int(d) for d in str(n)]
    counts = {}
    for digit in digits:
        if digit in counts:
            counts[digit] += 1
        else:
            counts[digit] = 1
    for digit, count in counts.items():
        if count != digit:
            return False
    return True

print(is_magic_number(224444))
