from manim import *

class Primeiro(Scene):
    def construct(self):
        texto = Text("Hello, Manim!")
        self.play(Write(texto))
        self.wait()