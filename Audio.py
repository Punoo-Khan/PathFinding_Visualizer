import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init(frequency=44100)
        self.beep = pygame.mixer.Sound("beep.wav")

    def play_sound(self, volume=1.0, pitch=1.0):
        self.beep.set_volume(volume)
        self.beep.play()  # Play the sound but do not wait for it to finish

    def adjust_pitch(self, pitch):
        # This method is not perfect and will only simulate pitch change by adjusting the sound volume.
        volume = max(0.0, min(1.0, pitch))  # Ensure volume is between 0.0 and 1.0
        self.beep.set_volume(volume)
