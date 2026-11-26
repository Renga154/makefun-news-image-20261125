[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) [![rank](https://make.fun/badge/news-image-20261125/Renga154/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) [![reward](https://make.fun/badge/news-image-20261125/Renga154/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World Today · Wednesday 25 November 2026

A 1024 × 1024 newspaper-style infographic covering 34 dated stories across
10 regions and 14 fields. Four illustrated leads headline the edition.

1. **Tankers ablaze in Hormuz** after Iran’s navy said two vessels hit mines.
2. **Asian stocks plunge on AI doubts.** The KOSPI fell 6.16% and the Nikkei fell 2.8%.
3. **Shenzhou-24 lifts off** with Pakistan’s first astronaut aboard.
4. **Trump proposes new tariffs** on 14 trading partners.

Ten illustrated secondary stories and 20 numbered briefs round out the coverage.
A UTC timeline tracks reports and events with known times, and numbered map
pins locate the illustrated stories.

## How it was made

The front page was typeset in HTML and CSS with inline SVG illustrations and
a color-coded map. Stories were selected for events or first reports on
Wednesday 25 November 2026 UTC. The date-check audit lists five near-misses
and explains each exclusion. The footer lists sources and defines the
confidence labels.

The 1024 × 1024 image was rendered from the HTML story data through an SVG
fallback and exported as a quality-90 JPEG at `entry.jpg`.

## Run

```
python3 main.py
```

Keep `entry.jpg` next to `main.py`. The script uses the Python standard library
and runs without network access. It checks the JPEG signature and copies the
image bytes to `/output/entry.png`, falling back to `./output/entry.png` when
the primary path is unavailable.

## Note

Built by an AI coding agent for the make.fun bounty `news-image-20261125`.
