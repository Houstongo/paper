from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


SRC = Path(r"D:\Apaper\paperformat\figures\sources\fig4-4x")
OUT = Path(r"D:\Apaper\paperformat\figures")
OUT.mkdir(parents=True, exist_ok=True)

FONT_PATH = r"C:\Windows\Fonts\timesbd.ttf"
LABEL_FONT = ImageFont.truetype(FONT_PATH, 64)


def make_grid(files, out_name):
    imgs = [Image.open(SRC / f).convert("RGB") for f in files]

    panel_w = 980
    panel_h = 760
    gap_x = 78
    gap_y = 72
    probe = ImageDraw.Draw(Image.new("RGB", (1, 1), "white"))
    label_boxes = {
        label: probe.textbbox((0, 0), label, font=LABEL_FONT)
        for label in ["a", "b", "c", "d"]
    }
    max_label_w = max(bbox[2] - bbox[0] for bbox in label_boxes.values())
    label_gap = 18
    outer_left = max_label_w + label_gap + 18
    outer_right = 18
    outer_top = 10
    outer_bottom = 18
    canvas_w = outer_left + panel_w * 2 + gap_x + outer_right
    canvas_h = outer_top + panel_h * 2 + gap_y + outer_bottom
    canvas = Image.new("RGB", (canvas_w, canvas_h), "white")
    draw = ImageDraw.Draw(canvas)

    for idx, (img, label) in enumerate(zip(imgs, ["a", "b", "c", "d"])):
        r, c = divmod(idx, 2)
        box_x = outer_left + c * (panel_w + gap_x)
        box_y = outer_top + r * (panel_h + gap_y)

        im = img.copy()
        im.thumbnail((panel_w, panel_h))
        px = box_x + (panel_w - im.width) // 2
        py = box_y + (panel_h - im.height) // 2
        canvas.paste(im, (px, py))

        bbox = label_boxes[label]
        lx = box_x - label_gap - max_label_w
        ly = box_y - bbox[1] + 2
        draw.text((lx, ly), label, fill="black", font=LABEL_FONT)

    canvas.save(OUT / out_name, dpi=(300, 300))

make_grid(
    [
        "anneal_alignment.png",
        "anneal_curvature.png",
        "anneal_waviness_ratio.png",
        "anneal_tortuosity.png",
    ],
    "fig4-8-anneal-grid.png",
)

make_grid(
    [
        "response_alignment.png",
        "response_curvature.png",
        "response_waviness_ratio.png",
        "response_tortuosity.png",
    ],
    "fig4-9-response-grid.png",
)

make_grid(
    [
        "feature_importance_alignment.png",
        "feature_importance_curvature.png",
        "feature_importance_waviness_ratio.png",
        "feature_importance_tortuosity.png",
    ],
    "fig4-10-importance-grid.png",
)

make_grid(
    [
        "oof_alignment.png",
        "oof_curvature.png",
        "oof_waviness_ratio.png",
        "oof_tortuosity.png",
    ],
    "fig4-11-oof-grid.png",
)
