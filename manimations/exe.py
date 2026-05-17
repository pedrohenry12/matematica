from manim import *

VINHO  = "#6B1A3A"
VERDE  = "#009C3B"
AMARELO = "#FFDF00"
AZUL   = "#002776"

def titulo_slide(texto):
    barra = Rectangle(width=14, height=0.7, fill_color=VINHO,
                      fill_opacity=1, stroke_width=0).to_edge(UP, buff=0)
    label = Text(texto, font_size=24, color=WHITE).move_to(barra)
    return VGroup(barra, label)


class BandeiraBrasil(Scene):

    def construct(self):
        t = titulo_slide("Bandeira do Brasil — Áreas e Porcentagem")
        self.play(FadeIn(t))
        self.wait(0.3)

        # ── Cena 1: dados do problema ─────────────────────────────────────
        dados_title = Tex(r"\textbf{Dados do problema}", font_size=32, color=AMARELO)\
            .shift(UP*2.8)

        dados = BulletedList(
            r"Retângulo: $200\,\text{cm} \times 140\,\text{cm}$",
            r"Vértices do losango distam $17\,\text{cm}$ dos lados do retângulo",
            r"Raio do círculo: $r = 35\,\text{cm}$",
            r"$\pi = \dfrac{22}{7}$",
            font_size=30,
            buff=0.35,
        ).next_to(dados_title, DOWN, buff=0.4).to_edge(LEFT, buff=1)

        self.play(Write(dados_title))
        self.play(LaggedStart(*[Write(d) for d in dados], lag_ratio=0.4))
        self.wait(2)
        self.play(FadeOut(dados_title), FadeOut(dados))

        # ── Cena 2: área do retângulo ─────────────────────────────────────
        sec1 = Tex(r"\textbf{Área do Retângulo}", font_size=32, color=VERDE)\
            .shift(UP*2.8)

        eq_ret = MathTex(
            r"A_{\text{ret}} &= 200 \times 140 \\",
            r"A_{\text{ret}} &= 28{.}000\,\text{cm}^2",
            font_size=36,
        ).next_to(sec1, DOWN, buff=0.5)

        self.play(Write(sec1))
        self.play(Write(eq_ret), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(sec1), FadeOut(eq_ret))

        # ── Cena 3: dimensões do losango ──────────────────────────────────
        sec2 = Tex(r"\textbf{Dimensões do Losango}", font_size=32, color=AMARELO)\
            .shift(UP*2.8)

        expl = Tex(
            r"Os vértices distam $17\,\text{cm}$ de cada lado, então:",
            font_size=28,
        ).next_to(sec2, DOWN, buff=0.4).to_edge(LEFT, buff=0.8)

        eq_los = MathTex(
            r"d_1 &= 200 - 2\times 17 = 200 - 34 = 166\,\text{cm} \\",
            r"d_2 &= 140 - 2\times 17 = 140 - 34 = 106\,\text{cm}",
            font_size=32,
        ).next_to(expl, DOWN, buff=0.4).shift(RIGHT*0.3)

        note = Tex(
            r"onde $d_1$ e $d_2$ são as diagonais do losango.",
            font_size=26, color=GRAY,
        ).next_to(eq_los, DOWN, buff=0.3).to_edge(LEFT, buff=0.8)

        self.play(Write(sec2))
        self.play(Write(expl))
        self.play(Write(eq_los), run_time=1.5)
        self.play(Write(note))
        self.wait(1.5)
        self.play(FadeOut(sec2), FadeOut(expl), FadeOut(eq_los), FadeOut(note))

        # ── Cena 4: área do losango ───────────────────────────────────────
        sec3 = Tex(r"\textbf{Área do Losango}", font_size=32, color=AMARELO)\
            .shift(UP*2.8)

        eq_losarea = MathTex(
            r"A_{\text{los}} &= \frac{d_1 \times d_2}{2} \\[6pt]",
            r"&= \frac{166 \times 106}{2} \\[6pt]",
            r"&= \frac{17{.}596}{2} \\[6pt]",
            r"&= 8{.}798\,\text{cm}^2",
            font_size=34,
        ).next_to(sec3, DOWN, buff=0.5)

        self.play(Write(sec3))
        for e in eq_losarea:
            self.play(Write(e), run_time=0.9)
            self.wait(0.2)
        self.wait(1.5)
        self.play(FadeOut(sec3), FadeOut(eq_losarea))

        # ── Cena 5: área do círculo ───────────────────────────────────────
        sec4 = Tex(r"\textbf{Área do Círculo}", font_size=32, color=AZUL)\
            .shift(UP*2.8)

        eq_circ = MathTex(
            r"A_{\text{cir}} &= \pi \cdot r^2 \\[6pt]",
            r"&= \frac{22}{7} \times 35^2 \\[6pt]",
            r"&= \frac{22}{7} \times 1{.}225 \\[6pt]",
            r"&= 22 \times 175 \\[6pt]",
            r"&= 3{.}850\,\text{cm}^2",
            font_size=34,
        ).next_to(sec4, DOWN, buff=0.5)

        self.play(Write(sec4))
        for e in eq_circ:
            self.play(Write(e), run_time=0.9)
            self.wait(0.2)
        self.wait(1.5)
        self.play(FadeOut(sec4), FadeOut(eq_circ))

        # ── Cena 6: resposta a) área verde ────────────────────────────────
        sec5 = Tex(r"\textbf{a) Área pintada de Verde}", font_size=32, color=VERDE)\
            .shift(UP*2.8)

        expl_v = Tex(
            r"Área verde $=$ Área do retângulo $-$ Área do losango",
            font_size=28,
        ).next_to(sec5, DOWN, buff=0.4)

        eq_verde = MathTex(
            r"A_{\text{verde}} &= 28{.}000 - 8{.}798 \\[8pt]",
            r"A_{\text{verde}} &= 19{.}202\,\text{cm}^2",
            font_size=38,
        ).next_to(expl_v, DOWN, buff=0.5)

        box_v = SurroundingRectangle(eq_verde[1], color=VERDE, buff=0.15)

        self.play(Write(sec5))
        self.play(Write(expl_v))
        self.play(Write(eq_verde), run_time=1.5)
        self.play(Create(box_v))
        self.wait(2)
        self.play(FadeOut(sec5), FadeOut(expl_v), FadeOut(eq_verde), FadeOut(box_v))

        # ── Cena 7: resposta b) porcentagem amarela ───────────────────────
        sec6 = Tex(
            r"\textbf{b) Porcentagem da Área Amarela}", font_size=32, color=AMARELO
        ).shift(UP*2.8)

        expl_a = Tex(
            r"Área amarela $=$ Área do losango $-$ Área do círculo",
            font_size=28,
        ).next_to(sec6, DOWN, buff=0.35)

        eq_amar = MathTex(
            r"A_{\text{amar}} &= 8{.}798 - 3{.}850 = 4{.}948\,\text{cm}^2",
            font_size=32,
        ).next_to(expl_a, DOWN, buff=0.35)

        expl_p = Tex(
            r"Porcentagem em relação à área total:",
            font_size=28,
        ).next_to(eq_amar, DOWN, buff=0.4)

        eq_porc = MathTex(
            r"\% &= \frac{A_{\text{amar}}}{A_{\text{ret}}} \times 100 \\[6pt]",
            r"&= \frac{4{.}948}{28{.}000} \times 100 \\[6pt]",
            r"&\approx 17{,}67\%",
            font_size=34,
        ).next_to(expl_p, DOWN, buff=0.3).shift(RIGHT*0.5)

        box_p = SurroundingRectangle(eq_porc[2], color=AMARELO, buff=0.15)

        self.play(Write(sec6))
        self.play(Write(expl_a))
        self.play(Write(eq_amar))
        self.play(Write(expl_p))
        for e in eq_porc:
            self.play(Write(e), run_time=0.9)
            self.wait(0.2)
        self.play(Create(box_p))
        self.wait(2)
        self.play(FadeOut(sec6), FadeOut(expl_a), FadeOut(eq_amar),
                  FadeOut(expl_p), FadeOut(eq_porc), FadeOut(box_p))

        # ── Cena 8: resumo final ──────────────────────────────────────────
        resumo_title = Tex(r"\textbf{Respostas}", font_size=36).shift(UP*2.5)

        resp_a = MathTex(
            r"\text{a) Área verde} = 19{.}202{,}00\,\text{cm}^2",
            font_size=34, color=VERDE,
        ).shift(UP*0.8)

        resp_b = MathTex(
            r"\text{b) Área amarela} \approx 17{,}67\%\ \text{da bandeira}",
            font_size=34, color=AMARELO,
        ).shift(DOWN*0.2)

        box_a = SurroundingRectangle(resp_a, color=VERDE, buff=0.15)
        box_b = SurroundingRectangle(resp_b, color=AMARELO, buff=0.15)

        self.play(Write(resumo_title))
        self.play(Write(resp_a), Create(box_a))
        self.wait(0.5)
        self.play(Write(resp_b), Create(box_b))
        self.wait(3)