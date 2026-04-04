from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


SRC = Path(r"D:\Apaper\paperformat\figures\sources\fig4-4x")
OUT = Path(r"D:\Apaper\paperformat\figures")
OUT.mkdir(parents=True, exist_ok=True)

FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
LABEL_FONT = ImageFont.truetype(FONT_PATH, 34)


def make_grid(files, labels, out_name):
    imgs = [Image.open(SRC / f).convert("RGB") for f in files]

    panel_w = 980
    panel_h = 760
    label_h = 72
    gap_x = 55
    gap_y = 48
    margin = 28
    canvas_w = margin * 2 + panel_w * 2 + gap_x
    canvas_h = margin * 2 + (panel_h + label_h) * 2 + gap_y
    canvas = Image.new("RGB", (canvas_w, canvas_h), "white")
    draw = ImageDraw.Draw(canvas)

    for idx, (img, label) in enumerate(zip(imgs, labels)):
        r, c = divmod(idx, 2)
        box_x = margin + c * (panel_w + gap_x)
        box_y = margin + r * (panel_h + label_h + gap_y)

        im = img.copy()
        im.thumbnail((panel_w, panel_h))
        px = box_x + (panel_w - im.width) // 2
        py = box_y + (panel_h - im.height) // 2
        canvas.paste(im, (px, py))

        bbox = draw.textbbox((0, 0), label, font=LABEL_FONT)
        tw = bbox[2] - bbox[0]
        tx = box_x + (panel_w - tw) // 2
        ty = box_y + panel_h + 14
        draw.text((tx, ty), label, fill="black", font=LABEL_FONT)

    canvas.save(OUT / out_name, dpi=(300, 300))


LABELS = ["(a) 取向度", "(b) 平均曲率", "(c) 波曲度", "(d) 迂曲度"]


make_grid(
    [
        "anneal_alignment.png",
        "anneal_curvature.png",
        "anneal_waviness_ratio.png",
        "anneal_tortuosity.png",
    ],
    LABELS,
    "fig4-8-anneal-grid.png",
)

make_grid(
    [
        "response_alignment.png",
        "response_curvature.png",
        "response_waviness_ratio.png",
        "response_tortuosity.png",
    ],
    LABELS,
    "fig4-9-response-grid.png",
)

make_grid(
    [
        "feature_importance_alignment.png",
        "feature_importance_curvature.png",
        "feature_importance_waviness_ratio.png",
        "feature_importance_tortuosity.png",
    ],
    LABELS,
    "fig4-10-importance-grid.png",
)

make_grid(
    [
        "oof_alignment.png",
        "oof_curvature.png",
        "oof_waviness_ratio.png",
        "oof_tortuosity.png",
    ],
    LABELS,
    "fig4-11-oof-grid.png",
)
