from manim import *

# ── Paleta inspirada nos slides UTFPR ──────────────────────────────────────
VINHO   = "#6B1A3A"
LARANJA = "#E07B00"
ROSA    = "#C0006B"
AZUL    = "#1A5CA8"
CINZA   = "#EEEEEE"


def titulo_slide(texto):
    """Barra de título estilo UTFPR."""
    barra = Rectangle(width=14, height=0.7, fill_color=VINHO,
                      fill_opacity=1, stroke_width=0).to_edge(UP, buff=0)
    label = Text(texto, font_size=24, color=WHITE).move_to(barra)
    return VGroup(barra, label)


# ══════════════════════════════════════════════════════════════════════════════
class HeronDeducao(Scene):
    """Dedução completa da Fórmula de Heron."""

    # ── helpers ──────────────────────────────────────────────────────────────
    def play_title(self):
        t = titulo_slide("Área do Triângulo:  Fórmula de Heron")
        self.play(FadeIn(t))
        self.title = t
        return t

    def clear_body(self, *mobjects):
        self.play(*[FadeOut(m) for m in mobjects])

    # ── Cena 1 : triângulo + Pitágoras ───────────────────────────────────────
    def cena1(self):
        # --- triângulo ---
        B = np.array([-3.0, -1.5, 0])
        C = np.array([ 3.0, -1.5, 0])
        A = np.array([-0.5,  1.5, 0])
        H = np.array([-0.5, -1.5, 0])   # pé da altura

        tri = Polygon(B, C, A, color=WHITE, stroke_width=2,
                      fill_color=ROSA, fill_opacity=0.25)

        altura = DashedLine(A, H, color=ROSA)

        lbl_A = MathTex("A", font_size=30).next_to(A, UP, buff=0.1)
        lbl_B = MathTex("B", font_size=30).next_to(B, LEFT, buff=0.1)
        lbl_C = MathTex("C", font_size=30).next_to(C, RIGHT, buff=0.1)
        lbl_H = MathTex("H", font_size=28).next_to(H, DOWN+RIGHT*0.3, buff=0.05)

        mid_AB = (A + B) / 2
        mid_AC = (A + C) / 2
        mid_BH = (B + H) / 2
        mid_HC = (H + C) / 2

        lbl_c = MathTex("c", font_size=28, color=AZUL).next_to(mid_AB, LEFT, buff=0.15)
        lbl_b = MathTex("b", font_size=28, color=AZUL).next_to(mid_AC, RIGHT, buff=0.15)
        lbl_h = MathTex("h", font_size=28, color=ROSA).next_to((A+H)/2, RIGHT, buff=0.1)
        lbl_x = MathTex("x", font_size=26).next_to(mid_BH, DOWN, buff=0.1)
        lbl_ax = MathTex("a-x", font_size=26).next_to(mid_HC, DOWN, buff=0.1)
        lbl_a  = MathTex("a",   font_size=26).next_to((B+C)/2, DOWN, buff=0.3)

        angulo = RightAngle(Line(H, A), Line(H, C), length=0.18, color=WHITE)

        # --- texto introdutório ---
        intro = Tex(
            r"Aplicando Pitágoras nos triângulos retângulos $AHB$ e $AHC$",
            font_size=28
        ).to_edge(LEFT, buff=0.5).shift(UP*0.5)

        fig = VGroup(tri, altura, angulo,
                     lbl_A, lbl_B, lbl_C, lbl_H,
                     lbl_c, lbl_b, lbl_h, lbl_x, lbl_ax, lbl_a)

        self.play(Write(intro))
        self.play(Create(tri), run_time=1.2)
        self.play(Create(altura), Create(angulo))
        self.play(LaggedStart(
            FadeIn(lbl_A), FadeIn(lbl_B), FadeIn(lbl_C), FadeIn(lbl_H),
            FadeIn(lbl_c), FadeIn(lbl_b), FadeIn(lbl_h),
            FadeIn(lbl_x), FadeIn(lbl_ax), FadeIn(lbl_a),
            lag_ratio=0.15))
        self.wait(1)

        # --- equações Pitágoras ---
        eq_I = MathTex(
            r"\text{(I)}\quad c^2 = h^2 + x^2",
            r"\;\Rightarrow\; h^2 = c^2 - x^2",
            font_size=30
        ).next_to(intro, DOWN, buff=0.4).to_edge(LEFT, buff=0.5)

        eq_II = MathTex(
            r"\text{(II)}\quad b^2 = h^2 + (a-x)^2",
            font_size=30
        ).next_to(eq_I, DOWN, buff=0.25).to_edge(LEFT, buff=0.5)

        sub_label = Tex(r"Substituindo (I) em (II):", font_size=28)\
            .next_to(eq_II, DOWN, buff=0.35).to_edge(LEFT, buff=0.5)

        eq_sub = MathTex(
            r"b^2 &= c^2 - x^2 + (a-x)^2 \\",
            r"    &= c^2 - x^2 + a^2 - 2ax + x^2 \\",
            r"\Rightarrow\; x &= \frac{a^2 - b^2 + c^2}{2a}",
            r"\quad \text{(III)}",
            font_size=30
        ).next_to(sub_label, DOWN, buff=0.2).shift(RIGHT*0.5)

        self.play(Write(eq_I))
        self.wait(0.5)
        self.play(Write(eq_II))
        self.wait(0.5)
        self.play(Write(sub_label))
        self.play(Write(eq_sub), run_time=2)
        self.wait(2)

        self.clear_body(intro, fig, eq_I, eq_II, sub_label, eq_sub)

    # ── Cena 2 : h² em função de a,b,c ───────────────────────────────────────
    def cena2(self):
        intro = Tex(r"Substituindo (III) em (I), veja que", font_size=30)\
            .to_edge(LEFT, buff=0.7).shift(UP*2.5)

        eq1 = MathTex(
            r"h^2 = c^2 - \left(\frac{a^2-b^2+c^2}{2a}\right)^{\!2}",
            font_size=34
        ).next_to(intro, DOWN, buff=0.5).shift(RIGHT*0.5)

        eq2 = MathTex(
            r"\Longrightarrow\; h^2 = \frac{4a^2c^2 - (a^2-b^2+c^2)^2}{4a^2}",
            r"\quad \text{(IV)}",
            font_size=32
        ).next_to(eq1, DOWN, buff=0.5)

        sendo = Tex(r"Sendo $A = \dfrac{BC \cdot h}{2}$, então,", font_size=30)\
            .next_to(eq2, DOWN, buff=0.6).to_edge(LEFT, buff=0.7)

        eq_A2 = MathTex(
            r"A^2 = \frac{a^2 \cdot h^2}{4} \quad \text{(V)}",
            font_size=34
        ).next_to(sendo, DOWN, buff=0.4).shift(RIGHT*0.5)

        self.play(Write(intro))
        self.play(Write(eq1), run_time=1.5)
        self.wait(0.5)
        self.play(Write(eq2), run_time=1.5)
        self.wait(0.5)
        self.play(Write(sendo))
        self.play(Write(eq_A2))
        self.wait(2)

        self.clear_body(intro, eq1, eq2, sendo, eq_A2)

    # ── Cena 3 : expansão de A² ───────────────────────────────────────────────
    def cena3(self):
        intro = Tex(r"Substituindo (V) em (IV), obtemos:", font_size=30)\
            .to_edge(LEFT, buff=0.7).shift(UP*3)

        steps = MathTex(
            r"A^2 &= \frac{a^2 \cdot h^2}{4} \\[6pt]",
            r"&= \frac{a^2 \cdot \bigl(4a^2c^2 - (a^2-b^2+c^2)^2\bigr)}{16a^2} \\[6pt]",
            r"&= \frac{(2ac)^2 - (a^2-b^2+c^2)^2}{16} \\[6pt]",
            r"&= \frac{\bigl[2ac+(a^2-b^2+c^2)\bigr]\cdot\bigl[2ac-(a^2-b^2+c^2)\bigr]}{16} \\[6pt]",
            r"&= \frac{\bigl[(a^2+2ac+c^2)-b^2\bigr]\cdot\bigl[-(a^2-2ac+c^2)+b^2\bigr]}{16}",
            font_size=28
        ).next_to(intro, DOWN, buff=0.4).shift(RIGHT*0.3)

        # destaque diferença de quadrados
        rect_dq = SurroundingRectangle(steps[2], color=LARANJA, buff=0.08)
        lbl_dq  = Tex(r"diferença de quadrados", font_size=22, color=LARANJA)\
            .next_to(rect_dq, RIGHT, buff=0.1)

        self.play(Write(intro))
        for s in steps:
            self.play(Write(s), run_time=1.2)
            self.wait(0.3)
        self.play(Create(rect_dq), FadeIn(lbl_dq))
        self.wait(2)

        self.clear_body(intro, steps, rect_dq, lbl_dq)

    # ── Cena 4 : fatoração e semiperímetro ────────────────────────────────────
    def cena4(self):
        fat = MathTex(
            r"A^2 &= \frac{(a+c)^2 - b^2}{?} \cdot \frac{b^2 - (a-c)^2}{?} \\[8pt]",
            r"&= \frac{(a+c-b)(a+c+b)}{4} \cdot \frac{(-a+c+b)(a-c+b)}{4} \\[8pt]",
            r"&= \frac{a+c-b}{2}\cdot\frac{a+c+b}{2}\cdot"
            r"\frac{-a+c+b}{2}\cdot\frac{a-c+b}{2}",
            font_size=30
        ).shift(UP*1.2)

        # Reescrever com p
        semi = Tex(
            r"Seja $p$ o semiperímetro, isto é, "
            r"$p = \dfrac{a+b+c}{2}$, então,",
            font_size=30
        ).next_to(fat, DOWN, buff=0.5).to_edge(LEFT, buff=0.7)

        # p-a, p-b, p-c
        ident = MathTex(
            r"\frac{a+b+c}{2} - a &= p - a \\",
            r"\frac{a+b+c}{2} - b &= p - b \\",
            r"\frac{a+b+c}{2} - c &= p - c",
            font_size=28
        ).next_to(semi, DOWN, buff=0.3).shift(RIGHT)

        result = MathTex(
            r"S^2 = p\,(p-a)\,(p-b)\,(p-c)",
            font_size=38, color=LARANJA
        ).next_to(ident, DOWN, buff=0.5)

        for m in [fat, semi, ident]:
            self.play(Write(m), run_time=1.5)
            self.wait(0.4)
        self.play(Write(result), run_time=1.2)
        self.wait(1.5)

        self.clear_body(fat, semi, ident, result)

    # ── Cena 5 : fórmula final ────────────────────────────────────────────────
    def cena5(self):
        box = RoundedRectangle(width=8, height=2.2, corner_radius=0.2,
                               color=AZUL, fill_color=AZUL, fill_opacity=0.15,
                               stroke_width=2)

        formula = MathTex(
            r"A = \sqrt{p(p-a)(p-b)(p-c)}",
            font_size=52
        )
        formula_group = VGroup(box, formula).arrange(ORIGIN)

        bullet = Tex(
            r"\textbullet\; Esta fórmula permite calcular a área de qualquer triângulo\\",
            r"\phantom{\textbullet\;} conhecendo apenas as medidas de seus três lados.",
            font_size=28
        ).next_to(formula_group, DOWN, buff=0.7).to_edge(LEFT, buff=1)

        self.play(DrawBorderThenFill(box), Write(formula), run_time=1.5)
        self.wait(0.5)
        self.play(Write(bullet), run_time=1.5)
        self.wait(3)

    # ── construct ─────────────────────────────────────────────────────────────
    def construct(self):
        self.play_title()
        self.wait(0.3)
        self.cena1()
        self.cena2()
        self.cena3()
        self.cena4()
        self.cena5()
        self.wait(1)