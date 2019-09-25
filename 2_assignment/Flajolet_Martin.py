import math
import mmh3

def get_least_significant_bit_index(x):
    """Returns the index, counting from 0, of the
    least significant set bit in `x`.
    """
    if x ==0:
        return 0
    return (x&-x).bit_length()-1

class FaljoletMartin:
    def __init__(self, stream, bit_map_size=100):
        self.stream  =stream
        self.bit_map = [0] * bit_map_size
        self.largest_index_in_bit_map = 0
        self.phai = 0.77351

    def _add(self, key):
        key_hash = mmh3.hash(str(key))
        least_sig_bit_index = get_least_significant_bit_index(key_hash)
        self.bit_map[least_sig_bit_index] = 1
        self.largest_index_in_bit_map = max(least_sig_bit_index, self.largest_index_in_bit_map)


    def get_cardinality(self):
        for key in stream:
            self._add(key)
        return math.ceil( pow(2,self.largest_index_in_bit_map) / self.phai)


'''test'''
stream = [1,1,2,3,1,4,2]
stream = ['A','A','B','B','A','A','B','B','A','A','A']


x= FaljoletMartin(stream)

print(x.get_cardinality())

"""

Purpose: Flajolet and Martin (FM) Algorthm

input: stream M

output: Cardinality of M

dependency: mmh3

"""