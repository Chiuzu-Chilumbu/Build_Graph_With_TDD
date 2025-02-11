from flask import request, render_template, jsonify
from app.controllers.stack_logic import StackController
from app.controllers.queue_logic import QueueController


stack_controller = None 
queue_controller = None

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
    

    '''
    Stack Operations
    '''
    # initialise stack
    @app.route('/stack/initialise', methods=['POST'])
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
        
    # Push Operation
    @app.route('/stack/push', methods=['POST'])
    def push():
        global stack_controller
        if not stack_controller:
            return jsonify({
                'success': False,
                'message': 'Stack not initialised'
            }), 400
        data = request.json.get('data')
        return stack_controller.push(data)
    
    # Pop Operation
    @app.route('/stack/pop', methods=['POST'])
    def pop():
        global stack_controller
        if not stack_controller:
            return jsonify({
                'success': False,
                'message': 'Stack not initialised'
            }), 400
        return stack_controller.pop()
    
    # Get Stack data
    @app.route('/stack/data', methods=['GET'])
    def get_stack_data():
        global stack_controller
        if not stack_controller:
            return jsonify({
                'success': False,
                'message': 'Stack not initialised'
            }), 400
        return stack_controller.get_stack_data()
    

    '''
    Queue Operations
    '''
    # Initialise queue
    @app.route('/queue/initialise', methods=['POST'])
    def initialsise_queue():
        global queue_controller
        try:
            capacity = request.json.get('capacity', 5)
            queue_controller = QueueController(capacity)

            return jsonify({
                'success': True,
                'message': f'Queue initialised with capacity {capacity}'
            }), 200
        
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 400 
        
    # Enqueue Operaton
    @app.route('/queue/enqueue', methods=['POST'])
    def enqueue():
        global queue_controller
        if not queue_controller:
            return jsonify({
                'success': False,
                'message': 'Queue not initialised'
            }), 400
        
        data = request.json.get('data')
        return queue_controller.enqueue(data)
    
    # Deqeue operation 
    @app.route('/queue/dequeue', methods=['POST'])
    def dequeue():
        global queue_controller
        if not queue_controller:
            return jsonify({
                'sucess': False,
                'message': 'Queue not initialised'
            })
        
        return queue_controller.dequeue()
    

    # GET queue data
    @app.route('/queue/data', methods=['GET'])
    def get_queue_data():
        global queue_controller
        if not queue_controller:
            return jsonify({
                'success': False,
                'message': "Queue not initialised"
            }), 400
        
        return queue_controller.get_queue_data()

        
    
    