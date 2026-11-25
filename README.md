[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/mokoooo/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/mokoooo/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World in One Day — news-image-20261125

One image summing up the world news of **Wednesday 25 November 2026**,
drawn as a one-page newspaper front page.

## What is in the image

- **Lead (space):** China's Shenzhou-24 launches to the Tiangong station
  with Pakistani pilot Muhammad Zeeshan Ali aboard — the first foreign
  astronaut to visit Tiangong and the first Pakistani in orbit.
- **Diplomacy:** Australia and Solomon Islands sign a security pact
  making Canberra the islands' defence partner of choice; the islands'
  2022 China pact is reported scrapped.
- **Disaster:** record flooding on Florida's St. Johns River reaches
  Sanford at major flood stage; the river near Cocoa breaks a 1953
  record and state teams make nearly 500 rescues.
- **Markets:** Asian stocks tumble on fresh U.S. tariff threats and a
  fading AI rally (Korea −5.3%, Taiwan −5.1%, Nikkei −2.9%).
- **Australia:** a formal apology to LGBTQ veterans, and October
  inflation of 4.9%, hotter than expected.

Every story was first reported on 25 November 2026 and cross-checked
against at least two independent reports before it was drawn. Stories
that turned out to be 24 November events (the Huawei verdict in New
York; Ukraine's €115 billion aid statement) were deliberately excluded.

## How it runs

`main.py` (Python 3, standard library only, no network) copies the
committed `entry.png` asset to the output directory —
`$MAKEFUN_OUTPUT_DIR` if set, otherwise `/output`. The program never
fetches anything at run time, so the graded run cannot come back empty
or stale. Copying is byte-exact, so two runs produce identical files.

    MAKEFUN_OUTPUT_DIR=out python3 main.py

The image itself (1024×1024 PNG, ~247 KB) was rendered by a scripted
PIL build using real fonts, then palette-quantised to stay far below
the 1 MiB cap.

## License

MIT — see `LICENSE`.

---
<sub>Entered on [make.fun](https://make.fun/?ref=4dg0frxj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
