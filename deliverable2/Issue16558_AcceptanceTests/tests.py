import numpy as np
import matplotlib.pyplot as plt

backends = ['pdf', 'svg', 'pgf']
draws = {
    "FIGURE": "figuredraw",
    "CANVAS": "canvasdraw"
}

def run_test(backend, type):
    plt.switch_backend('pdf')
    fig, ax = plt.subplots(figsize=(6, 3.0), ncols=2, nrows=1,
                           constrained_layout=True, sharey=True)
    fig.set_constrained_layout_pads(wspace=0.03)

    ax[0].plot(np.arange(4), 'r', label=r'Really longgggg label 1')
    ax[1].plot(np.arange(5), 'b', label=r'Really longgggg label 2')
    (leg_h0, leg_lab0) = ax[0].get_legend_handles_labels()
    (leg_h1, leg_lab1) = ax[1].get_legend_handles_labels()

    # add a legend to one of the axes to make space at the top of the figure
    leg0 = ax[0].legend(leg_h0, leg_lab0, loc='lower center',
                        bbox_to_anchor=(0.5, 1.07))

    leg0.set_in_layout(True)  # force to steal space from top of the figure

    # Trigger a draw (required for constrained_layout to work)
    if (type == draws['FIGURE']):
        fig.draw(fig.canvas.get_renderer())
    elif (type == draws['CANVAS']):
        fig.canvas.draw()

    # Thanks constrained_layout, your work is done! turning you off now
    fig.set_constrained_layout(False)

    # Remove legend from axes and add a figure legend
    # which includes entries from both axes
    leg0.remove() 
    fig_leg = fig.legend(*zip(leg_h0, leg_h1), *zip(leg_lab0, leg_lab1),
                         loc='lower center', ncol=2, columnspacing=5,
                         bbox_to_anchor=(0.5, 0.85))
    fig.savefig('test_{0}_{1}.png'.format(backend, type), dpi=200)

for backend in backends:
    run_test(backend, draws['FIGURE'])
    run_test(backend, draws['CANVAS'])