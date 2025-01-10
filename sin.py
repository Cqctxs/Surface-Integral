from manim import *

class te (Scene):
    def construct(self):
        f = MathTex("f(x) = \sin x")
        f1 = MathTex("f^{\prime}(x) = \cos x")
        f1.set_color(YELLOW)

        self.play(Write(f))
        self.wait(0.5)
        self.play(f.animate.shift(UP * 1))
        self.play(Write(f1))
        self.wait(0.5)
    