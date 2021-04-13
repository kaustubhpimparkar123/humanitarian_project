#importing librarries
import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip

#extracting the audio from the video file. hard coded the file names for now
transcribed_audio_file_name = "transcribed_speech.wav"
zoom_video_file_name = "Fork_tutorial.mp4"
audioclip = AudioFileClip(zoom_video_file_name)
audioclip.write_audiofile(transcribed_audio_file_name)

#finding out the total duration of the audio clip
with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
total_duration = math.ceil(duration / 60)

#transcribing the audio in to text in chunks of 10 MB (limitation of the api call)
r = sr.Recognizer()
for i in range(0, total_duration):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
    f = open("transcription.txt", "a")
    f.write(r.recognize_google(audio))
    f.write(" ")
f.close()