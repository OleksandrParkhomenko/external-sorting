# External Merge Sorting implementation

<hr>

## Explanation 
1. Divide large file that doesn't fit into RAM into smaller chunks.
2. Sort chunks of data using Quick Sort algorithm
3. Merge sorted chunks with K-Way Merge

<hr>

## How to run?

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```

2. To run example use:
   ```
    python run.py
   ```
   
or
   ```
    python run.py --example
   ```
   
3. To run example with randomly generated input data:
   ```
    python run.py --random
   ```
   
4. To run sorting for exact file using given amount of RAM:
   ```
   python run.py --ram 100000 --file data/example100mb.txt
   ```

5. To run tests:
   ```
   python -m unittest test.py
   ```

<hr>

## How to use separate parts of project?

1. To generate file with random "Lorum ipsum" sentences(function returns absolute path to generated file):
   ```
   input = generate_input_file(file_size)
   ```
   
2. To sort file using ExternalMergeSort (function returns absolute path to result file):
   ```
    ram = 10_000_000 # 10 mb
    merge = ExternalMergeSort("data/example10mb.txt", ram)
    result = merge.sort()
    ```
    
<hr>

All input and result data stored in data folder.
