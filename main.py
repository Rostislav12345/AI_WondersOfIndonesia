import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/chatbot', methods=['POST'])
def chatbot():
    #render_template("index.html")
    data = request.get_json()
    user_message = data.get("message")
    genai.configure(api_key="APIKEY")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Pertanyaan Berikut tentang wonders of indonesia, hanya jawab tentang kebudayaan indonesia jangan jawaban lain:" + user_message)
    print(response.text)
    return jsonify({"reply":response.text})

if __name__ == '__main__':
    app.run(debug=True)            
