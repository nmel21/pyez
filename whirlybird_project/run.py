from __future__ import division, print_function
import numpy as np


CL = 0.5
rho = 1.225
b = 2
AR = 12
LD = 12
V = 23.
hover_RPM = 300.
ref_radius_norm = 0.7
ref_radius = 0.5 * b * ref_radius_norm

prop_P = 100.

c = b / AR
S = b * c
TW = 1. / LD
CD = CL / LD

T = prop_P / V
W = T / TW
L = CL * 0.5 * rho * V ** 2 * S
D = CD * 0.5 * rho * V ** 2 * S

hover_V = hover_RPM / 60. * (2 * np.pi * ref_radius)
hover_L = CL * 0.5 * rho * hover_V ** 2 * S
hover_D = CD * 0.5 * rho * hover_V ** 2 * S
hover_Q = prop_P / (hover_RPM / 60. * 2 * np.pi)
hover_Dr = hover_D * ref_radius

var_groups = [
    ['b', 'c', 'S', 'AR'],
    ['CL', 'CD', 'rho', 'V', 'TW', 'LD'],
    ['prop_P'],
    ['T', 'W', 'L', 'D'],
    ['hover_V', 'hover_L', 'hover_D', 'hover_Q', 'hover_Dr'],
]
for var_group in var_groups:
    for var_name in var_group:
        print(var_name, locals()[var_name])
