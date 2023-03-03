import mimetypes
import os
import re

from flask import Flask,request, send_file, Response,render_template

app=Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    """ 
        Simple wrapper around send_file which handles HTTP 206 Partial Content
        (byte ranges)
        TODO: handle all send_file args, mirror send_file's error handling
        (if it has any)
    """
    path="SampleVideo.mp4"
    range_header = request.headers.get('Range', None)
    if not range_header: return send_file(path)
    
    size = os.path.getsize(path)    
    byte1, byte2 = 0, None
    
    m = re.search('(\d+)-(\d*)', range_header)
    g = m.groups()
    
    if g[0]: byte1 = int(g[0])
    if g[1]: byte2 = int(g[1])

    length = size - byte1
    if byte2 is not None:
        length = byte2 - byte1
    
    data = None
    #with open(path, 'rb') as f:
    with open('SampleVideo.mp4', 'rb') as f:
        f.seek(byte1)
        data = f.read(length)

    rv = Response(data,206,mimetype=mimetypes.guess_type(path)[0],direct_passthrough=True)
    rv.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(byte1, byte1 + length - 1, size))

    return rv

if __name__ == '__main__':
	app.run()
