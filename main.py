import numpy
import matplotlib.pyplot as plt
# from numba import autojit

# @autojit
def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j

    for i in range(max_iter):
        z = z*z + c
        if (z.real * z.real + z.image * z.imag) >= 4:
            return i

    return max_iter;

