import copy
import pygame

MOVE_SPD = 6
SIZE_SCALE = 1.5



class Obstacle:

    def __init__(self, image_path='', delegate=None):
        if image_path == '' or delegate is None:
            return
        self.image = pygame.image.load(image_path)
        self.image_rect = self.image.get_rect()
        self.delegate = delegate

        # resize
        if self.image_rect.width > self.image_rect.height:
            imgW = int(self.delegate.ground_absloute_height / 2)
            imgH = int(self.image_rect.height * imgW / self.image_rect.width)
        else:
            imgH = int(self.delegate.ground_absloute_height / 2)
            imgW = int(self.image_rect.width * imgH / self.image_rect.height)
        imgH = int(imgH*SIZE_SCALE)
        imgW = int(imgW*SIZE_SCALE)
        self.image = pygame.transform.scale(self.image, (imgW, imgH))
        self.image_rect = self.image.get_rect()

        self.coord = self.delegate.coordinate_convert((self.delegate.width, 0))

        self.image_rect.left = self.coord[0]
        self.image_rect.bottom = self.coord[1]

    def duplicate(self):
        obs = copy.copy(self)
        obs.image_rect = self.image_rect.copy()
        return obs

    def refresh(self):
        self.image_rect = self.image_rect.move([-MOVE_SPD, 0])
        self.delegate.screen.blit(self.image, self.image_rect)
        pass

    def crash(self, character):
        return self.image_rect.colliderect(character.image_rect)
        pass

    def checkout(self):
        if not self.image_rect.colliderect(self.delegate.screen.get_rect()):
            self.delegate.obstacles.remove(self)
