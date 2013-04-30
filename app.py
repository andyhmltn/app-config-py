import json
import app_config

from flask import *

app = Flask(app_config.PROJECT_NAME)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/js/config.js')
def config_js():
	config = {}

	for k, v in app_config.__dict__.items():
		if k.upper() == k:
			config[k] = v

	js = 'window.CONFIG = ' + json.dumps(config)

	return js, 200, { 'Content-Type': 'application/javascript' }

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)