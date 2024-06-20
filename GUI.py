from tkinter import *
from tkiner_function import browse_directory,update_list_box,merged_pdf

root=Tk()
root.title("PDF file searching Program")
root.geometry('700x600')
label_dir=Label(root,text='Directory',font='Bold')
label_dir.grid(row=0,column=0,padx=20,pady=30)
selected_dir=" "
entry_dir=Entry(root,width=60)
entry_dir.grid(row=0,column=1)
button_browse=Button(root,text='Browse Folder',command=lambda:browse_directory(selected_dir,entry_dir,list_box,list_box_merged))
button_browse.grid(row=1,column=0)
label_list=Label(root,text='PDF files: ',font='Bold')
label_list.grid(row=2,column=0,pady=15)
list_box=Listbox(root,width=50)
list_box.grid(row=3,column=0,columnspan=4)


list_box_merged_label=Label(root,text='Merged PDF',font='Bold')
list_box_merged_label.grid(row=4,column=0)
list_box_merged=Listbox(root,width=50)
list_box_merged.grid(row=5,column=0,columnspan=4)

root.mainloop()