import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def run_test(backend, align):
    print('########## TEST ##########')
    print('Switching to backend:', backend)
    plt.switch_backend(backend)

    x = np.logspace(-2, 3)
    y = 1 / (np.exp(1 / x) - 1)

    fig = plt.figure(1, figsize=(4, 4))
    plt.loglog(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.tight_layout()

    ax = plt.gca()
    ax.yaxis.set_ticklabel_horizontal_alignment(align)
    print('Setting alignment:', align)
    fname = 'outcome_{0}_{1}.png'.format(backend, align)
    plt.savefig(fname)
    print('Saved as: ', fname)


# Backends acquired by getting all matplotlib backends and discarding the ones that are not able to be switched to
# without installing extra software
backends = ['agg', 'pdf', 'pgf', 'ps', 'svg', 'template', 'tkagg']
aligns = ['right', 'left', 'center']

for backend in backends:
    for align in aligns:
        run_test(backend, align)
