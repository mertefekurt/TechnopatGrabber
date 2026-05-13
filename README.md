<div align="center">

![Banner](https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=250&section=header&text=TechnopatGrabber&fontSize=60&fontAlignY=35&desc=A%20razor-fast%20terminal%20news%20reader%20that%20turns%20Technopat%20headlines%20into%20clean%2C%20navigable%2C%20browser-free%20reading.%20Fetch%20the%20latest%20stories%2C%20open%20details%20on%20demand%2C%20and%20move%20through%20the%20feed%20with%20single-key%20control.&descAlignY=55&descSize=20)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/Parser-BeautifulSoup-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/HTTP-Requests-FF6F00?style=for-the-badge&logo=icloud&logoColor=white)
![Terminal](https://img.shields.io/badge/UI-Colorama%20CLI-06B6D4?style=for-the-badge&logo=gnometerminal&logoColor=white)

</div>

![Header](https://readme-typing-svg.demolab.com/?font=Space+Mono&weight=700&size=26&color=33C9FF&width=500&height=40&lines=News+Without+The+Browser)

TechnopatGrabber is a focused Python CLI that fetches Technopat's public news feed, extracts article cards, and renders readable terminal views. It keeps the workflow fast: scan the outline, jump between stories, inspect article content, and exit without opening a single tab.

<table>
  <tr>
    <td width="50%" valign="top">

![Header](https://readme-typing-svg.demolab.com/?font=Space+Mono&weight=700&size=26&color=FF4ECD&width=500&height=40&lines=Core+Features)

- 📰 Pulls current Technopat news cards from the public listing page
- 🧭 Supports next, previous, outline, and quit navigation
- 📦 Draws terminal-friendly boxed article views with Colorama
- 🧼 Wraps long content to the active terminal width
- 🕸️ Parses article body text on demand with BeautifulSoup
- ⏱️ Uses timeouts and browser-like headers for reliable fetches

    </td>
    <td width="50%" valign="top">

![Code Snapshot](assets/code-snapshot.png)

    </td>
  </tr>
</table>

![Header](https://readme-typing-svg.demolab.com/?font=Space+Mono&weight=700&size=26&color=9DFF57&width=500&height=40&lines=Blazing+Fast+CLI+Demo)

![Demo](https://readme-typing-svg.demolab.com/?font=Fira+Code&duration=1500&pause=500&multiline=true&width=900&height=130&color=F8F8F2&background=282A3600&lines=%24+python3+main.py;%3E+Fetch+latest+Technopat+headlines;%3E+Press+N+or+P+to+move+through+articles;%3E+Press+O+for+outline+or+Q+to+quit)

![Header](https://readme-typing-svg.demolab.com/?font=Space+Mono&weight=700&size=26&color=FFB86C&width=500&height=40&lines=Fetch+Pipeline)

```mermaid
flowchart LR
    A[Start CLI] --> B[Request Technopat Listing]
    B --> C[Parse Article Cards]
    C --> D[Render Outline]
    D --> E{Navigation Key}
    E -->|N or P| F[Fetch Selected Article]
    E -->|O| D
    E -->|Q| G[Exit Reader]
    F --> H[Normalize Body Text]
    H --> I[Draw Boxed Detail View]
    I --> E
    classDef start fill:#33C9FF,stroke:#0F172A,color:#0F172A,stroke-width:2px
    classDef network fill:#FFB86C,stroke:#4A2500,color:#0F172A,stroke-width:2px
    classDef parser fill:#9DFF57,stroke:#17320E,color:#0F172A,stroke-width:2px
    classDef ui fill:#FF4ECD,stroke:#2A0A1F,color:#FFFFFF,stroke-width:2px
    classDef exit fill:#64748B,stroke:#111827,color:#FFFFFF,stroke-width:2px
    class A start
    class B,F network
    class C,H parser
    class D,E,I ui
    class G exit
```

![Header](https://readme-typing-svg.demolab.com/?font=Space+Mono&weight=700&size=26&color=33C9FF&width=500&height=40&lines=Quick+Start)

```bash
git clone https://github.com/mertefekurt/TechnopatGrabber.git
cd TechnopatGrabber
python3 -m venv .venv
source .venv/bin/activate
pip install requests beautifulsoup4 colorama
python3 main.py
```

<details>
<summary>🛠️ View CLI Reference / Advanced Config</summary>

| Key | Action |
| --- | --- |
| `N` | Open the next article |
| `P` | Return to the previous article |
| `O` | Show the headline outline |
| `Q` | Exit the reader |

| Constant | Purpose |
| --- | --- |
| `BASE_URL` | Public Technopat news listing URL |
| `REQUEST_TIMEOUT` | Maximum wait time for network requests |
| `HEADERS` | Browser-like request headers for consistent responses |

If Technopat changes its page markup, update the selectors inside `fetch_news_list()` and `fetch_news_content()`.

</details>

![Header](https://readme-typing-svg.demolab.com/?font=Space+Mono&weight=700&size=26&color=FF4ECD&width=500&height=40&lines=Screenshots)

| Outline View | Detail View |
| --- | --- |
| ![Outline View](screenshots/SS1.png) | ![Detail View](screenshots/SS2.png) |

![Header](https://readme-typing-svg.demolab.com/?font=Space+Mono&weight=700&size=26&color=9DFF57&width=500&height=40&lines=Project+Map)

```text
TechnopatGrabber/
├── main.py
├── screenshots/
│   ├── SS1.png
│   └── SS2.png
└── assets/
    └── code-snapshot.png
```
