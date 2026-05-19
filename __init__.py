from .core import VoidEngine

_engine = VoidEngine()

def draw(image, x, y, size=None):
    _engine.draw(image, x, y, size)

def run():
    _engine.run()