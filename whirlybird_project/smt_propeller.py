import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt

from smt.surrogate_models import RMTB, RMTC, IDW


scaling = [
    1,
    1,
    1.,
    1,
]

def get_propeller_smt():
    this_dir = os.path.split(__file__)[0]

    xt = np.loadtxt(os.path.join(this_dir, 'xt_data.dat'))
    yt = np.loadtxt(os.path.join(this_dir, 'yt_data.dat'))

    for ind in range(2):
        xt[:, ind] /= scaling[ind]

    xlimits = np.array([
        [xt[:,0].min(), xt[:,0].max()],
        [xt[:,1].min(), xt[:,1].max()],
    ])

    return xt, yt, xlimits

def plot_propeller_smt(xt, yt, limits, interp):
    num = 100
    x = np.zeros((num, 2))

    lins_vars = [
    np.linspace(limits[0][0], limits[0][1], num),
    np.linspace(limits[1][0], limits[1][1], num),
    ]

    #Set slice parameters
    x_vars = [
    0.,       #Blad2
    15          #PitchAngle
    ]

    # for ind in range(4):
    for ind in range(2):
        x_vars[ind] /= scaling[ind]

    nrow = 1
    ncol = 2
    plt.figure(figsize = (10,5))
    plotcounter = 1
    plt.suptitle("Coefficient of Torque/Thrust versus Blade Pitch Angle")

    diff_alphas = [
        3.,
        2.,
        1.,
        -0.,
        -1.,
        -2.,
        -3.
    ]

    for i in diff_alphas:
        x[:, 0] = i
        x[:, 1] = lins_vars[1]
        y = interp.predict_values(x)

        for iy in range(2):
            plt.subplot(nrow, ncol, plotcounter)
            plt.plot(x[:,1], y[:, iy])
            plt.ylim([0,1])
            if plotcounter == 1:
                plt.xlabel("Blade Pitch Angle (Degrees)")
                plt.ylabel("Coefficient of Torque")
                plotcounter = 2
            else:
                plotcounter = 1
                plt.xlabel("Blade Pitch Angle (Degrees)")
                plt.ylabel("Coefficient of Thrust")
    ax = plt.subplot(nrow, ncol, 1)
    ax.legend(["α = 3,", "α = 2", "α = 1", "α = 0", "α = -1", "α = -2", "α = -3"], title = "Blade Angle of Attack (°)")

    plt.tight_layout(rect = [0,0.03,1,0.95])
    plt.savefig('smt_slice.pdf')
    plt.show()

if __name__ == '__main__':
    xt, yt, xlimits = get_propeller_smt()

    interp = RMTC(
        num_elements=50, 
        xlimits = xlimits, nonlinear_maxiter =0, min_energy = True, 
        regularization_weight = 0e-10, 
        smoothness=[1e1,1e3],
        energy_weight=1e3,
        # data_dir = "work",
        print_global=False,
        approx_order = 2,
        extrapolate = True,
    )
    interp.set_training_values(xt, yt)
    interp.train()
# angle of attack of the blade , pitch angle
    x = np.array([
        [-3., 4.99],
    ])
    y = interp.predict_values(x)
    print('C_T:', y[:, 0])
    print('C_Q:', y[:, 1])

    print('min AoA:', xlimits[0, 0])
    print('max AoA:', xlimits[0, 1])
    print('min pitch:', xlimits[1, 0])
    print('max pitch:', xlimits[1, 1])

    plot_propeller_smt(xt, yt, xlimits, interp)