def is_magic_number(n):
    digits = [int(digit) for digit in str(n)]
    counts = [digits.count(i) for i in range(10)]
    for i in range(10):
        if counts[i] != i:
            return False
    return True

print(is_magic_number(122))
