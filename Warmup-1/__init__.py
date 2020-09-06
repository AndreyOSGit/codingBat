def sleep_in(weekday, vacation):
    SLEEP_IN = False
    if weekday == False or vacation == True:
        SLEEP_IN = True

    return SLEEP_IN


print(sleep_in(True, False))


def monkey_trouble(a_smile, b_smile):
    WE_ARE_IN_TROUBLE = False
    if (a_smile and b_smile) == True or not (a_smile or b_smile) == True:
        WE_ARE_IN_TROUBLE = True

    return WE_ARE_IN_TROUBLE


print(monkey_trouble(True, False))


def sum_double(a, b):
    c = 0
    if a != b:
        c = a + b
    elif a == b:
        c = (a + b) * 2

    return c


print(sum_double(3, 3))
print(sum_double(3, 4))


def diff21(n):
    c = abs(21 - n)
    if n > 21:
        c = 2 * abs(21 - n)

    return c


print(diff21(115))


def parrot_trouble(talking, hour):
    WE_ARE_IN_TROUBLE = True
    if (talking == True and (7 <= hour <= 20)) or talking == False:
        WE_ARE_IN_TROUBLE = False

    return WE_ARE_IN_TROUBLE


print(parrot_trouble(True, 6))


def makes10(a, b):
    c = False
    if (a + b == 10) or (a == 10 or b == 10):
        c = True

    return c


print(makes10(1, 5))


def missing_char(str, n):
    c = ''
    if 0 <= n <= (len(str)):
        c = str[0:n] + str[n+1:len(str)]

    return c

print(missing_char('testing', 6))

