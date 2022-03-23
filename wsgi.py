from flask import Flask
application = Flask(__name__)

#tasks = [
#    {
#        'id': 1,
#        'title': u'Buy groceries',
#        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#        'done': False
#    },
#    {
#        'id': 2,
#        'title': u'Learn Python',
#        'description': u'Need to find a good Python tutorial on the web',
#        'done': True
#    },
#    {
#        'id': 3,
#        'title': u'Explore IntelliJ',
#        'description': u'This Docker Integration plugin is awesome',
#        'done': False
#    }
#]

#@app.route('/api/tasks', methods=['GET'])
#def get_tasks():
#    return jsonify({'tasks': tasks})

@application.route("/")
def hello():
    return "Hello World!_test"

if __name__ == "__main__":
    application.run()
