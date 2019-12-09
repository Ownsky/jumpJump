import pygame
import random
import copy
from .character import Character
from .ground import Ground
from .obstacle import Obstacle

# FRAME = (640, 480)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAVITY_ACC = 10    #9.8   # acceleration of gravity
TIME_CYCLE = 10   # ms
OBSTACLE_OCCURRENCE = 0.5

FONT_TILE = 'resources/font/AdobeHeiti.otf'
CHARACTER_FILE = 'resources/image/steve.png'
OBSTACLE_FILES = [
    'resources/image/Zombie.png',
    'resources/image/Creeper.png',
    'resources/image/Silverfish.png',
    'resources/image/Skeleton.png',
    'resources/image/Slime.png',
]


class JumpGameDelegate:

    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = 480
        self.ground_absloute_height = height / 5
        # self.ground_y = height - height/5
        self.sky_height = height - self.ground_absloute_height

    # Texture of ground
    # groundfield = list()

    # All type of obstacles.
    obstacle_list = list()

    character = None
    obstacles = list()

    screen = None
    playing = True
    score = 0.0

    score_font = None
    score_surface = None
    score_coordinate = (0, 0)
    go_surface = None
    over_coordinate = (0, 0)

    counter100 = 100

    def coordinate_convert(self, coordinate):
        return tuple([coordinate[0], self.height - self.ground_absloute_height - coordinate[1]])

    def start(self):
        self.init_screen()
        self.create_world()
        self.init_game()
        self.run()

    def init_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("jump jump!")

    def create_world(self):

        self.score_font = pygame.font.Font(FONT_TILE, 20)
        self.score_coordinate = self.coordinate_convert(
            (self.width - self.ground_absloute_height, self.sky_height - self.ground_absloute_height/2)
        )
        self.over_coordinate = (self.ground_absloute_height/2, self.ground_absloute_height/2)

        # self.refresh_score()

        self.character = Character(CHARACTER_FILE, self)
        for f in OBSTACLE_FILES:
            obs = Obstacle(f, self)
            self.obstacle_list.append(obs)
        pass

    def init_game(self):
        self.obstacles = list()
        self.score = 0.0
        self.counter100 = 100
        self.playing = True
        self.character.stop()
        self.character.refresh()

    def draw_background(self):
        self.screen.fill(WHITE)
        pygame.draw.line(self.screen, BLACK,
                         self.coordinate_convert((0, 0)),
                         self.coordinate_convert((self.width, 0)))

    def refresh_score(self):
        self.score_surface = self.score_font.render(str(int(self.score)), False, BLACK)
        self.screen.blit(self.score_surface, self.score_coordinate)

    def game_over(self):
        self.playing = False
        self.go_surface = self.score_font.render("GAME OVER, press r to restart.", False, BLACK)
        self.screen.blit(self.go_surface, self.over_coordinate)
        pygame.display.flip()
        pygame.time.delay(1000)
        # self.character.stop()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            if self.playing:

                self.draw_background()

                self.loop()

                if self.counter100 > 0:
                    self.counter100 -= 1
                else:
                    self.counter100 = 100
                    self.loop100()

                pygame.display.flip()
                pygame.time.delay(TIME_CYCLE)
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    self.init_game()

    def loop(self):

        # check jump
        keys = pygame.key.get_pressed()
        if not self.character.jumping:
            if keys[pygame.K_SPACE]:
                self.character.jump()

        self.character.refresh()

        for obs in self.obstacles:
            obs.refresh()
            if obs.crash(self.character):
                # TODO: stop()
                self.game_over()
                # self.character.refresh()

        self.score += TIME_CYCLE/1000 * 10
        self.refresh_score()

        pass

    def loop100(self):
        r = random.random()
        if r < OBSTACLE_OCCURRENCE:
            obs = random.choice(self.obstacle_list)
            obs1 = obs.duplicate()
            self.obstacles.append(obs1)
        pass



