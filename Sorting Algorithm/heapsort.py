#Time Complexity is Building Max Heap is = O(n)
#Extracting Max elemnent time taken is =O(nlogn)
#Overall Time Complexity is = O(n) + O(nlogn) = O(nlogn)
def heapify(heap, n, i):
  largest = i
  left = 2*i + 1
  right = 2*i + 2
  if left < n and heap[left] > heap[largest]:
    largest = left
  if right < n and heap[right] >heap[largest]:
    largest = right
  if largest != i:
    heap[i], heap[largest] = heap[largest], heap[i]
    heapify(heap, n, largest)
def heapSort(heap):
  n = len(heap)
  # Build Max Heap
  for i in range(n//2 -1, -1, -1):
    heapify(heap, n, i)
  # Extract elements from the heap one by one
  for i in range(n-1, 0 , -1):
    heap[0], heap[i] = heap[i], heap[0]
    heapify(heap, i, 0)

heap = [12, 11, 13, 5, 6, 7]
heapSort(heap)
print("Sorted array:", heap) 