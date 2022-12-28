import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def obt_legends():
    """Function to get the mpatches for plotting labels

    Returns:
        List: List of patches
    """
    bp = mpatches.Patch(color='b', label='One Max')
    rp = mpatches.Patch(color='r', label='Dec One Max')
    gp = mpatches.Patch(color='g', label='K Dec One Max')
    return [bp, rp, gp]


def plotting(vals, opt_probs, ea_algs):
    """Plotting the evolutionary algorithm performance

    Args:
        vals (List): Maximum values from the result of Evolutionary algorithms
        opt_probs (str or Dict keys): String with name of evolutionary
            algorithm or Dict keys when comparing among all the algorithms
            and objective functions
        ea_algs (str or Dict keys):  String with name of evolutionary
            algorithm or Dict keys when comparing among all the algorithms
            and objective functions
    """
    print(ea_algs)
    if len(vals) == 1:
        plt.plot(vals[0], label=opt_probs)
        plt.xlabel('Number of epochs')
        plt.ylabel('Maximum Value')
        plt.title(f'Solving {opt_probs} with {ea_algs}')
        plt.legend()
    else:
        cols = ['b', 'r', 'g', 'y', 'black', 'purple']
        _, axes = plt.subplots(nrows=len(ea_algs), figsize=(18, 10))
        c = 0
        for alg in range(len(ea_algs)):
            for solver, col in zip(range(len(opt_probs)), cols):
                axes[alg].plot(vals[c], color=col)
                axes[alg].set_xlabel('Number of epochs')
                axes[alg].set_ylabel('Maximum Value')
                axes[alg].set_title(f'Solver: {list(ea_algs)[alg]}')
                axes[alg].legend(handles=obt_legends()[:len(opt_probs)])
                c += 1
    plt.tight_layout()
    plt.show()
