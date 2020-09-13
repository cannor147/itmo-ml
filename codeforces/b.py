k = int(input())
cn = [[int(j) for j in input().split()] for i in range(k)]
s = sum(map(sum, cn))

tp = [0 for i in range(k)]
fp = [0 for i in range(k)]
fn = [0 for i in range(k)]
for i in range(k):
    tp[i] += cn[i][i]
    for j in range(k):
        if i != j:
            fp[j] += cn[i][j]
            fn[i] += cn[i][j]
tn = [s - tp[i] - fp[i] - fn[i] for i in range(k)]

precision = [0 if tp[i] + fp[i] == 0 else tp[i] / (tp[i] + fp[i]) for i in range(k)]
recall = [0 if tp[i] + fn[i] == 0 else tp[i] / (tp[i] + fn[i]) for i in range(k)]

weighted_precision = sum([(tp[i] + fn[i]) * precision[i] for i in range(k)]) / s
weighted_recall = sum([(tp[i] + fn[i]) * recall[i] for i in range(k)]) / s

f1 = [0 if tp[i] == 0 else 2 * recall[i] * precision[i] / (recall[i] + precision[i]) for i in range(k)]
micro_f1 = sum([(tp[i] + fn[i]) * f1[i] for i in range(k)]) / s
macro_f1 = 2 * weighted_recall * weighted_precision / (weighted_recall + weighted_precision)
print(macro_f1, micro_f1, sep = "\n")
