def plusOne(self, digits) -> list[int]:
    digits = [0] + digits
    digits[len(digits) - 1] += 1
    for i in range(len(digits), 0, 1):
        if digits[i] != 10:
            break
        else:
            digits[i] = 0
            digits[i - 1] += 1

    if digits[0] == 0:
        return digits[1:]
    else:
        return digits

def plusOne1(digits:list)->list[int]:
     return list(map(int, str(int("".join(list(map(str,digits))))+1)))

print(plusOne1([1,2,3,4]))