from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
               
class Cust_Win:
                    def __init__(self, root):
                        self.root = root
                        self.root.title("Hotel Management System")
                        self.root.geometry("1130x470+230+220")
                        
                    #===========================variaables=============================
                        self.var_ref=StringVar()
                        x=random.randint(1000,9999)
                        self.var_ref.set(str(x))
                        
                        self.var_cust_name=StringVar()
                        self.var_cust_gender=StringVar()
                        self.var_cust_mobile=StringVar()
                        self.var_cust_email=StringVar()
                        self.var_cust_nationality=StringVar()
                        self.var_cust_address=StringVar()
                        self.var_cust_id_proof=StringVar()
                        self.var_cust_id_number=StringVar()
                        
                    
                    
                    
                    
                        
                        #===========================title===============================
                        lbl_title = Label(self.root, text="ADD HOSTELLER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
                        lbl_title.place(x=0, y=0, width=1130, height=50)
                        
                        
                        
                        
                        #=======logo=============================
                        img2 = Image.open(r"C:\hotel management system(DBMS)\images\logo.jpg")
                        img2 = img2.resize((100, 45), Image.LANCZOS)
                        self.photoimg2 = ImageTk.PhotoImage(img2)

                        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
                        lblimg.place(x=5, y=2, width=100, height= 45)
                        
                        
                        
                        
                        # ==========label frame ============================== 
                        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Hosteller Details",font=("times new roman", 12, "bold"),padx=2)
                        Labelframeleft.place(x=5,y=50,width=425,height=410)
                        
                        
                    # ========labels and enteries========================
                    #customer reference
                        lbl_cust_ref=Label(Labelframeleft,text="HOSTELLER REF:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lbl_cust_ref.grid(row=0,column=0,sticky=W)
                        
                        
                        entry_ref=Entry(Labelframeleft,textvariable=self.var_ref,font=("arial", 13, "bold"),width=25,state="readonly",background="yellow")
                        entry_ref.grid(row=0,column=1)
                        
                        #customer name
                        cname =Label(Labelframeleft,text="HOSTELLER NAME:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        cname.grid(row=1,column=0,sticky=W)
                        
                        
                        text_cname=Entry(Labelframeleft,textvariable=self.var_cust_name,width=25,font=("arial", 13, "bold"),background="yellow")
                        text_cname.grid(row=1,column=1)
                        
                        
                        #gender combobox
                        label_gender =Label(Labelframeleft,text="GENDER:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        label_gender.grid(row=2,column=0,sticky=W)
                        
                        combo_Gender=ttk.Combobox(Labelframeleft,textvariable=self.var_cust_gender,font=("arial", 12, "bold"),width=23,state="readonly")
                        combo_Gender["value"]=("Male","Female","Other")
                        combo_Gender.current(0)
                        combo_Gender.grid(row=2,column=1)
                        
                        #postcode
                    # lblPostCode =Label(Labelframeleft,text="CODE:",font=("arial", 12, "bold"),padx=2,pady=6) 
                    # lblPostCode.grid(row=3,column=0,sticky=W)
                        
                        
                    # txt_postCode=Entry(Labelframeleft,width=25,font=("arial", 13, "bold"),background="yellow")
                    # txt_postCode.grid(row=3,column=1)
                        
                        
                        #phone number
                        lblMobile =Label(Labelframeleft,text="PHONE NO:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblMobile.grid(row=4,column=0,sticky=W)
                        
                        
                        txt_Mobile=Entry(Labelframeleft,textvariable=self.var_cust_mobile,width=25,font=("arial", 13, "bold"),background="yellow")
                        txt_Mobile.grid(row=4,column=1)
                        
                        #email
                        lblEmail =Label(Labelframeleft,text="EMAIL:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblEmail.grid(row=5,column=0,sticky=W)
                        
                        
                        txt_Email=Entry(Labelframeleft,textvariable=self.var_cust_email,width=25,font=("arial", 13, "bold"),background="yellow")
                        txt_Email.grid(row=5,column=1)
                        
                        
                        #NATIONALITY
                        lblNationality =Label(Labelframeleft,text="NATIONALITY:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblNationality.grid(row=6,column=0,sticky=W)
                        
                        
                        combo_Nationality=ttk.Combobox(Labelframeleft,textvariable=self.var_cust_nationality,font=("arial", 12, "bold"),width=23,state="readonly")
                        combo_Nationality["value"]=("pakistan","bangladesh","Indian","American","saudia Arabia")
                        combo_Nationality.current(0)
                        combo_Nationality.grid(row=6,column=1)
                        
                        
                        
                        #id proof 
                        lblIdProof =Label(Labelframeleft,text="ID PROOF TYPE:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblIdProof.grid(row=7,column=0,sticky=W)
                        
                        
                        combo_id=ttk.Combobox(Labelframeleft,textvariable=self.var_cust_id_proof,font=("arial", 12, "bold"),width=23,state="readonly")
                        combo_id["value"]=("NIC","DRIVING LICENSE","PASSPORT",)
                        combo_id.current(0)
                        combo_id.grid(row=7,column=1)
                        
                        
                        
                        
                        #id number 
                        lblIdNumber =Label(Labelframeleft,text="ID NUMBER:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblIdNumber.grid(row=8,column=0,sticky=W)
                        
                        
                        textIdNumber=Entry(Labelframeleft,textvariable=self.var_cust_id_number,width=25,font=("arial", 13, "bold"),background="yellow")
                        textIdNumber.grid(row=8,column=1)
                        
                        
                        
                        #address 
                        lblAddress =Label(Labelframeleft,text="ADDRESS:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lblAddress.grid(row=9,column=0,sticky=W)
                        
                        
                        textAddress=Entry(Labelframeleft,textvariable=self.var_cust_address ,width=25,font=("arial", 13, "bold"),background="yellow")
                        textAddress.grid(row=9,column=1)
                        
                        
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
                        
                    
                    
        #-======================tabel frame and search system====================== 
                        
                        tabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW Details",font=("times new roman", 12, "bold"),padx=2)
                        tabelframe.place(x=435,y=50,width=690,height=410)
                        
                        lblSeearchBy =Label(tabelframe,text="SERACH BY:",font=("arial", 12, "bold"),bg="purple",fg="black") 
                        lblSeearchBy.grid(row=0,column=0,sticky=W ,padx=2)
                        
                        self.Search_var=StringVar()
                        combo_Search=ttk.Combobox(tabelframe,textvariable=self.Search_var,font=("arial", 12, "bold"),width=18,state="readonly")
                        combo_Search["value"]=("Mobile","REF")
                        combo_Search.current(0)
                        combo_Search.grid(row=0,column=1)
                        
                        self.txt_search=StringVar()
                        txt_Search=Entry(tabelframe,textvariable=self.txt_search,width=18,font=("arial", 13, "bold"),background="yellow")
                        txt_Search.grid(row=0,column=2,padx=2)
                    
                        btnSearch=Button(tabelframe,text="Search",command=self.Search,font=("arial", 13, "bold"),bg="black",fg="gold",width=8)
                        btnSearch.grid(row=0,column=3,padx=1)
                        
                        
                        btnShowAll=Button(tabelframe,text="Show All",command=self.fetch_data,font=("arial", 13, "bold"),bg="black",fg="gold",width=8)
                        btnShowAll.grid(row=0,column=4,padx=1)
                        
                        
                        
                        #-======================show table data  ======================
                        
                        details_table=Frame(tabelframe,bd=2,relief=RIDGE)
                        details_table.place(x=0,y=50,width=650,height=320) 
                    
                        Scroll_x =ttk.Scrollbar(details_table,orient=HORIZONTAL)
                        Scroll_Y =ttk.Scrollbar(details_table,orient=VERTICAL)
                        
                        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","gender","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_Y.set)
                    
                        Scroll_x.pack(side=BOTTOM,fill=X)
                        Scroll_Y.pack(side=RIGHT,fill=Y)
                        
                        Scroll_x.config(command=self.Cust_Details_Table.xview)
                        Scroll_Y.config(command=self.Cust_Details_Table.yview)
                        
                        self.Cust_Details_Table.heading("ref",text="Refer No")
                        self.Cust_Details_Table.heading("name",text="Name")
                        self.Cust_Details_Table.heading("gender",text="Gender")
                        self.Cust_Details_Table.heading("mobile",text="Phone No")
                        self.Cust_Details_Table.heading("email",text="Email")
                        self.Cust_Details_Table.heading("nationality",text="Nationality")
                        self.Cust_Details_Table.heading("idproof",text="D Proof")
                        self.Cust_Details_Table.heading("idnumber",text="ID No")
                        self.Cust_Details_Table.heading("address",text="Address")
                        
                        
                        self.Cust_Details_Table["show"]="headings"
                        
                        self.Cust_Details_Table.column("ref",width=100)
                        self.Cust_Details_Table.column("name",width=100)
                        self.Cust_Details_Table.column("gender",width=100)
                        self.Cust_Details_Table.column("mobile",width=100)
                        self.Cust_Details_Table.column("email",width=100)
                        self.Cust_Details_Table.column("nationality",width=100)
                        self.Cust_Details_Table.column("idproof",width=100)
                        self.Cust_Details_Table.column("idnumber",width=100)
                        self.Cust_Details_Table.column("address",width=100)
                        
                        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
                        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
                        self.fetch_data()
                
                
                    def add_data(self): 
                        if self.var_cust_mobile.get()=="" or self.var_cust_address.get()=="":
                            messagebox.showerror("Error","All fields are required")
                        else:
                            try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                                mycursor=conn.cursor()
                                mycursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                    
                                    self.var_ref.get(),
                                    self.var_cust_name.get(),
                                    self.var_cust_gender.get(),
                                    self.var_cust_mobile.get(),
                                    self.var_cust_email.get(),
                                    self.var_cust_nationality.get(),
                                    self.var_cust_id_proof.get(),
                                    self.var_cust_id_number.get(),
                                    self.var_cust_address.get(),
                                    
                                    ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","customer has been added",parent=self.root)
                            except Exception as es:
                                messagebox.showwarning("warning",f"Some thing went wrong:{str(es)}",parent=self.root)
                                
                    def fetch_data(self):
                        conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                        mycursor=conn.cursor()
                        mycursor.execute("select * from customer")
                        rows=mycursor.fetchall()
                        if len(rows)!= 0:
                            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                            for i in rows:
                                self.Cust_Details_Table.insert("",END,values=i)
                            conn.commit()
                        conn.close()
                        
                        
                    def get_cursor(self,event=""): 
                        cursor_row=self.Cust_Details_Table.focus()
                        content=self.Cust_Details_Table.item(cursor_row)
                        row =content["values"]
                        
                        self.var_ref.set(row[0])
                        self.var_cust_name.set(row[1]) 
                        self.var_cust_gender.set(row[2])
                        self.var_cust_mobile.set(row[3]) 
                        self.var_cust_email.set(row[4])
                        self.var_cust_nationality.set(row[5])
                        self.var_cust_id_proof.set(row[6])
                        self.var_cust_id_number.set(row[7])
                        self.var_cust_address.set(row[8])    
                    
                    
                    def update(self):
                        if self.var_cust_mobile.get() == "":
                            messagebox.showerror("Error", "Please enter a mobile number", parent=self.root)
                        else:
                            try:
                                conn = mysql.connector.connect(host="localhost", username="root", password="1234qwer!@", database="management")
                                mycursor = conn.cursor()
                                mycursor.execute("""
                                            UPDATE customer 
                                            SET Name=%s, Gender=%s, Mobile=%s, Email=%s, Nationality=%s, IdProof=%s, IdNumber=%s, Address=%s 
                                            WHERE Ref=%s
                                        """, (
                                            self.var_cust_name.get(),
                                            self.var_cust_gender.get(),
                                            self.var_cust_mobile.get(),
                                            self.var_cust_email.get(),
                                            self.var_cust_nationality.get(),
                                            self.var_cust_id_proof.get(),
                                            self.var_cust_id_number.get(),
                                            self.var_cust_address.get(),
                                            self.var_ref.get()
                                    ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Update", "Customer details have been updated successfully", parent=self.root)
                            except Exception as es:
                                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
                                
                                
                    def mDelete(self): 
                        mDelete=messagebox.askyesno("hotel Management System ","Do YOU want to delete this customer",parent=self.root)
                        if mDelete>0:
                           conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                           mycursor=conn.cursor() 
                           query="delete from customer WHERE Ref=%s"
                           value=(self.var_ref.get(),)
                           mycursor.execute(query,value)
                        else:
                            if not mDelete:
                                return
                        conn.commit()
                        self.fetch_data()
                        conn.close() 
                        
                        
                    def reset(self):
                       # self.var_ref.set("")
                        self.var_cust_name.set("") 
                        #self.var_cust_gender.set("")
                        self.var_cust_mobile.set("") 
                        self.var_cust_email.set("")
                        #self.var_cust_nationality.set("")
                        #self.var_cust_id_proof.set("")
                        self.var_cust_id_number.set("")
                        self.var_cust_address.set("")
                        
                        
                        x=random.randint(1000,9999)
                        self.var_ref.set(str(x))     
                    
                    
                    def Search(self):
                        conn = mysql.connector.connect(host="localhost", username="root", password="1234qwer!@", database="management")
                        mycursor = conn.cursor()
                        
                        # Using parameterized queries to avoid SQL injection
                        search_by = self.Search_var.get()
                        search_value = self.txt_search.get()
                        
                        if search_by == "Mobile":
                            query = "SELECT * FROM customer WHERE Mobile LIKE %s"
                        elif search_by == "REF":
                            query = "SELECT * FROM customer WHERE Ref LIKE %s"
                        else:
                            # If an invalid search_by value is encountered
                            messagebox.showerror("Error", "Invalid search criteria")
                            conn.close()
                            return
                        
                        mycursor.execute(query, ("%" + search_value + "%",))
                        rows = mycursor.fetchall()
                        
                        if len(rows) != 0:
                            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                            for i in rows:
                                self.Cust_Details_Table.insert("", END, values=i)
                            conn.commit()
                        
                        conn.close()
                  
                    
                    
                            
                                    
if __name__ == "__main__":
                    root=Tk()
                    obj=Cust_Win(root)
                    root.mainloop()        