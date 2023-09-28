import os
import h5py
import numpy as np

in_paths = [
    './how2100m_tsp_features.h5',
]
out_path = 'tsp'

if not os.path.exists(out_path):
    os.mkdir(out_path)

for in_path in in_paths:
    d = h5py.File(in_path)
    for key in d.keys():
        v_d = d[key][:]
        np.save(os.path.join(out_path, key+'.npy'), v_d)
