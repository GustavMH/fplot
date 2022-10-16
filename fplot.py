#!/usr/bin/env python3
import matplotlib.pyplot as plt

idx_ref = lambda val, tup: val if len(tup) == 0 else idx_ref(val[tup[0]], tup[1:])

def dim_range(*shape):
    nr, nc, *r = [*shape, None, None, None]
    if not nr: return [[]]
    if not nc: return [[i] for i in range(nr)]
    return [(i,j) for i in range(nr) for j in range(nc)]

get_shape = lambda lst: (len(lst), *get_shape(lst[0])) if isinstance(lst, list) else ()

def split_dict(d, keys):
    return [*[[k,v] for k,v in d.items() if k in keys][0],
            dict([[k,v] for k,v in d.items() if k not in keys])]

def subplots(t, val, axs, dims, args):
    for idx in dim_range(*dims):
        if t == "line"   : idx_ref(axs, idx).plot   (*idx_ref(val, idx), **args)
        if t == "img"    : idx_ref(axs, idx).imshow ( idx_ref(val, idx), **args)
        if t == "scatter": idx_ref(axs, idx).scatter(*idx_ref(val, idx), **args)
        if t == "bar"    : idx_ref(axs, idx).bar    (*idx_ref(val, idx), **args)

def stack(*layers):
    shape    = get_shape(list(layers[0].values())[0])
    fig, axs = plt.subplots(*[1,*shape[:len(shape)-2]][-2:])
    for l in layers:
        t, val, args = split_dict(l, ["plot", "img", "scatter", "bar"])
        subplots(t, val, axs, shape[:len(shape)-2], args)

def fplot(*args, style_=None):
    stack(*args)
    style = style_ if style_ else {}
    for k, v in style.items():
        {"title":  plt.title,
         "ylabel": plt.ylabel,
         "xlabel": plt.xlabel,
         "legend": plt.legend}[k](v)
