from flask import Flask

from flask import current_app, flash, jsonify, make_response, redirect, request, url_for, render_template
import openai
# Flask Constructor
app = Flask(__name__)

openai.api_key = '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'

# decorator to associate 
# a function with the url
@app.route("/")
def showHomePage():
      # response from the server
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message']
    
    response_text = chat_with_gpt(message)
    
    return jsonify({'response': response_text})

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )
    return response['choices'][0]['text'].strip()



 
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)