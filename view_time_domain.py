import librosa
import librosa.display

filename = 'Haunting_song_of_humpback_whales.wav'
y, sr = librosa.load(filename)
# trim silent edges
whale_song, _ = librosa.effects.trim(y)
librosa.display.waveplot(whale_song, sr=sr);
