#SelectionSort
def selectionSort(array, size):
       
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            
            if array[i] < array[min_idx]:
                min_idx = i
         
        
        (array[step], array[min_idx]) = (array[min_idx], array[step])


#BubbleSort
def bubbleSort(array):
    
  
  for i in range(len(array)):

    
    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:

        
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

#InsertionSort
def insertionSort(array):
        
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
                
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        
        array[j + 1] = key
        
#MergeSort
def mergeSort(array):
    if len(array) > 1:

      
        r = len(array)//2
        L = array[:r]
        M = array[r:]

      
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

       
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1