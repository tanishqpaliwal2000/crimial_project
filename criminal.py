from tkinter import*
from ast import Delete, Try
from cgitb import text
from concurrent.futures.process import _chain_from_iterable_of_lists
from email.mime import image
from logging import root
from msilib.schema import tables
from multiprocessing.sharedctypes import Value
from operator import ge
from re import L, T
from select import select
#from ssl import _PasswordType

from tkinter import Tk, scrolledtext
from tkinter.tix import COLUMN

from tkinter import ttk
from typing_extensions import Self
from typing_extensions import Self
from unicodedata import name
from webbrowser import get
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry



class criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('criminal management')

        #variables
        self.var_case_id=StringVar()
        self.var_criminalid=StringVar()
        self.var_name=StringVar()
        self.var_Nickname=StringVar()
        self.var_arrestdate=StringVar()
        self.var_dateofcrime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar()
        self.var_criminaltype=StringVar()
        self.var_fathername=StringVar()
        self.var_gender=StringVar()
        self.var_mostwanted=StringVar()


        # add data


        lbl_title=Label(self.root,text='criminal management system software',font=('times new roman',45,'bold'),bg='black',fg='red')
        lbl_title.place(x=0,y=0,width=1300,height=70)

        #image logo
        img_logo=Image.open('images/logo.jpg')
        img_logo=img_logo.resize((50,50),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=10,y=5,width=60,height=60)

        #img frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1500,height=130)

        #img frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=0,y=170,width=1500,height=400)

        #img frame
        down_frame=Frame(self.root,bd=3,relief=RIDGE,bg='violet')
        down_frame.place(x=0,y=500,width=1500,height=500)

        # Label entry

        # case id
        case_id=Label(main_frame,text='Case id',font=('arial',11,'bold'),bg='white')
        case_id.grid(row=0,column=0,padx=0,sticky=W)

        caseentry=ttk.Entry(main_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=0,sticky=W)

        #criminal name
        criminal_name=Label(main_frame,text='Criminal name',font=('arial',11,'bold'),bg='white')
        criminal_name.grid(row=1,column=0,padx=0,pady=2,sticky=W)

        caseentry=ttk.Entry(main_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=1,column=1,padx=2,pady=2,sticky=W)

        #arrest date
        arrest_date=Label(main_frame,text='Arrest date',font=('arial',11,'bold'),bg='white')
        arrest_date.grid(row=2,column=0,padx=0,pady=2,sticky=W)
        
        

        caseentry=DateEntry(main_frame,textvariable=self.var_arrestdate,width=22,selectmode='day')
        caseentry.grid(row=2,column=1,padx=2,pady=2,sticky=W)

        #address
        address=Label(main_frame,text='Address',font=('arial',11,'bold'),bg='white')
        address.grid(row=3,column=0,padx=0,pady=2,sticky=W)

        caseentry=ttk.Entry(main_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=3,column=1,padx=2,pady=2,sticky=W)

        #occupation
        occupation=Label(main_frame,text='Occupation',font=('arial',11,'bold'),bg='white')
        occupation.grid(row=4,column=0,padx=0,pady=2,sticky=W)

        caseentry=ttk.Entry(main_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=4,column=1,padx=2,pady=2,sticky=W)

        #criminal id
        criminal_id=Label(main_frame,text='Criminal id',font=('arial',11,'bold'),bg='white')
        criminal_id.grid(row=0,column=2,padx=5,pady=4,sticky=W)

        caseentry=ttk.Entry(main_frame,textvariable=self.var_criminalid,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=3,padx=5,pady=2,sticky=W)

        #Nick name
        nickname=Label(main_frame,text='Nick name',font=('arial',11,'bold'),bg='white')
        nickname.grid(row=1,column=2,padx=5,pady=4,sticky=W)

        caseentry=ttk.Entry(main_frame,textvariable=self.var_Nickname,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=1,column=3,padx=5,pady=2,sticky=W)

        #date of crime
        DOC=Label(main_frame,text='Date of Crime',font=('arial',11,'bold'),bg='white')
        DOC.grid(row=2,column=2,padx=5,pady=4,sticky=W)

        caseentry=DateEntry(main_frame,textvariable=self.var_dateofcrime,width=22,selectmode='day')
        caseentry.grid(row=2,column=3,padx=5,pady=2,sticky=W)

        #AGE
        AGE=Label(main_frame,text='Age',font=('arial',11,'bold'),bg='white')
        AGE.grid(row=3,column=2,padx=5,pady=4,sticky=W)

        caseentry=DateEntry(main_frame,textvariable=self.var_age,width=22,selectmode='day')
        caseentry.grid(row=3,column=3,padx=5,pady=2,sticky=W)

        #BIRTHMARK
        BIRTHMARK=Label(main_frame,text='Birthmark',font=('arial',11,'bold'),bg='white')
        BIRTHMARK.grid(row=4,column=2,padx=5,pady=4,sticky=W)

        caseentry=ttk.Entry(main_frame,textvariable=self.var_birthmark,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=4,column=3,padx=5,pady=2,sticky=W)

        #CRIME TYPE
        CRIMETYPE=Label(main_frame,text='Crime Type',font=('arial',11,'bold'),bg='white')
        CRIMETYPE.grid(row=0,column=4,padx=5,pady=4,sticky=W)

        caseentry=ttk.Entry(main_frame,textvariable=self.var_criminaltype,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=5,padx=5,pady=2,sticky=W)

        #FATHER NAME 
        CRIMETYPE=Label(main_frame,text='Father Name',font=('arial',11,'bold'),bg='white')
        CRIMETYPE.grid(row=1,column=4,padx=5,pady=4,sticky=W)

        caseentry=ttk.Entry(main_frame,textvariable=self.var_fathername,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=1,column=5,padx=5,pady=2,sticky=W)


        #GENDER

        GENDER=Label(main_frame,font=('arial',11,'bold'),text='Gender',bg='white')
        GENDER.grid(row=3,column=4,sticky=W,padx=2,pady=4)

        # radioframegender

        radioframe=Frame(main_frame,bd=2,relief=RIDGE,bg='white')
        radioframe.place(x=730,y=90,width=190,height=30)

        MALE=Radiobutton(radioframe,variable=self.var_gender,text='male',value='male',font=('arial',9,'bold'),bg='white')
        MALE.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        FEMALE=Radiobutton(radioframe,variable=self.var_gender,text='female',cursor="hand2",value='Female',font=('arial',9,'bold'),bg='white')
        FEMALE.grid(row=0,column=1,sticky=W,padx=5,pady=2)


        # wantedframegender

        wantedframe=Frame(main_frame,bd=2,relief=RIDGE,bg='white')
        wantedframe.place(x=730,y=130,width=190,height=30)

        yes=Radiobutton(wantedframe,variable=self.var_mostwanted,text='yes',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        no=Radiobutton(wantedframe,variable=self.var_mostwanted,text='no',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,sticky=W,padx=5,pady=2)




        #wanted
        wanted=Label(main_frame,font=('arial',11,'bold'),text='Most Wanted',bg='white')
        wanted.grid(row=4,column=4,sticky=W,padx=2,pady=4)

        #buttons frame
        Buttonframe=Frame(main_frame,bd=2,relief=RIDGE,bg='white')
        Buttonframe.place(x=650,y=200,width=630,height=45)

        #add but
        Add_button=Button(Buttonframe,command=self.ad,text='record save',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        Add_button.grid(row=0,column=0,padx=3,pady=5)
        #update button
        save_button=Button(Buttonframe,text='update',command=self.update_data,font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        save_button.grid(row=0,column=1,padx=3,pady=5)

        #clear buttonz
        update_button=Button(Buttonframe,command=self.clear_data,text='clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        update_button.grid(row=0,column=2,padx=3,pady=5)

        #exitbutton
        update_button=Button(Buttonframe,command=self.delete_data,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        update_button.grid(row=0,column=3,padx=3,pady=5)

        #SEARCH FRAME
        searchframe=Frame(main_frame,bd=2,relief=RIDGE,bg='violet')
        searchframe.place(x=0,y=250,width=1300,height=300)

        searchbar=Label(searchframe,bd=2,font=('arial',14,'bold'),bg='white')
        searchbar.place(x=5,y=10,width=1250,height=60)

        searchby=Label(searchbar,text='Search by :',font=('arial',15,'bold'),bg='red',fg='white')
        searchby.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        #combobo
        self.var_com_search=StringVar()
        Combobox=ttk.Combobox(searchbar,textvariable= self.var_com_search,font=('arial',15,'bold'),width=18,state='readonly')
        Combobox['value']=('select option','case_id','criminal_no')
        Combobox.current(0)
        Combobox.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        search_text=ttk.Entry(searchbar,textvariable=self.var_search,width=18,font=('arial',15,'bold'))
        search_text.grid(row=0,column=5)


        #search button
    
        search_button=Button(searchbar,command=self.searrch_data,text="search",bg='pink',fg='white',width=15,font=('arial',12,'bold'))
        search_button.grid(row=0,column=6,padx=10,pady=0)

        show_button=Button(searchbar,command=self.fetch_data,text="show all",bg='pink',fg='white',width=15,font=('arial',12,'bold'))
        show_button.grid(row=0,column=7,padx=10,pady=0)

        #table frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=10,width=1400,height=130)

        # scrolledtext
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='case id')
        self.criminal_table.heading('2',text='crime no')
        self.criminal_table.heading('3',text='criminal name')
        self.criminal_table.heading('4',text='nick name')
        self.criminal_table.heading('5',text='arrest date')
        self.criminal_table.heading('6',text='crime of date')
        self.criminal_table.heading('7',text='address')
        self.criminal_table.heading('8',text='age')
        self.criminal_table.heading('9',text='occupation')
        self.criminal_table.heading('10',text='birth mark')
        self.criminal_table.heading('11',text='crime type')
        self.criminal_table.heading('12',text='father name')
        self.criminal_table.heading('13',text='gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

       #add function
    def ad(self):

        if self.var_case_id.get()=="":
            messagebox.showerror('Error','ALL fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='YES',database='criminal managementl',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                                self.var_case_id.get(),
                                                                                                                self.var_criminalid.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_Nickname.get(),
                                                                                                                self.var_arrestdate.get(),
                                                                                                                self.var_dateofcrime.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_age.get(),
                                                                                                                self.var_occupation.get(),
                                                                                                                self.var_birthmark.get(),
                                                                                                                self.var_criminaltype.get(),
                                                                                                                self.var_fathername.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_mostwanted.get()
                                                                                                                




                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','criminal record has been added')
            except Exception as es:
                messagebox.showerror("Error",f"due to {str(es)}")
               
    #fetch data
    def fetch_data(self):
         conn=mysql.connector.connect(host='localhost',user='root',password='YES',database='criminal managementl',auth_plugin='mysql_native_password')
         my_cursor=conn.cursor() 
         my_cursor.execute('select * from criminal')
         data=my_cursor.fetchall()
         if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']


        self.var_case_id.set(data[0])
        self.var_criminalid.set(data[1])
        self.var_name.set(data[2])
        self.var_Nickname.set(data[3])
        self.var_arrestdate.set(data[4])
        self.var_dateofcrime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_criminaltype.set(data[10])
        self.var_fathername.set(data[11])
        self.var_gender.set(data[12])
        self.var_mostwanted.set(data[13])
    #update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are requuired')
        else:
            try:  
                update=messagebox.askyesno('Update','Are you sure update this criminal')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='YES',database='criminal managementl',auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal set criminalid=%s,name=%s,Nickname=%s,arrestdate=%s,dateofcrime=%s,address=%s,age=%s,occupation=%s,birthmark=%s,criminaltype=%s,fathername=%s,gender=%s,mostwanted=%s where case_id=%s',(

                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                self.var_criminalid.get(),
                                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                                self.var_Nickname.get(),
                                                                                                                                                                                                                                                self.var_arrestdate.get(),
                                                                                                                                                                                                                                                self.var_dateofcrime.get(),
                                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                                self.var_age.get(),
                                                                                                                                                                                                                                                self.var_occupation.get(),
                                                                                                                                                                                                                                                self.var_birthmark.get(),
                                                                                                                                                                                                                                                self.var_criminaltype.get(),
                                                                                                                                                                                                                                                self.var_fathername.get(),
                                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                                self.var_mostwanted.get(),
                                                                                                                                                                                                                                                self.var_case_id.get(),

                                                                                                                                                                                                                                         ))
                                                                                                                                                                                                                                
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','criminal record has been UPDATED') 
            except Exception as es:
                messagebox.showerror("Error",f"due to {str(es)}")
              
    #delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error","all fields are required")
        else:
            try:
                Delete=messagebox.askyesno("Delete",'are you sure delete this criminal')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='YES',database='criminal managementl',auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where case_id =%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','criminal record has been successfully deleted')
            except Exception as es:
                messagebox.showerror("Error",f"due to {str(es)}")
             

    #clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminalid.set("")
        self.var_name.set("")
        self.var_Nickname.set("")
        self.var_arrestdate.set("")
        self.var_dateofcrime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_criminaltype.set("")
        self.var_fathername.set("")
        self.var_gender.set("")
        self.var_mostwanted.set("")
    #searrch
    def searrch_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='YES',database='criminal managementl',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute( ' select * from criminal where '+str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                     self.criminal_table.delete(*self.criminal_table.get_children())
                     for i in rows:
                        self.criminal_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"due to {str(es)}")        

     

                                                                                                                                                                                                                        
                                                                                                                                                                                                                               

if __name__=='__main__':
    root=Tk()
    obj=criminal(root)
    root.mainloop()