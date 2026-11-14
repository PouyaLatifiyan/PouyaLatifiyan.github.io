"""Run python _source/build.py after editing translations or family biographies."""
from html import escape
from pathlib import Path
import json
from translations import LANGS, TEXT

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://pouyalatifiyan.github.io'
NAMES = dict(zip(LANGS, ['English','فارسی','العربية','中文','Français']))
SLUG = {'home':'', 'bio':'biography/', 'docs':'credentials/', 'family':'family/', 'research':'research/', 'portfolio':'projects/', 'papers':'publications/', 'notes':'notes/'}
GROUPS = {'parents':['father','mother'], 'paternal':['paternal-grandfather','paternal-grandmother'], 'maternal':['maternal-grandfather','maternal-grandmother']}
for people in GROUPS.values():
    SLUG.update({p:'family/'+p+'/' for p in people})
# Optional records: {"father": {"fa": {"name":"…", "paragraphs":["…"]}}}
records = json.loads((ROOT/'_source/family.json').read_text())
def path(lang, page):
    if page == 'home':
        return f'/{lang}/'
    return ('/' if lang == 'en' else '/'+lang+'/') + SLUG[page]
def link(url, label, cls=''):
    return f'<a class="{cls}" href="{escape(url,quote=True)}">{label}</a>'
def arrow():
    return '<span class="arr" aria-hidden="true">→</span>'
def section(title, items, id=''):
    return f'<section class="section feature" id="{id}"><h2>{title}</h2><div>{items}</div></section>'
def entry(title, desc, date=''):
    return f'<article class="entry"><span class="date">{date}</span><h3>{title}</h3><p>{desc}</p></article>'
def button(url, title):
    return link(url,title+' '+arrow(),'btn')
def label(value):
    return f'<p class="eyebrow">{value}</p>'
def sub(title, intro, tag='', action=''):
    return f'<div class="subhero">{label(tag) if tag else ""}<h1>{title}</h1><p class="intro">{intro}</p>{action}</div>'
def home(l,t):
    actions=button(path(l,'research'),t('current'))+link(path(l,'bio'),t('readbio'),'quiet')
    hero=f'<section class="hero" id="home"><div class="hero-copy">{label(t("scope"))}<h1>{t("name")}</h1><p class="intro">{t("identity")}</p><div class="actions">{actions}</div></div></section>'
    items = [(t('doctoral'),t('degree')),('Beihang University',t('school')),(t('advisor'),'<bdi>Prof. Yanhong Kou</bdi>')]
    affil = '<div class="affil">'+''.join(f'<div><span class="caption">{a}</span><strong>{b}</strong></div>' for a,b in items)+'</div>'
    framework = f'<section class="section feature" id="framework"><div>{label(t("current"))}<span class="display" lang="en">Alert</span></div><div><h2>{t("framework")}</h2><p class="intro">{t("alertintro")}</p><p class="domains"><span class="caption">{t("applications")}</span>{t("domains")}</p></div></section>'
    future = ''.join(f'<article class="card"><h3>{t(k)}</h3><p>{t(d)}</p></article>' for k,d in [('ai','aitext'),('quantum','qtext')])
    highlights='<section class="section"><div class="sectionline"><h2>'+t('portfolio')+'</h2>'+link(path(l,'portfolio'),t('portfolio')+' '+arrow(),'quiet')+'</div><div class="cards">'+project_cards(l,t)+'</div></section>'
    return hero+affil+framework+highlights+f'<section class="section"><h2>{t("future")}</h2><div class="cards">{future}</div></section>'
def project_cards(l,t):
    entries=[('Mahbot1 · NASA Astrobee','mah','astrobee'),('NASA Impact Visual Analysis System','nivas','impact')]
    return ''.join(f'<article class="card project"><div class="diagram {art}" aria-hidden="true"><span></span><i></i><b></b></div><div class="card-copy"><h3 dir="ltr">{name}</h3><p>{t(desc)}</p></div></article>' for name,desc,art in entries)
