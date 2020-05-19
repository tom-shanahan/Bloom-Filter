from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1
from cs5112_hash import cs5112_hash2
from cs5112_hash import cs5112_hash3

# Implementation of a basic bloom filter. Uses exactly three hash functions.
class BloomFilter:
  def __init__(self, size=10):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.size = size
    self.array = FixedSizeArray(size)
    for i in range(0, size):
      self.array.set(i, False)

  # To add an element to the bloom filter, use each of the k=3 hash functions we provided and compute
  # the positions that we are setting in the fixed size array using modulo operation.
  def add_elem(self, elem):
    p1 = cs5112_hash1(elem) % self.size
    p2 = cs5112_hash2(elem) % self.size
    p3 = cs5112_hash3(elem) % self.size
    self.array.set(p1, True)
    self.array.set(p2, True)
    self.array.set(p3, True)

  # Returns False if the given element was definitely not added to the filter. 
  # Returns True if it's possible that the element was added to the filter.
  def check_membership(self, elem):
    p1 = cs5112_hash1(elem) % self.size
    p2 = cs5112_hash2(elem) % self.size
    p3 = cs5112_hash3(elem) % self.size
    if not self.array.get(p1) or not self.array.get(p2) or not self.array.get(p3):
      return False
    
    return True
