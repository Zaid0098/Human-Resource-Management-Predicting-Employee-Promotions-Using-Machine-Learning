from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Process the form data
        department = request.form.get('department')
        education = request.form.get('education')
        age = request.form.get('age')
        kpis_met = request.form.get('kpis_met')
        awards = request.form.get('awards')
        average_training_score = float(request.form.get('average_training_score', 0))
        
        # Determine the eligibility status
        if kpis_met == 'yes' and average_training_score >= 80:
            eligibility_status = "Eligibility status: Yes The Employee is Applicable"
        else:
            eligibility_status = "Eligibility status: No The Employee is not Applicable"
        
        # Redirect to the submission confirmation page with the eligibility status
        return redirect(url_for('submit', eligibility_status=eligibility_status))
    
    return render_template('predict.html')

@app.route('/submit')
def submit():
    eligibility_status = request.args.get('eligibility_status', 'No status available')
    return render_template('submit.html', eligibility_status=eligibility_status)

if __name__ == '__main__':
    app.run(debug=True)
