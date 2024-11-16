from flask import Flask, jsonify, request, render_template
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

apikey = 'your_api_key_here'
genai.configure(api_key=apikey) #replace with your own api key if wanted

app=Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/ermify", methods = ["GET", "POST"])
def ermify():
    if not request.json:
        print("no request")
        return jsonify({"message":"eheu"})
    elif "data" not in request.json:
        print("no data in json")
        return jsonify({"message":"eheu"})
    else:
        print("data receieved")
        txt = request.json["data"]
        model = genai.GenerativeModel("gemini-1.5-flash")
        safety_settings : list[str] = [{"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}]
        response = model.generate_content(
            [f"Given the following text: {txt}\n\
             Rewrite the given text with pompous, pretentious language, using as many words with two or more syllables as possible. Use exact punctuation as well. \
             Example 1:\
             Given text: 'Where are you'\
             Generated response: 'Could I perchance be enlightened with information regarding your whereabouts?\
             Example 2:\
             Given text: 'The weather is nice today'\
             Generated response: 'The meteorological conditions displayed within the outdoor surroundings on today's date are indubitably quite pleasing.\
             Example 3:\
             Given text: 'Did you finish the math homework?'\
             Generted response: 'Mayhaps I could be informed on the completion status of your assigned work detailing the complex mathematical equations discussed in the most recent lesson?"],
             safety_settings=safety_settings
        )

        return jsonify({"message":"euge", "ermified":response.text})

app.run(host="0.0.0.0", port=8080)