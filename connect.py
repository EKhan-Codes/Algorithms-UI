import tkinter
import AllSort as Sort
window_main = tkinter.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("400x200")
 
def BubbleSort() :
 inp = list(map(int, (inputtxt.get(1.0, "end-1c").strip().split())))
 Sort.bubbleSort(inp)
 lbl.config(text = "Bubble Sort: "+str(inp))

def SelectionSort() :
 inp = list(map(int, (inputtxt.get(1.0, "end-1c").strip().split())))
 size = len(inp)
 Sort.selectionSort(inp, size)
 lbl.config(text = "Selection Sort: "+str(inp))
 
def InsertionSort() :
 inp = list(map(int, (inputtxt.get(1.0, "end-1c").strip().split())))
 Sort.insertionSort(inp)
 lbl.config(text = "Insertion Sort: "+str(inp))
 
def MergeSort() :
 inp = list(map(int, (inputtxt.get(1.0, "end-1c").strip().split())))
 Sort.mergeSort(inp)
 lbl.config(text = "Merge Sort: "+str(inp))


inputtxt = tkinter.Text(window_main,
                   height = 1,
                   width = 20)
  
inputtxt.place(x=125, y=50)
  
# Button Creation
printButton = tkinter.Button(window_main,
                        text = "Bubble Sort", 
                        command = BubbleSort)
printButton.place(x=20, y=10)

printButton1 = tkinter.Button(window_main,
                        text = "Selection Sort", 
                        command = SelectionSort)
printButton1.place(x=20, y=35)
printButton2 = tkinter.Button(window_main,
                        text = "Insertion Sort", 
                        command = InsertionSort)
printButton2.place(x=20, y=61)
printButton3 = tkinter.Button(window_main,
                        text = "Merge Sort", 
                        command = MergeSort)
printButton3.place(x=20, y=88)

  
# Label Creation
lbl = tkinter.Label(window_main, text = "")
lbl.pack()
window_main.mainloop()