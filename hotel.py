from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Room_booking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Management System")
        self.root.geometry("1550x800+0+0")
        
        #=======1st image=========================
        img1 = Image.open(r"C:\hotel management system(DBMS)\images\top2.jpg")
        img1 = img1.resize((1500, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1500, height=140)
        
        #=======logo=============================
        img2 = Image.open(r"C:\hotel management system(DBMS)\images\logohostel2.jpg")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4,bg="lightgreen", relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
        
        #===========================title===============================
        lbl_title = Label(self.root, text="HOSTEL MANAGEMENT SYSTEM", font=("Georgia", 40, "bold","italic"), bg="lightgreen", fg="blue", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1500, height=50)
        
        #===========================main frame===============================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1500, height=590)
        
        #=============================menu=========================
        lbl_menu = Label(main_frame, text="ALL DETAILS", font=("times new roman", 20, "bold","italic"), bg="lightgreen", fg="blue", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)
        
        #===========================btn frame===============================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)
        
        cust_btn = Button(btn_frame, text="HOSTELLER",command=self.custdetails, width=22, font=("times new roman", 14, "bold","italic"), bg="lightgreen", fg="blue", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)
        
        room_btn = Button(btn_frame, text="ROOM",command=self.roombooking, width=22, font=("times new roman", 14, "bold","italic"), bg="lightgreen", fg="blue", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)
        
        details_btn = Button(btn_frame, text="DETAILS",command=self.details_room, width=22, font=("times new roman", 14, "bold","italic"), bg="lightgreen", fg="blue", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)
        
        # report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold","italic"),bg="lightgreen", fg="blue", bd=0, cursor="hand2")
        # report_btn.grid(row=3, column=0, pady=1)
        
        # logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold","italic"),bg="lightgreen", fg="blue", bd=0, cursor="hand1")
        # logout_btn.grid(row=4, column=0, pady=1)
        
        #=================right side image==============================
        img3 = Image.open(r"C:\hotel management system(DBMS)\images\hostel2.jpg")
        img3 = img3.resize((1130, 500), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1130, height=500)
        
        #=================down images==============================
        img4 = Image.open(r"C:\hotel management system(DBMS)\images\hostel.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=150, width=230, height=220)
        
        img5 = Image.open(r"C:\hotel management system(DBMS)\images\food.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=370, width=230, height=130)
        
    def custdetails(self):
        self.new_window=Toplevel(self.root)
        self.app =Cust_Win(self.new_window)

    
    
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app =Room_booking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app =DetailsRoom(self.new_window)








        
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
