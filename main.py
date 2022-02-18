from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    # !Change file path of the .wav file
    audio_file_path = 'C:\\Users\\User\\Desktop\\well_16k.wav'  # if file contains INFO chunks (created by editing
    # software) then a WavFileWarning is thrown

    # Read the data and calculate information about the audio file
    sample_rate = wavfile.read(audio_file_path)[0]
    audio_data = wavfile.read(audio_file_path)[1]
    number_of_channels = audio_data.shape[1]    # dimensions of the audio file
    length = audio_data.shape[0] / sample_rate    # time in seconds (total samples / sample rate)

    # Print information about the audio data
    print(f"file = \t{audio_file_path}")
    print(f"sample rate = \t{sample_rate}")
    print(f"channels = \t{number_of_channels}")
    print(f"length = \t{length} sec")

    # Show a plot of the waveform
    time = np.linspace(0., length, audio_data.shape[0])
    plt.plot(time, audio_data[:, 0], label="Left channel")
    plt.plot(time, audio_data[:, 1], label="Right channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()
