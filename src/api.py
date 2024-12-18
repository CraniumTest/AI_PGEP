from flask import Flask, jsonify, request
from recommendation_system import recommend_activities
from nlp_service import setup_virtual_assistant, interact_with_guest

app = Flask(__name__)

# Initialize NLP assistant
assistant = setup_virtual_assistant()

@app.route('/api/recommend', methods=['GET'])
def recommend():
    guest_id = request.args.get('guest_id')
    recommendations = recommend_activities(guest_id, guest_data, activity_matrix)
    return jsonify({'recommendations': recommendations.tolist()})

@app.route('/api/concierge', methods=['POST'])
def concierge():
    user_input = request.json.get('message')
    response = interact_with_guest(assistant, user_input)
    return jsonify({'response': response[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
