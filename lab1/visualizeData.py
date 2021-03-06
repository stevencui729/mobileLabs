import numpy as np
import parse_data
import generateFeatures
import matplotlib.pyplot as plt

def varGraphs(data, key):
    activities = ["Driving", "Standing", "Walking"]
    #activities = ["Jumping", "Standing"]
    colors = ['red','green','blue','purple']
    for activity, color, i in zip(activities, colors, np.arange(len(activities))):
        #varDict, _, _, _ = generateFeatures.generateFeatures(data[0])
        varList = []
        for trace in data[activity]:
            varDict, _, _, _ = generateFeatures.generateFeatures(trace)
            varList.append(varDict[key])
        plt.scatter([i]*len(varList), varList, c = color, label = activity)
        plt.legend()
        plt.title("variance of" + key)

    #plt.show(block = False)

def plotSpectrum(trace, key, title):
    _, powerSpectrums, _, relTime = generateFeatures.generateFeatures(trace)
    plt.plot(powerSpectrums[key])
    plt.title(title)

def plotMidSpectrums(data, channel):
    activities = ['Driving', 'Walking']
    colors = ['red', 'blue']
    for activity, color, i in zip(activities, colors, np.arange(len(activities))):
        midList = []
        for trace in data[activity]:
            _, _, midPower, _ = generateFeatures.generateFeatures(trace)
            midList.append(midPower[channel])
        plt.scatter([i]*len(midList), midList, c = color, label = activity)
        plt.legend()
        plt.title("middle power " + channel)

def nextFig(i):
    plt.figure(i)
    return i+1
def main():
    dataKeys = ['xAccl', 'yAccl', 'zAccl', 'time']
    data = parse_data.parse_data()
    drivingData = data["Driving"]
    jumpingData = data["Jumping"]
    standingData = data["Standing"]
    walkingData = data["Walking"]

    #varDict, powerSpectrums, spectrumPeaks, relTime = generateFeatures.generateFeatures(drivingData[0])
    fig = nextFig(0)
    plotMidSpectrums(data, 'xAccl')
    fig = nextFig(fig)
    plotMidSpectrums(data, 'yAccl')
    fig = nextFig(fig)
    plotMidSpectrums(data, 'zAccl')

    # varGraphs(data, 'yAccl')

    # fig = nextFig(fig)
    # varGraphs(data, 'xAccl')

    fig = nextFig(fig)
    varGraphs(data, 'zAccl')
    for i in range(2):
        fig = nextFig(fig)
        plotSpectrum(drivingData[i*3], 'yAccl', 'drive')

        fig = nextFig(fig)
        plotSpectrum(walkingData[i*3], 'yAccl', 'walk')

if __name__ == "__main__":
    main()
    plt.show()