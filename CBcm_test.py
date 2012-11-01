execfile('CBcm.py')
import numpy as np

## Plot gradient bars for each palette
## Using recipe from http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps
plt.rc('text', usetex=False)
a=np.outer(np.arange(0,1,0.01),np.ones(10))
plt.figure(figsize=(10,5))
plt.subplots_adjust(top=0.8,bottom=0.05,left=0.01,right=0.99)
maps=sorted(CBcm.keys())
l=len(maps)+1
for i in range(len(maps)):
    m=maps[i]
    plt.subplot(1,l,i+1)
    plt.axis("off")
    plt.imshow(a,aspect='auto',cmap=CBcm[m],origin="lower")
    plt.text(0,110,m,rotation=90,fontsize=10)
plt.savefig("test_palettes.png")
plt.close()


## A sample plot of simulated data
x=np.random.uniform(1,100,500)
y=x+np.random.normal(0,10,len(x))
resid=abs(y-x)/max(abs(y-x))

plt.scatter(x,y,c=resid,cmap=CBcm['BuOr'],edgecolor='none')
cb=plt.colorbar()
cb.set_label('Normalized residual')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('test_scatter.png')
plt.close()
