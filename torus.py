from manim import *


class Sphere(ThreeDScene):
    def construct(self):
        def f(s, t):
            a = 2
            b = 6
            return np.array([((b+a*np.cos(s))*np.cos(t)), ((b+a*np.cos(s))*np.sin(t)), a*np.sin(s)])
        axes = ThreeDAxes(x_range=[-10, 10], y_range=[-10, 10], z_range=[-10, 10])
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")
        torus = Surface(
            lambda u, v: axes.c2p(*f(u, v)),
            u_range=[0, 2 * PI],
            v_range=[0, 2 * PI],
        )

        # zoom out so we see the axes
        self.set_camera_orientation(zoom=0.5)
        self.play(Write(axes), Write(labels))
        self.wait(0.5)

        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)
        self.play(Write(torus))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)




#torus = Surface(f, color=RED, s_range=[0, 2 * PI], t_range=[0, 2 * PI])