from manim import *


class Torus(Scene):
    def construct(self):
        b = 2
        a = 6

        axes = Axes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            x_length=10,
            y_length=10,
        )
        
        x_label = axes.get_x_axis_label("y")
        y_label = axes.get_y_axis_label("z")

        circle = Circle(
            radius=1,
            fill_opacity=0.5,
            color=BLUE
        ).shift(RIGHT * 3)  

        line2 = Line(start=axes.c2p(0, 0), end=axes.c2p(a, 0), color=RED)
        line2_label = MathTex("a").next_to(line2, buff=0.7).set_color(RED)    
        line = Line(start=axes.c2p(a, 0), end=axes.c2p(a + b*np.cos(PI/4), b*np.sin(PI/4)), color=BLUE)
        line_label = MathTex("b").next_to(line, buff=0.7).set_color(BLUE)
        x_axis = Line(start=axes.c2p(-10, 0), end=axes.c2p(10, 0), color=None)
        def get_angle():
            angle = np.arctan2(line.get_end()[1] - line.get_start()[1], line.get_end()[0] - line.get_start()[0])
            if angle >= 0:
                return angle
            else: 
                return angle + 2 * PI
         
        angle_arc = always_redraw(lambda: Angle(
            x_axis, line,
            radius=0.3,
            color=BLUE
        ))
        
        angle_label = always_redraw(lambda:MathTex("t").next_to(line, RIGHT, buff=0.1).set_color(BLUE))
        self.camera.frame_height *= 1.35
        self.camera.frame_width *= 1.35
        self.add(axes, x_label, y_label)

        self.add(circle)
        self.play(Write(line2), Write(line2_label))
        self.wait(0.2)
        self.play(Write(line), Write(line_label))
        self.wait(1)
        self.play(FadeOut(line_label), FadeOut(line2_label))
        self.remove(line_label, line2_label)
        self.play(Write(angle_arc), Write(angle_label))

        # Bring the line, angle, and labels to the front
        self.bring_to_front(line, angle_arc, angle_label)

        # Rotate the line around the circle
        self.play(Rotating(line, radians=7*PI/4, about_point=axes.c2p(a, 0)), run_time=6, rate_func=smooth)
        self.wait(1)

        text = MathTex(r"0 \leq t \leq 2\pi").to_corner(UL)

        self.play(Transform(angle_label, text))
        self.remove(angle_label)
        self.add(text)
        self.wait(2)
        self.play(Rotating(line, radians=PI / 3, about_point=axes.c2p(a, 0)), run_time=2, rate_func=smooth)
        
        end_point = line.get_end()
        x_val = end_point[0]

        perpendicular_point = axes.c2p(x_val+((a+1)/2), 0)

        perpendicular_line = Line(end_point, perpendicular_point, color=GREEN)

        self.play(Write(perpendicular_line), FadeOut(line2))
        yline = Line(axes.c2p(a, 0), perpendicular_point, color=GREEN)
        self.play(Write(yline))
        self.play(FadeOut(text, axes, circle, x_label, y_label, angle_arc))
        self.remove(angle_arc)
        tr = VGroup(yline, perpendicular_line,line)
        self.wait(2)
        # Label "a" under the yline
        self.play(tr.animate.scale(3).shift(LEFT * 3))
        label_a = MathTex("b \cos t").next_to(tr, DOWN, buff=0.3)
        label_b = MathTex("z = b \sin t").next_to(tr, RIGHT, buff=0.3)
        self.play(Write(label_a))
        self.play(Write(label_b))
        self.wait(3)

        