from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Find this line:
from flask import Flask, render_template, request, redirect, url_for

# Change it to this:
from flask import Flask, render_template, request, redirect, url_for, jsonify


import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# --- Database Configuration ---
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)
# --- Config End ---


# --- Database Model ---
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(280), nullable=False)

    def __repr__(self):
        return f'<Message {self.id}: {self.content[:20]}...>'
# --- Model End ---


# --- Routes ---
@app.route("/")
def hello():
    user_name = "Way"
    my_skills = ["Python", "Flask", "Linux", "C++"]
    return render_template(
        "index.html", 
        name=user_name, 
        skills=my_skills
    )

@app.route("/about")
def about():
    return render_template("about.html")

# --- MODIFIED ROUTE ---
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    # This block runs ONLY when the user submits the form (POST request)
    if request.method == 'POST':
        # 1. Get message content from the form
        message_content = request.form['user_message']
        
        # 2. Create a new Message object
        new_msg = Message(content=message_content)
        
        # 3. Add the new message to the database session
        db.session.add(new_msg)
        
        # 4. Commit the session to save the change to database.db
        db.session.commit()
        
        # 5. Redirect the user to the new 'messages' page
        return redirect(url_for('messages'))
    
    # This block runs when the user just visits the page (GET request)
    return render_template("contact.html")

# --- DELETED ROUTE ---
# We no longer need the '/success' route.
# It has been replaced by '/messages'.

# --- NEW ROUTE ---
@app.route("/messages")
def messages():
    # 1. Query the database to get ALL messages
    #    We order them by id in descending order (newest first)
    all_messages = Message.query.order_by(Message.id.desc()).all()
    
    # 2. Render the new 'messages.html' template
    #    Pass the list of messages to the template
    return render_template("messages.html", messages=all_messages)



# --- NEW API ROUTE ---
# This route will return all messages as JSON data
@app.route("/api/messages")
def api_messages():
    # 1. Query the database to get all messages
    #    This is the same as in your '/messages' route
    all_messages = Message.query.order_by(Message.id.desc()).all()

    # 2. We must convert the list of 'Message' objects into a list of dictionaries
    #    JSON doesn't understand Python objects
    messages_list = []
    for msg in all_messages:
        messages_list.append({
            "id": msg.id,
            "content": msg.content
        })

    # 3. Use 'jsonify' to return the list as a JSON response
    return jsonify(messages=messages_list)
# --- API Route End ---


# --- NEW API ROUTE (POST) ---
# This route will create a new message
# It only accepts POST requests
@app.route("/api/messages/create", methods=['POST'])
def api_create_message():
    # 1. Get the JSON data from the request body
    #    We use request.json instead of request.form
    data = request.json

    # 2. Check if the 'content' key exists in the JSON
    if 'content' not in data:
        # If not, return an error message
        return jsonify({"error": "Missing 'content' key"}), 400 # 400 means Bad Request

    # 3. Get the content from the data
    message_content = data['content']

    # 4. Create, add, and commit the new message to the database
    #    (This is the same logic as your contact() function)
    new_msg = Message(content=message_content)
    db.session.add(new_msg)
    db.session.commit()

    # 5. Return a success response in JSON format
    return jsonify({
        "success": True, 
        "message": "Message created successfully",
        "new_message": {
            "id": new_msg.id,
            "content": new_msg.content
        }
    }), 201 # 201 means "Created"
# --- API Route End ---

# --- NEW API ROUTE (DELETE) ---
# This route will delete a single message by its ID
# It uses a dynamic route <int:message_id>
# It only accepts DELETE requests
@app.route("/api/messages/delete/<int:message_id>", methods=['DELETE'])
def api_delete_message(message_id):
    # 1. Find the message by its ID.
    #    .get_or_404() is a helper that automatically returns
    #    a 404 Not Found error if the ID doesn't exist.
    message_to_delete = Message.query.get_or_404(message_id)

    # 2. Delete the message from the database session
    db.session.delete(message_to_delete)

    # 3. Commit the change to the database file
    db.session.commit()

    # 4. Return a success response
    return jsonify({
        "success": True,
        "message": f"Message with ID {message_id} has been deleted."
    })
# --- API Route End ---


# --- NEW API ROUTE (PUT) ---
# This route will update an existing message by its ID
# It only accepts PUT requests
@app.route("/api/messages/update/<int:message_id>", methods=['PUT'])
def api_update_message(message_id):
    # 1. Find the existing message or return 404 if not found
    message_to_update = Message.query.get_or_404(message_id)

    # 2. Get the new data from the request.json body
    data = request.json

    # 3. Validate if the 'content' key is in the received data
    if 'content' not in data:
        return jsonify({"error": "Missing 'content' key"}), 400 # 400 means Bad Request

    # 4. Apply the update to the message object in the session
    message_to_update.content = data['content']

    # 5. Commit the session to save the change to the database
    db.session.commit()

    # 6. Return a success response with the updated object's data
    return jsonify({
        "success": True,
        "message": f"Message {message_id} has been updated.",
        "updated_message": {
            "id": message_to_update.id,
            "content": message_to_update.content
        }
    })
# --- API Route End ---


if __name__ == "__main__":
    app.run(debug=True)


