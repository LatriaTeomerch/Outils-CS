import numpy as np
from random import random
from sounddevice import play as sdplay

SAMPLING_FREQ = 44100


def pure_beep(freq: int = 440, duration: float = 1.0) -> np.array:
    """
    Generates a pure beep waveform with a single frequency tone.


    Parameters:
        freq (int, optional): The frequency of the tone in Hz. Defaults to 440.
        duration (int, optional): The duration of the generated waveform in seconds. Defaults to 1.

    Returns:
        np.array: An array of generated waveform samples.

    """
    amp = 1.0
    t = np.linspace(0, duration, int(duration * SAMPLING_FREQ), False)
    note = amp * np.sin(freq * t * 2 * np.pi)
    return note


def fat_beep(
    freq: int = 440,
    duration: float = 1,
) -> np.array:
    """
    Generates a fat beep waveform with harmonics using additive synthesis.

    Parameters:
        freq (int, optional): The frequency of the fundamental tone in Hz. Defaults to 440.
        duration (float, optional): The duration of the generated waveform in seconds. Defaults to 1.

    Returns:
        np.array: An array of generated waveform samples.

    """
    harms = 5
    decay = 0.6
    amp = 1.0
    t = np.linspace(0, duration, int(duration * SAMPLING_FREQ), False)
    note = amp * np.sin(freq * t * 2 * np.pi)

    for i in range(harms):
        amp *= decay
        note += amp * np.sin((i + 1) * freq * t * 2 * np.pi)
    return note


