import statistics
from turtle import distance
import pyrg_funkcje
FOLDER = "daneztreningow/"
CHARTS = "Wykresy/"
def read_swim_data(filename):

    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")

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
    mins_secs, hundredths = f"{(average / 100):.2f}".split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes * 60
    average = f"{minutes}:{seconds:0>2},{hundredths}" 

    return swimmer, age, distance, stroke, times, average, converts #zwracamy krotke

def produce_bar_chart(fn):
    """Na podstawie nazwy pliku pływaka, generuje wykres słupkowy, używając HTML i SVG.

    Wykres jest zapisywany w katalogu określonym przez stałą CHATRS. Funkcja zwraca
    ścieżkę dostępu do pliku wykresu.
    """
    swimmer, age, distance, stroke, times, average, converts = read_swim_data(fn)
    title = f"{swimmer} (poniżej {age} lat), {distance}, styl: {stroke}"
    from_max =max(converts)
    
    times.reverse()
    converts.reverse()
    header = f"""<!DOCTYPE html>
                <html>
                    <head>
                        <title>
                            {title}
                        </title>
                    </head>
                    <body>
                        <h3>{title}</h3>"""
    body = ""
    for n, t in enumerate(times):
        bar_width = pyrg_funkcje.convert2range(converts[n], 0, from_max, 0, 350)

        body = body + f"""
                            <svg height="30" width="400">
                                <rect height="30" width="{bar_width}" style="fill:rgb(100,29,110);" />
                            </svg>{t}<br />
                        """
    footer = f"""
                                <p>Średni czas: {average}</p>
                    </body>
                </html>
        """
    page = header + body + footer
    save_to = f"Wykresy/{fn.removesuffix(".txt")}.html"
    with open(save_to, "w") as sf:
        print(f"{page}", file=sf)

    return save_to