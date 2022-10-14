from tkinter import*
import random
root= Tk()
root.title("Picnic List")
root.geometry("500x500")
label1= Label(root)
Label2= Label(root)
List1= ["Bottle", "muffins", "Id cards", "Chocolates", "Chips", "Tickets", "Hankerchief"]
label1["text"]= "List for picnic iss:"+str(List1)

def picnic_list():
    random_list= random.randint(0,6)
    Label2["text"]= "item number  "+str(random_list)+" Put In Bag  "
    
    
btn= Button(root, text= "Select Items  To Be Added In The Bag", command= picnic_list, bg="silver", fg="black")
btn.place(relx=0.5, rely=0.5, anchor= CENTER)

label1.place(relx=0.5, rely=0.4, anchor=CENTER)
Label2.place(relx=0.5, rely=0.6, anchor= CENTER)
root.mainloop()