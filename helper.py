'''
Corresp : r.beaut@sussex.ac.uk
Created : 07/11/2023
'''

import mne
import os



#Dictionnary of extension for EEG recordings and their corresp with MNE reader
read_funcs = {
        '.edf': mne.io.read_raw_edf,
        '.fif': mne.io.read_raw_fif,
        '.egi': mne.io.read_raw_egi
    }




# Function to select a file by name or index
def select_file(files, selection):
    if isinstance(selection, int):
        # Select by index
        if 0 <= selection < len(files):
            return files[selection]
        else:
            raise IndexError("Selection index out of range.")
    elif isinstance(selection, str):
        # Select by file name
        if selection in files:
            return selection
        else:
            raise ValueError("File not found.")
    else:
        raise ValueError("Selection must be an index or a filename.")
    



#Get the raw data
def get_raw(EEG_file,
            DATASET_path,
            plot_raw=False):
    
    # Read the raw data
    print(f"Processing EEG file: {EEG_file}")
    _, ext = os.path.splitext(EEG_file)
    EEG_path = os.path.join(DATASET_path, EEG_file)

    if ext in read_funcs:
        raw = read_funcs[ext](EEG_path, preload=True)
    else:
        print(f"The file format '{ext}' is not supported by this pipeline.")
        return
    if plot_raw:
        raw.plot()
    
    return raw



def get_EEG_duration(raw_eeg):

    duration_eeg = len(raw_eeg) / raw_eeg.info['sfreq']
    print(f"Duration of recording: {duration_eeg} seconds")
    return duration_eeg