#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, i):
        # code here
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        if left < len(arr) and arr[left] > arr[largest]:
            largest = left
        if right < len(arr) and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, largest)
            
    
    #Function to build a Heap from array.
    def buildHeap(self,arr):
        # code here
        for i in range(len(arr)//2, -1, -1):
            self.heapify(arr, i)
            
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr)
        arr.sort()
            
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends