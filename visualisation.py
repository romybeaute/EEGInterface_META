'''
@Author : Romy Beauté
@Date : 05/11/2023
@Corresp : r.beaut@sussex.ac.uk

'''


import mne
import os

# A dictionary mapping file extensions to their respective MNE function : see here to add more extensions https://mne.tools/stable/reading_raw_data.html
read_funcs = {
    '.edf': mne.io.read_raw_edf,
    '.fif': mne.io.read_raw_fif,
    '.egi': mne.io.read_raw_egi
}



def read_EEG(EEG_file,DATASET_path,print_infos=True,plot_raw=True):

    print(f"EEG file : {EEG_file}")
    _, ext = os.path.splitext(EEG_file)
    EEG_path = os.path.join(DATASET_path, EEG_file)

    if ext in read_funcs:
        raw = read_funcs[ext](EEG_path, preload=True)
    else:
        print(f"The file format '{ext}' is not supported by this pipeline.")
        try:
            # Attempt to read with the default function
            raw = mne.io.read_raw(EEG_path, preload=True)
        except Exception as e:
            print(f"Failed to read file with the default reader: {e}")
    if print_infos:
        print(f"Details for file: {EEG_file}\n {raw.info}")
    if plot_raw:
        raw.plot()
    
    return raw

    