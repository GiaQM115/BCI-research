import mne


def normalize_data(filename):
    mne.set_log_level(verbose='ERROR')
    print("Setting EEG Average Reference for " + filename)
    raw = mne.io.read_raw_edf(filename)
    raw.set_eeg_reference(projection=True)
    return raw


def epoch_data(data):
    eventlist, event_ids = mne.events_from_annotations(data)
    epochs = mne.Epochs(data, eventlist, event_id=event_ids, baseline=None, preload=True)
    return epochs, event_ids, eventlist

