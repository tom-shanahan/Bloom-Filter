def cs5112_hash1(obj):
  return hash(obj)

def cs5112_hash2(obj):
  return hash(str(hash(obj)) + "salt 1")

def cs5112_hash3(obj):
  return hash(str(hash(obj)) + "pepper 2")
