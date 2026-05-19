# img (mini library)
# pip-installable image drawing helper built on pygame

import pygame
import sys

pygame.init()

class VoidEngine:
    def __init__(self, width=800, height=600, title="img"):
        self.w = width
        self.h = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.objects = []
        self.running = False

    def draw(self, image_name, x, y, size_px=None):
        """
        image_name: file path
        x, y: position
        size_px: FINAL rendered width (keeps aspect ratio)
        """
        img = pygame.image.load(image_name).convert_alpha()

        if size_px:
            ratio = img.get_height() / img.get_width()
            img = pygame.transform.scale(img, (size_px, int(size_px * ratio)))

        self.objects.append((img, (x, y)))

    def run(self):
        self.running = True
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))

            for img, pos in self.objects:
                self.screen.blit(img, pos)

            pygame.display.flip()

# ----------------------
# pip packaging layout (IMPORTANT)
# ----------------------

"""
project structure:

img/
 ├── img/
 │    ├── __init__.py
 │    └── core.py   (this file)
 ├── pyproject.toml
 ├── README.md

usage after pip install:

from img import Img

i = Img()
i.draw("cat.png", 100, 150, 200)
i.run()
"""

# __init__.py idea:
# from .core import ImgEngine as Img

# pyproject.toml idea:
"""
[project]
name = "img"
version = "0.1.0"
dependencies = ["pygame"]
"""