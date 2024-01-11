from flask import Flask, request, jsonify
import question_book as qb
app = Flask(__name__)



current_question_index = 0

@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    global current_question_index
    if request.method == 'POST':
        user_response = request.json.get('response')
        print(user_response)
        current_question_index = int(user_response)
        if current_question_index < len(qb.questions):
            next_question = qb.questions[current_question_index][0]
            subject=qb.questions[current_question_index][1]
            return jsonify({'question': next_question,
                            'subject':subject})
        else:
            return jsonify({'question': 'Bye! You answered all the questions.',
                            'subject':"pass"})
    return jsonify({'question': qb.questions[current_question_index],
                    'subject':"pass"})

if __name__ == '__main__':
    app.run(debug=True)
