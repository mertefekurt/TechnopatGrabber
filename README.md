<div align="center">

![Technopat Grabber banner](https://capsule-render.vercel.app/api?type=cylinder&height=180&color=0:111827,100:06b6d4&text=Technopat%20Grabber%20CLI&fontColor=ffffff&fontAlign=50&desc=Readable%20tech%20news%20from%20your%20terminal&descAlign=50&descAlignY=68)

![License](https://img.shields.io/badge/license-MIT-06b6d4?style=flat-square)
![Language](https://img.shields.io/badge/language-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Build](https://img.shields.io/badge/build-passing-22c55e?style=flat-square)
![CLI](https://img.shields.io/badge/interface-terminal-111827?style=flat-square)

</div>

## Terminal-First News Reading

Technopat Grabber CLI gives you a fast way to scan current Technopat news without opening a browser tab. It fetches the latest article list, formats each story in a clean terminal box, and lets you move through details with single-key navigation.

![typing demo](https://readme-typing-svg.demolab.com?font=Hack&duration=1500&pause=500&color=06B6D4&background=11182700&width=900&lines=python3+main.py;N+for+next+story.;O+for+the+outline.;Q+when+you+are+done.)

## What It Does Well

- Pulls headline cards from `https://www.technopat.net/haber/`
- Fetches article body text on demand
- Wraps content to the current terminal width
- Renders boxed views with `colorama`
- Supports next, previous, outline, and quit actions

> This project reads public pages from Technopat. Be respectful with repeated runs and avoid automated polling.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests beautifulsoup4 colorama
python3 main.py
```

Keyboard controls:

| Key | Action |
| --- | --- |
| <kbd>N</kbd> | Open the next article |
| <kbd>P</kbd> | Return to the previous article |
| <kbd>O</kbd> | Show the headline outline |
| <kbd>Q</kbd> | Exit the reader |

## News Pipeline

```mermaid
flowchart LR
    A[User runs python3 main.py] --> B[Fetch Technopat listing]
    B --> C[Parse article cards]
    C --> D[Render outline]
    D --> E{Navigation key}
    E -->|N or P| F[Fetch selected article]
    E -->|O| D
    E -->|Q| G[Exit]
    F --> H[Draw boxed detail view]
    H --> E
    style B fill:#06b6d4,stroke:#0f172a,color:#0f172a
    style H fill:#ecfeff,stroke:#0891b2,color:#164e63
```

<details>
<summary>Advanced configuration notes</summary>

The fetch behavior is intentionally simple:

- `BASE_URL` points to the Technopat news listing.
- `REQUEST_TIMEOUT` protects the CLI from hanging on slow network responses.
- `HEADERS` sets a browser-like user agent for consistent page responses.

If Technopat changes its markup, update the selectors in `fetch_news_list()` and `fetch_news_content()`.

</details>

## Screenshots

### Outline View

![Outline View](screenshots/SS1.png)

### Article Detail View

![Detail View](screenshots/SS2.png)

## Project Layout

```text
TechnopatGrabber/
├── main.py
├── screenshots/
│   ├── SS1.png
│   └── SS2.png
└── README.md
```

## License

Released under the MIT License.
