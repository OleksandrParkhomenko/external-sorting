import os
import sys
import heapq
from datetime import datetime
import shutil


class ExternalMergeSort:

    def __init__(self, file_path, available_ram):
        self.available_ram = available_ram
        self.file_path = file_path
        self.dir = os.path.join(os.path.dirname(file_path), 'tmp')  # temporary folder for storing chunks of data
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        self.chunks = []  # list for storing file paths of chunks of data

    def sort(self):
        print("Start external merge sort process...")
        curr_file_pos = 0
        # divide into chunks with allowed size
        with open(self.file_path, 'r'):
            print("Dividing large file into chunks")
            while curr_file_pos != -1:  # equals -1 when the end of file reached
                curr_file_pos = self.__create_new_chunk(curr_file_pos)

        file_path = self.__k_way_merge()
        self.__remove_tmp_files()
        print("Sorted successfully")
        return file_path

    def __close_files(self, files):
        for file in files:
            file.close()

    def __k_way_merge(self):
        print("Merging chunks into result file")
        files = list(map(lambda f: open(f, 'r'), self.chunks))
        merged_num_generator = (map(str, file) for file in files)
        sorted_complete_data = heapq.merge(*merged_num_generator)
        result_path = os.path.join(os.path.dirname(self.file_path),
                                   "result-{}.txt".format(datetime.now().strftime("%Y%m%d-%H%M%S")))
        with open(result_path, 'a+') as result_file:
            for line in sorted_complete_data:
                result_file.write(line)
        self.__close_files(files)
        return result_path

    def __remove_tmp_files(self):
        print("Deleting temporary files & directory")
        shutil.rmtree(self.dir)

    def __create_new_chunk(self, curr_file_pos):
        chunk_num = len(self.chunks)
        chunk_data = []
        # read allowed amount of data
        with open(self.file_path, 'r') as input_file:
            input_file.seek(curr_file_pos)
            # sort method requires log(n) additional space
            # that's why we need to limit chunk size to half of available RAM
            while sys.getsizeof(chunk_data) < self.available_ram / 2:
                line = input_file.readline()
                chunk_data.append(line)
                # last line of file doesn't contain \n at the end
                if not line.endswith("\n"):
                    curr_file_pos = - 1  # set a flag for this state
                    break
                else:
                    curr_file_pos = input_file.tell()
        self.__quick_sort(chunk_data, 0, len(chunk_data) - 1)
        # save sorted chunk to tmp folder
        chunk_path = os.path.join(self.dir, 'chunk-{}.txt'.format(chunk_num))
        with open(chunk_path, 'a+') as chunk_file:
            for line in chunk_data:
                chunk_file.write(line)
        self.chunks.append(chunk_path)
        print("Chunk #{} successfully created and sorted".format(chunk_num))
        return curr_file_pos  # remember position in input file

    def __partition(self, data, low, high):
        i = low - 1
        pivot = data[high]
        for j in range(low, high):
            if data[j] <= pivot:
                i = i + 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    def __quick_sort(self, data, low, high):
        if len(data) <= 1:
            return data
        if low < high:
            pi = self.__partition(data, low, high)
            self.__quick_sort(data, low, pi - 1)
            self.__quick_sort(data, pi + 1, high)
