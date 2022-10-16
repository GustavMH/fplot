#!/usr/bin/env python3
import matplotlib.pyplot as plt

idx_ref = lambda val, tup: val if len(tup) == 0 else idx_ref(val[tup[0]], tup[1:])
flat_n = lambda lsts, n: lsts if n == 0 else flat_n([e for sl in lsts for e in sl], n-1)

# should be replaced, by more general solution
def dim_range(*shape):
    nr, nc, *r = [*shape, None, None, None] # eww
    if not nr: return [[]]                     # case 1
    if not nc: return [[i] for i in range(nr)] # case 2... so on
    return [(i,j) for i in range(nr) for j in range(nc)]

get_shape = lambda lst: (len(lst), *get_shape(lst[0])) if isinstance(lst, list) else ()

def subplots(t, val, axs, dims, args):
    for idx in dim_range(*dims):
        if t == "img": idx_ref(axs, idx).imshow ( idx_ref(val, idx), **args)
        else: getattr(idx_ref(axs, idx), t)(*idx_ref(val, idx), **args)

def stack(*layers):
    shape    = get_shape(list(layers[0].values())[0])[:-2]
    # Maybe the axs getter can be replaced by flattening the input and axs
    fig, axs = plt.subplots(*shape)
    for l in layers:
        plot = [[k,v] for k,v in l.items() if k     in ["plot", "img", "scatter", "bar"]]
        args = [[k,v] for k,v in l.items() if k not in ["plot", "img", "scatter", "bar"]]
        subplots(*plot[0], axs, shape, dict(args))

def fplot(*args, style_=None):
    stack(*args)
    style = style_ if style_ else {}
    for k, v in style.items():
        {"title":  plt.title,  "ylabel": plt.ylabel,
         "xlabel": plt.xlabel, "legend": plt.legend}[k](v)
