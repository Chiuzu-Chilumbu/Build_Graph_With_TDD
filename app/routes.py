from flask import request, render_template, jsonify
from app.controllers.stack_logic import StackController

stack_controller = None  # Global variable to hold the stack controller instance


def register_routes(app):
    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route('/stack')
    def stack():
        return render_template('stack.html')

    @app.route('/queue')
    def queue():
        return render_template('queue.html')

    @app.route('/graph')
    def graph():
        return render_template('graph.html')

    @app.route('/initialise', methods=['POST'])
    def initialise_stack():
        global stack_controller
        try:
            capacity = request.json.get('capacity', 5)  # Default to 5 if not provided
            stack_controller = StackController(capacity)
            return jsonify({
                'success': True,
                'message': f"Stack initialised with capacity {capacity}"
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 400

    @app.route('/stack/push', methods=['POST'])
    def push():
        if not stack_controller:
            return jsonify({
                'success': False,
                'message': 'Stack not initialised'
            }), 400
        data = request.json.get('data')
        return stack_controller.push(data)

    @app.route('/stack/pop', methods=['POST'])
    def pop():
        if not stack_controller:
            return jsonify({
                'success': False,
                'message': 'Stack not initialised'
            }), 400
        return stack_controller.pop()

    @app.route('/stack/data', methods=['GET'])
    def get_stack_data():
        if not stack_controller:
            return jsonify({
                'success': False,
                'message': 'Stack not initialised'
            }), 400
        return stack_controller.get_stack_data()
