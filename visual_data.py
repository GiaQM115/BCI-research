import normalization_and_epoching as nae
import numpy as np
import os

if __name__ == '__main__':

    error_log = []

    # iterate through EDF data
    directory = os.getcwd() + "/data/"
    print("Getting data from " + directory)
    for d in os.listdir(directory):
        if d[0] != 'S' and len(d) != 4:
            continue
        for f in os.listdir(directory + d):
            filename = directory + d + "/" + f
            new_filename = directory + "epoch_arrays/" + filename[-11:-4] + ".npy"
            print("reading from " + filename)
            print("writing to " + new_filename)

            # read EDF, normalize, epoch
            raw = nae.normalize_data(filename)
            epochs, ids, events = nae.epoch_data(raw)
            epoch_matrix = epochs.get_data()

            # write epoch matrix to new binary file
            try:
                np.save(new_filename, epoch_matrix)
            except any as err:
                error_log.append([new_filename, err])
                pass

