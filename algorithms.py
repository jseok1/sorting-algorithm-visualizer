from visualizer import update


def bubble_sort(screen, lst):
  """Bubble sort implementation in Python."""
  for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
      if lst[j] > lst[j + 1]:
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
      update(screen, lst.copy(), {j, j + 1, len(lst) - i})
  update(screen, lst.copy(), {})


def selection_sort(screen, lst):
  """Selection sort implementation in Python."""
  for i in range(len(lst)):
    smallest = i
    for j in range(i + 1, len(lst)):
      if lst[j] < lst[smallest]:
        smallest = j
      update(screen, lst.copy(), {i - 1, j, smallest})
    lst[smallest], lst[i] = lst[i], lst[smallest]
    update(screen, lst.copy(), {i - 1, i, smallest})
  update(screen, lst.copy(), {})


def insertion_sort(screen, lst):
  """Insertion sort implementation in Python."""
  for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1
    while j >= 0 and lst[j] > key:
      lst[j + 1], lst[j] = lst[j], lst[j + 1]
      update(screen, lst.copy(), {i, j, j + 1})
      j -= 1
    lst[j + 1], key = key, lst[j + 1]
    update(screen, lst.copy(), {i, j + 1})
  update(screen, lst.copy(), {})


def merge_sort(screen, lst):
  """Used to call merge sort."""
  _merge_sort(screen, lst, 0, len(lst) - 1)
  update(screen, lst.copy(), {})


def _merge_sort(screen, lst, low, high):
  """Merge sort implementation in Python."""
  if low >= high:
    update(screen, lst.copy(), {})
  else:
    mid = (low + high) // 2
    _merge_sort(screen, lst, low, mid)
    _merge_sort(screen, lst, mid + 1, high)
    _merge(screen, lst, low, mid, high)


def _merge(screen, lst, low, mid, high):
  """Helper function for merge sort."""
  merged = []
  i = low
  j = mid + 1
  while i <= mid and j <= high:
    if lst[i] < lst[j]:
      merged.append(lst[i])
      update(screen, lst.copy(), {i, j})
      i += 1
    else:
      merged.append(lst[j])
      update(screen, lst.copy(), {i, j})
      j += 1
  while i <= mid:
    merged.append(lst[i])
    update(screen, lst.copy(), {i})
    i += 1
  while j <= high:
    merged.append(lst[j])
    update(screen, lst.copy(), {j})
    j += 1
  for k in range(len(merged)):
    lst[k + low] = merged[k]
    update(screen, lst.copy(), {k + low})


def quick_sort(screen, lst):
  """Used to call quick sort."""
  _quick_sort(screen, lst, 0, len(lst) - 1)
  update(screen, lst.copy(), {})


def _quick_sort(screen, lst, low, high):
  """Quick sort implementation in Python."""
  if low >= high:
    update(screen, lst.copy(), {})
  else:
    pivot = _partition(screen, lst, low, high)
    _quick_sort(screen, lst, low, pivot)
    _quick_sort(screen, lst, pivot + 1, high)


def _partition(screen, lst, low, high):
  """Helper function for quick sort."""
  pivot = lst[low]
  i = low
  j = high
  while True:
    while lst[i] < pivot:
      update(screen, lst.copy(), {i, j, low})
      i += 1
    while lst[j] > pivot:
      update(screen, lst.copy(), {i, j, low})
      j -= 1
    if i >= j:
      return j
    lst[i], lst[j] = lst[j], lst[i]
    update(screen, lst.copy(), {i, j, low})
    i += 1
    j -= 1


def heap_sort(screen, lst):
  """Heap sort implementation in Python."""
  for i in range(len(lst) // 2 - 1, -1, -1):
    _heapify(screen, lst, len(lst), i)
  for i in range(len(lst) - 1, 0, -1):
    lst[i], lst[0] = lst[0], lst[i]
    update(screen, lst.copy(), {0, i})
    _heapify(screen, lst, i, 0)
  update(screen, lst.copy(), {})


def _heapify(screen, lst, size, i):
  """Helper function for heap sort."""
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2
  update(screen, lst.copy(), {size, largest})
  if left < size:
    if lst[largest] < lst[left]:
      largest = left
    update(screen, lst.copy(), {size, largest, left})
  if right < size:
    if lst[largest] < lst[right]:
      largest = right
    update(screen, lst.copy(), {size, largest, right})
  if largest != i:
    lst[i], lst[largest] = lst[largest], lst[i]
    update(screen, lst.copy(), {size, largest, i})
    _heapify(screen, lst, size, largest)
