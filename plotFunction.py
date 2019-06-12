#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
set of functions used for plotting colormap
'''

import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mpcol
from matplotlib.colors import LinearSegmentedColormap


def plot_color_gradients(cmap_category, cmap_list, nrows):
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    
    fig, axes = plt.subplots(nrows=nrows)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
    axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

def grayscale_cmap(cmap):
    """Return a grayscale version of the given colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    
    # convert RGBA to perceived grayscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]
        
    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)

def grayify_cmap(cmapname):
    """Return a grayscale version of the colormap"""
    ccmap = plt.cm.get_cmap(cmapname)
    colors = ccmap(np.arange(ccmap.N))
    
    # convert RGBA to perceived greyscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]
    
    return mpcol.LinearSegmentedColormap.from_list(ccmap.name + "_grayscale", colors, ccmap.N)

def show_colormap(cmap):
    "Show colormap and grayscale version (luminance converted version) of colormap"
    im = np.outer(np.ones(10), np.arange(100))
    fig, ax = plt.subplots(2, figsize=(6, 1.5),
                           subplot_kw=dict(xticks=[], yticks=[]))
    fig.subplots_adjust(hspace=0.1)
    ax[0].imshow(im, cmap=cmap)
    ax[1].imshow(im, cmap=grayify_cmap(cmap)) 
    

def view_colormap(cmap):
    """Plot a colormap with its grayscale equivalent"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    
    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))
    
    fig, ax = plt.subplots(2, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])
    
def compare_colormap(cmapname, image):
    """Show image using the specified colormap, a grayscale
       version of that colormap and using the actual grayscale colormap"""
    cmaps = [plt.cm.get_cmap(cmapname), grayify_cmap(cmapname), plt.cm.gray]
    fig, axes = plt.subplots(1, 3, figsize=(20, 5))
    fig.subplots_adjust(wspace=0.05)

    for cmap, ax in zip(cmaps, axes):
        ax.axis("off")
        im = ax.imshow(image, cmap=cmap)
        ax.set_title(cmap.name)
        #fig.colorbar(im, ax=ax)

