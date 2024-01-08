from flask import Flask, request, jsonify

app = Flask(__name__)

questions = [
    "What's something that made you smile today?",
    "If you could travel anywhere right now, where would you go?",
    "What's a hobby you'd love to pick up?",
    "Share a favorite memory from the past year.",
    "If you had a superpower, what would it be and why?"
]

current_question_index = 0

@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    global current_question_index
    if request.method == 'POST':
        user_response = request.json.get('response')
        print(user_response)
        current_question_index = int(user_response)
        if current_question_index < len(questions):
            next_question = questions[current_question_index]
            return jsonify({'question': next_question})
        else:
            return jsonify({'message': 'Bye! You answered all the questions.'})
    return jsonify({'question': questions[current_question_index]})

if __name__ == '__main__':
    app.run(debug=True)
