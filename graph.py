import matplotlib.pyplot as plt
import statistics
estimates=[34, 12, 56, 78, 23, 90, 45, 67, 89, 10, 25, 37, 48, 59, 60, 71, 82, 93, 14, 15]
y=[]


estimates.sort()
tv=int(0.1*(len(estimates)))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
for i in range(len(estimates)):
    y.append(5)
plt.plot(estimates,y,'r--')
plt.plot([statistics.mean(estimates)],[5],'ro')
plt.plot([statistics.median(estimates)],[5],'bs')
plt.show()