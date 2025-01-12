from manim import *


class Torus(Scene):
    def construct(self):
        a = 4

        axes = Axes(
            x_range=[-8, 8],
            y_range=[-8, 8],
            x_length=8,
            y_length=8,
        )
        
        x_label = axes.get_x_axis_label("y")
        y_label = axes.get_y_axis_label("z")

        circle = Circle(
            radius=2,
            fill_opacity=0.5,
            color=BLUE
        )

        line = Line(start=axes.c2p(0, 0), end=axes.c2p(a*np.cos(PI/4), a*np.sin(PI/4)), color=RED)
        line_label = MathTex("a").next_to(line, buff=0.7).set_color(RED)        
        def get_angle():
            angle = np.arctan2(line.get_end()[1] - line.get_start()[1], line.get_end()[0] - line.get_start()[0])
            return angle
         
        angle_arc = always_redraw(lambda: Arc(
            start_angle=0,
            angle=get_angle(),
            radius=0.5,
            color=RED
        ))
        
        angle_label = always_redraw(lambda:MathTex("t").next_to(line, RIGHT, buff=0.1).set_color(RED))
        self.camera.frame_height *= 1.35
        self.camera.frame_width *= 1.35
        self.add(axes, x_label, y_label)

        self.add(circle)
        self.play(Write(line), Write(line_label))
        self.wait(1)
        self.play(FadeOut(line_label))
        self.remove(line_label)
        self.play(Write(angle_arc), Write(angle_label))

        # Bring the line, angle, and labels to the front
        self.bring_to_front(line, angle_arc, angle_label)

        # Rotate the line around the circle
        self.play(Rotating(line, radians=PI / 4, about_point=axes.c2p(0, 0)), run_time=2, rate_func=smooth)
        self.play(Rotating(line, radians=-PI, about_point=axes.c2p(0, 0)), run_time=4, rate_func=smooth)
        self.play(Rotating(line, radians=PI / 2, about_point=axes.c2p(0, 0)), run_time=2, rate_func=smooth)
        self.wait(1)

        text = MathTex(r"-\frac{\pi}{2} \leq t \leq \frac{\pi}{2}").to_corner(UL)

        self.play(Transform(angle_label, text))
        self.remove(angle_label)
        self.add(text)
        self.play(Rotating(line, radians=PI / 3, about_point=axes.c2p(0, 0)), run_time=2, rate_func=smooth)
        
        end_point = line.get_end()
        x_val = end_point[0]

        perpendicular_point = axes.c2p(x_val+1, 0)

        perpendicular_line = Line(end_point, perpendicular_point, color=GREEN)

        self.play(Write(perpendicular_line))
        yline = Line(axes.c2p(0, 0), perpendicular_point, color=GREEN)
        self.play(Write(yline))
        self.play(FadeOut(text, axes, circle, x_label, y_label))
        tr = VGroup(yline, perpendicular_line,line,angle_arc)
        self.wait(2)
        # Label "a" under the yline
        self.play(tr.animate.scale(3))
        label_a = MathTex("a \cos t").next_to(tr, DOWN, buff=0.3)
        label_b = MathTex("z = a \sin t").next_to(tr, RIGHT, buff=0.3)
        self.remove(angle_arc)
        self.play(Write(label_a))
        self.play(Write(label_b))
        self.wait(3)

        