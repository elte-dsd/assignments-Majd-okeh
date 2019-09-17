import mmh3
import numpy as np

class CountMinSketch:
    def __init__(self, width, hash_funcs_num):
        self.width = width
        self.hash_funcs_num = hash_funcs_num
        self.matrix = np.zeros([hash_funcs_num, width])  # empty matrix for with occurences for all keys
        self.seed = np.random.randint(width, size = hash_funcs_num)
        self.stream_size = 0

    def add(self, key):
        self.stream_size += 1
        for i in range(0, self.hash_funcs_num):
            index = mmh3.hash(key, self.seed[i]) % self.width
            self.matrix[i, index] += 1

    def get(self, key):
        min_count = self.stream_size + 1
        for i in range(0, self.hash_funcs_num):
            index = mmh3.hash(key, self.seed[i]) % self.width
            min_count = min(self.matrix[i, index], min_count)
        return min_count


'''test'''
x= CountMinSketch(width=10, hash_funcs_num=5)
stream = 'AABBAABBAACAC'
for c in stream:
    x.add(c)

print(x.get('A'))
print(x.get('B'))
print(x.get('C'))