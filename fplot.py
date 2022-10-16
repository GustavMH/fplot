#!/usr/bin/env python3
import matplotlib.pyplot as plt

idx_ref = lambda val, tup: val if len(tup) == 0 else idx_ref(val[tup[0]], tup[1:])

# should be replaced, by more general solution
def dim_range(*shape):
    nr, nc, *r = [*shape, None, None, None] # eww
    if not nr: return [[]]                     # case 1
    if not nc: return [[i] for i in range(nr)] # case 2... so on
    return [(i,j) for i in range(nr) for j in range(nc)]

get_shape = lambda lst: (len(lst), *get_shape(lst[0])) if isinstance(lst, list) else ()

# should also be replaced, dont know how
def split_dict(d, keys):
    return [*[[k,v] for k,v in d.items() if k in keys][0],
            dict([[k,v] for k,v in d.items() if k not in keys])]

# getattr should remove the if chunk
def subplots(t, val, axs, dims, args):
    for idx in dim_range(*dims):
        if t == "plot"   : idx_ref(axs, idx).plot   (*idx_ref(val, idx), **args)
        if t == "img"    : idx_ref(axs, idx).imshow ( idx_ref(val, idx), **args)
        if t == "scatter": idx_ref(axs, idx).scatter(*idx_ref(val, idx), **args)
        if t == "bar"    : idx_ref(axs, idx).bar    (*idx_ref(val, idx), **args)

def stack(*layers):
    shape    = get_shape(list(layers[0].values())[0])[:len(shape)-2]
    fig, axs = plt.subplots(*[1,*shape][-2:])
    for l in layers:
        t, val, args = split_dict(l, ["plot", "img", "scatter", "bar"])
        subplots(t, val, axs, shape, args)

def fplot(*args, style_=None):
    stack(*args)
    style = style_ if style_ else {}
    for k, v in style.items():
        {"title":  plt.title,
         "ylabel": plt.ylabel,
         "xlabel": plt.xlabel,
         "legend": plt.legend}[k](v)
