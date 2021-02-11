def addstudent():
    def submitadd():
        # pass
        id  =  idval.get()
        name =  nameval.get()
        mobile =  mobileval.get() 
        email  = emailval.get()
        address = addressval.get()
        gender =  genderval.get()    
        dob  =  dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")
        # print(addeddate,addedtime)
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addedtime,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notification','Id {} Name {} Added succesfully.. and want to clean the form'.format(id,name),parent=addroot)
            if(res==True): # Here we clear the form after pressing yes option
                idval.set('')  # from idval we can take the value and as well as set the value 
                nameval.set('')
                mobileval.set('') # each val is set to null for clear form
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')          
        except:
            messagebox.showerror('Notification','Id Already Exist try another id',parent=addroot)
        strr = 'select * from studentdata'    
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        # print(datas)              
        studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
        for i in datas:    # Loop will show the data in form of list
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            # print(vv)
            studenttable.insert('',END,values=vv)   # It shows (insert the data from start to end) the data in the frame 
        # print(id,name,email)
    # print('student added')
    addroot = Toplevel(master=DataEntryFrame) # its done because while cliking te button (such as add student) it should show the window in DataEntryFrame
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('Student_management.ico ')
    addroot.resizable(False,False)
#------------------------------------------------------------------ Add student label--------------------------------------------
    idlabel = Label(addroot,text="Enter ID : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text="Enter Name : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text="Enter Mobile : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text="Enter Email : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text="Enter Address : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text="Enter Gender : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text="Enter D.O.B : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    doblabel.place(x=10,y=370)

#------------------------------------------------------------------------Add student entry -------------------------------------------------------------------

    idval = StringVar()  # from idval we can take the value and as well as set the value 
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('roman',15,'bold'),textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('roman',15,'bold'),textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('roman',15,'bold'),textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('roman',15,'bold'),textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font=('roman',15,'bold'),textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(addroot,font=('roman',15,'bold'),textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(addroot,font=('roman',15,'bold'),textvariable=dobval)
    dobentry.place(x=250,y=370)

#---------------------------------------------------------------- Add button ------------------------------

    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=120,y=420)

    addroot.mainloop()

def searchstudent():
    def search():
        id  =  idval.get()
        name =  nameval.get()
        mobile =  mobileval.get() 
        email  = emailval.get()
        address = addressval.get()
        gender =  genderval.get()    
        dob  =  dobval.get()
        # addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")
        
        if(id != ''):
            strr = 'select * from studentdata where id =%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
            for i in datas:    # Loop will show the data in form of list
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)   # It shows (insert the data from start to end) the data in the frame 

        elif(name != ''):
            strr = 'select * from studentdata where name =%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
            for i in datas:    # Loop will show the data in form of list
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)   # It shows (insert the data from start to end) the data in the frame 

        elif(mobile != ''):
            strr = 'select * from studentdata where mobile =%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
            for i in datas:    # Loop will show the data in form of list
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)   # It shows (insert the data from start to end) the data in the frame 

        elif(email != ''):
            strr = 'select * from studentdata where email =%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
            for i in datas:    # Loop will show the data in form of list
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)   # It shows (insert the data from start to end) the data in the frame 
        
        elif(address != ''):
            strr = 'select * from studentdata where address =%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
            for i in datas:    # Loop will show the data in form of list
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)   # It shows (insert the data from start to end) the data in the frame 


        elif(gender != ''):
            strr = 'select * from studentdata where gender =%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
            for i in datas:    # Loop will show the data in form of list
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)   # It shows (insert the data from start to end) the data in the frame 

        elif(dob != ''):
            strr = 'select * from studentdata where dob =%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
            for i in datas:    # Loop will show the data in form of list
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)   # It shows (insert the data from start to end) the data in the frame 


        elif(addeddate != ''):
            strr = 'select * from studentdata where addeddate =%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
            for i in datas:    # Loop will show the data in form of list
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)   # It shows (insert the data from start to end) the data in the frame 


        # print('search')
    # print('student search')
    searchroot = Toplevel(master=DataEntryFrame) # its done because while cliking the button (such as add student) it should show the window in DataEntryFrame
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='blue')
    searchroot.iconbitmap('Student_management.ico ')
    searchroot.resizable(False,False)
