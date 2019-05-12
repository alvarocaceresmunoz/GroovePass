from constants import TOUCH_ON
from constants import TOUCH_OFF

"""
Touch sensor measures very fast, so every knock is registered as several
consecutive 1's. Clean the data by just getting the first 1 out of each group of
1's
"""
def getPeaks(knocks):
    peaks = [False for knock in knocks]
    previousWasKnock = False

    previousWasKnock = False
    for i, knock in enumerate(knocks):
        if knock == TOUCH_ON:
            if not previousWasKnock:
                peaks[i] = True
            previousWasKnock = True
        else:
            previousWasKnock = False

    return peaks

"""
Remove exceeding 0's after last 1 in the list of knocks
"""
def removeSilenceAfterLastPeak(peaks):
    silenceAtTheEnd = False
    checkingSilenceAtTail = True

    if peaks[-1] == False:
        silences = 0
        for peak in peaks[::-1]:
            silences += 1
            if peak:
                break
        result = peaks[:len(peaks)-silences+1]
    else:
        result = peaks

    return result

"""
Turn a sequence of knocks into a password (string)
"""
def getPassword(knocks):
    #!TODO

    """
    peaks = getPeaks(knocks)
    cleanPeaks = removeSilenceAfterLastPeak(peaks)

    peakDuration = 0
    peakDurations = []
    previousWasPeak = False

    for peak in cleanPeaks:
        if previousWasPeak and not peak:
            peakDuration += 1
    """

    return '0101'
