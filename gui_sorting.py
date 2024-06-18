''' Code by Rohit M  ID: 1002091557'''

import tkinter as tk
from tkinter import ttk
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class SortingGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sorting Algorithm Visualizer")
        self.geometry("500x300")

        self.label = ttk.Label(self, text="Enter the size of the array:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(self)
        self.entry.pack()

        self.radio_frame = ttk.Frame(self)
        self.radio_frame.pack(pady=10)

        self.var = tk.StringVar()
        self.var.set("Bubble Sort")

        self.radio_bubble = ttk.Radiobutton(self.radio_frame, text="Bubble Sort", variable=self.var,
                                            value="Bubble Sort")
        self.radio_bubble.pack(side="left", padx=10)

        self.radio_insertion = ttk.Radiobutton(self.radio_frame, text="Insertion Sort", variable=self.var,
                                               value="Insertion Sort")
        self.radio_insertion.pack(side="left", padx=10)

        self.radio_selection = ttk.Radiobutton(self.radio_frame, text="Selection Sort", variable=self.var,
                                               value="Selection Sort")
        self.radio_selection.pack(side="left", padx=10)

        self.radio_selection = ttk.Radiobutton(self.radio_frame, text="Mergesort", variable=self.var,
                                               value="Mergesort")
        self.radio_selection.pack(side="left", padx=10)

        self.radio_selection = ttk.Radiobutton(self.radio_frame, text="Quicksort", variable=self.var,
                                               value="Quicksort")
        self.radio_selection.pack(side="left", padx=10)

        self.radio_selection = ttk.Radiobutton(self.radio_frame, text="Median of 3 - Quicksort", variable=self.var,
                                               value="Quicksort3")
        self.radio_selection.pack(side="left", padx=10)

        self.radio_selection = ttk.Radiobutton(self.radio_frame, text="Heapsort", variable=self.var,
                                               value="Heapsort")
        self.radio_selection.pack(side="left", padx=10)

        self.button = ttk.Button(self, text="Sort", command=self.sort)
        self.button.pack(pady=10)
        self.button = tk.Button(self, text="Refresh", command=self.refresh_window)
        self.button.pack()

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.pack(pady=10, padx=10, fill="both", expand=True)

        self.label_result = ttk.Label(self, text="")
        self.label_result.pack(pady=10)

        scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.listbox.xview)
        scrollbar.pack(side="bottom", fill="x")
        self.listbox.configure(xscrollcommand=scrollbar.set)

#graph plot
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.plot.set_xlabel('Sorting Method')
        self.plot.set_ylabel('Runtime (seconds)')

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def refresh_window(self):
        # close the current window
        self.destroy()
        # create a new instance of the window
        # new_root = tk.Tk()
        new_window = SortingGUI()
        # new_root.mainloop()

    def sort(self):
        try:
            size = int(self.entry.get())
            arr = [random.randint(1, 10000) for _ in range(size)]
            arr2 = arr.copy()
            method = self.var.get()
            # methods = ["Bubble Sort", "Insertion Sort", "Selection Sort"]
            runtimes = []
            if method == "Bubble Sort":
                start_time = time.time()
                self.bubble_sort(arr)
                end_time = time.time()
            elif method == "Insertion Sort":
                start_time = time.time()
                self.insertion_sort(arr)
                end_time = time.time()
            elif method == "Selection Sort":
                start_time = time.time()
                self.selection_sort(arr)
                end_time = time.time()
            elif method == "Quicksort":
                start_time = time.time()
                arr = self.quicksort(arr)
                end_time = time.time()
            elif method == "Mergesort":
                start_time = time.time()
                arr = self.mergesort(arr)
                end_time = time.time()
            elif method == "Quicksort3":
                start_time = time.time()
                arr = self.quicksort3(arr)
                end_time = time.time()
            elif method == "Heapsort":
                start_time = time.time()
                arr = self.heapsort(arr)
                end_time = time.time()


            runtime = end_time - start_time
            runtimes.append(runtime)

            self.listbox.delete(0, tk.END)
            self.listbox.insert(tk.END, f"Original Array: {arr2}")
            self.listbox.insert(tk.END, "")
            self.listbox.insert(tk.END, f"Sorted Array: {arr}")
            self.listbox.insert(tk.END, "")
            self.listbox.insert(tk.END, f"Runtime: {runtime:.9f} seconds")

            self.plot.bar(method, runtimes, color='green')
            self.canvas.draw()

        except ValueError:
            self.label_result.config(text="Invalid input. Please enter an integer.")


    def bubble_sort(self, arr):

        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    # return arr

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left_arr = self.mergesort(arr[:mid])
        right_arr = self.mergesort(arr[mid:])

        return self.merge(left_arr, right_arr)

    def merge(self, left_arr, right_arr):
        merged_arr = []
        i = j = 0

        if not left_arr:
            return right_arr
        elif not right_arr:
            return left_arr
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                merged_arr.append(left_arr[i])
                i += 1
            else:
                merged_arr.append(right_arr[j])
                j += 1

        merged_arr.extend(left_arr[i:])
        merged_arr.extend(right_arr[j:])
        arr = merged_arr
        return arr
        # Sort the array after the merge
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr


    # Heapsort
    def heapsort(self, arr):
        # sorted_arr = arr.copy()
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

        return arr

    def heapify(self, arr, n, i):
        # sorted_arr = arr.copy()
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    # Quicksort using random element as Pivot

    def quicksort(self, arr):
        # sorted_arr = arr.copy()
        if len(arr) <= 1:
            return arr
        else:
            pivot = random.choice(arr)
            left = []
            right = []
            equal = []
            for x in arr:
                if x < pivot:
                    left.append(x)
                elif x > pivot:
                    right.append(x)
                else:
                    equal.append(x)
            return self.quicksort(left) + equal + self.quicksort(right)

    # Quicksort with median of 3

    def quicksort3(self, arr):
        # sorted_arr = arr.copy()
        if len(arr) <= 1:
            return arr
        else:
            # Select pivot element using median of three technique
            first = arr[0]
            last = arr[-1]
            middle = arr[len(arr) // 2]

            if first < middle < last or last < middle < first:
                pivot = middle
            elif middle < first < last or last < first < middle:
                pivot = first
            else:
                pivot = last

            left = []
            right = []
            for i in range(len(arr)):
                if arr[i] < pivot:
                    left.append(arr[i])
                elif arr[i] > pivot:
                    right.append(arr[i])

            return self.quicksort3(left) + [pivot] + self.quicksort3(right)


if __name__ == "__main__":
    app = SortingGUI()
    app.mainloop()
