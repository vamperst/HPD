from chalice import Chalice

app = Chalice(app_name="helloworld")

@app.route("/")
def hello_world():
    return {"hello": "world"}
