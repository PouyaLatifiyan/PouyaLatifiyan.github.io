# PouyaLatifiyan.github.io
Professional CV and Portfolio Website - Pouya Latifiyan

English uses the root URL. Persian, Arabic, Chinese and French use /fa/, /ar/, /zh/ and /fr/. Each page is static HTML.

## Editing the site

Edit the five language versions in `_source/translations.py`. The layout and bibliography are in `_source/build.py`. To add a family biography, edit `_source/family.json`, using a person's route key and the language of the text. For example:

```json
{
  "father": {
    "fa": {
      "name": "نام",
      "paragraphs": ["بند نخست زندگی‌نامه"]
    }
  }
}
```

Run `python3 -B _source/build.py` and commit the source and generated pages together. A family biography enters the sitemap when it has text in that language.
