import numpy as np

#stacking many N 1D (columns/arrays of size M) together into one M*N array:
x=y=z=np.arange(0,10,1)
print(np.c_[x,y,z])

#saving multiple array using np.savetxt command:
np.savetxt('testfile', np.c_[x,y,z], delimiter=', ', newline='\n', header="col1, col2, col3", footer='some_useful_information_of_the_file_being_saved', comments='#')
