import math as m
import cmath


pi = m.pi


nan = m.nan
isnan = m.isnan
log10 = m.log10
log2 = m.log2
log1p = m.log1p


def sgn(z):
    return -1 if z < 0 else 1 if z else 0


def exp(x):
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
        if (isinstance(s, float) and m.isnan(s)) or (isinstance(s, complex) and m.isnan(s.real) and m.isnan(s.imag)):
            break
    return +s


def log(x, base=None):
    if base is not None:
        return log(x) / log(base)

    x = x - 1
    if isinstance(x, complex):
        return log(abs(x)) + cmath.phase(x)
    if abs(x) >= 1:
        return -log(1/(x + 1))
    i, lasts, s, num, sign = 1, 0, x, x, 1
    while s != lasts:
        lasts = s
        i += 1
        num *= x
        sign *= -1
        s += num / i * sign
        if (isinstance(s, float) and m.isnan(s)) or (isinstance(s, complex) and m.isnan(s.real) and m.isnan(s.imag)):
            break
    return +s


def sin(x):
    if isinstance(x, float) or isinstance(x, int):
        x -= sgn(x) * int((abs(x) - float(pi)) / (2 * float(pi)) + 1) * 2 * float(pi)
    elif isinstance(x, complex):
        re = x.real
        x = re - sgn(re) * int((abs(re) - float(pi)) / (2 * float(pi)) + 1) * 2 * float(pi) + x.imag * 1j
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return +s


def cos(x):
    if isinstance(x, float) or isinstance(x, int):
        x -= sgn(x) * int((abs(x) - float(pi)) / (2 * float(pi)) + 1) * 2 * float(pi)
    elif isinstance(x, complex):
        re = x.real
        x = re - sgn(re) * int((abs(re) - float(pi)) / (2 * float(pi)) + 1) * 2 * float(pi) + x.imag * 1j
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return +s


def tan(x):
    res = sin(x) / cos(x)
    return res


def cotan(x):
    res = cos(x) / sin(x)
    return res


def isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0):
    diff = abs(a - b)
    return diff <= abs_tol or diff / max(abs(a), abs(b)) <= rel_tol


if __name__ == "__main__":
    log(-3+1e-6j)
