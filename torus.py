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
        # Top View
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=1.5)
        self.wait(5)
        # Front View
        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, run_time=1.5)
        self.wait(5)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=1.5)

        equation = MathTex(
            r"\vec{r}(s,t) = ((a + b \cos t) \cos s, (a + b \cos t) \sin s, b \sin t)"
        ).scale(0.75).to_corner(UL)
        self.play(FadeOut(axes), FadeOut(labels), FadeOut(torus))
        self.wait(1.5)
        self.play(Write(equation))
        self.wait(10)
        partial_s = MathTex(
            r"\frac{\partial \vec{r}}{\partial s} = (- (a + b \cos t) \sin s, (a + b \cos t) \cos s, 0)").scale(0.75).next_to(equation, DOWN).align_to(equation, LEFT)
        partial_t = MathTex(
            r"\frac{\partial \vec{r}}{\partial t} = ((-b \cos s \sin t), (-b \sin s \sin t), (b \cos t))").scale(0.75).next_to(partial_s, DOWN).align_to(equation, LEFT)
        self.play(Write(partial_s))
        self.wait(5)
        self.play(Write(partial_t))
        self.wait(5)
        cross = MathTex(
            r"\frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} = \begin{vmatrix} - (a + b \cos t) \sin s & (a + b \cos t) \cos s & 0 \\ -b \cos s \sin t & -b \sin s \sin t & b \cos t \end{vmatrix}").scale(0.75).next_to(partial_t, DOWN).align_to(equation, LEFT)
        self.play(Write(cross))
        self.wait(10)
        
        step1 = MathTex(r"\frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} = (b (a+b\cos t)\cos s \cos t, b (a+b\cos t) \sin s \cos t, b (a+b\cos t) \sin{s}^2 \sin t + b (a+b\cos t) \cos{s}^2 \sin t)").scale(0.5).next_to(cross, DOWN).align_to(equation, LEFT)
        step2 = MathTex(r"\frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} = (b (a+b\cos t)\cos s \cos t, b (a+b\cos t) \sin s \cos t, b (a+b\cos t)( \sin{s}^2 \sin t + \cos{s}^2 \sin t))").scale(0.75).next_to(cross, DOWN).align_to(equation, LEFT)
        step3 = MathTex(r"\frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} = (b (a+b\cos t)\cos s \cos t, b (a+b\cos t) \sin s \cos t, b (a+b\cos t)(\sin t (\sin{s}^2 + \cos{s}^2)))").scale(0.75).next_to(cross, DOWN).align_to(equation, LEFT)
        step4 = MathTex(r"\frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} = (b (a+b\cos t)\cos s \cos t, b (a+b\cos t) \sin s \cos t, b (a+b\cos t)\sin t)").scale(0.75).next_to(cross, DOWN).align_to(equation, LEFT)
        step5 = MathTex(r"\frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} = b(a+b\cos t)(\cos s \cos t, \sin s \cos t, \sin t)").scale(0.75).next_to(cross, DOWN).align_to(equation, LEFT)
        step6 = MathTex(r"\| \frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} \| = b(a+b\cos t)\sqrt{(\cos s \cos t)^2 + (\sin s \cos t)^2 + (\sin t)^2}").scale(0.75).next_to(cross, DOWN).align_to(equation, LEFT)
        step7 = MathTex(r"\| \frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} \| = b(a+b\cos t)\sqrt{\cos{t}^2 (\cos{s}^2 + \sin{s}^2) + \sin{t}^2}").scale(0.75).next_to(cross, DOWN).align_to(equation, LEFT)
        step8 = MathTex(r"\| \frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} \| = b(a+b\cos t)\sqrt{\cos{t}^2 + \sin{t}^2}").scale(0.75).next_to(cross, DOWN).align_to(equation, LEFT)
        step9 = MathTex(r"\| \frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} \| = b(a+b\cos t)").scale(0.75).next_to(cross, DOWN).align_to(equation, LEFT)
        step10 = MathTex(r"\| \frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} \| = a b + b^2 \cos t").scale(0.75).next_to(cross, DOWN).align_to(equation, LEFT)
        
        self.play(Write(step1))
        self.wait(1)
        self.play(Transform(step1, step2))
        self.wait(1)
        self.play(Transform(step1, step3))
        self.wait(1)
        self.play(Transform(step1, step4))
        self.wait(1)
        self.play(Transform(step1, step5))
        self.wait(5)
        self.play(Transform(step1, step6))
        self.wait(1)
        self.play(Transform(step1, step7))
        self.wait(1)
        self.play(Transform(step1, step8))
        self.wait(1)
        self.play(Transform(step1, step9))
        self.wait(1)
        self.play(Transform(step1, step10))
        self.wait(5)
        
        self.play(FadeOut(equation), FadeOut(partial_s), FadeOut(partial_t), FadeOut(cross), FadeOut(step1))
        self.wait(5)
        
        dA = MathTex(r"dA = \| \frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} \| ds dt").scale(0.75).to_corner(UL)
        dA2 = MathTex(r"dA = (a b + b^2 \cos t) ds dt").scale(0.75).to_corner(UL)
        self.play(Write(dA))
        self.wait(1)
        self.play(Transform(dA, dA2))
        self.wait(5)
        
        formula = MathTex(r"\iint_{SA} \| \frac{\partial \vec{r}}{\partial s} \times \frac{\partial \vec{r}}{\partial t} \| ds dt = \iint (a b + b^2 \cos t) ds dt").scale(0.75).to_corner(UL)
        self.play(Transform(dA, formula))
        int1 = MathTex(r"=\int_{0}^{2\pi} \int_{0}^{2\pi} (a b + b^2 \cos t) ds dt").scale(0.75).next_to(dA, DOWN).align_to(dA, LEFT)
        int2 = MathTex(r"=\int_{0}^{2\pi} [a b s + b^2 \cos t s]_{0}^{2\pi} dt").scale(0.75).next_to(int1, DOWN).align_to(dA, LEFT)
        int3 = MathTex(r"=\int_{0}^{2\pi} (2\pi a b + 2\pi b^2 \cos t - (0) a b - (0) b^2 \cos t) dt").scale(0.75).next_to(int1, DOWN).align_to(dA, LEFT)
        int4 = MathTex(r"=\int_{0}^{2\pi} (2\pi a b + 2\pi b^2 \cos t) dt").scale(0.75).next_to(int1, DOWN).align_to(dA, LEFT)
        int5 = MathTex(r"=2\pi[a b t - b^2 \sin t]_{0}^{2\pi}").scale(0.75).next_to(int2, DOWN).align_to(dA, LEFT)
        int6 = MathTex(r"=2\pi[2\pi a b  - b^2 \sin (2\pi) - (0) a b + b^2 \sin (0)]").scale(0.75).next_to(int2, DOWN).align_to(dA, LEFT)
        int7 = MathTex(r"=2\pi[2\pi a b]").scale(0.75).next_to(int2, DOWN).align_to(dA, LEFT)
        result = MathTex(r"SA=4\pi^2 a b").scale(0.75).next_to(int5, DOWN).align_to(dA, LEFT)
        
        self.play(Write(int1))
        self.wait(1)
        self.play(Write(int2))
        self.wait(1)
        self.play(Transform(int2, int3))
        self.wait(1)
        self.play(Transform(int2, int4))
        self.wait(1)
        self.play(Write(int5))
        self.wait(1)
        self.play(Transform(int5, int6))
        self.wait(1)
        self.play(Transform(int5, int7))
        self.wait(1)
        self.play(Write(result))
        self.wait(1)
        self.play(result.animate.scale(3).move_to(ORIGIN), FadeOut(dA), FadeOut(int1), FadeOut(int2), FadeOut(int5))
        self.wait(5)