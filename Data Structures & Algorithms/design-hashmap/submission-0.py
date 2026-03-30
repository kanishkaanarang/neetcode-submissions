class MyHashMap:

    def __init__(self):
        # Step 1: Initialize bucket size
        self.size = 1000
        
        # Step 2: Create buckets (each bucket stores key-value pairs)
        self.buckets = []
        for _ in range(self.size):
            self.buckets.append([])

    # Step 3: Hash function
    def hash_function(self, key):
        return key % self.size

    # Step 4: Put (insert/update)
    def put(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        bucket = self.buckets[index]

        # Check if key already exists → update
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return
        
        # If not found → insert new pair
        bucket.append((key, value))

    # Step 5: Get value
    def get(self, key: int) -> int:
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return -1

    # Step 6: Remove key
    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return