
# MyFilesystem
A primitive and crappy Filesystem ,implemented in about 100 lines of python, I made for a presentation.

## How it works.
It puts an "index" at the start of the file/disk. This Index starts with decimal digits and then follows a "s", so we know, when the digits end. Those digits get parsed into a integer and this then is the length of the rest of the index. This rest is a json string, which holds information on where the next file should be placed into the storate and for each stored file: the name, where it starts and ends.

## How to use.
The name of the file/disk is hardcoded into the python script (variable: disk)

There are only 4 commands: install, dump, store, get

- install just writes an empty "index" to the start of the file/disk-storage CAUTION!! can and will without asking break the filesystem that is currently on the file/disk
- dump reads the index (probably errors, when there is no index)
- store writes a file to the disk
- get reads a file from the disk

`python myfs.py install`
`python myfs.py dump`
`python myfs.py store <name of file to store>`
`python myfs.py <name of file to get>`



``


