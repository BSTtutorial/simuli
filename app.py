from flask import Flask, render_template, request, jsonify
import requests
import os

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
        
        # Use SageMathCell public API
        response = requests.post(
            'https://sagecell.sagemath.org/service',
            data={'code': code},
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            
            # Get stdout (printed output and results)
            stdout = result.get('stdout', '')
            
            return jsonify({
                'success': True,
                'result': stdout if stdout else 'Code executed successfully',
                'output': stdout
            })
        else:
            return jsonify({
                'success': False,
                'error': 'SageMath service unavailable. Please try again.'
            }), 500
            
    except requests.Timeout:
        return jsonify({
            'success': False,
            'error': 'Request timeout. Calculation took too long.'
        }), 408
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
