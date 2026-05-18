from manim import *

# ── Paleta inspirada nos slides UTFPR ──────────────────────────────────────
VINHO   = "#6B1A3A"
LARANJA = "#E07B00"
ROSA    = "#C0006B"
AZUL    = "#1A5CA8"
CINZA   = "#EEEEEE"


# Gera a barra roxa com o título no topo da tela
def titulo_slide(texto):
    """Barra de título estilo UTFPR."""
    barra = Rectangle(width=14, height=0.7, fill_color=VINHO,
                      fill_opacity=1, stroke_width=0).to_edge(UP, buff=0)
    label = Text(texto, font_size=24, color=WHITE).move_to(barra)
    return VGroup(barra, label)


# ══════════════════════════════════════════════════════════════════════════════
class HeronDeducao(Scene):
    """Dedução completa da Fórmula de Heron."""

    # Exibe o título e guarda a referência em self.title
    def play_title(self):
        t = titulo_slide("Área do Triângulo:  Fórmula de Heron")
        self.play(FadeIn(t))
        self.title = t
        return t

    # Faz fade out em todos os objetos passados como argumento
    def clear_body(self, *mobjects):
        self.play(*[FadeOut(m) for m in mobjects])

    # Cena 1: aplica Pitágoras no triângulo para isolar x (projeção de c sobre a)
    def cena1(self):
        intro = Tex(
            r"Seja um triângulo de lados $a$, $b$, $c$ e altura $h$ relativa a $a$,\\",
            r"com $x$ a projeção de $c$ sobre $a$. Aplicando Pitágoras:",
            font_size=28
        ).to_edge(LEFT, buff=0.5).shift(UP * 2.8)

        # FIX: \quad separado em argumento próprio
        eq_I = MathTex(
            r"\text{(I)}",
            r"\quad c^2 = h^2 + x^2",
            r"\;\Rightarrow\; h^2 = c^2 - x^2",
            font_size=30
        ).next_to(intro, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)

        eq_II = MathTex(
            r"\text{(II)}",
            r"\quad b^2 = h^2 + (a - x)^2",
            font_size=30
        ).next_to(eq_I, DOWN, buff=0.35).to_edge(LEFT, buff=0.5)

        sub_label = Tex(r"Substituindo (I) em (II):", font_size=28)\
            .next_to(eq_II, DOWN, buff=0.45).to_edge(LEFT, buff=0.5)

        eq_sub = MathTex(
            r"b^2 &= c^2 - x^2 + (a - x)^2 \\",
            r"    &= c^2 - x^2 + a^2 - 2ax + x^2 \\",
            r"\Rightarrow\; x &= \frac{a^2 - b^2 + c^2}{2a}",
            r"\quad \text{(III)}",       # \quad no início de argumento: OK
            font_size=30
        ).next_to(sub_label, DOWN, buff=0.25).shift(RIGHT * 0.5)

        self.play(Write(intro))
        self.wait(0.5)
        self.play(Write(eq_I))
        self.wait(0.4)
        self.play(Write(eq_II))
        self.wait(0.4)
        self.play(Write(sub_label))
        self.play(Write(eq_sub), run_time=2)
        self.wait(2)

        self.clear_body(intro, eq_I, eq_II, sub_label, eq_sub)

    # Cena 2: substitui x (III) em h² (I) e define A² = a²h²/4
    def cena2(self):
        intro = Tex(r"Substituindo (III) em (I), veja que", font_size=30)\
            .to_edge(LEFT, buff=0.7).shift(UP * 2.5)

        eq1 = MathTex(
            r"h^2 = c^2 - \left(\frac{a^2 - b^2 + c^2}{2a}\right)^{\!2}",
            font_size=34
        ).next_to(intro, DOWN, buff=0.5).shift(RIGHT * 0.5)

        # FIX: \quad no início do segundo argumento: OK
        eq2 = MathTex(
            r"\Longrightarrow\; h^2 = \frac{4a^2c^2 - (a^2 - b^2 + c^2)^2}{4a^2}",
            r"\quad \text{(IV)}",
            font_size=32
        ).next_to(eq1, DOWN, buff=0.5)

        sendo = Tex(r"Como $A = \dfrac{a \cdot h}{2}$, então:", font_size=30)\
            .next_to(eq2, DOWN, buff=0.6).to_edge(LEFT, buff=0.7)

        # FIX: \quad no início do segundo argumento: OK
        eq_A2 = MathTex(
            r"A^2 = \frac{a^2 \cdot h^2}{4}",
            r"\quad \text{(V)}",
            font_size=34
        ).next_to(sendo, DOWN, buff=0.4).shift(RIGHT * 0.5)

        self.play(Write(intro))
        self.play(Write(eq1), run_time=1.5)
        self.wait(0.5)
        self.play(Write(eq2), run_time=1.5)
        self.wait(0.5)
        self.play(Write(sendo))
        self.play(Write(eq_A2))
        self.wait(2)

        self.clear_body(intro, eq1, eq2, sendo, eq_A2)

    # Cena 3: expande A² passo a passo usando diferença de quadrados
    def cena3(self):
        intro = Tex(r"Substituindo (IV) em (V), obtemos:", font_size=30)\
            .to_edge(LEFT, buff=0.7).shift(UP * 3)

        steps = MathTex(
            r"A^2 &= \frac{a^2 \cdot h^2}{4} \\[6pt]",
            r"&= \frac{a^2 \cdot \bigl(4a^2c^2 - (a^2 - b^2 + c^2)^2\bigr)}{16a^2} \\[6pt]",
            r"&= \frac{(2ac)^2 - (a^2 - b^2 + c^2)^2}{16} \\[6pt]",
            r"&= \frac{\bigl[2ac + (a^2 - b^2 + c^2)\bigr]\cdot"
            r"\bigl[2ac - (a^2 - b^2 + c^2)\bigr]}{16} \\[6pt]",
            r"&= \frac{\bigl[(a + c)^2 - b^2\bigr]\cdot"
            r"\bigl[b^2 - (a - c)^2\bigr]}{16}",
            font_size=28
        ).next_to(intro, DOWN, buff=0.4).shift(RIGHT * 0.3)

        # Destaque visual no passo onde aparece a diferença de quadrados
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

    # Cena 4: fatoração final, introduz o semiperímetro p e chega em A² = p(p-a)(p-b)(p-c)
    def cena4(self):
        fat = MathTex(
            r"A^2 &= \frac{(a + c - b)(a + c + b)}{4}"
            r"\cdot \frac{(b - a + c)(b + a - c)}{4} \\[8pt]",
            r"&= \frac{a + c - b}{2}\cdot\frac{a + b + c}{2}\cdot"
            r"\frac{-a + b + c}{2}\cdot\frac{a - b + c}{2}",
            font_size=30
        ).shift(UP * 1.5)

        semi = Tex(
            r"Seja $p = \dfrac{a + b + c}{2}$ o semiperímetro. Então:",
            font_size=30
        ).next_to(fat, DOWN, buff=0.5).to_edge(LEFT, buff=0.7)

        # FIX: cada parcela em argumento separado — \quad no INÍCIO de cada um
        ident = MathTex(
            r"p - a = \frac{b + c - a}{2}",
            r",\quad p - b = \frac{a + c - b}{2}",
            r",\quad p - c = \frac{a + b - c}{2}",
            font_size=28
        ).next_to(semi, DOWN, buff=0.35)

        result = MathTex(
            r"A^2 = p\,(p - a)\,(p - b)\,(p - c)",
            font_size=38, color=LARANJA
        ).next_to(ident, DOWN, buff=0.55)

        for m in [fat, semi, ident]:
            self.play(Write(m), run_time=1.5)
            self.wait(0.4)
        self.play(Write(result), run_time=1.2)
        self.wait(1.5)

        self.clear_body(fat, semi, ident, result)

    # Cena 5: exibe a fórmula final de Heron dentro de uma caixa azul destacada
    def cena5(self):
        box = RoundedRectangle(width=9, height=2.2, corner_radius=0.2,
                               color=AZUL, fill_color=AZUL, fill_opacity=0.15,
                               stroke_width=2)

        formula = MathTex(
            r"A = \sqrt{p(p - a)(p - b)(p - c)}",
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

    # Orquestra a animação completa chamando as cenas em ordem
    def construct(self):
        self.play_title()
        self.wait(0.3)
        self.cena1()
        self.cena2()
        self.cena3()
        self.cena4()
        self.cena5()
        self.wait(1)