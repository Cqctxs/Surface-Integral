from manim import *

class title (Scene):
    def construct(self):
        title = Tex("Surface Integrals", font_size=120)
    
        title.move_to(ORIGIN)
        
        self.play(Write(title))
       
        self.wait(2)
