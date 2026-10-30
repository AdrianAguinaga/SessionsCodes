# Courses index

Short map of this repo. Details live in the files it points to.

| Course | Manifest | Templates | Last cohort |
|---|---|---|---|
| 106 · jQuery & Azure Functions | `courses/106.json` | `Templates/106` | 72 |
| 107 · React with Vite | `courses/107.json` | `Templates/107` | 70 |

## New cohort

1. Paste the Zoom invitations into `ZoomData/<course>.md`.
2. `python scripts/process.py --course <course> --cohort <n>`
3. Set `last_generated_cohort` in `courses/<course>.json`.
4. `python scripts/check.py` must print `OK`.

## Live labs

- One self-contained `labs/<course>/<lab>/index.html` per lab (no build, no dependencies).
- Pushing changes under `labs/` publishes it to `https://adrianaguinaga.github.io/SessionsCodes/<course>/<lab>/` (`.github/workflows/pages.yml`).
- Canvas strips `<script>`, so a lab is embedded with an `<iframe>` plus an "Open in a new tab" link in the session template (see `Templates/106/session2.txt`).
- List it under `labs` for that session in the manifest; `check.py` fails if the template does not embed it.

| Lab | Sessions | Notes |
|---|---|---|
| `106/http-inspector` | 106 S2 (reusable for S3 POST, S4 DELETE) | Simulated server by default. The real API only allows CORS from Live Server (`127.0.0.1:5500` / `localhost:5500`), so "Real course API" shows a CORS error on Pages, on purpose. |
