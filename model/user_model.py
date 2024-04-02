
import mysql.connector
# import json
from flask import make_response
class user_model():
    
    def __init__(self):
    # Connection establishment code
        try:

            self.con=mysql.connector.connect(host="localhost", user="root", password="", database="flask_todos")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successful")
            
        except:
            print("Some error")





    def user_getall_model(self):
        self.cur.execute("SELECT * FROM todos")
        result = self.cur.fetchall()
        if len(result)>0:
           return make_response({"payload": result}, 200)
             
          #  return json.dumps(result)
        else:
           return make_response ({"message": "no data found"}, 204)
        

      
    def user_addone_model(self,data):
        # print(data)
        self.cur.execute("INSERT INTO todos(fullname, email) VALUES(%s,%s)",(data['fullname'],data['email']))

        # print(data['name'])
        
        return make_response({"message": "user created successfully","status": "1"}, 201)
        

    def user_update_model(self,data):
        self.cur.execute(f"UPDATE todos SET fullname='{data['fullname']}', email='{data['email']}' WHERE id={data['id']}")
        # print(data['name'])
        if self.cur.rowcount>0:
             return make_response({"message": "user updated successfully", "status":1}, 201)
        else:
             return make_response({"message": "Nothing to update", "status":0},202) 
        
       
       
    def user_delete_model(self,data):
        print("delete modal",data['id'])
        id = data['id']
        self.cur.execute(f"DELETE FROM 	todos WHERE id={id}")
        if self.cur.rowcount>0:
             return make_response({"message": "user Deleted successfully", "status":1}, 200)
        else:
             return make_response({"message": "Nothing to delete", "status":0}, 202)
        

    def user_patch_model(self, data, id):
        qry = "UPDATE 	todos SET"
        for key in data:
            qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id={id}"
         #UPDATE 	todos SET col=val, col=val WHERE id={id}
        # return qry
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"User Updated Successfully"}, 201)
        else:
            return make_response({"message":"Nothing to update"}, 202)

    def user_pagination_model(self, limit, page):
        limit=int(limit)
        page=int(page)
        start=(page*limit) - limit
        qry = f"SELECT * FROM 	todos LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        if len(result)>0:
           res = make_response({"payload": result, "page_no":page, "limit":limit}, 200)
           return res
             
          #  return json.dumps(result)
        else:
           return make_response ({"message": "no data found"}, 204)
        