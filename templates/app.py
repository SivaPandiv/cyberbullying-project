from flask import Flask, render_template, request

app = Flask(__name__)

def detect(text):
    bad_words = ["hate", "idiot", "stupid", "ugly"]
    
    for word in bad_words:
        if word in text.lower():
            return "🚫 Bullying Detected"
    
    return "✅ Normal Content"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    
    if request.method == "POST":
        user_text = request.form["text"]
        result = detect(user_text)
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)