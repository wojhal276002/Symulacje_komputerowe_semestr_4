def conversion(x, b):
    if x == 0:
        return "0"
    else:
        result = ""
        while x > 0:
            rem = x % b
            x //= b
            result += str(rem)
        return result[::-1]

print(conversion(13,1))




