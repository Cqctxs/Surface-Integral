from manim import *


class Sphere(ThreeDScene):
    def construct(self):
        a = 2
        def f(s, t):
            return np.array([a*np.cos(t)*np.cos(s),a*np.cos(t)*np.sin(s),a*np.sin(t)])

        axes = ThreeDAxes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            z_range=[-10, 10],
            x_length=10,
            y_length=10,
            z_length=10
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")
        sphere = Surface(
            lambda u, v: axes.c2p(*f(u, v)),
            u_range=[0, 2 * PI],
            v_range=[-PI/2, PI/2],
            checkerboard_colors=[BLUE, BLUE],
            stroke_width=0
        )

        # Define the radius line
        line = Line3D(start=axes.c2p(0, 0, 0), end=axes.c2p(a, 0, 0), color=RED)
        label = MathTex("a").next_to(line, UP).set_color(RED_A)

        self.set_camera_orientation(zoom=0.5)
        self.play(Write(axes), Write(labels))
        self.wait(0.5)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)
        self.play(Write(sphere))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(0.5)
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES, zoom=1, run_time=1.5)
        self.play(AnimationGroup(Write(line), Write(label)))
        self.bring_to_front(line, label)
        self.wait(5)