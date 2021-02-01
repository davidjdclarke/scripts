import numpy as np
from matplotlib import pyplot as plt
import random


class Device:
    def __init__(self, T):
        measurements = {'speed': [],
                        'F_B_shock': [],
                        'GAcc': [],
                        'leanAngle': [],
                        'GPS:': [],
                        'temperature': [],
                        'light': []}
        period = T
        active = False


def genParameters(num):
    freq_range = [.01, 100]
    amp_range = [0, 10]


def deviceRead(measurements, sample_rate):
    for key in measurements.keys():
        time = np.linspace(1, 60, sample_rate)
        freq = random.uniform(0.01, 10)
        amp =random.uniform(0, 10)
        measurements[key] = genSignal(freq, amp, time)

def getSpeed(num_dir=1):
    return 0

def addLinearNoise(signal):
    signal += generateNoise(signal, 0)
    return signal


def genSignal(freq, amps, time):
    new_signal = []
    composite_signals = []
    for i in range(len(freq)):
        composite_signals.append(amps[i] * np.sin(freq[i]*time/np.pi))
    for i in range(len(time)):
        new_signal.append(0)
        for j in range(len(composite_signals)):
            new_signal[i] += composite_signals[j][i]
    return new_signal


def getWatts(signal):
    return [signal[i] ** 2 for i in range(len(sig))]


def generateNoise(signal, mean_noise):
    sig_watts = getWatts(signal)
    sig_avg_watts = np.mean(sig_watts)
    noise = np.random.normal(mean_noise, np.sqrt(sig_avg_watts), len(sig_watts))
    return noise

def get_rand_parameters():
    params = {'amp': [], 'freq': []}
    num = random.randint(0, 10)
    for key in params.keys():
        for i in range(num):
            params[key].append(random.randint(0, 100))
    params['amp'] = [params['amp'][i] / 10 for i in range(num)]
    params['freq'] = [params['freq'][i] / 100 for i in range(num)]
    return params

if __name__ == "__main__":
    # Recorded values
    measurements = {'speed': [],
                    'F_B_shock': [],
                    'GAcc': [],
                    'leanAngle': [],
                    'GPS:': [],
                    'temperature': [],
                    'light': []}
    time = np.linspace(1, 100, 1000)

    params = get_rand_parameters()

    sig = genSignal(params['freq'], params['amp'], time)
    sig = addLinearNoise(sig)

    plt.plot(time, sig)
    plt.title('Signal')
    plt.ylabel('Voltage (V)')
    plt.xlabel('Time (s)')
    plt.show()