from flask import Flask,jsonify,request

app=Flask(__name__)

#creating a array of different task
data=[
    {
        'contact':'9987644456',
        'name':u'Raju',
        'done':False,
        'id':1
    },
    {
        'contact':'9876543222',
        'name':'Rahul',
        'done':False,
        'id':2
    }
]

@app.route("/get-data")
def gettask():
    return jsonify({
        "data":tasks
    })

@app.route("/add-data",methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    contact={
        'id':data[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False

    }    
    data.append(data)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })


if(__name__ == "__main__"):
    app.run(debug=True)

