#trimmed mean
from statistics import mean
from scipy import stats
Estimates=[ 34, 12, 56, 78, 23, 90, 45, 67, 89, 10, 25, 37, 48, 59, 60, 71, 82, 93, 14, 15
]
Estimates.sort()
trim=int(0.1*len(Estimates))
Estimates=Estimates[trim:]
Estimates=Estimates[:len(Estimates)-trim]
trimmed_mean=mean(Estimates)
print(trimmed_mean)
m=stats.trim_mean(Estimates,0.1)
print(m)