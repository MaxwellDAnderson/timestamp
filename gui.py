import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Timestamp:
    __root = Tk()

    # Window Size
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # Scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):
        # icon
        try:
            self.__root.wm_iconbitmap("Timestamp.ico")
        except:
            pass

        # Default Window Size
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Title
        self.__root.title("Untitled - Timestamp")

        # Window Center
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # Left Align
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # Right Align
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # Top and Bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        # Auto Resize
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Controls
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # Create New Fil
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)

        # Open
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)

        # Save
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)

        # To create a line in the dialog box
        self.__thisFileMenu.add_separator()

        # To terminate
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)

        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)

        # Cut
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)

        # Copy
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)

        # Paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)

        # Editing Feature
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        # About
        self.__thisHelpMenu.add_command(label="About Timestamp",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        self.__thisScrollBar.config(command=self.__thisTextArea.yview)

        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo("Timestamp", "Mrinal Verma")

    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":
            # No File
            self.__file = None
        else:
            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Timestamp")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Timestamp")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):
        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile="Untitled.txt",
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - Timestamp")

        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        # Run main application
        self.__root.mainloop()


# Run main application


timestamp = Timestamp(width=600, height=400)


timestamp.run()

