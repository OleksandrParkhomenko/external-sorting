import os
import lorem
from datetime import datetime


def generate_input_file(size=1_000_000):
    print("Start generating input file...")
    curr_size = 0
    base_folder = os.path.dirname(os.path.abspath(__file__))
    filename = "data/input-{}.txt".format(datetime.now().strftime("%Y%m%d-%H%M%S"))
    file_path = os.path.join(base_folder, filename)

    with open(file_path, 'a+') as f:
        while curr_size < size:
            curr_size = os.path.getsize(file_path)
            f.write(lorem.sentence() + "\n")
    print("Generated successfully")
    return os.path.abspath(file_path)
