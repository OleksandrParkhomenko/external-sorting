from input_generation import *
from external_sorting import ExternalMergeSort
import os
import sys

#generate_input_file(100_000_000) # 100 mb

# test = generate_input_file(10000000)
# merge = ExternalMergeSort(test, 1000000)
# merge.sort()

# run || run --example
if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == '--example'):
    print("Running example...")
    merge = ExternalMergeSort('data/example100mb.txt', 1000000)
    result = merge.sort()
    print("Result file: {}".format(result))
# run --random
elif len(sys.argv) == 3 and sys.argv[1] == '--random':
    print("Running example with randomly generated input data...")
    try:
        file_size = int(sys.argv[2])
        if file_size < 10000:
            print("Example file size must be greater than 10 000 bytes")
        else:
            input_file = generate_input_file(file_size)
            merge = ExternalMergeSort(input_file, file_size // 10)
            result = merge.sort()
            print("Result file: {}".format(result))
    except ValueError as e:
        print("Invalid file size")
# run --ram 100000 --file example100mb.txt
elif len(sys.argv) == 5 and sys.argv[1] == '--ram' and sys.argv[3] == '--file':
    try:
        available_ram = int(sys.argv[2])
        if os.path.exists(os.path.join(os.getcwd(), sys.argv[4])):
            if available_ram < 10000: #
                print("Available RAM must be greater than 10 000 bytes")
            else:
                print("Running sorting for {} using {} RAM".format(sys.argv[4], sys.argv[2]))
                merge = ExternalMergeSort(sys.argv[4], available_ram)
                result = merge.sort()
                print("Result file: {}".format(result))
        else:
            print("File {} not found".format(sys.argv[4]))
    except ValueError as e:
        print("Invalid value for RAM")
else:
    print("Wrong number or order of arguments")