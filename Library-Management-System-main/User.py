import mysql.connector
import Tables
        
#--------------------------------------------------------------------------------------------------------------------------------        
def display_user():
    print()
    print("User Records: \n")
    mycursor.execute("""SELECT UserRecord.UserID,UserRecord.UserName,UserRecord.Password,BookRecord.BookName,BookRecord.BookID
                        FROM UserRecord
                        LEFT JOIN BookRecord ON UserRecord.BookID=BookRecord.BookID""")
    records=mycursor.fetchall()
    row_no=0
    for rows in records :
        row_no+=1
        print("******************************","Row no.",row_no,"******************************") #Perkelti i konstantas, del tvarkos ir skirtingu dydziu isvengimo
        print("\t             UserID: ", rows[0])
        print("\t           UserName: ", rows[1])
        print("\t           Password: ", rows[2])
        print("\t        Book Issued: ", rows[3])
        print("\t         Its BookID: ", rows[4])
        print()
        print("Press any key to return to the User Menu")
    
#--------------------------------------------------------------------------------------------------------------------------------             
def insert_user():
    while True :
        data=()
        print()
        user_id=input(" Enter UserID: ")
        username=input(" Enter User Name: ")
        password=input(" Enter Password to be Set: ")
        data=(UserID, UserName, Password,None)
        query="INSERT INTO UserRecord VALUES (%s, %s, %s,%s)"
        mycursor.execute(query,data)
        mydb.commit()
        print()
        ch=input("Do you wish to do add more Users?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
#--------------------------------------------------------------------------------------------------------------------------------             
def delete_user():
    while True:
        print()
        user_id=input(" Enter UserID whose details to be deleted : ")  
        mycursor.execute("DELETE from UserRecord where UserID = {0} ".format("\'"+UserID+"\'"))
        mydb.commit()
        ch=input("Do you wish to delete more Users?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    
#--------------------------------------------------------------------------------------------------------------------------------         
def search_user():
    while True:
        print()
        search=input(" Enter UserID to be Searched: ")  
        mycursor.execute("SELECT UserID, UserName, Password , BookName, UserRecord.BookID\
                    FROM Library.UserRecord LEFT JOIN Library.BookRecord\
                    ON BookRecord.BookID=UserRecord.BookID\
                    WHERE UserRecord.UserID={0}".format("\'"+Search+"\'"))
        records=mycursor.fetchall()
        row_no=0 
        if records:
            for rows in records :
                row_no+=1
                print("******************************","Searched User Record","******************************")
                print("\t             UserID: ", rows[0])
                print("\t           UserName: ", rows[1])
                print("\t           Password: ", rows[2])
                print("\t        Book Issued: ", rows[3])
                print("\t         Its BookID: ", rows[4])
                print()
        else:
            print("Search Unsuccesfull")
            
        ch=input("Do you wish to Search more Users?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    
#--------------------------------------------------------------------------------------------------------------------------------     
def update_user():
    while True:
        print()
        data=()
        user_id=input(" Enter User ID for whose details need to be updated : ")
        username=input(" Enter Updated User Name : ")
        password=input(" Enter Updated Password : ")
        query="UPDATE UserRecord SET Username = %s, Password = %s WHERE UserID=%s"
        data=(UserName,Password,UserID)
        mycursor.execute(query,data)
        mydb.commit()
        print("Updated succesfully")
        ch=input("Do you wish to Update more Users?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return   
#--------------------------------------------------------------------------------------------------------------------------------     
mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="Library")
mycursor=mydb.cursor()

        
