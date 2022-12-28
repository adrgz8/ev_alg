"""
Testing simple Evolutionary Algorithms with different
Optimization problems

by: Adrian Rodriguez
"""
import argparse
import tools.plots as plots
from evol_algs import pbil, umda, cga
from opt_problems import one_max, dec_one_max


def main():

    # Creating dictionaries for parsing evolutionary algorithms
    EA_OPTIONS = {
        'pbil': pbil,
        'umda': umda,
        'cga': cga
    }

    # Creating dictionary for parsing optimization problems
    OPT_PROB = {
        'one_max': one_max,
        'dec_one_max': dec_one_max,
    }

    # Adding parsers
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--opt_prob',
        type=str,
        help='Choose optimization problem to solve',
        default='one_max',
        required=False
    )
    parser.add_argument(
        '--ea',
        type=str,
        help='Select evolutionary algorithm to solve opt problem',
        default='umda',
        required=False
    )
    parser.add_argument(
        '--compare_all',
        action=argparse.BooleanOptionalAction,
        help='Compare all Evolutionary algorithm with every opt problem',
        required=False
    )
    parser.add_argument(
        '--plotting',
        action=argparse.BooleanOptionalAction,
        help='Plot results',
        required=False
    )
    parser.add_argument(
        '--length',
        type=int,
        help='Choose length of the sequence',
        default=50,
        required=False
    )
    parser.add_argument(
        '--N',
        type=int,
        help='Choose N size',
        default=100,
        required=False
    )
    parser.add_argument(
        '--epochs',
        type=int,
        help='Choose number of epochs',
        default=100,
        required=False
    )
    parser.add_argument(
        '--lr',
        type=float,
        help='Choose learning rate',
        default=0.1,
        required=False
    )
    parser.add_argument(
        '--mutation',
        type=float,
        help='Choose mutation probability',
        default=0.02,
        required=False
    )
    parser.add_argument(
        '--shift',
        type=float,
        help='Choose mutatin shift',
        default=0.05,
        required=False
    )
    args = parser.parse_args()

    # Running algorithm
    if args.compare_all:
        all_max_vals = list()
        for ea_solver in EA_OPTIONS.values():
            for opt_prob in OPT_PROB.values():
                max_vals = ea_solver(
                    length=args.length,
                    N=args.N,
                    lr=args.lr,
                    mutation=args.mutation,
                    shift=args.shift,
                    epochs=args.epochs,
                    method=opt_prob,
                    verbose=False
                )
                all_max_vals.append(max_vals)
        plots.plotting(all_max_vals, OPT_PROB.keys(), EA_OPTIONS.keys())
    else:
        max_vals = EA_OPTIONS[args.ea](
                    length=args.length,
                    N=args.N,
                    lr=args.lr,
                    mutation=args.mutation,
                    shift=args.shift,
                    epochs=args.epochs,
                    method=OPT_PROB[args.opt_prob],
                    verbose=False
                    )
        if args.plotting:
            plots.plotting([max_vals], args.opt_prob, args.ea)


if __name__ == '__main__':
    main()
