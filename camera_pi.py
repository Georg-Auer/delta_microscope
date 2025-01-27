import io
import time
import logging
import picamera
from base_camera import BaseCamera

# https://picamera.readthedocs.io/en/release-1.13/recipes2.html#unencoded-video-capture
class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
