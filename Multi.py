# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:32:15 2019

@author: MSI
"""
import matplotlib.pyplot as plt
import numpy as np
def run():
    label = ("Shopping","Board Game","Hang out","Home")
    val=(2,8,2,3)
    plt.pie(val ,labels=label,startangle=90,autopct="%1.2f%%",explode=(0,0.1,0,0))
    plt.axis("equal")
    plt.show()

if __name__ == '__main__':
    run()