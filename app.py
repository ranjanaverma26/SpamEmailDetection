from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    user_message = ""
    if request.method == 'POST':
        user_message = request.form.get('message', '')
        if user_message:
            try:
                pred = model.predict([user_message])[0]
                if str(pred) == '1' or str(pred).lower() == 'spam':
                    result = "SPAM 🔴"
                else:
                    result = "NOT SPAM 🟢"
            except Exception as e:
                result = f"Error: {e}"
                print(e)

    return render_template('index.html', result=result, message=user_message)

if __name__ == '__main__':
    app.run(debug=True)