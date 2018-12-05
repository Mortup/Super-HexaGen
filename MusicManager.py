import pygame

beat_number = 1 #or 2 or 3 or 4
currentBpm = 107
crotchet = 60000.0 / currentBpm;
delay = 0;

muted = False

songs = ['audio/Ouroboros.mp3', 'audio/NoTurningBack.mp3', 'audio/Momentum.mp3']
bpms = [107, 140, 180]

def play(index):
    global currentBpm, crotchet
    currentBpm = bpms[index]
    crotchet = 60000.0 / currentBpm

    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play(0)

    if muted:
        pygame.mixer.music.set_volume(0)

def get_song_position():
    return float(pygame.mixer.music.get_pos()) - float(delay);