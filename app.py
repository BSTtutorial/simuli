from flask import Flask, render_template, request, jsonify
import requests
import os
import json

app = Flask(__name__)

# Get CoCalc API key from environment variable
COCALC_API_KEY = os.environ.get('COCALC_API_KEY', '')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Check if API key is configured
        if not COCALC_API_KEY:
            return jsonify({
                'success': False,
                'error': 'CoCalc API key not configured. Please set COCALC_API_KEY environment variable in Render dashboard.'
            }), 500
        
        data = request.get_json()
        code = data.get('code', '')
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        # Make request to CoCalc API with authentication
        try:
            # Using CoCalc API v1 compute endpoint
            response = requests.post(
                'https://cocalc.com/api/v1/compute',
                auth=(COCALC_API_KEY, ''),  # API key as username, empty password
                json={
                    'code': code,
                    'type': 'sage'
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result_data = response.json()
                
                # Extract output from CoCalc response
                stdout = result_data.get('stdout', '')
                stderr = result_data.get('stderr', '')
                
                if stderr:
                    return jsonify({
                        'success': False,
                        'error': stderr
                    }), 400
                
                result_text = stdout if stdout else 'Code executed successfully'
                
                return jsonify({
                    'success': True,
                    'result': result_text,
                    'output': result_text
                })
            elif response.status_code == 401:
                return jsonify({
                    'success': False,
                    'error': 'Invalid CoCalc API key. Please check your COCALC_API_KEY environment variable.'
                }), 401
            else:
                return jsonify({
                    'success': False,
                    'error': f'CoCalc API error: {response.status_code} - {response.text}'
                }), 500
                
        except requests.Timeout:
            return jsonify({
                'success': False,
                'error': 'Request timeout. Calculation took too long.'
            }), 408
        except requests.RequestException as e:
            return jsonify({
                'success': False,
                'error': f'CoCalc service error: {str(e)}'
            }), 503
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/health')
def health():
    """Health check endpoint"""
    has_api_key = bool(COCALC_API_KEY)
    return jsonify({
        'status': 'healthy',
        'api_key_configured': has_api_key
    }), 200

if __name__ == '__main__':
    if not COCALC_API_KEY:
        print("⚠️  WARNING: COCALC_API_KEY environment variable is not set!")
        print("📝 Get your API key from: https://cocalc.com (Settings > Account Settings > API Keys)")
    else:
        print("✅ CoCalc API key configured")
    
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
