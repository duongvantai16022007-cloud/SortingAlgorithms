import numpy as np
import time
import sys
import os
from pathlib import Path

# Tăng giới hạn đệ quy cho QuickSort/MergeSort
sys.setrecursionlimit(2000000)

class SortingAlgorithms:
    """Lớp chứa các thuật toán sắp xếp"""
    
    @staticmethod
    def numpy_sort(arr):
        return np.sort(arr)

    @staticmethod
    def heap_sort(arr):
        def heapify(a, n, i):
            largest = i
            l, r = 2*i + 1, 2*i + 2
            if l < n and a[l] > a[largest]: largest = l
            if r < n and a[r] > a[largest]: largest = r
            if largest != i:
                a[i], a[largest] = a[largest], a[i]
                heapify(a, n, largest)
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        return arr

    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        # Trộn mảng
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]: res.append(left[i]); i += 1
            else: res.append(right[j]); j += 1
        res.extend(left[i:]); res.extend(right[j:])
        return res

    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 1: return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)

class BenchmarkManager:
    def __init__(self, folder_name="Data_create"):
        self.folder_path = Path(folder_name)
        if not self.folder_path.exists():
            print(f"Lỗi: Thư mục '{folder_name}' không tồn tại!")
            sys.exit()

    def run_all_tests(self):
        # Lấy danh sách tất cả các file trong thư mục, sắp xếp theo tên
        files = sorted([f for f in self.folder_path.iterdir() if f.is_file()])
        
        print(f"{'File Name':<25} | {'Algorithm':<12} | {'Time (s)':<10}")
        print("-" * 55)

        for file_path in files:
            print(f"Đang xử lý: {file_path.name}...")
            # Nạp dữ liệu
            data = np.loadtxt(file_path)
            
            # --- Thực hiện Benchmark ---
            # 1. NumPy Sort (Luôn chạy vì rất nhanh)
            self._measure(data.copy(), SortingAlgorithms.numpy_sort, "NumPy Sort", file_path.name)
            
            # 2. Heap Sort (Bỏ comment để chạy - Cảnh báo: 1 triệu số rất chậm)
            # self._measure(data.copy(), SortingAlgorithms.heap_sort, "Heap Sort", file_path.name)
            
            # 3. Quick Sort (Bỏ comment để chạy)
            # self._measure(data.tolist(), SortingAlgorithms.quick_sort, "Quick Sort", file_path.name)

    def _measure(self, arr, sort_func, alg_name, file_name):
        start = time.time()
        sort_func(arr)
        duration = time.time() - start
        print(f"{file_name:<25} | {alg_name:<12} | {duration:.5f}s")

if __name__ == "__main__":
    benchmark = BenchmarkManager(folder_name="Data_create")
    benchmark.run_all_tests()