#------------------------------------------------------------------ Add student label--------------------------------------------
    idlabel = Label(searchroot,text="Enter ID : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text="Enter Name : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text="Enter Mobile : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text="Enter Email : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    emaillabel.place(x=10,y=190)

    addresslabel = Label(searchroot,text="Enter Address : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text="Enter Gender : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    genderlabel.place(x=10,y=310)

    doblabel = Label(searchroot,text="Enter D.O.B : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    doblabel.place(x=10,y=370)

    datelabel = Label(searchroot,text="Enter date : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    datelabel.place(x=10,y=430)

#------------------------------------------------------------------------Add student entry -------------------------------------------------------------------

    idval = StringVar()  # from idval we can take the value and as well as set the value 
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot,font=('roman',15,'bold'),textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('roman',15,'bold'),textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('roman',15,'bold'),textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('roman',15,'bold'),textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(searchroot,font=('roman',15,'bold'),textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(searchroot,font=('roman',15,'bold'),textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(searchroot,font=('roman',15,'bold'),textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(searchroot,font=('roman',15,'bold'),textvariable=dateval)
    dateentry.place(x=250,y=430)

#---------------------------------------------------------------- Add button ------------------------------

    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=search)
    submitbtn.place(x=120,y=480)

    searchroot.mainloop()   


def deletestudent():
    cc = studenttable.focus() # it specifically focus which row we have to delete
    content = studenttable.item(cc) 
    # print(content)  
    pp = content['values'][0]  # wrt id we delete the data (id is present in 0th index)
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit() # its the imp step to delete the data
    messagebox.showinfo('Notifications','ID {} deleted sucessfully...'.format(pp))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children()) # when we add new data it will crear all the data present before and it will again regeneratethe data with new + prev data
    for i in datas:    # Loop will show the data in form of list
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)   # It shows (delete the data from start to end) the data in the frame

    # print('student delete')



def updatestudent():
    def update():
        # print('update')
        id = idval.get()     # here get is used because taking the data and update the data in the db 
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    # print('student update')
    updateroot = Toplevel(master=DataEntryFrame) # its done because while cliking te button (such as add student) it should show the window in DataEntryFrame
    updateroot.grab_set()
    updateroot.geometry('470x585+220+150')
    updateroot.title('Student Management System')
    updateroot.config(bg='firebrick')
    updateroot.iconbitmap('Student_management.ico ')
    updateroot.resizable(False,False)
#------------------------------------------------------------------ Add student label--------------------------------------------
    idlabel = Label(updateroot,text="Enter ID : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text="Enter Name : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text="Enter Mobile : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text="Enter Email : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    emaillabel.place(x=10,y=190)

    addresslabel = Label(updateroot,text="Enter Address : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text="Enter Gender : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    genderlabel.place(x=10,y=310)

    doblabel = Label(updateroot,text="Enter D.O.B : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text="Enter date : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    datelabel.place(x=10,y=430)

    timelabel = Label(updateroot,text="Enter Time : " ,bg='gold',font=('times',14,'bold'),relief=GROOVE,width = 12,borderwidth=3,anchor='w') #ancror ---> text in west direction      
    timelabel.place(x=10,y=490)

#------------------------------------------------------------------------Add student entry -------------------------------------------------------------------

    idval = StringVar()  # from idval we can take the value and as well as set the value 
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('roman',15,'bold'),textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('roman',15,'bold'),textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('roman',15,'bold'),textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('roman',15,'bold'),textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(updateroot,font=('roman',15,'bold'),textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(updateroot,font=('roman',15,'bold'),textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(updateroot,font=('roman',15,'bold'),textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(updateroot,font=('roman',15,'bold'),textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry = Entry(updateroot,font=('roman',15,'bold'),textvariable=timeval)
    timeentry.place(x=250,y=490)

#---------------------------------------------------------------- Add button ------------------------------

    submitbtn = Button(updateroot,text='Update',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=update)
    submitbtn.place(x=120,y=530)
    
    cc = studenttable.focus()      # when we select the data there all details should show in update section (student entry frame)
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):     # if the content is not equal to 0 (i.e it should consist of atleast one data )
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])       # here each data(i.e after click) is stored in each box
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()   


def showstudent():
    # print('student show')
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def exportstudent():
    ff = filedialog.asksaveasfilename() 
    gg = studenttable.get_children()   # By these method we have all te data 
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]  # seperat list 
    for i in gg:
        content = studenttable.item(i)  #  here it takes one by one item  
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
   
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']    # export part where the excel headline
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd) # all the append data is stored one by one
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))
    # print('student export')
    

def exittudent():
    # print('student exit')
    res = messagebox.askyesnocancel('Notification','Do you want to exit')
    # print(res)
    if(res == True):
        root.destroy()   # after clicking the button yes it will exit


######################################## Connection of db #####################################
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password =  passwordval.get()
        # host = 'localhost'
        # user = 'root'
        # password = ''
        # print(host,user,password)
        try:
            con = pymysql.connect(host=host,user=user,password=password) 
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        
        try:
            strr='create database studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50), dob varchar(50), date varchar(50), time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notificaton','Database created and now you are connected to the database.....', parent=dbroot)

        except:
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notificaton','Now you are connected to the database....!', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('Student_management.ico ')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
#--------------------------------Connectdb Labels--------------------------------------------------------------
    idLabel = Label(dbroot,text="Enter host : " ,bg='gold',font=('timer',14,'bold'),relief=GROOVE,width = 13,borderwidth=3,anchor='w') #ancror ---> text in west direction   
    idLabel.place(x=10,y=10)
    
    userLabel = Label(dbroot,text="Enter user : " ,bg='gold',font=('timer',14,'bold'),relief=GROOVE,width = 13,borderwidth=3,anchor='w') #ancror ---> text in west direction   
    userLabel.place(x=10,y=70)
    
    passwordLabel = Label(dbroot,text="Enter password : " ,bg='gold',font=('timer',14,'bold'),relief=GROOVE,width = 13,borderwidth=3,anchor='w') #ancror ---> text in west direction   
    passwordLabel.place(x=10,y=130)    

#--------------------------------Connectdb Entry--------------------------------------------------------------
    hostval = StringVar()
    # hostval.set('hello')
    userval = StringVar() 
    passwordval =StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)
    
    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

#------------------------------------------Button----------------------------------------------------------

    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),width=20,activebackground='blue',activeforeground='white',bd=5,bg='red',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()


#########################################################################
def Tick():     #clock function
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y") 
    clock.config(text='date :' +date_string+"\n"+"Time : "+time_string)
    clock.after(200,Tick)  # changes time ever 200 mili sec 

    # print(time_string,date_string)

######################################## Intro Slider #####################################
import random
colors = ['red','green','blue','pink','red2','gold2']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(100,IntroLabelColorTick)
def IntroLabelTick():  # slider function
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200,IntroLabelTick)   # changes slider operation ever 200 mili sec 
############################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog # Here  Top level is small window 
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql 
import pandas
import time
root = Tk()
root.title('Student Management system') 
root.config(bg='gold')    # background colour
root.geometry('1174x700+200+50')   # x axis space= 200 , y axis space = 50 it's done because the screen should be in same place 
root.iconbitmap('Student_management.ico ') #logo
root.resizable(False,False)  # No change in size of width and height 

