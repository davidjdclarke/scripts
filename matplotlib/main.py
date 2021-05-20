import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

PERIOD = 10

if __name__ == "__main__":
    file = './demo4.csv'
    df = pd.read_csv(file)
    
    keys = df.keys()
    l = len(df[keys[0]])

    t = np.linspace(0, 10, num=l)

    if file == './demo1.csv' or file == './demo2.csv':
        for i in range(l):
            df['qd1'][i] = df['qd1'][0]
            df['qd2'][i] = df['qd2'][0]
            df['qd3'][i] = df['qd3'][0]

        df['qd1'][0] = df['q1'][0]
        df['qd2'][0] = df['q2'][0]
        df['qd3'][0] = df['q3'][0]

    fig, axs = plt.subplots(3)
    axs[0].plot(t, df['q1'], label='q1')
    axs[0].plot(t, df['qd1'], label='q1_d')
    axs[0].set_title("q1 vs q1_d")
    axs[0].legend()

    axs[1].plot(t, df['q2'], label='q1')
    axs[1].plot(t, df['qd2'], label='q2_d')
    axs[1].set_title("q2 vs q2_d")
    axs[1].legend()

    axs[2].plot(t, df['q3'], label='q1')
    axs[2].plot(t, df['qd3'], label='q3_d')
    axs[2].set_title("q3 vs q3_d")
    axs[2].legend()

    if file == './demo1.csv':
        fig.suptitle("Demo 1")
    elif file == './demo2.csv':
        fig.suptitle("Demo 2")
    elif file == './demo3.csv':
        fig.suptitle("Demo 3")
    elif file == './demo4.csv':
        fig.suptitle("Demo 4")
    plt.show()
