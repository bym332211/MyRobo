import speech
import time
import win32com.client
import urllib.request as request

class listener:
    def callback(phrase, listener):
        # speech.say("You said %s" % phrase)
        print(phrase)
        if phrase == "turn off":
            listener.stoplistening()
        request.Request('http://localhost:7777/asr')
        return phrase

    def start(self):
        phraseList = ['来福']
        listen = speech.listenfor(phraseList, self.callback)
        # listener = speech.listenforanything(asdf)
        while listen.islistening():
            time.sleep(1)
            print("Still waiting...")
        # speaker = win32com.client.Dispatch("SAPI.SpVoice")
        # speaker.Speak("你好")

if __name__ == '__main__':
    li = listener()
