from flask import Flask,render_template,request
import helper

app =Flask(__name__)



@app.route('/',methods=['POST','GET'])
def home():
    prediction = None   
    
    if request.method == 'POST': 
        
        text=request.form['review_text']
        
        prediction=helper.predictions(text)
                
    return render_template('index.html',prediction_txt=prediction)


if __name__ == '__main__': 
    app.run(debug=True)
    