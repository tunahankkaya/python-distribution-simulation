import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


mean=5
std=0.01
size = 1000000

data = np.random.normal(mean,std,size)
#print(data)

plt.hist(data,bins=100,density=True, alpha=0.6)
plt.xlabel("çap(mm)")
plt.ylabel("Yoğunluk")
plt.title("Fabrikada üretilen cıvataların milimetre cinsinden çapı")

x = np.linspace(mean-(4*std),mean+(4*std),1000)
pdf_y = stats.norm.pdf(x,loc=mean,scale=std) #olasılık yoğunluk fonksiyonu
cdf_y = stats.norm.cdf(x,loc=mean,scale=std) #birikimli dağılım

ax1= plt.gca() #gca => get current axis
ax2 = ax1.twinx()

ax2.plot(x,cdf_y,label="CDF",color="red",zorder=10)
ax1.plot(x,pdf_y,label="PDF",color="green",zorder=2)

plt.show()




