import os

dir = 'tsp'

for f in os.listdir(dir):
    f_name, f_ext = os.path.splitext(f)
    f_name = 'v_' + f_name + f_ext
    print(f_name)
    os.rename(os.path.join(dir, f), os.path.join(dir, f_name))
