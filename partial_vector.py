from manim import *


class Partial(ThreeDScene):
    def construct(self):
        a = 4
        def f(s, t):
            return np.array([a*np.cos(t)*np.cos(s),a*np.cos(t)*np.sin(s),a*np.sin(t)])

        axes = ThreeDAxes(
            x_range=[-8, 8],
            y_range=[-8, 8],
            z_range=[-8, 8],
            x_length=8,
            y_length=8,
            z_length=8
        )

        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        z_label = axes.get_z_axis_label("z")

        sphere = Surface(
            lambda u, v: axes.c2p(*f(u, v)),
            u_range=[0, 2 * PI],
            v_range=[-PI/2, PI/2],
            stroke_width=0,
            fill_opacity=0.25,
        )
        vec0 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=axes.c2p(*f(PI/3, PI/3)),
            resolution=8
        )
        label0 = MathTex(r"\vec{r}(s,t)").next_to(vec0, UP).scale(0.75)
        vecds = Arrow3D(
            start=np.array([0, 0, 0]),
            end=axes.c2p(*f(PI/3 + 0.5, PI/3)),
            resolution=8
        )
        labelds = MathTex(r"\vec{r}(s+ds,t)").next_to(vecds, UP).scale(0.75)
        vecdt = Arrow3D(
            start=np.array([0, 0, 0]),
            end=axes.c2p(*f(PI/3, PI/3 + 0.5)),
            resolution=8
        )
        labeldt = MathTex(r"\vec{r}(s,t+dt)").next_to(vecdt, UP).scale(0.75)
        
        partialds = Arrow3D(
            start=axes.c2p(*f(PI/3, PI/3)),
            end=axes.c2p(*f(PI/3 + 0.5, PI/3)),
            resolution=8,
            color=RED
        )
        partialdt = Arrow3D(
            start=axes.c2p(*f(PI/3, PI/3)),
            end=axes.c2p(*f(PI/3, PI/3 + 0.5)),
            resolution=8,
            color=BLUE
        )
        
        labelpartialds = MathTex(r"\frac{\partial \vec{r}}{\partial s} ds").next_to(partialds, LEFT).scale(0.75)
        labelpartialdt = MathTex(r"\frac{\partial \vec{r}}{\partial t} dt").next_to(partialdt, RIGHT).scale(0.75)
        
        poly = Polygon(axes.c2p(*f(PI/3, PI/3)), axes.c2p(*f(PI/3 + 0.5, PI/3)), axes.c2p(*f(PI/3 + 0.5, PI/3)) + (axes.c2p(*f(PI/3, PI/3 + 0.5))-axes.c2p(*f(PI/3, PI/3))), axes.c2p(*f(PI/3, PI/3 + 0.5)), stroke_width=1, stroke_color=WHITE, fill_opacity=0.5, color=GREEN)
        labelpoly = MathTex(r"dA").next_to(poly, UP).scale(0.75)

        self.move_camera(zoom=0.5)
        self.add(axes, x_label, y_label, z_label)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, zoom=0.75, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.15)

        self.play(Write(sphere))
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=1.5)

        self.play(Write(vec0), Write(label0))
        self.wait(3)
        self.play(FadeOut(label0))
        self.play(Write(vecds), Write(labelds), Write(vecdt), Write(labeldt))
        self.wait(3)
        self.play(FadeOut(labelds), FadeOut(labeldt))
        self.play(Write(partialds), Write(partialdt), Write(labelpartialds), Write(labelpartialdt))
        self.wait(3)
        self.play(FadeOut(labelpartialds), FadeOut(labelpartialdt))
        self.play(Write(poly), Write(labelpoly))
        self.wait(5)
        group = VGroup(partialds, partialdt, poly)
        self.play(FadeOut(vec0), FadeOut(vecds), FadeOut(vecdt), FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(z_label), FadeOut(sphere), FadeOut(labelpoly), run_time=1.5)
        self.play(group.animate.scale(3).shift(DOWN))
        da = MathTex(r"dA").next_to(group, LEFT)
        ds = MathTex(r"\frac{\partial\vec{r}}{\partial s}ds").next_to(group, UP)
        dt = MathTex(r"\frac{\partial\vec{r}}{\partial t}dt").next_to(group, RIGHT)
        labelpoly2 = MathTex(r"dA = \| \frac{\partial\vec{r}}{\partial s}ds \times \frac{\partial\vec{r}}{\partial t}dt \|").next_to(group, LEFT * 2)
        labelpoly3 = MathTex(r"dA = \| \frac{\partial\vec{r}}{\partial s} \times \frac{\partial\vec{r}}{\partial t} \| ds dt").next_to(group, LEFT * 2)
        formula = MathTex(r"SA = \iint_{SA} \| \frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} \| ds dt")
        
        self.play(Write(ds), Write(dt), Write(da))
        self.wait(3)
        self.play(Transform(da, labelpoly2))
        self.wait(3)
        self.play(Transform(da, labelpoly3))
        self.wait(3)
        self.play(FadeOut(group), FadeOut(ds), FadeOut(dt), FadeOut(da))
        self.play(Write(formula))
        self.wait(3)
        self.play(formula.animate.scale(3).move_to(ORIGIN))
        self.wait(5)

        


