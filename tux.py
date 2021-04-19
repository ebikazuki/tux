import json
import requests
from flask import Flask, render_template, request
from desk_get import desk_result
import datetime as dt

app = Flask(__name__)

 # MESH人感センサからのデータ受取り
@app.route("/desk", methods=['POST'])
def desk():
    post = request.data.decode()
    if post=="reset":
        data = desk_result()*2
        archive = {"time_min":data}
        today = dt.date.today()
        yesterday = today-dt.timedelta(days=1)
        file = open("desk_archive/"+yesterday.strftime("%Y%m%d")+".json" , "w")
        json.dump(archive , file)

        file = open("desk.json", "w")
        json.dump({"desk":0} , file)

    else:
        data = desk_result()
        update = {"desk":data+1}
        file = open("desk.json", "w")
        json.dump(update , file)
    return str(data)

# データの確認
@app.route("/desk", methods=['GET'])
def desk_get():
    data = desk_result()
    data = str(data//2)
    return render_template("tux.html",data=data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
