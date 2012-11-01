"""
This script establishes a set of continuous colormaps
for matplotlib based on the color-blind-friendly palette 
developed by Okabe & Ito:

http://jfly.iam.u-tokyo.ac.jp/color/

Their palette is illustrated here:

http://jfly.iam.u-tokyo.ac.jp/color/image/pallete.jpg

The script 'CBcm_test.py' illustrates the use of these maps

The output figure 'test_palette.png' illustrates the colors
and 'test_scatter.png' illustrates usage
"""

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
CBcm={}
for key in CBcdict:
    for key2 in CBcdict:
        if key!=key2: CBcm[key+key2]=matplotlib.colors.LinearSegmentedColormap.from_list('CMcm'+key+key2,[CBcdict[key],CBcdict[key2]])



##Test
