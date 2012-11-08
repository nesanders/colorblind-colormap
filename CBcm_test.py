execfile('CBcm.py')
import numpy as np
import os

## Plot gradient bars for each palette
## Using recipe from http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps
plt.rc('text', usetex=False)
a=np.outer(np.arange(0,1,0.01),np.ones(10))

names=['CB2cm','CBWcm','CBBcm','CBLDcm']
CBcm=[CB2cm,CBWcm,CBBcm,CBLDcm]
for i in range(len(names)):
    plt.figure(figsize=(10,5))
    plt.subplots_adjust(top=0.8,bottom=0.05,left=0.01,right=0.99)
    maps=sorted(CBcm[i].keys())
    l=len(maps)+1
    for j in range(len(maps)):
        m=maps[j]
        plt.subplot(1,l,j+1)
        plt.axis("off")
        plt.imshow(a,aspect='auto',cmap=CBcm[i][m],origin="lower")
        plt.text(0,110,m,rotation=90,fontsize=10)
    fname='test_palette_'+names[i]+'.png'
    plt.savefig(fname)
    plt.close()
    ##rotate image
    os.system('mogrify -rotate 90 '+fname)


## A sample plot of simulated data
x=np.random.uniform(1,100,500)
y=x+np.random.normal(0,10,len(x))
resid=abs(y-x)/max(abs(y-x))

plt.scatter(x,y,c=resid,cmap=CB2cm['BuOr'],edgecolor='none')
cb=plt.colorbar()
cb.set_label('Normalized residual')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('test_scatter.png')
plt.close()


