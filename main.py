import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)

def stream(camera_index):
    cam = cv2.VideoCapture(camera_index)
    while True:
        _, frame = cam.read()
        ret, jpg = cv2.imencode('.jpg', frame)
        jpg2bytes = jpg.tobytes()
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpg2bytes + b'\r\n\r\n'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stream_feed')
def stream_feed():
    return Response(stream(0), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(host='0.0.0.0', port=8000, debug=False)
