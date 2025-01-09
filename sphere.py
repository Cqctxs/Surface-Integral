from manim import *


class Sphere(ThreeDScene):
    def construct(self):
        def f(s, t):
            a = 2
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
        torus = Surface(
            lambda u, v: axes.c2p(*f(u, v)),
            u_range=[0, 2 * PI],
            v_range=[-PI/2, PI/2],
            fill_opacity=0,
        )

        # zoom out so we see the axes
        self.set_camera_orientation(zoom=0.5)
        self.play(Write(axes), Write(labels))
        self.wait(0.5)

        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)
        self.play(Write(torus))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)