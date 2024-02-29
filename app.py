from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'JJ API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def process_message():
    try:
        # Get the message from the POST request
        message = request.get_data(as_text=True)
        from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)


        # Use OpenAI API to send a request and get a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=150
        )

        # Extract the generated response from OpenAI
        generated_response = response.choices[0].text.strip()

        # Return the response as JSON
        return jsonify({'message': generated_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
