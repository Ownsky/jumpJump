import pygame
import jumpJump.jumpgame as game


def main():
    delegate = game.JumpGameDelegate()
    delegate.start()


if __name__ == "__main__":
    main()