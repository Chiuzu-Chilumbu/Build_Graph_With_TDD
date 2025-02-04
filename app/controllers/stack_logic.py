from flask import jsonify
from app.models.stack_adt import Stack

class StackController:
    def __init__(self, capacity=10):
        self.stack = Stack(capacity)

    def push(self, data):
        try:
            self.stack.push(data)
            return jsonify({
                'success': True,
                'message': f"Successfully pushed {data}",
                'result': self.stack.get_stack()
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 400

    def pop(self):
        try:
            popped_item = self.stack.pop()
            return jsonify({
                'success': True,
                'message': f'Successfully popped {popped_item}',
                'result': self.stack.get_stack()
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 400

    def get_stack_data(self):
        return jsonify({
            'success': True,
            'result': self.stack.get_stack()
        }), 200
