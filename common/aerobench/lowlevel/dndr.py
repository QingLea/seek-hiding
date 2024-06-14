'''
Stanley Bak
F16 GCAS in Python
dndr function
'''

import numpy as np
from common.aerobench.util import fix, sign

def dndr(alpha, beta):
    'dndr function'

    a = np.array([[-.018, -.052, -.052, -.052, -.054, -.049, -.059, -.051, -.030, -.037, -.026, -.013], \
        [-.028, -.051, -.043, -.046, -.045, -.049, -.057, -.052, -.030, -.033, -.030, -.008], \
        [-.037, -.041, -.038, -.040, -.040, -.038, -.037, -.030, -.027, -.024, -.019, -.013], \
        [-.048, -.045, -.045, -.045, -.044, -.045, -.047, -.048, -.049, -.045, -.033, -.016], \
        [-.043, -.044, -.041, -.041, -.040, -.038, -.034, -.035, -.035, -.029, -.022, -.009], \
        [-.052, -.034, -.036, -.036, -.035, -.028, -.024, -.023, -.020, -.016, -.010, -.014], \
        [-.062, -.034, -.027, -.028, -.027, -.027, -.023, -.023, -.019, -.009, -.025, -.010]], dtype=float).T

    s = .2 * alpha
    k = fix(s)
    if k <= -2:
        k = -1

    if k >= 9:
        k = 8

    da = s - k
    l = k + fix(1.1 * sign(da))
    s = .1 * beta
    m = fix(s)
    if m <= -3:
        m = -2

    if m >= 3:
        m = 2

    db = s - m
    n = m + fix(1.1 * sign(db))
    l = l + 3
    k = k + 3
    m = m + 4
    n = n + 4
    t = a[k-1, m-1]
    u = a[k-1, n-1]
    v = t + abs(da) * (a[l-1, m-1] - t)
    w = u + abs(da) * (a[l-1, n-1] - u)
    return v + (w - v) * abs(db)
