import mne
import numpy as np

if __name__ == '__main__':
    # load the data
    raw = mne.io.read_raw_edf("data/")
    print(raw)
    print(raw.info)

    # plot the data for each channel
    # block to prevent window from closing when program finishes
    raw.plot(block=True)