################################################ Frames ###############################################

DataEntryFrame = Frame(root,bg='gold',relief=GROOVE,borderwidth=5)          #relief=SOLID
DataEntryFrame.place(x=10,y=80,width=500,height=600)

#--------------------------------------------- dataentry frame Intro----------------------------------------

frontlabel=Label(DataEntryFrame,text='------------------Welcome-------------------',width=30,font=('arial',20,'italic bold'),bg='gold')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'italic bold'),bd=6,bg='skyblue3',activebackground='blue',activeforeground='white',relief=RIDGE,command=addstudent) 
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('chiller',20,'italic bold'),bd=6,bg='skyblue3',activebackground='blue',activeforeground='white',relief=RIDGE,command=searchstudent) 
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('chiller',20,'italic bold'),bd=6,bg='skyblue3',activebackground='blue',activeforeground='white',relief=RIDGE,command=deletestudent) 
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('chiller',20,'italic bold'),bd=6,bg='skyblue3',activebackground='blue',activeforeground='white',relief=RIDGE,command=updatestudent) 
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('chiller',20,'italic bold'),bd=6,bg='skyblue3',activebackground='blue',activeforeground='white',relief=RIDGE,command=showstudent) 
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export Data',width=25,font=('chiller',20,'italic bold'),bd=6,bg='skyblue3',activebackground='blue',activeforeground='white',relief=RIDGE,command=exportstudent) 
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('chiller',20,'italic bold'),bd=6,bg='skyblue3',activebackground='blue',activeforeground='white',relief=RIDGE,command=exittudent) 
exitbtn.pack(side=TOP,expand=True)
 

# ShowEntryFrame = Frame(root,bg='gold',relief=GROOVE,borderwidth=5)          
# ShowEntryFrame.place(x=550,y=80,width=620,height=600)

#--------------------------------------------------Show data frame
ShowDataFrame = Frame(root,bg='gold',relief=GROOVE,borderwidth=5)          
ShowDataFrame.place(x=550,y=80,width=620,height=600)

#------------------------------------------------------------ Showdataframe ---------------------------------
style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='cyan')

Scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
Scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)

studenttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=Scroll_y.set,xscrollcommand=Scroll_x.set )

Scroll_x.pack(side=BOTTOM,fill=X)
Scroll_y.pack(side=RIGHT,fill=Y)
Scroll_x.config(command=studenttable.xview)
Scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile',text='Mobile')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'   # By indexing it shows the headings perfect (no extra col is displayed )
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)

studenttable.pack(fill=BOTH,expand=1)  # by expand 1 the right portion of frame become white 


################################################ Slider ###############################################
ss='Welcome to Student management system'
count = 0
text = ''
###############################################
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')          
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
################################################ clock ###############################################
clock = Label(root,font=('timer',14,'bold'),relief=RIDGE,borderwidth=5,bg='lawn green',bd =10)
clock.place(x=0,y=0)
Tick()

############################################### Connect Db button ######################################
connectbutton = Button(root,text='Connect To Database',font=('chiller',19,'italic bold'),width=23,bd=8,bg='green2',activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=920,y=0)
root.mainloop()    # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.

