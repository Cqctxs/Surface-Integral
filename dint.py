from manim import *

class DoubleIntegralScene(Scene):
    def construct(self):
        integral = MathTex(r"\int\int_A f(x, y) \, dA")
        integral_expr = MathTex(r"\int_{x_1}^{x_2} \int_{y_1}^{y_2} f(x, y) \, dy \, dx")
        integral_expr.to_edge(UP)

        # Create the axes in the first quadrant
        axes = Axes(
            x_range=[0, 6],  # Positive x-axis, from 0 to 6
            y_range=[0, 4],  # Positive y-axis, from 0 to 4
            axis_config={"color": WHITE, "include_tip": False}
        )

        # Create labels for x and y axes
        x_label = MathTex(r"x").next_to(axes.x_axis.get_right(), DOWN)
        y_label = MathTex(r"y").next_to(axes.y_axis.get_top(), LEFT)

        # Add everything to the scene
        self.play(Write(integral))
        self.wait(2)
        self.play(Transform(integral, integral_expr))
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Create custom labels for x_1 and x_2 on the x-axis
        x1_label = MathTex(r"x_1").next_to(axes.c2p(1, 0), DOWN)
        x2_label = MathTex(r"x_2").next_to(axes.c2p(4, 0), DOWN)

        # Create custom labels for x_1 and x_2 on the x-axis
        y1_label = MathTex(r"y_1").next_to(axes.c2p(0, 1), LEFT)
        y2_label = MathTex(r"y_2").next_to(axes.c2p(0, 3), LEFT)
        
        # Add the custom x labels to the scene
        self.play(Write(x1_label), Write(x2_label), Write(y1_label), Write(y2_label))

        self.wait(3)

        line = Line(axes.c2p(1, 1), axes.c2p(1, 3), color=RED)
        box = Rectangle(width = 1.05, height= 1.6, fill_opacity=0)
        box.shift(UP * 2.8)
        box.shift(LEFT * 0.85)
        self.play(Create(box))
        self.play(Create(line), run_time=1)
        self.wait(2)
        self.play(box.animate.shift(LEFT * 1.1))
        self.wait(2)
        rectangle = Rectangle(width = 0, height= 3, fill_opacity=1)
        rectangle.move_to(axes.c2p(1, 2))
        self.play(Create(rectangle))
        rectangl = Rectangle(width = 6, height= 3, fill_opacity=1)
        rectangl.move_to(axes.c2p(2.5, 2))
        self.play(Transform(rectangle, rectangl))
        self.wait(2)
