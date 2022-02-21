import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

#

from nltk.tokenize import RegexpTokenizer
from pdfminer.high_level import extract_text
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk







# main window side
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        

        # pengaturan rampilan main window
        self.geometry("400x200")
        self.title('Frekunsi kalimat By: Mr.DNS')
        self.resizable(False,False)

        # tombol input
        self.input_button_1 = ttk.Button(
            self,
            text='Open file',
            command=self.pilih_file,
        )
        self.input_button_1.place(x=30, y=20)

        self.input_button_2 = ttk.Button(
            self,
            text = 'RUN',
            command=self.open_window_run
        )
        self.input_button_2.place(x=280, y=20)

            
    # fungsi pilih file
    def pilih_file(self):
        global linkse

        # file tipe fungsi
        self.file_tipe = (
            ('text files', '*.pdf'),
            ('All files', '*.*'),
            
        )

        # open desk fungsi
        self.openfile = fd.askopenfilename(
            title='open file',
            initialdir='/home/MRDNS/Documents/python/project_python/analicys/bundir/',
            filetypes= self.file_tipe
        )

        # teks
        self.reks1 = tk.Text(
            self,
            height=2,
            width=35,
            
        )
        self.reks1.place(x=56, y=60)
        self.reks1.insert(tk.END, self.openfile,)
        
        # mangambil link
        linkse = self.openfile
       
       
    # membut open window Run
    def open_window_run(self):
           
        if  self.openfile is None:
            showinfo(
                title = "No select file",
                message="No file selected"
            )                                     
        elif not self.openfile:
             showinfo(
                title = "No select file",
                message="No file selected"
            ) 
        else:
            window_run = Run_sektor()     
            # window_run.grab_set()


# run sektor logika run
class Run_sektor():    # sektor update nanti
   
#     def __init__(self):
#         super().__init__()
#         self.geometry("1000x700")
#         prc = Procec()
       
#         #visual data
#         fig = plt.figure(figsize=(10,4))
#         plt.gcf().subplots_adjust(bottom=0.15)
#         fig.add_subplot().plot(prc.long_frekunc_pdf)
#         canvas = FigureCanvasTkAgg(fig, self)
#         toolbar = NavigationToolbar2Tk(canvas, self)
#         toolbar.update()
#         canvas._tkcanvas.pack(fill=tk.BOTH, expand=10)

        
# class Procec():

    def __init__(self):
        path_pdf = extract_text(linkse)
        tokenz_pdf = RegexpTokenizer('\w+')
        tokens_pdf = tokenz_pdf.tokenize(path_pdf)
        frekunsi_pdf = FreqDist(tokens_pdf)
        self.long_frekunc_pdf = [words for words in tokens_pdf if len(words) == 3 and frekunsi_pdf[words] > 14]
        fig = plt.figure(0)
        fig.canvas.set_window_title('frekunsi MR DNS')
        plt.title('digaram', size=16)
        FreqDist(self.long_frekunc_pdf).plot()

apps = App()
apps.mainloop()