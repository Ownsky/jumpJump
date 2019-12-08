import pygame


class Character:
    def __init__(self, image, screen):
        self.image = image
        self.screen = screen

    def jump(self):
        pass

    # back to the ground
    def stop(self):
        pass

    def refresh(self):