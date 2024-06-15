conn=mysql.connector.connect(host="localhost",username="root",password="1234qwer!@",database="management") 
                        mycursor=conn.cursor()
                        mycursor.execute("select * from details")
                        rows=mycursor.fetchall()