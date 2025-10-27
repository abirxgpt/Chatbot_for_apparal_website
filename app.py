from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="API_REMOVED_")
model = genai.GenerativeModel("models/gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("template.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "")
        if not user_message:
            return jsonify({"response": "Please enter a message."})

        response = model.generate_content(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
