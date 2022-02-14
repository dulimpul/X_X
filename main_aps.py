import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from pdfminer import high_level






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

        # file tipe fungsi
        self.file_tipe = (
            ('text files', '*.pdf'),
            ('All files', '*.*'),
            
        )

        # open desk fungsi
        self.openfile = fd.askopenfilename(
            title='open file',
            initialdir='/home/MRDNS/Documents/python/project_python/lab_ujicoba/gui_ujicoba/gui_pdf_dan_file',
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

        global linkse
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
            window_run.grab_set()


# run sektor logika run
class Run_sektor(tk.Toplevel):    # sektor update nanti
   
    def __init__(self):
        super().__init__()
        self.geometry("1000x700")
        prc = Procec()
        self.reks1 = tk.Text(
            self,
            height=2,
            width=35,
            
        )
        self.reks1.place(x=56, y=60)
        self.reks1.insert(tk.END,prc.extrack_hasil)


class Procec():

    def __init__(self):
        lnk = App
        path = linkse
        pages = [0] # page 1
        self.extrack_hasil = high_level.extract_text(path, "",pages)
        

class Visualisasi:   #< ---- sektor visual
    pass

    
apps = App()
apps.mainloop()