def education(t):
    return entry(t('degree'),t('school')+' · '+t('scope')+'<br>'+t('advisor')+' · <bdi>Prof. Yanhong Kou</bdi>','2026 – '+t('present'))+entry(t('master'),t('masterinfo'),'2024 – 2026')+entry(t('bachelor'),t('bachinfo'),'2020 – 2024')
PAPERS = [
 ('Autonomous Lunar Lander Navigation via Tightly-Coupled LunaNet/INS Integration Under Sparse Satellite Visibility','Pouya Latifiyan, Muhammad Arsalan, Haniyeh Zahra Budaqi','Journal of Deep Space Exploration',''),
 ('Domain Randomization for Adversarial Robustness in Orbital Collision Avoidance: A Deep Reinforcement Learning Approach','Pouya Latifiyan, Aparna Dongale, Maria Chowdhury, Lucky Bose','International Conference on Guidance, Navigation and Control (2026)','review'),
 ('VR-LunaNav: A VR-Computer Vision Testbed for Wearable Visual Navigation Aids in Lunar Surface EVAs','Pouya Latifiyan, Zhao Danpei, Bo Yuan','2026 Academic Readings on Cosmonautics','10.5281/zenodo.19434090'),
 ('Onboard Computer Vision for Spacecraft: Real-Time Earth Disaster Monitoring and Resilient Space Operations','Pouya Latifiyan, Zhao Danpei','UN GEONOW 2025','10.13140/RG.2.2.17160.07680'),
 ('Using CubeSats for Planetary Research','Pouya Latifiyan, Xiucong Sun','22nd Scientists Conference “Fundamental and Applied Space Research” (2025)','')]
def bio(l,t):
    top = '<div class="biohead">'+sub(t('biotitle'),t('story'),t('bio'))+f'<img class="portrait" src="/assets/portrait.webp" alt="{t("name")}" width="630" height="840"></div>'
    experience = ''.join(entry(t(k),t(k+'text'),year) for k,year in [('job1','2025.09 – '+t('present')),('job2','2024.02 – 2024.07'),('job3','2023.06 – 2024.02')])
    projects = entry('Mahbot1 · NASA Astrobee',t('mah'))+entry(link('https://github.com/lunex-project-2025/NIVAS','NASA Impact Visual Analysis System (NIVAS)'),t('nivas'))
    return top+section(t('edu'),education(t),'education')+section(t('exp'),experience,'experience')+section(t('projects'),projects,'projects')+section(t('pub'),publications(t),'publications')+section(t('skills'),t('skillsbody'),'skills')
def publications(t):
    pubs=''
    for title,authors,venue,identifier in PAPERS:
        details = f'<span dir="ltr" lang="en">{authors}<br>{venue}</span>'
        if identifier=='review':
            details += ' · '+t('review')
        elif identifier:
            details += ' · '+link('https://doi.org/'+identifier,'DOI '+identifier)
        pubs += entry(f'<bdi lang="en">{escape(title)}</bdi>', details)
    return pubs
def docs(t):
    top=sub(t('docs'),t('docintro'),t('name'),'<div class="actions">'+button('/CV.pdf',t('cv')+' · PDF')+'</div>')
    awards=entry(t('award1'),'Asia Simulation Federation International Summer School','2026.07')+entry(t('award2'),'NASA Space Apps Challenge · Tokyo','2025.10')+entry(t('award3'),t('olym'),'2017.07')
    return top+section(t('edu'),education(t),'education')+section(t('awards'),awards,'awards')
def family(l,t,p):
    if p=='family':
        groups=''
        for g, people in GROUPS.items():
            rows=''.join(link(path(l,k),t(k)+arrow(),'linkrow') for k in people)
            groups+=section(t(g),rows,g)
        return sub(t('familytitle'),t('familyintro'),t('name'))+groups
    record=records.get(p,{}).get(l,{})
    text='</p><p class="intro">'.join(escape(s) for s in record.get('paragraphs',[])) or t('empty')
    return sub(escape(record.get('name',t(p))),text,t('family')+' / '+t(p),'<div class="actions">'+link(path(l,'family'),t('familytitle')+' '+arrow(),'quiet')+'</div>')
