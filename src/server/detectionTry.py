import pyaudio
import wave
import struct
import math

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44d.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 10 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test.wav' # name of .wav file
swidth=2
audio = pyaudio.PyAudio() # create pyaudio instantiation
#energy threshold 20 dB
threshold= 20
SHORT_NORMALIZE= (1.0/32768.0)

def convertData(input):
    count = len(input)/swidth
    format= "%dh"%(count)
    #short is 16 bit int
    shorts = struct.unpack(format, input)
    
    sum_square=0.0
    for sample in shorts:
        n= sample * SHORT_NORMALIZE
        sum_square += n*n
    #compute rms
    rms=math.pow(sum_square/count,0.5);
    return rms * 1000
# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
print("Started recording..!")
frames = []
silent = 0
# loop through stream and append audio chunks to frame array
for ii in range(0,int((samp_rate/chunk)*record_secs)+1):
    data = stream.read(chunk)
    rms_value = convertData(data)
    if rms_value > threshold :
        print("Sound detected.!")
        silent = 1
    frames.append(data)
if silent == 0:
    print("Time out no sound detected!")
print("Finished recording.!")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
#audio.terminate()

# save the audio frames as .wav file
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()
