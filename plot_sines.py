#!/usr/bin/env python

"""
    This script will plot a variable number of sine waves of increasingly
    doubled frequency as determined by input script arguments.  The plot
    will be rendered to the local matplotlib backend as well as optionally
    saved to a file, as determined by another input argument.
"""
import numpy as np
from matplotlib import pyplot as plt


def construct_sines(n):
    """
        Construct the x axis and the sines depending on the
        integer number provided.

        Returns x, y numpy 1D arrays
    """
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.zeros(len(x))
    for i in range(n):
        y += np.sin(2 * i * x)
    y = np.array(y) / max(y)    
    return x, y


def plot_function(x, y, title=None, filename=None):
    """
        Plot the function based on the numpy arrays provided.

        If optional keyword argument filename is provided, save
        the figure there
    """

    if title is None:
        plt.title('Plot of X and Y')
    else:
        plt.title(str(title))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xticks

    if not filename:
        plt.savefig(filename)

    plt.show()


def main(options):
    """
        Main function to handle the input arguments and do the work
    """
    pass

if __name__ == '__main__':
    # Script arguments go here
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-N', action='store', dest='N',
                    help='Store number of sines', type = int, required = True)  
    parser.add_argument('--title', action='store', dest='title',
                    help='Store the tile')  
    parser.add_argument('--file', action='store', dest='filename',
                    help='Store the file')
    
    options = parser.parse_args()

    main(options)
