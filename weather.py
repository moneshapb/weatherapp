from flask import Flask, request, render_template
import requests

app = Flask(__name__)
  
@app.route('/', methods =["GET", "POST"])
def index(): 
    Data = ''
    error = 0
    city = ''
    if request.method == "POST":       
        city = request.form.get("city")  
        if city:
            Api_Key = '9d6004d73c651f1cc942a2e38a45d349'
            url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=" + Api_Key + "&units=metric"
            Data = requests.get(url).json()
        else:
            error = 1    
    return render_template('weather.html', data = Data, city = city, error = error)
if __name__ == "__main__":
    app.run()
