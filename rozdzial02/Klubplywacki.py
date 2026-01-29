import statistics
from turtle import distance
FOLDER = "daneztreningow/"

def read_swim_data(filename):

    swimmer, age, distance, stroje = filename.removesuffix(".txt").split("-")

    with open (FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip().split(";")

    converts = []

    for t in times:
        if ":" in t:
            minutes, rest = t.split(":")
            seconds, hunderths = rest.split(",")
        else:
            minutes = 0
            seconds, hunderths = t.split(",")
    
        converts.append( int(minutes) * 6000 + int(seconds) * 100 + int(hunderths))

    average = statistics.mean(converts)
    mins_secs, hunderths = str(round(average / 100, 2)).split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes * 60
    average = str(minutes) + ":" + str(seconds) + "," + hunderths
    return swimmer, age, distance, stroje, times, average #zwracamy krotke

