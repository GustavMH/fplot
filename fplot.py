#!/usr/bin/env python3
import matplotlib.pyplot as plt

def get_shape(lsts):
    """ Returns the shape of a nested list ala Numpy """
    if hasattr(lsts, '__iter__'):
        return (len(lsts), *get_shape(lsts[0]))
    else:
        return ()

def flatten(lsts):
    """ Flatten a list of lists once """
    return [e for sl in lsts for e in sl]

def flatten_to_depth(lsts, n):
    """ Structure a list to be nested at depth n """
    dims = len(get_shape(lsts))
    if dims > n: return flatten_to_depth(flatten(lsts), n)
    if dims < n: return flatten_to_depth([lsts], n)
    return lsts

def multiplot(t, vals, args={}, style={}):
    """ Plot multiple plot in one figure

    Args:
        t: string annotating the type of plot
        vals: list (x, y) or image data to be plotted
        args: arguments to be passed to the AxisSubplot
        style: arguments to be passed to the figure
    """
    shape    = get_shape(vals)[:-2]
    fig, axs = plt.subplots(*shape)
    axs_ = flatten_to_depth(axs, 1)
    val_ = flatten_to_depth(vals, 3)
    for ax, v in zip(axs_, val_):
        if t == "imshow": ax.imshow(v, **args)
        else: getattr(ax, t)(*v, **args)
        ax.label_outer()
    for k, v in style.items():
        getattr(plt, k)(v)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    # From https://stackoverflow.com/questions/312443
    # Useful for making plots from a list
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