def kpst_pluck(freq: int, duration: float = 1.0) -> np.array:
    """
    Generates a plucked string waveform using the Karplus-Strong algorithm.

    Parameters:
        duration (float): The duration of the generated waveform in seconds.
        freq (int): The frequency of the plucked string in Hz.

    Returns:
        np.array: An array of generated waveform samples.

    """
    resampled_sampling_frequency = int(SAMPLING_FREQ * (2.0 / duration))
    wavelength_in_samples = int(
        round((SAMPLING_FREQ / freq) * (resampled_sampling_frequency / SAMPLING_FREQ))
    )

    noise_samples = [random() * 2 - 1 for _ in range(wavelength_in_samples)]

    output_samples = []

    for _ in range(SAMPLING_FREQ * 2 // len(noise_samples)):
        for output_position in range(len(noise_samples)):
            wavetable_position = output_position % len(noise_samples)
            noise_samples[wavetable_position] = (
                noise_samples[wavetable_position]
                + noise_samples[(wavetable_position - 1) % len(noise_samples)]
            ) / 2

        output_samples += noise_samples

    exp_size = int(duration * SAMPLING_FREQ)
    output = np.zeros(exp_size)
    for i, val in enumerate(output_samples):
        try:
            output[i] = val
        except IndexError:
            pass

    return output


SEMITONE_RATIO = 256.0 / 243


def guitar_string(
    fret: int, tuning: float = 82.41, duration: float = 2.0
) -> np.ndarray:
    """
    Generate a plucked guitar string sound.

    Parameters:
    - fret (int): The fret number to play on the guitar string.
    - tuning (float): The frequency of the string's initial tuning (default: 82.41 Hz for E2).
    - duration (float): The duration of the generated sound in seconds (default: 2.0 seconds).

    Returns:
    - np.ndarray: An array representing the generated sound.
    """
    # Calculate the frequency based on the tuning and fret number
    string_freq = tuning * (SEMITONE_RATIO**fret)
    return kpst_pluck(freq=string_freq, duration=duration)


def create_base(duration: float) -> np.array:
    """
    Create the base sampling array for a song.

    Parameters:
        duration (float): The duration of the base sampling array in seconds.

    Returns:
        np.array: A numpy array of zeros representing the base sampling array.

    """
    return np.zeros(int(duration * SAMPLING_FREQ))


def add_note(base: np.array, note: np.array, start: float) -> np.array:
    """
    Add a note to the base sampling array for a song.

    Parameters:
        base (np.array): The base sampling array.
        note (np.array): The array representing the note to be added.
        start (float): The start time of the note in seconds.

    Returns:
        np.array: A numpy array representing the updated base sampling array with the added note.

    """
    id_start = int(start * SAMPLING_FREQ)

    base_out = base.copy()
    if id_start >= base.size:
        return base_out
    id_end = min(id_start + note.size, base.size)
    base_out[id_start:id_end] += note[0 : id_end - id_start]

    return base_out


class GuitarString:
    def __init__(self, tuning: float = 82.41):
        self.tuning = tuning

    def pluck(self, fret: int, duration: float = 2.0) -> np.array:
        return guitar_string(fret=fret, tuning=self.tuning, duration=duration)


class Guitar:
    def __init__(self, strings_tunings: list):
        self.st = []
        for tuning in strings_tunings:
            self.st.append(GuitarString(tuning))

    def pluck(self, frets: list, duration: float, speed=0.04):
        note = create_base(duration)
        for i, fret in enumerate(frets):
            if fret is not None:
                # note += self.st[i].pluck(fret, duration)
                note = add_note(note, self.st[i].pluck(fret, duration), speed * i)
        return note


if __name__ == '__main__':

# Simple beep
# sdplay(pure_beep(freq=440, duration=1.0), blocking=True, samplerate=SAMPLING_FREQ)

#Harmonic beep
# sdplay(fat_beep(freq=440, duration=1.0), blocking=True, samplerate=SAMPLING_FREQ)

#Guitar string one note
# sdplay(kpst_pluck(freq=440, duration=1), blocking=True, samplerate=SAMPLING_FREQ)

#Song 
# create the necessary notes
n7 = guitar_string(fret=7, tuning=110.0, duration=1)
n10 = guitar_string(fret=10, tuning=110.0, duration=1)
n5 = guitar_string(fret=5, tuning=110.0, duration=1)
n3 = guitar_string(fret=3, tuning=110.0, duration=1)
n2 = guitar_string(fret=2, tuning=110, duration=1)

# create a 4.3 second long void song
song = create_base(duration=3.5)

# Declare the tab
song = add_note(song, n7, 0.1)
song = add_note(song, n7, 0.826)
song = add_note(song, n10, 1.068)
song = add_note(song, n7, 1.43)
song = add_note(song, n5, 1.79)
song = add_note(song, n3, 2.035)
song = add_note(song, n2, 3.002)

# sdplay(song, blocking=True, samplerate=SAMPLING_FREQ)



#Simple Chord

# create the necessary notes
A_0f = guitar_string(fret=2, tuning=110.00, duration=2)
D_2f = guitar_string(fret=2, tuning=146.83, duration=2)
G_2f = guitar_string(fret=2, tuning=196.0, duration=2)
B_1f = guitar_string(fret=1, tuning=246.94, duration=2)
e_Of = guitar_string(fret=0, tuning=329.63, duration=2)

# create the basis for the chord
chord_Am = create_base(duration=2)

# Add notes
chord_Am = add_note(chord_Am, A_0f, 0.0)
chord_Am = add_note(chord_Am, D_2f, 0.025)
chord_Am = add_note(chord_Am, G_2f, 0.05)
chord_Am = add_note(chord_Am, B_1f, 0.075)
chord_Am = add_note(chord_Am, e_Of, 0.1)

# sdplay(chord_Am, blocking=True, samplerate=SAMPLING_FREQ)


#Simple Chord with objects

string_e = GuitarString(tuning=329.63)
string_B = GuitarString(tuning=246.94)
string_G = GuitarString(tuning=196.00)
string_D = GuitarString(tuning=146.83)
string_A = GuitarString(tuning=110.00)
string_E = GuitarString(tuning=82.41)

# create the necessary notes
A_0f = string_A.pluck(fret=0, duration=2)
D_2f = string_D.pluck(fret=2, duration=2)
G_2f = string_G.pluck(fret=2, duration=2)
B_1f = string_B.pluck(fret=1, duration=2)
e_Of = string_e.pluck(fret=0, duration=2)


# sdplay(chord_Am, blocking=True, samplerate=SAMPLING_FREQ)

guitar = Guitar([82.41, 110.00, 146.83, 196.00, 246.94, 329.63])
chord_Am = guitar.pluck([None, 0, 2, 2, 1, 0], 2.0)
chord_C = guitar.pluck([0, 3, 2, 0, 1, 0], 2.0)
chord_D = guitar.pluck([None, None, 0, 2, 3, 2], 2.0)
chord_F = guitar.pluck([1, 3, 3, 2, 1, 1], 2.0)
chord_E7 = guitar.pluck([0, 2, 0, 1, 0, 0], 2.0)

# sdplay(chord_E, blocking=True, samplerate=SAMPLING_FREQ)

song = create_base(16)
song = add_note(song, chord_Am, 0)
song = add_note(song, chord_C, 2)
song = add_note(song, chord_D, 4)
song = add_note(song, chord_F, 6)
song = add_note(song, chord_Am, 8)
song = add_note(song, chord_E7, 10)
song = add_note(song, chord_Am, 12)
song = add_note(song, chord_E7, 14)

sdplay(song, blocking=True, samplerate=SAMPLING_FREQ)


