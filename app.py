from flask import Flask, render_template

app = Flask(__name__)

Pricing_Plans = [
    {
        'id': 1,
        'planName' : 'Free',
        'pricePerMonth': 0,
        # 'benefits' : 'Free Trial Tier, Pay Nothing, Limited to 3 X rays a month'
    },
    
    {
        'id' : 2,
        'planName' : 'Basic',
        'pricePerMonth': 500,
        'benefits' : 'Additional utility and annotation, Up to 15 X rays a month'
    },
    
    {
        'id' : 3,
        'planName' : 'Premium Corporate',
        'pricePerMonth': 2500,
        'benefits' : 'Unlimited uploads and classifications, 24 hour technical support available'
    } 
]

@app.route("/")
def hello_world():
    return render_template('home.html', plans = Pricing_Plans, company_name = "CovidDoc")

# No need for app.run() when using 'flask run'

#run using  flask run --debug