from flask import Flask,render_template,request, send_file
from pytube import YouTube
import io

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')


@app.route('/youtube',methods=['GET'])
def youtube():
    return render_template('youtube_download.html')

#download page 
@app.route('/download', methods=['POST'])
def download():
    url = request.form['link']
    if not url:
        return "Please enter a YouTube URL"
    
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        # Download the video to a BytesIO object
        byte_io = io.BytesIO()
        video.stream_to_buffer(byte_io)
        byte_io.seek(0) # Move the cursor to the beginning of the buffer
        
        return send_file(byte_io, as_attachment=True, download_name=f"{yt.title}.mp4", mimetype='video/mp4')
    
    except Exception as e:
        return str(e)


if __name__ =='__main__':
    app.run(debug=True)