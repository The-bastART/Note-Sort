import random
from midiutil import MIDIFile

def duration():
    duration=random.uniform(5.0,30.0)
    return duration

def pause():
    pause=random.randrange(20,100,10)
    pause2=pause/100.0
    return pause2
def volume():
    volume=random.randrange(60,100,1)
    return volume


def insertionSort(notes,time):
    for i, pitch in enumerate(notes):
        MyMIDI.addNote(track, channel, pitch, time, duration(), volume())
        time=time+pause()
    for index in range(1,len(notes)):
        currentvalue = notes[index]
        position = index
        while position>0 and notes[position-1]>currentvalue:
            notes[position]=notes[position-1]
            position = position-1

        notes[position]=currentvalue
        for i, pitch in enumerate(notes):
            MyMIDI.addNote(track, channel, pitch, time, duration(), volume())
            time=time+pause()

def selectionSort(notes, time):
    for i, pitch in enumerate(notes):
        MyMIDI.addNote(track, channel, pitch, time, duration(), volume())
        time=time+pause()
    for fillslot in range(len(notes)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if notes[location]>notes[positionOfMax]:
                positionOfMax = location

        temp = notes[fillslot]
        notes[fillslot] = notes[positionOfMax]
        notes[positionOfMax] = temp
        for i, pitch in enumerate(notes):
            MyMIDI.addNote(track, channel, pitch, time, duration(), volume())
            time=time+pause()

def bubbleSort(notes,time):
    for i, pitch in enumerate(notes):
            MyMIDI.addNote(track, channel, pitch, time, duration(), volume())
            time=time+pause()
    for passnum in range(len(notes)-1,0,-1):
        for i in range(passnum):
            if notes[i]>notes[i+1]:
                temp = notes[i]
                notes[i] = notes[i+1]
                notes[i+1] = temp

scales=[[2,2,1,2,2,2,1],            #00-Major
                [2,1,2,2,1,2,2],            #01-Natural Minor
                [2,1,2,2,2,2,1],            #02-Melodic Minor
                [2,1,2,2,1,3,1],            #03-Harmonic Minor
                [3,2,1,1,3,2],                #04-Minor Pentatonic
                [2,1,1,3,2,3],                #05-Major Blues
                [2,2,1,2,1,1,2,1],        #06-Major Bebop
                [2,1,1,1,2,2,1,2],        #07-Minor Bebop
                [1,2,1,2,2,2,2],            #08-Super Locrian
                [2,1,1,2,1,1,1,2,1],     #09-Nine Tone
                [2,1,2,2,2,1,2],            #10-Dorian
                [1,2,2,2,1,2,2],            #11-Phrygian
                [2,2,2,1,2,2,1],            #12-Lydian
                [2,2,1,2,2,1,2],            #13-Mixolydian
                [2,1,2,2,1,2,2],            #14-Aeolian
                [1,2,2,1,2,2,2],            #15-Locrian
                [3,2,2,3,2],                    #16-Pentatonic Minor
                [2,2,3,2,3],                    #17-Pentatonic Major
                [2,1,2,1,1,1,3,1],          #18-Algerian
                [2,2,1,1,2,2,2],            #19-Arabic
                [3,1,3,1,3,1],                  #20-Augmented
                [1,2,4,1,4],                    #21-Balinese
                [1,3,1,2,1,3,1],            #22-Byzantine
                [4,2,1,4,1],                    #23-Chinese
                [2,1,2,1,2,1,2,1],          #24-Diminished
                [1,2,1,2,1,2,1,2],          #25-Dominant Diminished
                [2,3,2,3,2],                    #26-Egyptian
                [1,2,1,1,1,2,2,2],          #27-Eight Tone Spanish
                [1,3,2,2,2,1,1],            #28-Enigmatic Major
                [1,2,3,1,3,1,1],            #29-Enigmatic Minor
                [2,1,2,2,1,2,2],            #30-Geez
                [2,2,1,2,1,2,2],            #31-Aeolian Dominant
                [1,4,1,4,2],                    #32-Hirajoshi
                [2,1,3,1,1,3,1],            #33-Hungarian Minor (Gypsy)
                [3,1,2,1,2,1,2],            #34-Hungarian Major
                [1,4,2,3,2],                    #35-Japanese
                [2,2,2,1,2,1,2],            #36-Lydian Dominant
                [1,2,2,2,1,3,1],            #37-Neapolitan Minor
                [1,2,2,2,2,2,1],            #38-Neapolitan Major
                [1,2,1,2,1,2,1,2],          #39-Octatonic (Half Whole)
                [2,1,2,1,2,1,2,1],          #40-Octatonic (Whole Half)
                [1,3,1,1,3,1,2],            #41-Oriental
                [2,2,2,2,2,2],              #42-Whole Tone
                [2,1,3,1,2,1,2],            #43-Romanian Minor
                [1,3,1,2,1,2,2],            #44-Spanish Gypsy (Phrygian Dominant)
                [2,3,2,2,3]]                    #45-Yo

track    = 0
channel  = 0
time     = 0
tempo    = 120  

MyMIDI = MIDIFile(1) 
MyMIDI.addTempo(track, time, tempo)

note_set=[39,41,44,46,48,51,53,56,58,63]
notes=[]
for i in range(0,50):
    notes.append(random.choice(note_set))

#insertionSort(notes,time)
selectionSort(notes, time)
#bubbleSort(notes,time)

with open("NoteSort.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
