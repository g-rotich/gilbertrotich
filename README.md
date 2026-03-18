# Gilbert Rotich — Portfolio

Live at: **https://g-rotich.github.io/gilbertrotich/**

---

## Folder structure

```
/
├── index.html              ← Master page (nav, hero, footer, section includes)
├── README.md               ← This file
│
├── css/
│   └── styles.css          ← All styling — colours, layout, typography
│
├── images/
│   ├── README.md           ← Image naming guide
│   ├── profile.jpg         ← Your headshot (add this)
│   └── ...                 ← Paper figures, project thumbnails
│
└── sections/
    ├── papers.html         ← Publications section
    ├── experience.html     ← Work experience & timeline
    ├── education.html      ← Degrees + research focus cards
    ├── skills.html         ← Programming languages, frameworks, research areas
    ├── presentations.html  ← Conference & workshop presentations
    └── projects.html       ← Research pipeline (satellite + general vision)
```

---

## How to deploy on GitHub Pages

### First time setup
1. Create a repo named `g-rotich.github.io` on GitHub (use your actual username)
2. Upload **all files and folders** — maintain the folder structure exactly
3. Go to **Settings → Pages → Source → Deploy from branch → main / root → Save**
4. Your site will be live at `https://g-rotich.github.io` within ~60 seconds

### Updating the site
Edit the relevant file, commit, and push. GitHub Pages rebuilds automatically.

---

## How to edit each section

### Add a new paper → `sections/papers.html`

Copy an existing `<a class="paper-card">` block and update:
- `paper-year` — publication year
- `paper-badge` + badge class (`badge-published` or `badge-prep`)
- `paper-title`, `paper-meta`, `paper-abstract`
- `paper-keywords` — add/remove `<span class="pkw">` tags
- **Thumbnail** — either keep the SVG or replace it with:
  ```html
  <img src="images/paper-yourpaper.jpg" alt="Figure description">
  ```

---

### Add a work entry → `sections/experience.html`

Copy a `.timeline-item` block and update the date, title, org, and bullet list.

---

### Update education → `sections/education.html`

- **Degree cards** — edit inside `.edu-grid`
- **Research focus areas** — edit the `.focus-card` blocks (f1–f5).
  To add a sixth focus: copy a card, add `f6` class, and add a matching `::after` rule in `css/styles.css`.

---

### Add a skill → `sections/skills.html`

Add a `<span class="skill-pill">New Skill</span>` inside the appropriate `.skill-group`.
To add a new group, copy a `.skill-group` div and update the title.

---

### Add a presentation → `sections/presentations.html`

Copy a `.pres-item` block and update the title, venue, and date.

---

### Add a project to the satellite pipeline → `sections/projects.html`

Find the correct `vtl-phase` block and insert a new `.vtl-node`:

```html
<div class="vtl-node">
  <div class="vtl-meta">
    <span class="vtl-year">2025</span>
    <div class="vtl-dot dot-geo"></div>   <!-- dot-geo | dot-ssl | dot-award | dot-current | dot-future -->
  </div>
  <div class="vtl-card card-geo">         <!-- card-geo | card-award | card-current | card-future -->
    <div class="vtl-thumb">
      <!-- Option A: keep SVG illustration -->
      <svg viewBox="0 0 90 70">...</svg>
      <!-- Option B: use a real image -->
      <!-- <img src="images/proj-myproject.jpg" alt="Project thumbnail"> -->
    </div>
    <div class="vtl-body">
      <div class="vtl-top">
        <span class="vtl-title">Your Project Title</span>
        <span class="vtl-badge vb-geo">Badge Text</span>
      </div>
      <span class="vtl-org">Organisation / Dataset</span>
      <p class="vtl-desc">Short description of the project and its contribution.</p>
      <div class="vtl-tags">
        <span class="vtag">Tag 1</span>
        <span class="vtag">Tag 2</span>
      </div>
    </div>
  </div>
</div>
```

**Dot + card colour guide:**

| Type              | dot class      | card class      | badge class  |
|-------------------|----------------|-----------------|--------------|
| Geospatial        | `dot-geo`      | `card-geo`      | `vb-geo`     |
| NLP / Language    | `dot-nlp`      | *(none)*        | `vb-nlp`     |
| SSL / Foundation  | `dot-ssl`      | *(none)*        | `vb-ssl`     |
| Award / Highlight | `dot-award`    | `card-award`    | `vb-award`   |
| Current work      | `dot-current`  | `card-current`  | `vb-current` |
| Future / Horizon  | `dot-future`   | `card-future`   | `vb-future`  |

---

### Add a dataset to General Vision & Video → `sections/projects.html`

Find `<div id="panel-other">` and add inside `.other-grid`:

```html
<div class="other-node on-mydata">
  <span class="other-node-icon">🎬</span>
  <div class="other-node-title">Dataset Name</div>
  <div class="other-node-org">Organisation</div>
  <div class="other-node-desc">Short description.</div>
  <div class="vtl-tags">
    <span class="vtag">Tag</span>
  </div>
</div>
```

Then add a border colour for `on-mydata` in `css/styles.css`:
```css
.other-node.on-mydata { border-left-color: #your-colour; }
```

Also update the grid column count in the `.other-grid` style attribute in `projects.html`:
```html
<div class="other-grid" style="grid-template-columns: repeat(7, 1fr);">
```

---

## Changing colours

All colours are CSS variables in `css/styles.css` under `:root`.
Change `--accent` for the gold, `--accent2` for teal, `--accent3` for purple, etc.
Every component picks up the change automatically.

---

## Adding a profile photo

1. Drop your photo into `images/profile.jpg`
2. In `index.html`, inside `.hero-left`, add:
   ```html
   <img src="images/profile.jpg" alt="Gilbert Rotich"
        style="width:100px;height:100px;border-radius:50%;object-fit:cover;margin-bottom:1.5rem;border:2px solid var(--border);">
   ```

---

## Important note on GitHub Pages and file includes

GitHub Pages serves **static files only** — it cannot stitch HTML files together server-side.
The `sections/` folder is for **your editing convenience** (each file is small and focused).

When deploying, paste the contents of each section file into `index.html` where the
`<!-- PASTE CONTENTS OF sections/xxx.html HERE -->` comments are.

Alternatively, use the self-contained `index.html` from the original build which has
everything in one file — that works on GitHub Pages immediately with no extra steps.
