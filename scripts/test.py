import os
import argparse


def parseargs():
    """
    specify command line arguments
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', '-act', action='store', dest='act_name',
                        type=str.lower,
                        default='attach',
                        help='action (default: %(default)s)'
                        )
    parser.add_argument('--policy', '-p', action='store', dest='pl_name',
                        type=str.lower,
                        default='terraform-sentinel-policies-aws',
                        help='action (default: %(default)s)'
                        )
    parser.add_argument('--workspace', '-w', action='store', dest='ws_name',
                        type=str.lower,
                        default='tian02-devl-etss-tian02ws',
                        help='action (default: %(default)s)'
                        )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    prog_name = os.path.basename(__file__)
    home_dir = os.path.expanduser("~")
    print('{0}: home dir = {1}'.format(prog_name, home_dir))
    options = parseargs()
    task = options.act_name
    pol_sets = options.pl_name
    wk_space = options.ws_name
    print('{0}: action = {1} - policy = {2} - workspace = {3}'.format(prog_name, task, pol_sets, wk_space))

