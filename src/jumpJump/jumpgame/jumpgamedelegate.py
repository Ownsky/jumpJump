import pygame
from .character import Character
from .ground import Ground
from .obstacle import Obstacle

# FRAME = (640, 480)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAVITY_ACC = 9.8   # acceleration of gravity
TIME_CYCLE = 10   # ms

class JumpGameDelegate:

    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = 480
        self.ground_height = height/5
        # self.ground_y = height - height/5
        self.sky_height = height - self.ground_height

    # Texture of ground
    # groundfield = list()

    # All type of obstacles.
    obstacle_List = list()

    character = None
    obstacles = list()

    screen = None
    playing = True
    score = 0
    scorefont = None
    scoresurface = None
    score_coordinate = (0, 0)
    # background = None

    def coordinate_convert(self, coordinate):
        return tuple([coordinate[0], self.height - self.ground_height - coordinate[1]])

    def start(self):
        self.init_screen()
        self.create_world()
        self.run()

    def init_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("jump jump!")

    def create_world(self):

        self.screen.fill(WHITE)
        pygame.draw.line(self.screen, BLACK,
                         self.coordinate_convert((0, self.ground_height)),
                         self.coordinate_convert((self.width, self.ground_height)))

        self.scorefont = pygame.font.Font('resources/font/AdobeHeiti.otf', 20)
        self.score_coordinate = self.coordinate_convert(
            (self.width - self.ground_height, self.sky_height - self.ground_height)
        )
        self.refresh_score()

        #TODO: init char
        self.character = Character(None, self.screen)

        pass
        pygame.display.flip()

    def refresh_score(self):
        self.scoresurface = self.scorefont.render(str(self.score), False, BLACK)
        self.screen.blit(self.scoresurface, self.score_coordinate)

    def run(self):
        while True:
            while self.playing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                self.loop()

    def loop(self):
        # TODO: check jump
        self.character.refresh()
        for obs in self.obstacles:
            obs.refresh()
            if obs.crash(self.character):
                pass
                # TODO: stop()
        pass