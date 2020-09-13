import math

metrics = {
    "euclidean":    lambda x, y: sum([abs(x[i] - y[i]) ** 2 for i in range(len(x))]) ** (1 / 2),
    "manhattan":    lambda x, y: sum([abs(x[i] - y[i]) for i in range(len(x))]),
    "chebyshev":    lambda x, y: max([abs(x[i] - y[i]) for i in range(len(x))])
}

kernels = {
    "uniform":      lambda x: 0 if abs(x) >= 1 else 1 / 2,
    "triangular":   lambda x: 0 if abs(x) >= 1 else 1 - abs(x),
    "epanechnikov": lambda x: 0 if abs(x) >= 1 else 3 / 4 * (1 - x ** 2),
    "quartic":      lambda x: 0 if abs(x) >= 1 else 15 / 16 * (1 - x ** 2) ** 2,
    "triweight":    lambda x: 0 if abs(x) >= 1 else 35 / 32 * (1 - x ** 2) ** 3,
    "tricube":      lambda x: 0 if abs(x) >= 1 else 70 / 81 * (1 - abs(x) ** 3) ** 3,
    "cosine":       lambda x: 0 if abs(x) >= 1 else math.pi / 4 * math.cos(math.pi / 2 * x),
    "gaussian":     lambda x: 1 / (math.sqrt(2 * math.pi)) * math.e ** (-0.5 * x ** 2),
    "logistic":     lambda x: 1 / (math.e ** x + 2 + math.e ** (-x)),
    "sigmoid":      lambda x: 1 / (math.e ** x + math.e ** (-x)) * 2 / math.pi
}

windows = {
    "fixed":        lambda distances, h: h,
    "variable":     lambda distances, h: sorted(distances)[h]
}

n, m = [int(i) for i in input().split()]
d = [[int(j) for j in input().split()] for i in range(n)]
q = [int(i) for i in input().split()]
metric, kernel, window, h = input(), input(), input(), int(input())

x, y = [], []
for i in range(n):
    x.append([d[i][j] for j in range(m)])
    y.append(d[i][m])

distances = list(map(metrics[metric], x, [q for i in range(n)]))
w = windows[window](distances, h)

weight_sum, result = 0, 0
for i, distance in enumerate(distances):
    weight = kernels[kernel](distance / w if w != 0 else 0) if distance == 0 or w != 0 else 0
    weight_sum += weight
    result += weight * y[i]
print(result / weight_sum if weight_sum != 0 else sum(y) / n)
