# Car Spotter Hunt

Tap-to-check car-logo scavenger hunt for a pre-reader. Open `index.html` in any
browser (or `python3 -m http.server` in this folder and visit localhost:8000).

## GitHub Pages

The site is plain static files, so it deploys straight from the `main` branch:

1. Push `main` to GitHub.
2. In the repo go to **Settings → Pages**.
3. Under **Build and deployment** set Source to **Deploy from a branch**,
   pick `main` and `/ (root)`, then Save.
4. After a minute the site is live at `https://<user>.github.io/Cars/`.

`.nojekyll` is checked in so Pages serves the files as-is (no Jekyll build).

- `index.html` — the whole app: layout, styles, and the checklist logic (progress
  saved to localStorage under `car-spotter-found-v2`).
- `logos/*.jpg` — one 300×186 badge per brand, referenced by `index.html`. Most are
  cropped from the source chart; `acura.jpg` and `blue-bird.jpg` were composed from
  Wikimedia Commons / Wikipedia logo files. `dodge.jpg` (ram's head badge) is cropped
  from ["Dodge Ram" by Falcon® Photography](https://commons.wikimedia.org/wiki/File:Dodge_Ram_(21402726981).jpg),
  CC BY-SA 2.0.
- `source/logo-chart.jpeg` — the original chart the logos were cropped from.
- `scripts/crop_logos.py` — regenerates `logos/` from the source chart
  (needs Pillow: `pip install pillow`). Tweak `TOP`/`BOTTOM`/`KEEP` there.

To add a brand: drop a `logos/<name>.jpg` and add a `<button class="car" data-name="Name">`
block in `index.html` — the script counts tiles automatically.

## MCU Movie Marathon (`marvel/`)

A separate checklist app that lives in its own folder and doesn't touch the car game.
It's live at `https://<user>.github.io/Cars/marvel/`. It lists every mainline Marvel
Studios film with its IMDb and Rotten Tomatoes scores, in story (timeline) order or
release order. Story order is split into chapters, and each card shows the year it happens. Tap a movie to mark it watched. Un-checking asks for confirmation first.

- `marvel/index.html` holds the whole app. The movie list is the `MOVIES` array near
  the top of the script. To add a film, add a row and give it a `story` position.
  Films whose release date hasn't arrived show as "coming soon" and aren't counted.
- Progress is saved in the browser's localStorage under `mcu-watched-v1`, so it stays
  on the device and browser where it was checked. Add the page to the home screen. On
  iPhone that also stops Safari from clearing saved data on sites you don't visit often.
