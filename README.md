# Blockboard

> Building connections, block by block.

Blockboard is a cross-disciplinary knowledge board for university students. When someone is stuck on a project, assignment, or community problem, they publish the **missing knowledge block** they need. Students from different disciplines can contribute a perspective, connect related ideas, and surface the most promising paths with green hearts.

Built for **SYNCS HACK 2026** and the theme **“Blocks That Make Up the World.”**

## The problem

University students are surrounded by people with useful skills, but disciplines often operate as islands. A computer-science student may need a design or behavioural-science insight; a design student may need engineering context. Existing forums make discussion easy, but do not make missing expertise, idea relationships, or cross-disciplinary collaboration visible.

## Our solution

Blockboard turns an ambiguous question into a visual, community-powered chain:

```text
Missing block (a challenge) → knowledge blocks (new perspectives) → links/remixes → a stronger solution
```

Rather than rewarding the loudest reply, the interface lets people recognise useful ideas with **green hearts**. The board deliberately frames each contribution as a reusable block that can unlock another discipline's work.

## Features

- Create a challenge with a title, context, discipline, and tags.
- Browse a branded feed of active knowledge challenges.
- Filter challenges by Engineering, Design, Science, or Business.
- Add a green heart to signal that an idea is valuable.
- Add a knowledge block or begin linking/remixing related ideas.
- Persist challenges, knowledge blocks, and heart counts through Django/SQLite API endpoints.
- Responsive UI that remains usable on mobile screens.

## Tech stack

- Python and Django
- SQLite
- HTML, CSS, and vanilla JavaScript

No third-party UI component library or image asset is required.

## Run locally

Requirements: Python 3.10+.

```bash
python -m venv .venv
```

Activate the virtual environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
pip install "Django>=4.2,<5.0"
python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000/>.

## API

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/api/challenges/` | List saved challenges |
| `POST` | `/api/challenges/create/` | Create a missing knowledge block |
| `POST` | `/api/challenges/<id>/heart/` | Add a green heart |
| `POST` | `/api/challenges/<id>/blocks/` | Contribute a knowledge block |

Example challenge payload:

```json
{
  "title": "How might we make recycling instructions feel less invisible?",
  "description": "We need an insight from visual design or behavioural science.",
  "discipline": "Computer Science",
  "tags": "sustainability, UX design"
}
```

## Demo flow (under 3 minutes)

1. Open the board and explain the problem: valuable expertise is disconnected across faculties.
2. Choose a discipline filter to show that each problem asks for a specific missing perspective.
3. Click **Create a challenge** and publish a real challenge.
4. Show the new card appearing at the top of the feed.
5. Green-heart an idea, then click **Add your block** and **Link an idea** to explain the remix workflow.
6. Close with the outcome: Blockboard makes students' skills and ideas discoverable building blocks instead of isolated knowledge.

## Hackathon submission checklist

- [ ] Public GitHub repository with version history
- [ ] Working prototype URL or local-run instructions
- [ ] Devpost project description: problem, users, prototype, implementation
- [ ] Maximum three-minute demo video
- [ ] Third-party/open-source acknowledgements
- [ ] Each team member's contribution and role

## Team contributions

Fill this section before submitting to Devpost.

| Team member | Contribution |
| --- | --- |
| `Name` | `Role / feature delivered` |

## Licence

This project was created for SYNCS HACK 2026.
