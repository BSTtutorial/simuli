from flask import Flask, render_template, request, jsonify
from sage.all import *
import traceback
import sys
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            # Execute the SageMath code
            result = sage_eval(code, locals=globals())
            
            # Get any printed output
            output = sys.stdout.getvalue()
            
            # Format the result
            if result is not None:
                result_str = str(result)
            else:
                result_str = output if output else "Code executed successfully"
            
            return jsonify({
                'success': True,
                'result': result_str,
                'output': output
            })
            
        finally:
            sys.stdout = old_stdout
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
