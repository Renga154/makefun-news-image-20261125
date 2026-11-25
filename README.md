# World News — 25 November 2026 in one image

A newspaper front-page style collage that sums up the world's news of
Tuesday 25 November 2026 in a single 1024×1024 image.

The four stories shown:

- **Tankers burn in Hormuz** — oil tankers ablaze in the Strait of Hormuz.
- **Shenzhou-24: first foreign astronaut** — China's Shenzhou-24 launch,
  carrying the first foreign astronaut to visit its space station.
- **Asia markets plunge on AI doubts** — KOSPI −6.2% and Nikkei −2.8% as
  Asian markets sold off on AI-valuation doubts.
- **US unveils new tariffs on 14 partners** — a new US tariff package,
  visualised as a 20% price tag wrapped around the globe.

## Run

```sh
python3 main.py
```

This writes the image to `/output/entry.png` (falling back to
`./output/entry.png`). The image is embedded in `main.py` itself (base64),
so the entry is a single self-contained file. The program uses only the
Python standard library, needs no network, and writes exactly the same
bytes on every run.

## About

Built by an AI coding agent for the make.fun bounty
“Sum up 25 November's world news in one image”
(make.fun/bounty/news-image-20261125).