def research_page(l,t):
    return sub(t('current'),t('identity'),t('scope'))+section('Alert','<h3>'+t('framework')+'</h3><p class="intro">'+t('alertintro')+'</p><p class="domains">'+t('domains')+'</p>','framework')+section(t('future'),entry(t('ai'),t('aitext'))+entry(t('quantum'),t('qtext')),'future')
def project_page(l,t):
    return sub(t('portfolio'),t('biotitle'),t('name'))+section('Alert',t('alertintro')+'<div class="actions">'+button(path(l,'research')+'#framework',t('current'))+'</div>','alert')+'<div class="cards">'+project_cards(l,t)+'</div><div class="actions">'+link('https://github.com/lunex-project-2025/NIVAS','NIVAS · GitHub '+arrow(),'quiet')+'</div>'
def page(l,p):
    def t(k): return escape(TEXT[k][l])
    url=BASE+path(l,p)
    blank=p in {person for group in GROUPS.values() for person in group} and not records.get(p,{}).get(l,{}).get('paragraphs')
    title=(t('name')+' | '+t('field')+' · Beihang University') if p=='home' else (t('home' if p=='research' else p)+' | '+t('name'))
    descr=t({'home':'intro','bio':'story','docs':'docintro','family':'familyintro','research':'alertintro','portfolio':'identity','papers':'pub','notes':'noteTitle'}.get(p,'empty'))
    alt=''.join(f'<link rel="alternate" hreflang="{a}" href="{BASE+path(a,p)}">' for a in LANGS)
    default_url=BASE+('/' if p=='home' else path('en',p))
    alt+=f'<link rel="alternate" hreflang="x-default" href="{default_url}">'
    langs=''.join(f'<a href="{path(a,p)}" hreflang="{a}" lang="{a}" dir="auto"'+(' aria-current="true"' if a==l else '')+f'>{NAMES[a]}</a>' for a in LANGS)
    def page_link(k):
        name=t({'home':'homepage','research':'home'}.get(k,k))
        return f'<a href="{path(l,k)}"'+(' aria-current="page"' if p==k else '')+f'>{name}</a>'
    nav=''.join(page_link(k) for k in ('home','research','portfolio','papers'))
    more=''.join(page_link(k) for k in ('bio','docs','family','notes'))+link('#contact',t('contact'))
    theme='<label class="theme"><span aria-hidden="true">◐</span><select aria-label="'+t('theme')+'" id="theme">'+''.join(f'<option value="{k}">{t(k)}</option>' for k in ('system','light','dark'))+'</select></label>'
    search=f'''<button class="search-toggle" hidden aria-label="{t('search')}">⌕</button><dialog id="search-dialog"><form method="dialog"><label for="query">{t('search')}</label><button aria-label="{t('close')}">×</button></form><input type="search" id="query" placeholder="{t('search')}" autocomplete="off"><div id="results" data-empty="{t('nothing')}"></div></dialog>'''
    socials=''.join(link(u,n) for n,u in [('Google Scholar','https://scholar.google.com/citations?user=k05C_IgAAAAJ'),('ResearchGate','https://www.researchgate.net/profile/Pouya-Latifiyan'),('LinkedIn','https://www.linkedin.com/in/pouya-latifiyan/'),('GitHub','https://github.com/PouyaLatifiyan')])
    brand=f'<a class="brand" href="{path(l,"home")}"><span class="mark" aria-hidden="true">∿</span>{t("name")}</a>'
    head=f'<header><div class="bar wrap">{brand}<nav class="nav">{nav}<details class="langpick"><summary>{t("menu")} ⌄</summary><div class="langlist">{more}</div></details></nav><div class="tools">{theme}{search}<details class="langpick"><summary aria-label="{t("lang")} · {NAMES[l]}">{NAMES[l]} ⌄</summary><div class="langlist">{langs}</div></details></div></div></header>'
    footer=f'<footer id="contact"><div class="wrap"><div class="footrow"><div><span class="caption">{t("contact")}</span>{link("mailto:Pouya@BUAA.edu.cn","Pouya@BUAA.edu.cn")}</div><div class="footlinks">{socials}</div></div><nav class="footlinks footpages">{nav}{more}</nav><nav class="langs" aria-label="{t("lang")}">{langs}</nav></div></footer>'
    if p=='home': body=home(l,t)
    elif p=='research': body=research_page(l,t)
    elif p=='portfolio': body=project_page(l,t)
    elif p=='papers': body=sub(t('pub'),t('name'))+'<div class="paper-list">'+publications(t)+'</div>'
    elif p=='notes': body=sub(t('notes'),t('field'))+section(t('noteTitle'),t('noteBody')+'<div class="actions">'+button(path(l,'research')+'#framework',t('current'))+'</div>','timing')
    elif p=='bio': body=bio(l,t)
    elif p=='docs': body=docs(t)
    else: body=family(l,t,p)
    person={'@context':'https://schema.org','@type':'Person','@id':BASE+'/#person','name':'Pouya Latifiyan','url':BASE+'/','image':BASE+'/assets/portrait.webp','affiliation':{'@type':'CollegeOrUniversity','name':'Beihang University'},'knowsAbout':['Signal processing','Communication systems','Detection reliability','Dynamical systems']}
    extra='<meta name="robots" content="noindex,follow">' if blank else ''
    if p=='home':
        extra+='<script type="application/ld+json">'+json.dumps(person)+'</script>'
        if l=='en': extra+='<meta name="google-site-verification" content="google1af6c3eb30ceaa7e"><script defer src="/assets/legacy.js"></script>'
    return f'''<!doctype html>
<html lang="{l}" dir="{'rtl' if l in ('fa','ar') else 'ltr'}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>
<meta name="description" content="{descr}"><link rel="canonical" href="{url}">
{alt}<meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:title" content="{title}">
<meta property="og:description" content="{descr}"><meta property="og:image" content="{BASE}/assets/umbra.webp"><meta name="theme-color" content="#160f17">
<script src="/assets/theme.js?v=entrance"></script><link rel="stylesheet" href="/assets/site.css?v=umbra1"><script defer src="/assets/interaction.js?v=umbra1"></script>{extra}</head><body><a class="skip" href="#main">{t("skip")}</a>{head}<main id="main" class="wrap {'archive' if p!='home' else ''}">{body}</main>{footer}</body></html>
'''
from html.parser import HTMLParser
class SearchText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active=False
        self.words=[]
    def handle_starttag(self, tag, attrs):
        if tag=='main': self.active=True
    def handle_endtag(self, tag):
        if tag=='main': self.active=False
    def handle_data(self, data):
        if self.active and data.strip(): self.words.append(data.strip())
