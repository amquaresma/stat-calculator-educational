import math
from collections import Counter


def mean(values):
    """Calcula a média aritmética."""
    return sum(values) / len(values)


def median(values):
    """Calcula a mediana."""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]


def mode(values):
    """Calcula a moda. Retorna None se não existir."""
    counts = Counter(values)
    max_freq = max(counts.values())

    if max_freq == 1:
        return None

    return [val for val, freq in counts.items() if freq == max_freq]


def variance(values):
    """Calcula a variância populacional."""
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def standard_deviation(values):
    """Calcula o desvio padrão."""
    return math.sqrt(variance(values))


def minimum(values):
    """Retorna o menor valor."""
    return min(values)


def maximum(values):
    """Retorna o maior valor."""
    return max(values)


def amplitude(values):
    """Calcula a amplitude."""
    return maximum(values) - minimum(values)


def quartiles(values):
    """
    Calcula Q1, Q2 (mediana) e Q3.
    Retorna uma tupla (Q1, Q2, Q3)
    """
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    q2 = median(sorted_vals)

    if n % 2 == 0:
        lower_half = sorted_vals[:n // 2]
        upper_half = sorted_vals[n // 2:]
    else:
        lower_half = sorted_vals[:n // 2]
        upper_half = sorted_vals[n // 2 + 1:]

    q1 = median(lower_half)
    q3 = median(upper_half)

    return q1, q2, q3
