The script CBcm.py establishes a set of continuous colormaps
for matplotlib based on the color-blind-friendly palette 
developed by Okabe & Ito:

http://jfly.iam.u-tokyo.ac.jp/color/

Their palette is illustrated here:

http://jfly.iam.u-tokyo.ac.jp/color/image/pallete.jpg

Three dictionaries of palettes are established:

    * CB2cm: Linear gradients between each combination of the
             colors in the Okabe & Ito palette
    * CBWcm: 2 color gradient, transitioning to white in the middle
    * CBBcm: 2 color gradient, transitioning to black in the middle

The script 'CBcm_test.py' illustrates the use of these maps

The output figures 'test_palette_*.png' illustrate the palettes
and 'test_scatter.png' illustrates usage

Note that the CBcm.py script will overwrite the default
matplotlib colorcucle defined in matplotlib.rcParams,
but you can easily remove this behavior by deleting
the last line in CBcm.py
