import matplotlib
import matplotlib.pyplot as plt

CBcdict={
    'Bl':(0,0,0),
    'Or':(.9,.6,0),
    'SB':(.35,.7,.9),
    'bG':(0,.6,.5),
    'Ye':(.95,.9,.25),
    'Bu':(0,.45,.7),
    'Ve':(.8,.4,0),
    'rP':(.8,.6,.7),
}

##Two color gradient maps
CB2cm={}
for key in CBcdict:
    for key2 in CBcdict:
        if key!=key2: CB2cm[key+key2]=matplotlib.colors.LinearSegmentedColormap.from_list('CMcm'+key+key2,[CBcdict[key],CBcdict[key2]])

##Two color gradient maps with white in the middle
CBWcm={}
for key in CBcdict:
    for key2 in CBcdict:
        if key!=key2: CBWcm[key+key2]=matplotlib.colors.LinearSegmentedColormap.from_list('CMcm'+key+key2,[CBcdict[key],(1,1,1),CBcdict[key2]])

##Two color gradient maps with Black in the middle
CBBcm={}
for key in CBcdict:
    for key2 in CBcdict:
        if key!=key2: CBBcm[key+key2]=matplotlib.colors.LinearSegmentedColormap.from_list('CMcm'+key+key2,[CBcdict[key],(0,0,0),CBcdict[key2]])

##Change default color cycle
matplotlib.rcParams['axes.color_cycle'] = [CBcdict[c] for c in sort(CBcdict.keys())]




