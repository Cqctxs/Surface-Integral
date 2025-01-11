from manim import *

class partial(ThreeDScene):
    def construct(self):
        def f(s,t):
            return np.array([s,t,0.5*(s*s+t*t)])
        cut = Surface(
            lambda u, v: np.array([u, 0, v]),  
            u_range=[-5, 5],  
            v_range=[5, -5], 
            fill_opacity = 0.5,
            checkerboard_colors=None 
        )
        axes = ThreeDAxes(axis_config={"include_tip": False})
        para = Surface(
            lambda u, v: axes.c2p(*f(u, v)),    
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_color=GREEN,
            fill_opacity = 1,
            checkerboard_colors=None 
        )
        self.play(Write(axes))
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)
        self.wait(1)
        self.play(Write(para, run_time=3))
        self.wait(1)
        self.play(Write(para, run_time=0.5),Create(cut, run_time=1.5))
        self.wait(1)
        self.move_camera(phi=90 * DEGREES, theta=90 * DEGREES, zoom=1.5, run_time=1.5)
        self.wait(1)
    
