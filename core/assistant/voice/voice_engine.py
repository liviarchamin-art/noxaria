# voice_engine.py
import wave
from piper import PiperVoice

# Keep the configuration easily changeable here
ACTIVE_VOICE = "amy"

model_path = r"C:\Users\Administrator\Desktop\noxaria-diamond\core\assistant\voice\{0}\{0}.onnx".format(ACTIVE_VOICE)
config_path = r"C:\Users\Administrator\Desktop\noxaria-diamond\core\assistant\voice\{0}\{0}.json".format(ACTIVE_VOICE)

voice = PiperVoice.load(model_path, config_path=config_path)
