from flask import jsonify

class RemoteControl:
    def __init__(self):
        self.commands = {
            'power_on': self.turn_on_tv,
            'power_off': self.turn_off_tv,
            'volume_up': lambda: self.adjust_volume(increase=True),
            'volume_down': lambda: self.adjust_volume(increase=False),
            'channel_up': self.channel_up,
            'channel_down': self.channel_down,
            'mute': self.mute,
        }

    def execute_command(self, command):
        if command in self.commands:
            self.commands[command]()
            return jsonify({'status': 'success', 'message': f'Executed command: {command}'})
        return jsonify({'status': 'error', 'message': 'Invalid command'}), 400

    def turn_on_tv(self):
        print("Turning on the TV.")

    def turn_off_tv(self):
        print("Turning off the TV.")

    def adjust_volume(self, increase: bool):
        if increase:
            print("Increasing volume.")
        else:
            print("Decreasing volume.")

    def channel_up(self):
        print("Changing to next channel.")

    def channel_down(self):
        print("Changing to previous channel.")

    def mute(self):
        print("Muting/unmuting the TV.")
