from manim import *

class Tangent(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2 * PI], y_range=[-1.5, 1.5],
            axis_config={"color": BLUE, "include_tip": False},
        )

        sin_graph = axes.plot(lambda x: np.sin(x), color=WHITE)

        dot = Dot(color=YELLOW).move_to(axes.c2p(0, np.sin(0)))

        def tangent_line(x_val):
            slope = np.cos(x_val) 
            y_intercept = np.sin(x_val) - slope * x_val  
            return lambda x: slope * x + y_intercept  

       
        tangent_graph = axes.plot(tangent_line(0), color=GREEN)

        self.play(Create(axes), Create(sin_graph), Create(tangent_graph))

        dot_and_tangent_group = VGroup(dot, tangent_graph)

        for x_val in np.linspace(0, 2 * np.pi, 200):
            
            new_dot_pos = axes.c2p(x_val, np.sin(x_val))
            dot.move_to(new_dot_pos)

            new_tangent_line = axes.plot(tangent_line(x_val), color=GREEN)

            self.play(
                UpdateFromFunc(dot, lambda d: d.move_to(axes.c2p(x_val, np.sin(x_val)))),
                Transform(tangent_graph, new_tangent_line),
                run_time=0.05
            )

        self.wait(1)
