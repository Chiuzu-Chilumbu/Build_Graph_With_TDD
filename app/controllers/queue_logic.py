from flask import jsonify
from app.models.queue_adt import Queue


class QueueController:
    def __init__(self, capacity=5):
        self.queue = Queue(capacity)

    
    def enqueue(self, data):
        """Handle enqueue operation and returns JSON response"""
        try:
            self.queue.enqueue(data)
            return jsonify({
                'sucess': True,
                'message': f"Sucessfully enqueued {data}",
                'result': list(self.queue.get_queue())
            }), 200
        
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 400 
        
    
    def dequeue(self):
        """Handles dequeue operation and returns json response"""
        try:
            dequeued_item = self.queue.dequeue()
            return jsonify({
                'success': True,
                'message': f"Successfully dequeue {dequeued_item}",
                'result': list(self.queue.get_queue())
            }), 200
        
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 400 
        
    
    def get_queue_data(self):
        """return current queue state"""
        return jsonify({
            'success': True,
            'result': list(self.queue.get_queue()) # Convert to list for flask jsonify
        }), 200
    
    