if __name__ == '__main__':
    alternates=''.join(f'<link rel="alternate" hreflang="{l}" href="{BASE+path(l,"home")}">' for l in LANGS)
    alternates+=f'<link rel="alternate" hreflang="x-default" href="{BASE}/">'
    choices=''.join(f'<a href="{path(l,"home")}" lang="{l}" hreflang="{l}"><bdi>{NAMES[l]}</bdi></a>' for l in LANGS)
    source=ROOT/'_source'
    gate=(source/'entrance.html').read_text().replace('<!-- LANGUAGE_ALTERNATES -->',alternates).replace('<!-- LANGUAGE_LINKS -->',choices).replace('/* ENTRANCE_STYLE */',(source/'entrance.css').read_text())
    (ROOT/'index.html').write_text(gate,encoding='utf-8')
    pages=[BASE+'/']
    for lang in LANGS:
        search_index=[]
        for key in SLUG:
            destination=ROOT/path(lang,key).strip('/')/'index.html'
            destination.parent.mkdir(parents=True,exist_ok=True)
            html=page(lang,key)
            destination.write_text(html,encoding='utf-8')
            if 'content="noindex,follow"' not in html:
                pages.append(BASE+path(lang,key))
                title=TEXT[{'home':'homepage','research':'home'}.get(key,key)][lang]
                parser=SearchText()
                parser.feed(html)
                search_index.append(dict(url=path(lang,key),title=title,text=' '.join(parser.words)))
        (ROOT/'assets'/f'search-{lang}.json').write_text(json.dumps(search_index,ensure_ascii=False),encoding='utf-8')
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{u}</loc></url>\n' for u in pages)+'</urlset>\n')
