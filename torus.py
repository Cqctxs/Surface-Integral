from manim import *


class Torus(ThreeDScene):
    def construct(self):
        def f(s, t):
            a = 2
            b = 6
            return np.array([((b+a*np.cos(s))*np.cos(t)), ((b+a*np.cos(s))*np.sin(t)), a*np.sin(s)])
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
            v_range=[0, 2 * PI],
        )

        self.move_camera(zoom=0.5)
        self.play(Write(axes), Write(labels))
        self.wait(0.5)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=0.75, run_time=1.5)
        self.play(Write(torus))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        #Top View
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=1.5)
        self.wait(5)
        #Front View
        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, run_time=1.5)
        self.wait(5)
        equation = MathTex(r"\vec{r}(s,t) = ((a + b \cos t) \cos s, y = (a + b \cos t) \sin s, b \sin t").scale(0.75).to_corner(UL)
        self.play(Write(equation))
        self.play(FadeOut(axes), FadeOut(labels), FadeOut(torus))
        self.wait(5)
        partial_s = MathTex(r"\frac{\partial \vec{r}}{\partial s} = (- (a + b \cos t) \sin s, (a + b \cos t) \cos s, 0)").scale(0.75).next_to(equation, DOWN)
        partial_t = MathTex(r"\frac{\partial \vec{r}}{\partial t} = (a \cos s - b \cos s \sin t, a \sin s - b \sin s \sin t, b \cos t)").scale(0.75).next_to(partial_s, DOWN)
        self.play(Write(partial_s))
        self.wait(5)
        self.play(Write(partial_t))
        self.wait(5)
        cross = MathTex(r"\frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} = \begin{vmatrix} - (a + b \cos t) \sin s, (a + b \cos t) \cos s, 0\\a \cos s - b \cos s \sin t, a \sin s - b \sin s \sin t, b \cos t").scale(0.75).next_to(partial_t, DOWN)
        self.play(Write(cross))
        self.wait(5)        




#torus = Surface(f, color=RED, s_range=[0, 2 * PI], t_range=[0, 2 * PI])