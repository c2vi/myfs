
import numpy as np
import sys
import json
import os

disk="/path/to/device/or/file"
data_starts_at=10000

def main():

    if sys.argv[1] == "install":
        install()
        exit()

    if sys.argv[1] == "dump":
        print("FILES -----------------------")
        index = get_index()
        for file in index["files"]:
            print(file)

        print("NEXT FREE -------------------")
        print(index["next_free"])

        print("FILE COUNT ------------------")
        print(len(index["files"]))

        exit()

    if len(sys.argv) < 2:
        print("Not enough arguments")
        print("First argument is get or store, seccond is filename")
        exit()

    if sys.argv[1] == "get":
        get_file(sys.argv[2])

    elif sys.argv[1] == "store":
        store_file(sys.argv[2])


    else:
        print("Unknown Command")


def install():
    store_index({"files":[], "next_free": data_starts_at})

def get_file(filename):
    index = get_index()

    for file in index["files"]:
        if file["name"] == filename:
            with open(disk, "rb") as disk_file:
                #disk_file.seek()
                #data = disk_file.read(3)
                disk_file.seek(int(file["start"]))
                data = disk_file.read(file["end"] - file["start"])

                sys.stdout.buffer.write(data)

            break

def store_file(filename):
    index = get_index()
    file_size = os.path.getsize(filename)
    
    start = index["next_free"]

    index["files"].append({
        "name": filename,
        "start": start,
        "end": start + file_size,
    })
    index["next_free"] = start + file_size + 1

    store_index(index)

    # actually write the file
    in_file = open(filename, "rb")
    out_file = open(disk, "wb")

    out_file.seek(start)
    out_file.write(in_file.read())

    in_file.close()
    out_file.close()

def get_index():
    with open(disk, "rb") as file:
        len_str = ""
        while True:
            char = str(file.read(1).decode())
            if char == "s":
                break
            else:
                len_str += char

        index = str(file.read(int(len_str)).decode())

        return json.loads(index)

def store_index(index):
    with open(disk, "wb") as file:
        data = bytearray(json.dumps(index).encode())
        length = len(data)

        file.write(bytearray(str(length).encode()))
        file.write(bytearray("s".encode()))
        file.write(data)


if __name__ == "__main__":
    main()

