from app import app
from model.user_model import user_model
from flask import request
obj = user_model()


@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()
    

@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    data = request.json
    return obj.user_addone_model(data)
    
@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    data = request.json
    print(data)
    return obj.user_update_model(data)
    

@app.route("/user/delete", methods=["DELETE"])
def user_delete_controller():
    data = request.json
    return obj.user_delete_model(data)
    


@app.route("/user/patch/<id>", methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)


