from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

@app.route("/")
def home():
    return "AI Text Generator Backend Running"

@app.route("/generate", methods=["POST"])
def generate():
    print("Generate endpoint reached")
    data = request.json

    prompt = (
    "Answer the following question clearly and simply:\n"
    + data["prompt"]
)

    output = generator(
    prompt,
    max_new_tokens=100,
    temperature=0.6,
    do_sample=True,
    top_k=50,
    top_p=0.95
    )

    return jsonify({
        "generated_text":
        output[0]["generated_text"]
    })

if __name__ == "__main__":
    app.run(debug=True)