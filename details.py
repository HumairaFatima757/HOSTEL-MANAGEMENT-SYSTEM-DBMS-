from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
                    def __init__(self, root):
                        self.root = root
                        self.root.title("Hotel Management System")
                        self.root.geometry("1130x470+230+220")
                        
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
                        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman", 12, "bold"),padx=2)
                        Labelframeleft.place(x=5,y=50,width=540,height=350)
                        
                        #Floor
                        lbl_Floor=Label(Labelframeleft,text="FLOOR:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lbl_Floor.grid(row=0,column=0,sticky=W)
                        
                        
                        
                        self.var_floor=StringVar()
                        entry_Floor=Entry(Labelframeleft,textvariable=self.var_floor,font=("arial", 13, "bold"),width=15,background="yellow")
                        entry_Floor.grid(row=0,column=1,sticky=W)
                        
                        
                        
                        
                        
                        #room number========
                        lbl_RoomNo=Label(Labelframeleft,text="ROOM NO:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lbl_RoomNo.grid(row=1,column=0,sticky=W)
                        
                        self.var_roomNo=StringVar()
                        entry_RoomNo=Entry(Labelframeleft,textvariable=self.var_roomNo,font=("arial", 13, "bold"),width=15,background="yellow")
                        entry_RoomNo.grid(row=1,column=1,sticky=W)
                        
                        
                        
                        #room type=================
                        lbl_RoomType=Label(Labelframeleft,text="ROOM TYPE:",font=("arial", 12, "bold"),padx=2,pady=6) 
                        lbl_RoomType.grid(row=2,column=0,sticky=W)
                        
                        self.var_RoomType=StringVar()
                        entry_RoomType=Entry(Labelframeleft,textvariable=self.var_RoomType,font=("arial", 13, "bold"),width=15,background="yellow")
                        entry_RoomType.grid(row=2,column=1,sticky=W)
                        
                     #-======================buttons======================
                        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
                        btn_frame.place(x=0,y=180,width=412,height=40)
                        
                        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnAdd.grid(row=0,column=0,padx=1)
                        
                        
                        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnUpdate.grid(row=0,column=1,padx=1)
                        
                        
                        btnDELETE=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnDELETE.grid(row=0,column=2,padx=1)
                        
                        
                        btnRESET=Button(btn_frame,text="RESET",command=self.reset,font=("arial", 13, "bold"),bg="black",fg="gold",width=9)
                        btnRESET.grid(row=0,column=3,padx=1) 
                        
                        
                       #table farme search  
                        
                        tabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="SHOW ROOM DETAILS ",font=("times new roman", 12, "bold"),padx=2)
                        tabelframe.place(x=550,y=55,width=570,height=350) 
                        
                        
                        Scroll_x =ttk.Scrollbar(tabelframe,orient=HORIZONTAL)
                        Scroll_Y =ttk.Scrollbar(tabelframe,orient=VERTICAL)
                        
                        self.room_table=ttk.Treeview(tabelframe,column=("floor","roomno","roomtype"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_Y.set)
                    
                        Scroll_x.pack(side=BOTTOM,fill=X)
                        Scroll_Y.pack(side=RIGHT,fill=Y)
                        
                        Scroll_x.config(command=self.room_table.xview)
                        Scroll_Y.config(command=self.room_table.yview) 
                        
                        
                        self.room_table.heading("floor",text="Floor")
                        self.room_table.heading("roomno",text="Room No")
                        self.room_table.heading("roomtype",text="Room Type")
                       
                    
                        
                        
                        self.room_table["show"]="headings"
                        
                        self.room_table.column("floor",width=100)
                        self.room_table.column("roomno",width=100)
                        self.room_table.column("roomtype",width=100)
                        
                        self.room_table.pack(fill=BOTH,expand=1)
                        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
                        self.fetch_data()   
                        
#add data==================================================
                        
                    def add_data(self): 
                        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
                            messagebox.showerror("Error","All fields are required")
                        else:
                            try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                                mycursor=conn.cursor()
                                mycursor.execute("insert into details values(%s,%s,%s)",(
                                            self.var_floor.get(),
                                            self.var_roomNo.get(),
                                            self.var_RoomType.get(),
                                           
                                              ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","Room Added Successfully",parent=self.root)
                            except Exception as es:
                                messagebox.showwarning("warning",f"Some thing went wrong:{str(es)}",parent=self.root)     
                        
                     #===================fetchdata==============================
    
                    def fetch_data(self):
                        conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                        mycursor=conn.cursor()
                        mycursor.execute("select * from details")
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
                        
                        self.var_floor.set(row[0]),
                        self.var_roomNo.set(row[1]),
                        self.var_RoomType.set(row[2]),
                         
                         
                         
                         #=================update================================
                        
                    def update(self):
                        if self.var_floor.get() == "":
                            messagebox.showerror("Error", "Please enter a floor number", parent=self.root)
                        else:
                            try:
                                conn = mysql.connector.connect(host="localhost", username="root", password="1234qwer!@", database="management")
                                mycursor = conn.cursor()
                                mycursor.execute("""
                                            UPDATE details  
                                            SET  floor=%s, roomtype=%s where roomno=%s """, (
                                            
                                            self.var_floor.get(),
                                            self.var_RoomType.get(),
                                            self.var_roomNo.get(),
                                           
                                            
                                            
                                    ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Update", "new Room details have been updated successfully ", parent=self.root)
                            except Exception as es:
                                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

                    #=========================delete==================================================
  
                    def mDelete(self): 
                        mDelete=messagebox.askyesno("Hotel Management System ","Do you want to delete this room details",parent=self.root)
                        if mDelete>0:
                           conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                           mycursor=conn.cursor() 
                           query="delete from details WHERE roomno=%s"
                           value=(self.var_roomNo.get(),)
                           mycursor.execute(query,value)
                        else:
                            if not mDelete:
                                return
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        
                        
                        
      #===================reset==============================================
                    def reset(self):
                        self.var_floor.set(""),
                        self.var_roomNo.set(""),
                        self.var_RoomType.set(""),
                              
                        
                        
                        
if __name__ == "__main__":
                    root=Tk()
                    obj=DetailsRoom(root)
                    root.mainloop()