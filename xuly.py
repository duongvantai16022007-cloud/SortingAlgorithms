import numpy as np
import time
import sys
from pathlib import Path
sys.setrecursionlimit(2000000)
class Sorting:
    @staticmethod
    def Numpy_sort(arr): return np.sort(arr)

    @staticmethod
    def sort(arr): return sorted(arr)

    @staticmethod
    def heap_sort(arr):
        def heapify(a, n, i):
            largest = i
            l, r = 2*i+1, 2*i+2
            if l < n and a[l] > a[largest]: largest = l
            if r < n and a[r] > a[largest]: largest = r
            if largest != i:
                a[i], a[largest] = a[largest], a[i]
                heapify(a, n, largest)
        n = len(arr)
        for i in range(n//2-1, -1, -1): heapify(arr, n, i)
        for i in range(n-1, 0, -1): arr[i], arr[0] = arr[0], arr[i]; heapify(arr, i, 0)
        return arr

    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1: return arr
        mid = len(arr)//2
        left = Sorting.merge_sort(arr[:mid])
        right = Sorting.merge_sort(arr[mid:])
        res, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]: res.append(left[i]); i += 1
            else: res.append(right[j]); j += 1
        res.extend(left[i:]); res.extend(right[j:])
        return res

    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 1: return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]; mid = [x for x in arr if x == pivot]; right = [x for x in arr if x > pivot]
        return Sorting.quick_sort(left) + mid + Sorting.quick_sort(right)

class Benchmark:
    def __init__(self, folder_name="Data_create"):
        self.folder_path = Path(folder_name)
    def _get_time(self, arr, sort_func, to_list=False):
        test_data = arr.tolist() if to_list else arr.copy()
        start = time.time()
        sort_func(test_data)
        duration_ms = (time.time() - start) * 1000
        return f"{duration_ms:.2f}ms"

    def run_all_tests(self):
        files = sorted([f for f in self.folder_path.iterdir() if f.is_file()])
        print(f"{'File Name':<20} | {'Numpy_sort':<15} | {'Python_sort':<15} | {'Merge':<10} | {'Heap':<10} | {'Quick':<10}")
        for file_path in files:
            data = np.loadtxt(file_path)
            t_np = self._get_time(data, Sorting.Numpy_sort)
            t_sortpython = self._get_time(data, Sorting.sort)
            t_merge = self._get_time(data, Sorting.merge_sort, to_list=True)
            t_heap = self._get_time(data, Sorting.heap_sort)
            t_quick = self._get_time(data, Sorting.quick_sort, to_list=True)
            print(f"{file_path.name:<20} | {t_np:<15} | {t_sortpython:<15} | {t_merge:<10} | {t_heap:<10} | {t_quick:<10}")

benchmark = Benchmark(folder_name="Data_create")
benchmark.run_all_tests()