def is_magic_number(n):
    digits = [int(digit) for digit in str(n)]
    for i in range(1, max(digits)+1):
        if digits.count(i)!=0 and digits.count(i)!=i:
            return False
    return True

print(is_magic_number(44333))
