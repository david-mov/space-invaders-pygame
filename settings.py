from os.path import abspath, dirname
from os import walk
import pygame as pg

FPS = 60

BASE_PATH = abspath(dirname(__file__))

FONT_PATH = BASE_PATH + '/fonts'
IMAGE_PATH = BASE_PATH + '/images'
SOUND_PATH = BASE_PATH + '/sounds'

TEXT_COLOR = (245, 191, 3)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

BACKGROUND_SPEED = 2.5

PLAYER_POS = PLAYER_X, PLAYER_Y = 370, 450
PLAYER_SPEED = 3

BULLET_X_DIST = 16
BULLET_Y_DIST = 10

BULLET_SPEED = 12

ENEMY_IMAGES = next(walk(IMAGE_PATH + '/enemies'), (None, None, []))[2] # [] if no files
for idx in range(len(ENEMY_IMAGES)):
    ENEMY_IMAGES[idx] = IMAGE_PATH + '/enemies/' + ENEMY_IMAGES[idx]

NUM_OF_ENEMY_CATEGORIES = len(ENEMY_IMAGES)

NUM_OF_ENEMIES = 3

COLLISION_SCOPE = 35

MENU_TITLE_POS = MENU_TITLE_X, MENU_TITLE_Y = 25, 210
MENU_INSTRUCTIONS_POS = MENU_INSTRUCTIONS_X, MENU_INSTRUCTIONS_Y = 150, 290

GAME_OVER_TITLE_POS = GAME_OVER_TITLE_X, GAME_OVER_TITLE_Y = 140, 210
GAME_OVER_INSTRUCTIONS_POS = GAME_OVER_INSTRUCTIONS_X, GAME_OVER_INSTRUCTIONS_Y = 130, 290

SCORE_X = 10
SCORE_Y = 10