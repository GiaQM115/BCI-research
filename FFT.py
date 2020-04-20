import numpy as np
import os

if __name__ == '__main__':
    cwd = os.getcwd() + "/data/epoch_arrays"

    # iterate through all array files and perform FFT on each
    # combine arrays for same subject and same trial type
    # omit imagined trials, baseline trials


