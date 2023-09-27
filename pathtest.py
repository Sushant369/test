import heapq

class Element:
    def __init__(self, value, unique_id):
        self.value = value
        self.unique_id = unique_id

    def __lt__(self, other):
        if self.value == other.value:
            return self.unique_id < other.unique_id
        return self.value < other.value

# Initialize an empty priority queue
priority_queue = []

# Insert elements into the priority queue
element1 = Element(5, 1)
element2 = Element(3, 2)
element3 = Element(2, 3)
element4 = Element(2, 4)

heapq.heappush(priority_queue, element1)
heapq.heappush(priority_queue, element2)
heapq.heappush(priority_queue, element3)
heapq.heappush(priority_queue, element4)

# Remove elements from the priority queue
while priority_queue:
    element = heapq.heappop(priority_queue)
    print(f"Value: {element.value}, Unique ID: {element.unique_id}")

positive_infinity = float('inf')
print(positive_infinity)

arr=[1,2,43,4]
print (3 not in arr)