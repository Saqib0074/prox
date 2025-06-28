from flask import Flask, request, Response
import requests

app = Flask(__name__)

# CHANGE THIS to your real (blocked) proxy
REAL_PROXY = {
    'http': 'http://your.blocked.proxy:3128',
    'https': 'http://your.blocked.proxy:3128',
}

@app.route('/relay')
def relay():
    target_url = request.args.get('url')
    if not target_url:
        return "Missing 'url' parameter", 400

    try:
        r = requests.get(target_url, proxies=REAL_PROXY)
        return Response(r.content, status=r.status_code, content_type=r.headers.get('Content-Type'))
    except Exception as e:
        return f"Relay error: {e}", 502
