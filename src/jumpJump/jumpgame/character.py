import pygame

GRAVITY_ACC = 10    # 9.8    # acceleration of gravity
JUMP_RATIO = 3          # How high
START_SPD = 3           # How long and how high
TIME_CYCLE = 10
SIZE_SCALE = 1.5


class Character:

    jumping = False
    v = 0.0

    def __init__(self, image_path, delegate):
        # self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image_rect = self.image.get_rect()
        # self.screen = screen
        self.delegate = delegate

        imgH = int(self.delegate.ground_absloute_height/2)
        imgW = int(self.image_rect.width * imgH / self.image_rect.height)
        imgH = int(imgH * SIZE_SCALE)
        imgW = int(imgW * SIZE_SCALE)
        self.image = pygame.transform.scale(self.image, (imgW, imgH))
        self.image_rect = self.image.get_rect()
        self.coord = self.delegate.coordinate_convert((self.delegate.ground_absloute_height, 0))

        self.stop()
        self.refresh()

    def jump(self):
        self.jumping = True
        self.v = START_SPD
        pass

    # back to the ground
    def stop(self):
        self.jumping = False

        self.image_rect.left = self.coord[0]
        self.image_rect.bottom = self.coord[1]

        self.v = 0
        pass

    def refresh(self):
        if self.jumping:
            self.image_rect = self.image_rect.move([0, -self.v*JUMP_RATIO])
            self.v -= GRAVITY_ACC * TIME_CYCLE / 1000
            if self.image_rect.bottom >= self.coord[1]:
                self.stop()
            pass
        self.delegate.screen.blit(self.image, self.image_rect)
        pass