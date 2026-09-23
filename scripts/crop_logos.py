"""Re-crop brand logos from source/logo-chart.jpeg into logos/*.jpg.
acura.jpg, dodge.jpg and blue-bird.jpg are not on the chart; they were composed
from Wikimedia Commons / Wikipedia logo files and are not touched by this script.
Adjust TOP/BOTTOM (pixels above/below each row's anchor) to nudge the window,
then run:  python3 scripts/crop_logos.py
"""
from PIL import Image
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source" / "logo-chart.jpeg"
OUT = ROOT / "logos"
XS = [130, 365, 597, 833, 1063]            # column centres
YS = [105, 290, 470, 655, 840, 1020, 1200]  # row anchors
HALF_W, TOP, BOTTOM = 105, 67, 63          # crop window around each anchor
GRID = [
    ["infiniti", "mercedes-benz", "mitsubishi", "ford", "toyota"],
    ["jaguar", "seat", "chevrolet", "kia", "audi"],
    ["opel", "honda", "porsche", "volkswagen", "renault"],
    ["tesla", "hyundai", "jeep", "skoda", "peugeot"],
    ["bentley", "alfa-romeo", "bmw", "saab", "suzuki"],
    ["land-rover", "citroen", "chrysler", "ferrari", "nissan"],
    ["mazda", "volvo", "subaru", "lexus", "fiat"],
]
KEEP = {"toyota","honda","ford","chevrolet","hyundai","kia","nissan","mazda","subaru",
        "volkswagen","jeep","tesla","bmw","mercedes-benz","audi","lexus","infiniti",
        "mitsubishi","volvo"}

im = Image.open(SRC)
OUT.mkdir(exist_ok=True)
for r, y in enumerate(YS):
    for c, x in enumerate(XS):
        name = GRID[r][c]
        if name not in KEEP:
            continue
        crop = im.crop((x - HALF_W, y - TOP, x + HALF_W, y + BOTTOM))
        crop = crop.resize((300, round(300 * crop.height / crop.width)), Image.LANCZOS)
        crop.save(OUT / f"{name}.jpg", "JPEG", quality=85)
        print("wrote", name)
