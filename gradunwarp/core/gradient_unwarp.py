### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the gradunwarp package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
import argparse as arg
import logging
import globals

log = globals.get_logger()


def argument_parse_gradunwarp():
    '''Arguments parser from the command line
    '''
    # initiate
    p = arg.ArgumentParser(version=globals.VERSION, usage=globals.usage)

    # required arguments
    p.add_argument('infile', action='store')
    p.add_argument('outfile', action='store')
    p.add_argument('vendor', action='store', choices=['siemens', 'ge'])

    coef_grp = p.add_mutually_exclusive_group(required=True)
    coef_grp.add_argument('-g', '--gradfile', dest='gradfile')
    coef_grp.add_argument('-c', '--coeffile', dest='coeffile')

    # optional arguments
    p.add_argument('-w', '--warp', action='store_true', default=False)
    p.add_argument('-n', '--nojacobian', dest='nojac', action='store_true',
                  default=False)
    p.add_argument('--verbose', action='store_true', default=False)

    return p.parse_args()


class GradientUnwarpRunner(object):
    ''' Takes the option datastructure after parsing the commandline.
    run() method performs the actual unwarping
    write() method performs the writing of the unwarped volume
    '''
    def __init__(self, args):
        ''' constructor takes the option datastructure which is the
        result of (options, args) = parser.parse_args()
        '''
        self.args = args

        log.setLevel(logging.INFO)
        if hasattr(self.args, 'verbose'):
            log.setLevel(logging.DEBUG)

    def run(self):
        pass

    def write(self):
        pass


if __name__ == '__main__':
    args = argument_parse_gradunwarp()

    grad_unwarp = GradientUnwarpRunner(args)

    grad_unwarp.run()

    grad_unwarp.write()