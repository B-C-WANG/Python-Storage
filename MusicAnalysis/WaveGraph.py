import wave
import numpy as np
import os
import pylab as pl
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt


def mp3_to_wave(file_name):
    command = "ffmpeg -y -i  %s %s"% (file_name, file_name.replace("mp3","wav"))

    print(command)
    os.system(command)


def wave_plot(file_name):

    f = wave.open(file_name, "rb")

    params = f.getparams()

    n_channels, sample_width, frame_rate,n_frames = params[:4]

    frames = f.readframes(n_frames)
    # 提取所有frame的信息，得到的是String
    f.close()

    wave_data = np.fromstring(frames,dtype=np.short)
    # String转化，然后分开
    wave_data.shape = -1,2

    wave_data = wave_data.T

    time = np.arange(0, n_frames) * (1.0 / frame_rate)

    y = fft(wave_data[0])
    # fft
    def plot_strength():
        real_y = y.real
        imag_y = y.imag

        # 得到各个频率强度
        strength = np.sqrt (np.square(real_y) + np.square(imag_y))
        # 绘制频率 -强度图
        plt.plot(strength)
        plt.show()

    plot_strength()





if __name__ == '__main__':


    file_name = "C:\\Users\Administrator\Desktop\Python-Storage\MusicAnalysis\\KongaCongaKappa.wav"

    wave_plot(file_name)
    #mp3_to_wave(file_name)