#!/usr/bin/env python

"""
    This script will plot a variable number of sine waves of increasingly
    doubled frequency as determined by input script arguments.  The plot
    will be rendered to the local matplotlib backend as well as optionally
    saved to a file, as determined by another input argument.
"""


def construct_sines(n):
    """
        Construct the x axis and the sines depending on the
        integer numner provided.

        Returns x, y numpy 1D arrays
    """
    pass


def plot_function(x, y, filename=None):
    """
        Plot the function based on the numpy arrays provided.

        If optional keyword argument filename is provided, save
        the figure there
    """
    pass


def main(options):
    """
        Main function to handle the input arguments and do the work
    """
    pass

if __name__ == '__main__':
    # Script arguments go here
    options = None

    main(options)
