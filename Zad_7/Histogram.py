import matplotlib
import matplotlib.pyplot as plt
import numpy as np

histogramData = np.random.normal(200, 15, (200000))
histogramData.sort()

maximum = histogramData[-1]
minimum = histogramData[0]

num = int(np.sqrt(histogramData.size))
step = (maximum - minimum)/num
steps = np.arange(minimum,maximum,step)
histogram = dict.fromkeys(steps,0)

n = histogramData.size - 1
k = steps.size - 1
while (n >= 0 and k >= 0):
    if histogramData[n] >= steps[k]:
        histogram[steps[k]] += 1
        n -= 1
    else:
        k -= 1

hist = plt.subplot()
hist.bar(histogram.keys(),histogram.values())
plt.show()
