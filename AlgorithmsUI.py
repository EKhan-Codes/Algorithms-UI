import tkinter
window_main = tkinter.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("400x200")
 
def submitFunction() :
 global inp
 inp = list(map(int, (inputtxt.get(1.0, "end-1c").strip().split())))
 
 def bubbleSort(array):
        
  
  for i in range(len(array)):

    
    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:

        
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp



 
 bubbleSort(inp)
 lbl.config(text = "Bubble Sort: "+str(inp))
 
def submitFunction1() :
 
 inp = list(map(int, (inputtxt.get(1.0, "end-1c").strip().split())))   
 def selectionSort(array, size):
       
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            
            if array[i] < array[min_idx]:
                min_idx = i
         
        
        (array[step], array[min_idx]) = (array[min_idx], array[step]) 
      
 size = len(inp)
 selectionSort(inp, size)
 lbl.config(text = "Selection Sort: "+str(inp))  

def submitFunction2():
 
 inp = list(map(int, (inputtxt.get(1.0, "end-1c").strip().split())))
 def insertionSort(array):
    
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
                
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        
        array[j + 1] = key  

 insertionSort(inp)
 lbl.config(text = "Insertion Sort: "+str(inp))  
 
def submitFunction3():
 inp = list(map(int, (inputtxt.get(1.0, "end-1c").strip().split())))
 def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

 mergeSort(inp)   
 lbl.config(text = "Merge Sort: "+str(inp)) 


inputtxt = tkinter.Text(window_main,
                   height = 1,
                   width = 20)
  
inputtxt.place(x=125, y=50)
  
# Button Creation
printButton = tkinter.Button(window_main,
                        text = "Bubble Sort", 
                        command = submitFunction)
printButton.place(x=20, y=10)
printButton1 = tkinter.Button(window_main,
                        text = "Selection Sort", 
                        command = submitFunction1)
printButton1.place(x=20, y=35)
printButton2 = tkinter.Button(window_main,
                        text = "Insertion Sort", 
                        command = submitFunction2)
printButton2.place(x=20, y=61)
printButton3 = tkinter.Button(window_main,
                        text = "Merge Sort", 
                        command = submitFunction3)
printButton3.place(x=20, y=88)
  
# Label Creation
lbl = tkinter.Label(window_main, text = "")
lbl.pack()
window_main.mainloop()