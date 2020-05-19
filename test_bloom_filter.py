from bloom_filter import BloomFilter

bfilter = BloomFilter()
bfilter.add_elem("example_elem")
if bfilter.check_membership("example_elem"):
  print("Found this element in the bloom filter")
else:
  print("Bloom filter did not return True for added element ")
