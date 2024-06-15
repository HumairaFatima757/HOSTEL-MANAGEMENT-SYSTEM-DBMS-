from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Room_booking:
                    def __init__(self, root):
                        self.root = root
                        self.root.title("Hostel Management System")
                        self.root.geometry("1130x470+230+220")
                        
                        #=====================variable==================
                        self.var_contact=StringVar()
                        self.var_checkin=StringVar()
                        self.var_checkout=StringVar()
                        self.var_roomtype=StringVar()
                        self.var_roomavailable=StringVar()
                        self.var_meal=StringVar()
                        self.var_noofdays=StringVar()
                        self.var_total=StringVar()

                        #===========================title===============================
                        lbl_title = Label(self.root, text="ROOM BOOKING", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
                        lbl_title.place(x=0, y=0, width=1130, height=50)
                        
                        
                        
                        
                        #=======logo=============================
                        img2 = Image.open(r"C:\hotel management system(DBMS)\images\logo.jpg")
                        img2 = img2.resize((100, 45), Image.LANCZOS)
                        self.photoimg2 = ImageTk.PhotoImage(img2)

                        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
                        lblimg.place(x=5, y=2, width=100, height= 45)
                        
                        
                        # ==========label frame ============================== 
                        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING",font=("times new roman", 12, "bold"),padx=2)
                        Labelframeleft.place(x=5,y=50,width=425,height=410)
                        
                        
                     #fetchdata button ============================================= 
                        btnFetch=Button(Labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial", 8, "bold"),bg="black",fg="gold",width=7)
                        btnFetch.place(x=342,y=4)
                        
                        
                        
                        # ========labels and enteries========================
                    #customer contact
                        lbl_cust_contact=Label(Labelframeleft,text="HOSTELLER CONTACT:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lbl_cust_contact.grid(row=0,column=0,sticky=W)
                        
                        
                        entry_contact=Entry(Labelframeleft,textvariable=self.var_contact,font=("arial", 13, "bold"),width=15,background="yellow")
                        entry_contact.grid(row=0,column=1,sticky=W)
                        
                       
                        
                        
                        #check in date
                        check_in_date =Label(Labelframeleft,text="CHECK IN DATE:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        check_in_date.grid(row=1,column=0,sticky=W)
                        
                        
                        textcheck_in_date=Entry(Labelframeleft,textvariable=self.var_checkin,width=23,font=("arial", 13, "bold"),background="yellow")
                        textcheck_in_date.grid(row=1,column=1)
                        
                        
                        #checkout date 
                        label_Check_out_date =Label(Labelframeleft,text="CHECK OUT DATE:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        label_Check_out_date.grid(row=2,column=0,sticky=W)
                        
                        textcheck_out_date=Entry(Labelframeleft,textvariable=self.var_checkout,width=23,font=("arial", 13, "bold"),background="yellow")
                        textcheck_out_date.grid(row=2,column=1)
                        
                        
                        
                        #ROOM type
                        lblRoomType =Label(Labelframeleft,text="ROOM TYPE:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblRoomType.grid(row=3,column=0,sticky=W)
                        
                        
                        conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                        mycursor=conn.cursor()
                        mycursor.execute("select roomtype from details")
                        id=mycursor.fetchall()
                        
                     
                        combo_RoomType=ttk.Combobox(Labelframeleft,textvariable=self.var_roomtype,font=("arial", 12, "bold"),width=21,state="readonly")
                        combo_RoomType["value"]=id
                        combo_RoomType.current(0)
                        combo_RoomType.grid(row=3,column=1)
                        
                        #available room 
                        lblRoomAvailable =Label(Labelframeleft,text="AVAILABLE ROOM:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblRoomAvailable.grid(row=4,column=0,sticky=W)
                        
                        conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                        mycursor=conn.cursor()
                        mycursor.execute("select roomNo from details")
                        rows=mycursor.fetchall()
                        
                        combo_RoomNo=ttk.Combobox(Labelframeleft,textvariable=self.var_roomavailable,font=("arial", 12, "bold"),width=21,state="readonly")
                        combo_RoomNo["value"]=rows
                        combo_RoomNo.current(0)
                        combo_RoomNo.grid(row=4,column=1)
                        
                        
                        #MEAL
                        lblMeal =Label(Labelframeleft,text="MEAL:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblMeal.grid(row=5,column=0,sticky=W)
                        
                        txt_Meal=Entry(Labelframeleft,textvariable=self.var_meal,width=23,font=("arial", 13, "bold"),background="yellow")
                        txt_Meal.grid(row=5,column=1)
                        
                        
                        
                        
                        
                        #No Of Days
                        lblNoOfDays =Label(Labelframeleft,text="No Of Days:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblNoOfDays.grid(row=6,column=0,sticky=W)
                        
                        
                        txt_NoOfDays=Entry(Labelframeleft,textvariable=self.var_noofdays,width=23,font=("arial", 13, "bold"),background="yellow")
                        txt_NoOfDays.grid(row=6,column=1)
                        
                        
                    
                        #Total Cost 
                        lblIdNumber =Label(Labelframeleft,text="Total Cost:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblIdNumber.grid(row=7,column=0,sticky=W)
                        
                        
                        textIdNumber=Entry(Labelframeleft,textvariable=self.var_total,width=23,font=("arial", 13, "bold"),background="yellow")
                        textIdNumber.grid(row=7,column=1)
                        
                        #===============bill button==================
                        
                        
                        btnBill=Button(Labelframeleft,text="BILL",command=self.total,font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnBill.grid(row=9,column=0,padx=1,sticky=W)
                        
                      #-======================buttons======================
                        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
                        btn_frame.place(x=0,y=330,width=412,height=40)
                        
                        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnAdd.grid(row=0,column=0,padx=1)
                        
                        
                        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnUpdate.grid(row=0,column=1,padx=1)
                        
                        
                        btnDELETE=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnDELETE.grid(row=0,column=2,padx=1)
                        
                        
                        btnRESET=Button(btn_frame,text="RESET",command=self.reset,font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnRESET.grid(row=0,column=3,padx=1) 
                        
                        #=======right side image=============================
                        img3 = Image.open(r"C:\hotel management system(DBMS)\images\counter.jpg")
                        img3 = img3.resize((420, 200), Image.LANCZOS)
                        self.photoimg3 = ImageTk.PhotoImage(img3)

                        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
                        lblimg.place(x=700, y=55, width=420, height= 200)  
                        
                   #-======================tabel frame and search system====================== 
                        
                        tabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW Details",font=("times new roman", 12, "bold"),padx=2)
                        tabelframe.place(x=435,y=200,width=690,height=250)
                        
                        lblSeearchBy =Label(tabelframe,text="SERACH BY:",font=("arial", 12, "bold"),bg="purple",fg="black") 
                        lblSeearchBy.grid(row=0,column=0,sticky=W ,padx=2)
                        
                        self.Search_var=StringVar()
                        combo_Search=ttk.Combobox(tabelframe,textvariable=self.Search_var,font=("arial", 12, "bold"),width=18,state="readonly")
                        combo_Search["value"]=("Contact","Room")
                        combo_Search.current(0)
                        combo_Search.grid(row=0,column=1)
                        
                        self.txt_search=StringVar()
                        txt_Search=Entry(tabelframe,textvariable=self.txt_search,width=18,font=("arial", 13, "bold"),background="yellow")
                        txt_Search.grid(row=0,column=2,padx=2)
                    
                        btnSearch=Button(tabelframe,command=self.Search,text="Search",font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnSearch.grid(row=0,column=3,padx=2)
                        
                        
                        btnShowAll=Button(tabelframe,command=self.fetch_data,text="Show All",font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnShowAll.grid(row=0,column=4,padx=2)     
                        
                    
                    #-======================show table data  ======================
                        
                        details_table=Frame(tabelframe,bd=2,relief=RIDGE)
                        details_table.place(x=0,y=30,width=670,height=180) 
                    
                        Scroll_x =ttk.Scrollbar(details_table,orient=HORIZONTAL)
                        Scroll_Y =ttk.Scrollbar(details_table,orient=VERTICAL)
                        
                        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_Y.set)
                    
                        Scroll_x.pack(side=BOTTOM,fill=X)
                        Scroll_Y.pack(side=RIGHT,fill=Y)
                        
                        Scroll_x.config(command=self.room_table.xview)
                        Scroll_Y.config(command=self.room_table.yview)
                        
                        self.room_table.heading("contact",text="Contact")
                        self.room_table.heading("checkin",text="Check-in")
                        self.room_table.heading("checkout",text="Check-out")
                        self.room_table.heading("roomtype",text="Room Type ")
                        self.room_table.heading("roomavailable",text="Room No")
                        self.room_table.heading("meal",text="Meal")
                        self.room_table.heading("noOfdays",text="NoOfDays")
                    
                        
                        
                        self.room_table["show"]="headings"
                        
                        self.room_table.column("contact",width=100)
                        self.room_table.column("checkin",width=100)
                        self.room_table.column("checkout",width=100)
                        self.room_table.column("roomtype",width=100)
                        self.room_table.column("roomavailable",width=100)
                        self.room_table.column("meal",width=100)
                        self.room_table.column("noOfdays",width=100)
                        self.room_table.pack(fill=BOTH,expand=1)
                        
                        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
                        self.fetch_data()
                        
#add data===============================
                        
                    def add_data(self): 
                        if self.var_contact.get()=="" or self.var_checkin.get()=="":
                            messagebox.showerror("Error","All fields are required")
                        else:
                            try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                                mycursor=conn.cursor()
                                mycursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                            self.var_contact.get(),
                                            self.var_checkin.get(),
                                            self.var_checkout.get(),
                                            self.var_roomtype.get(),
                                            self.var_roomavailable.get(),
                                            self.var_meal.get(),
                                            self.var_noofdays.get()
                                               
                                                        
                                    
                                              ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","Room Booked",parent=self.root)
                            except Exception as es:
                                messagebox.showwarning("warning",f"Some thing went wrong:{str(es)}",parent=self.root)
    #===================fetchdata==============================
    
                    def fetch_data(self):
                        conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                        mycursor=conn.cursor()
                        mycursor.execute("select * from room")
                        rows=mycursor.fetchall()
                        if len(rows)!= 0:
                            self.room_table.delete(*self.room_table.get_children())
                            for i in rows:
                                self.room_table.insert("",END,values=i)
                            conn.commit()
                        conn.close()
                        
#===========================get cursor===================************=============
                    def get_cursor(self,event=""): 
                        cursor_row=self.room_table.focus()
                        content=self.room_table.item(cursor_row)
                        row =content["values"]
                        
                        self.var_contact.set(row[0]),
                        self.var_checkin.set(row[1]),
                        self.var_checkout.set(row[2]),
                        self.var_roomtype.set(row[3]),
                        self.var_roomavailable.set(row[4]),
                        self.var_meal.set(row[5]),
                        self.var_noofdays.set(row[6])
                        
#=================update================================
                        
                    def update(self):
                        if self.var_contact.get() == "":
                            messagebox.showerror("Error", "Please enter a mobile number", parent=self.root)
                        else:
                            try:
                                conn = mysql.connector.connect(host="localhost", username="root", password="1234qwer!@", database="management")
                                mycursor = conn.cursor()
                                mycursor.execute("""
                                            UPDATE room  
                                            SET  check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s where Contact=%s""", (
                                            
                                            self.var_checkin.get(),
                                            self.var_checkout.get(),
                                            self.var_roomtype.get(),
                                            self.var_roomavailable.get(),
                                            self.var_meal.get(),
                                            self.var_noofdays.get(),
                                            self.var_contact.get(),
                                            
                                            
                                    ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Update", "Room details have been updated successfully ", parent=self.root)
                            except Exception as es:
                                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
                                
  #=========================delete==================================================
  
                    def mDelete(self): 
                        mDelete=messagebox.askyesno("Hostel Management System ","Do YOU want to delete this room",parent=self.root)
                        if mDelete>0:
                           conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                           mycursor=conn.cursor() 
                           query="delete from room WHERE Contact=%s"
                           value=(self.var_contact.get(),)
                           mycursor.execute(query,value)
                        else:
                            if not mDelete:
                                return
                        conn.commit()
                        self.fetch_data()
                        conn.close()                              
 #===================reset==============================================
                    def reset(self):
                        self.var_contact.set(""),
                        self.var_checkin.set(""),
                        self.var_checkout.set(""),
                        self.var_roomtype.set(""),
                        self.var_roomavailable.set(""),
                        self.var_meal.set(""),
                        self.var_noofdays.set("") 
                        self.var_total.set("")                              
                                
                                
                        
                        
                  #===================all data============================================      
                    def Fetch_contact(self):
                        if self.var_contact.get()=="":
                            messagebox.showerror("Error","please enter contact number",parent=self.root)
                        else:
                            conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                            mycursor=conn.cursor()
                            query=("select Name from customer where Mobile=%s")
                            value=(self.var_contact.get(),)
                            mycursor.execute(query,value)
                            row=mycursor.fetchone()
                            
                            
                            if row==None:
                                messagebox.showerror("Error","This number Not Found",parent=self.root)
                            else:
                                conn.commit()
                                conn.close()
                                
                                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                                showDataframe.place(x=440,y=60,width=250,height=140)
                                
                                
                                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                                lblName.place(x=0,y=0) 
                                
                                lbl=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                                lbl.place(x=90,y=0)                      
                    
                    #-=============Gender========================================
                                conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                                mycursor=conn.cursor()
                                query=("select Gender from customer where Mobile=%s")
                                value=(self.var_contact.get(),)
                                mycursor.execute(query,value)
                                row=mycursor.fetchone()
                                
                                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                                lblGender.place(x=0,y=25) 
                                
                                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                                lbl2.place(x=90,y=25)
                        #=========================email==================
                                conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                                mycursor=conn.cursor()
                                query=("select Email from customer where Mobile=%s")
                                value=(self.var_contact.get(),)
                                mycursor.execute(query,value)
                                row=mycursor.fetchone()
                                
                                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                                lblemail.place(x=0,y=50) 
                                
                                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                                lbl3.place(x=70,y=50)
                                
                                
#=================================Nationality=============================

                                conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                                mycursor=conn.cursor()
                                query=("select Nationality from customer where Mobile=%s")
                                value=(self.var_contact.get(),)
                                mycursor.execute(query,value)
                                row=mycursor.fetchone()
                                
                                lblnationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                                lblnationality.place(x=0,y=75) 
                                
                                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                                lbl4.place(x=90,y=75)
 #======================ADDRESS==================================================
 
                                conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                                mycursor=conn.cursor()
                                query=("select Address from customer where Mobile=%s")
                                value=(self.var_contact.get(),)
                                mycursor.execute(query,value)
                                row=mycursor.fetchone()
                                
                                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                                lblAddress.place(x=0,y=100) 
                                
                                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                                lbl5.place(x=90,y=100)
#===========================serach system ==============================
                    def Search(self):
                        conn = mysql.connector.connect(host="localhost", username="root", password="1234qwer!@", database="management")
                        mycursor = conn.cursor()
                        
                        # Using parameterized queries to avoid SQL injection
                        search_by = self.Search_var.get()
                        search_value = self.txt_search.get()
                        
                        if search_by == "Contact":
                            query = "SELECT * FROM room WHERE Contact LIKE %s"
                        elif search_by == "Room":
                            query = "SELECT * FROM room WHERE room LIKE %s"
                        else:
                            # If an invalid search_by value is encountered
                            messagebox.showerror("Error", "Invalid search criteria")
                            conn.close()
                            return
                        
                        mycursor.execute(query, ("%" + search_value + "%",))
                        rows = mycursor.fetchall()
                        
                        if len(rows) != 0:
                            self.room_table.delete(*self.room_table.get_children())
                            for i in rows:
                                self.room_table.insert("", END, values=i)
                            conn.commit()
                        
                        conn.close()
                  
                  #  =====================================  
              
              
              
              
                                
                                
                    def total(self):
                        try:
                            inDate = self.var_checkin.get()
                            outDate = self.var_checkout.get()
                            inDate = datetime.strptime(inDate, "%d/%m/%Y")
                            outDate = datetime.strptime(outDate, "%d/%m/%Y")
                            self.var_noofdays.set(abs((outDate - inDate).days))
        
                            no_of_days = float(self.var_noofdays.get())
                            
                            # Prices for different meal and room type combinations
                            room_prices = {
                                "single": 500,
                                "double": 800,
                                "triple": 1000
                            }
                            
                            meal_prices = {
                                "Breakfast": 300,
                                "Lunch": 500,
                                "Dinner": 700
                            }
                            
                            room_price = room_prices.get(self.var_roomtype.get(), 0)
                            meal_price = meal_prices.get(self.var_meal.get(), 0)
                            
                            total_cost = no_of_days * (room_price + meal_price)
                            tax = total_cost * 0.1
                            total_cost_with_tax = total_cost + tax
                            
                            TT = "Rs. " + str("%.2f" % total_cost_with_tax)
                            self.var_total.set(TT)
                        except Exception as es:
                            messagebox.showerror("Error", f"Error calculating total: {str(es)}", parent=self.root)
                            
                            
                            
                            
                        #####################################
                        
                        
                    def total(self):
                        try:
                            inDate = self.var_checkin.get()
                            outDate = self.var_checkout.get()
                            inDate = datetime.strptime(inDate, "%d/%m/%Y")
                            outDate = datetime.strptime(outDate, "%d/%m/%Y")
                            self.var_noofdays.set(abs((outDate - inDate).days))
        
                            no_of_days = float(self.var_noofdays.get())
                            
                            # Prices for different meal and room type combinations
                            room_prices = {
                                "single": 500,
                                "double": 800,
                                "triple": 1000
                            }
                            
                            meal_prices = {
                                "Breakfast": 300,
                                "Lunch": 500,
                                "Dinner": 700
                            }
                            
                            room_price = room_prices.get(self.var_roomtype.get(), 0)
                            meal_price = meal_prices.get(self.var_meal.get(), 0)
                            
                            total_cost = no_of_days * (room_price + meal_price)
                            tax = total_cost * 0.1
                            total_cost_with_tax = total_cost + tax
                            
                            TT = "Rs. " + str("%.2f" % total_cost_with_tax)
                            self.var_total.set(TT)
                        except Exception as es:
                            messagebox.showerror("Error", f"Error calculating total: {str(es)}", parent=self.root)
                            
                        
                                    
                    
                        
                        
                        

if __name__ == "__main__":
                    root=Tk()
                    obj=Room_booking(root)
                    root.mainloop()