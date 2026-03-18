# images/

Place all website images in this folder.
Reference them in HTML as: `src="images/filename.jpg"`

## Suggested files to add

| Filename                  | Used in              | Description                          |
|---------------------------|----------------------|--------------------------------------|
| `profile.jpg`             | index.html hero      | Your headshot / profile photo        |
| `paper-robustness.jpg`    | sections/papers.html | Figure from robustness paper         |
| `paper-kd-compact.jpg`    | sections/papers.html | Figure from KD compact paper         |
| `paper-multimodal.jpg`    | sections/papers.html | Figure from multimodal SSL paper     |
| `paper-covid.jpg`         | sections/papers.html | Figure from COVID activity paper     |
| `paper-xview.jpg`         | sections/papers.html | Figure from xView detection paper    |
| `paper-fmow.jpg`          | sections/papers.html | Figure from fMoW/ConceptNet paper    |
| `proj-fmow.jpg`           | sections/projects.html | fMoW dataset sample image          |
| `proj-xview.jpg`          | sections/projects.html | xView overhead detection sample    |
| `proj-spacenet.jpg`       | sections/projects.html | SpaceNet SAR building sample       |
| `proj-ssl.jpg`            | sections/projects.html | SSL pretraining diagram            |
| `proj-multispectral.jpg`  | sections/projects.html | Multispectral band visualization   |
| `proj-charades.jpg`       | sections/projects.html | Charades dataset frame             |
| `proj-kinetics.jpg`       | sections/projects.html | Kinetics action frame              |
| `proj-epic.jpg`           | sections/projects.html | EPIC-Kitchens egocentric frame     |
| `proj-virat.jpg`          | sections/projects.html | VIRAT surveillance frame           |

## How to swap SVG thumbnails for real images

In `sections/papers.html` or `sections/projects.html`, find the `.paper-thumb` or `.vtl-thumb` div
and replace the `<svg>...</svg>` block with:

```html
<img src="images/your-image.jpg" alt="Description of figure">
```

The CSS in `css/styles.css` already handles sizing and hover effects for both SVGs and `<img>` tags inside `.vtl-thumb` and `.paper-thumb`.
