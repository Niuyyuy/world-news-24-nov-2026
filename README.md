# World News — 24 November 2026

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/news-image-20261124)
[![repo](https://img.shields.io/badge/github-Niuyyuy%2Fworld--news--24--nov--2026-black)](https://github.com/Niuyyuy/world-news-24-nov-2026)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Niuyyuy/world-news-24-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Niuyyuy/world-news-24-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261124)

A single dense front page that packs the whole of Tuesday 24 November
2026 into one 1024×1024 image: **62 items** — 58 stories grouped into
seven sections plus four extra briefs — every one of them checked
against a source dated that day.

## What happened on 24 November

The day's markets story was the Dow Jones closing above **50,000 for
the first time**, up 0.9% to 50,019, even as the Nasdaq slid. In Kyiv,
President Zelensky said Ukraine needs **€115bn for 2027**, with €25bn
still unsecured, hours before President Putin vowed retaliation for
Ukrainian strikes on Russian refineries. In Washington, President
Trump awarded Rudy Giuliani the Medal of Freedom and was reported to
be preparing new tariffs on China and the EU.

Elsewhere, a Houthi strike hit Riyadh's PIF Tower for a second time,
injuring 11 people; a US jury found Huawei guilty on 10 of 12 counts;
and China opened an investigation into Politburo member Chen Jining,
the Shanghai party chief.

## The 62 items at a glance

| Section | Stories |
| --- | ---: |
| Europe & Ukraine | 10 |
| Middle East | 10 |
| Asia-Pacific | 10 |
| Africa | 7 |
| Americas | 10 |
| Economy & Markets | 4 |
| Science, Tech & Sport | 7 |
| Also in brief | 4 |
| **Total** | **62** |

A UTC timeline runs through the day, from the overnight strike on
Zaporizhzhia (2 killed, 44 hurt) and a 01:00 gas blast in Hanoi,
through the 11:30 Xinhua report on Chen Jining and Zelensky's 19:15
funding appeal, to the Dow's 21:00 close above 50,000.

## How it works

The page is drawn by `draw.py` (kept out of the repo history as a
build helper) into `entry.png`, a 1024×1024 PNG. `main.py` is the
entry point the harness runs: it copies that finished image into the
output directory without touching a single pixel, so the published
picture is byte-identical to the one in this repo. Running it twice
produces the same file both times — no network, no randomness.

## The entry

- **Image:** `entry.png` (1024×1024, 220,491 bytes)
- **Competition:** [news-image-20261124 on make.fun](https://make.fun/bounties/news-image-20261124)
- **Date covered:** Tuesday 24 November 2026, full day
- **Verification:** every story was matched to a source dated
  24 November 2026; stories first reported on other days were left out.

## License

MIT — see [LICENSE](LICENSE).
