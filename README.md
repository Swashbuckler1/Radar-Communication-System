# Radar-Communication-System

To install the dependencies, run `pip install -r requirements.txt`

The file **Communication.ipynb** contains the main code
for the communication system. The stages are labeled inside the notebook.
Run all the cells.

The files **features.txt** and **train_labels.txt**
are for training the SVM classifier and **test_features.txt**
and **test_labels.txt** is for testing.

**data_12_14_2023_16_14_27.npy** and **data_12_14_2023_16_16_41.npy**
is for visualizing the range profile of forward-back and side-side
motion respectively.

**data_12_14_2023_14_36_04.npy** is the data collected from making the string `hello`.

**udp_server.py** is meant to be run on a Raspberry Pi so the client
script in **Communication.ipynb** can send the bytes and print
the string to the Sense Hat.