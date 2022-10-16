#!/usr/bin/env python3
import matplotlib.pyplot as plt

flat_n = lambda lsts, n: lsts if n <= 1 else flat_n([e for sl in lsts for e in sl], n-1)
get_shape = lambda lst: (len(lst), *get_shape(lst[0])) if isinstance(lst, list) else ()

def subplots(t, val, axs, args):
    for ax, v in zip(axs, val):
        if t == "img": ax.imshow (v, **args)
        else: getattr(ax, t)(*v, **args)

def stack(*layers):
    shape = get_shape(list(layers[0].values())[0])[:-2]
    axs   = flat_n(plt.subplots(*shape)[1], len(shape))
    for l in layers:
        t, val = [[k,v] for k,v in l.items() if k     in ["plot", "img", "scatter", "bar"]][0]
        args   = [[k,v] for k,v in l.items() if k not in ["plot", "img", "scatter", "bar"]]
        subplots(t, flat_n(val, len(shape)), axs, dict(args))

def fplot(*args, style={}):
    stack(*args)
    for k, v in style.items():
        getattr(plt, k)(v)
