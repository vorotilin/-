import pygame
import threading
import time
from flask import Flask, jsonify

app = Flask(__name__)

pygame.mixer.init()

first_beat_sound = pygame.mixer.Sound('first-beat.wav')
click_sound = pygame.mixer.Sound('click.wav')

is_playing = False
interval_id = None
current_beat = 0

input1_value = 4
input2_value = 1

def update_bpm(bpm):
    counter_top = input1_value
    counter_bottom = input2_value
    return (60 / bpm) * (counter_bottom / counter_top) * 1000

def play_metronome(bpm):
    global current_beat
    note_duration = update_bpm(bpm)
    
    while is_playing:
        if current_beat == 0:
            first_beat_sound.play()
        else:
            click_sound.play()
        
        current_beat = (current_beat + 1) % input1_value
        time.sleep(note_duration / 1000.0)

@app.route('/start/<int:bpm>', methods=['POST'])
def start_metronome(bpm):
    global is_playing, interval_id, current_beat
    if not is_playing:
        is_playing = True
        current_beat = 0
        interval_id = threading.Thread(target=play_metronome, args=(bpm,))
        interval_id.start()
        return jsonify({"status": "started", "bpm": bpm})
    return jsonify({"status": "already running"})

@app.route('/stop', methods=['POST'])
def stop_metronome():
    global is_playing, interval_id
    if is_playing:
        is_playing = False
        if interval_id is not None:
            interval_id.join()
        return jsonify({"status": "stopped"})
    return jsonify({"status": "not running"})

if __name__ == '__main__':
    app.run(debug=True)