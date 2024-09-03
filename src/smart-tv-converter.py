import json
from flask import Flask, jsonify, render_template, request
from .remote_control import RemoteControl
from .utils import load_config

class SmartTVConverter:
    def __init__(self, tv_model: str, screen_size: int):
        self.tv_model = tv_model
        self.screen_size = screen_size
        self.installed_apps = []
        self.system_info = {}
        self.free_channels = []
        self.free_streaming_apps = []
        self.app = Flask(__name__, template_folder='../templates', static_folder='../static')
        self.remote_control = RemoteControl()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def home():
            return render_template('index.html', 
                                   tv_model=self.tv_model, 
                                   screen_size=self.screen_size,
                                   installed_apps=self.installed_apps,
                                   free_channels=self.free_channels,
                                   free_streaming_apps=self.free_streaming_apps)

        @self.app.route('/get_status', methods=['GET'])
        def get_status():
            return jsonify({
                'tv_model': self.tv_model,
                'screen_size': self.screen_size,
                'system_info': self.system_info,
                'installed_apps': self.installed_apps,
                'free_channels': self.free_channels,
                'free_streaming_apps': self.free_streaming_apps
            })

        @self.app.route('/remote_control', methods=['POST'])
        def remote_control():
            data = request.get_json()
            command = data.get('command')
            return self.remote_control.execute_command(command)

        @self.app.route('/launch_app', methods=['POST'])
        def launch_app():
            data = request.get_json()
            app_name = data.get('app_name')
            return jsonify({'status': 'success', 'message': f'Launched app: {app_name}'})

        @self.app.route('/open_channel', methods=['POST'])
        def open_channel():
            data = request.get_json()
            channel_name = data.get('channel_name')
            return jsonify({'status': 'success', 'message': f'Opened channel: {channel_name}'})
