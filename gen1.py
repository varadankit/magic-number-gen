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

def generate_magic_numbers(start, end):
    magic_numbers = []
    for n in range(start, end+1):
        if is_magic_number(n):
            magic_numbers.append(n)
    return magic_numbers

print(generate_magic_numbers(1,10**6))
