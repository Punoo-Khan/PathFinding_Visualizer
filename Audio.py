import pygame
import time

class SoundManager:
    def __init__(self):
        pygame.mixer.init(frequency=44100)
        self.beep = pygame.mixer.Sound("beep.wav")

    def play_sound(self, volume=1.0, pitch=1.0):
        self.beep.set_volume(volume)
        # Adjust the playback frequency, which can crudely affect pitch
        new_frequency = int(44100 * pitch * 5.0)
        pygame.mixer.quit()
        pygame.mixer.init(frequency=new_frequency)
        self.beep.play()

    def stop_sound(self):
        self.beep.stop()
        pygame.mixer.quit()
        pygame.mixer.init(frequency=44100)  # Reset to normal frequency

