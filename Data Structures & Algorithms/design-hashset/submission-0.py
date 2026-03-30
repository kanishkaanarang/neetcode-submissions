class MyHashSet:

    def __init__(self):
        # Step 1: Choose a size for buckets
        self.size = 1000
        
        # Step 2: Create empty buckets (each bucket is a list)
        self.buckets = []
        for _ in range(self.size):
            self.buckets.append([])

    # Step 3: Hash function
    def hash_function(self, key):
        return key % self.size

    # Step 4: Add key
    def add(self, key: int) -> None:
        index = self.hash_function(key)
        bucket = self.buckets[index]

        # Check if key already exists
        for num in bucket:
            if num == key:
                return
        
        # If not present, add it
        bucket.append(key)

    # Step 5: Remove key
    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                return

    # Step 6: Check if key exists
    def contains(self, key: int) -> bool:
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for num in bucket:
            if num == key:
                return True

        return False