"""Run python _source/build.py after editing translations or family biographies."""
from html import escape
from pathlib import Path
import json
from translations import LANGS, TEXT
from heritage import PEOPLE, PARENTS, ROLES

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://pouyalatifiyan.github.io'
NAMES = dict(zip(LANGS, ['English','فارسی','العربية','中文','Français']))
SLUG = {'home':'', 'bio':'biography/', 'docs':'credentials/', 'family':'family/', 'research':'research/', 'portfolio':'projects/', 'papers':'publications/', 'notes':'notes/'}
SLUG['art'] = 'art/'
SLUG.update({key: 'family/'+key+'/' for key in PEOPLE})
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
    framework = f'<section class="section feature" id="framework"><div>{label(t("current"))}<span class="display" lang="en">Alert</span><div class="signal-arc" aria-hidden="true"><i></i><i></i><i></i><b></b></div></div><div><h2>{t("framework")}</h2><p class="intro">{t("alertintro")}</p><p class="domains"><span class="caption">{t("applications")}</span>{t("domains")}</p></div></section>'
    future = ''.join(f'<article class="card"><h3>{t(k)}</h3><p>{t(d)}</p></article>' for k,d in [('ai','aitext'),('quantum','qtext')])
    highlights='<section class="section"><div class="sectionline"><h2>'+t('portfolio')+'</h2>'+link(path(l,'portfolio'),t('portfolio')+' '+arrow(),'quiet')+'</div><div class="cards">'+project_cards(l,t)+'</div></section>'
    art=f'<aside class="art-invite"><div>{label(t("art"))}<h2>{t("artisttitle")}</h2>{button(path(l,"art"),t("art"))}</div></aside>'
    return hero+affil+awards_showcase(l,t)+framework+highlights+f'<section class="section"><h2>{t("future")}</h2><div class="cards">{future}</div></section>'+art
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
def distinctions(t):
    profile = 'https://www.linkedin.com/in/pouya-latifiyan/'
    return [
        ('2026', t('award1'), 'Asia Simulation Federation International Summer School', t('team'), profile),
        ('2025', t('award2'), 'LuneX · NIVAS · NASA Space Apps Tokyo', t('team'), '/CV.pdf'),
        ('2025', t('commend'), '6th Kibo Robot Programming Challenge', t('teamreport'), 'https://eg.linkedin.com/in/mnar-hmdy-0680672aa'),
        ('2017', t('award3'), t('olymstages'), t('recognition'), profile),
        ('2009', t('beststudent'), t('ministry'), t('recognition'), profile),
    ]

def awards_showcase(l,t):
    tiles = []
    for year,title,venue,kind,url in distinctions(t)[:3]:
        tiles.append(f'<article class="honour"><div class="medal" aria-hidden="true"><i></i></div><span class="award-year">{year}</span><p class="award-type">{kind}</p><h3>{title}</h3><p>{venue}</p></article>')
    return f'<section class="section honours" id="awards"><div class="sectionline"><h2>{t("awards")}</h2>{link(path(l,"docs")+"#awards",t("full_awards")+" "+arrow(),"quiet")}</div><div class="honour-grid">{"".join(tiles)}</div></section>'

def docs(t):
    top=sub(t('docs'),t('docintro'),t('name'),'<div class="actions">'+button('/CV.pdf',t('cv')+' · PDF')+'</div>')
    awards=''.join(entry(title,venue+'<br>'+link(url,t('teamreport') if kind==t('teamreport') else ('CV · PDF' if url.endswith('.pdf') else t('profile'))),year) for year,title,venue,kind,url in distinctions(t))
    return top+section(t('edu'),education(t),'education')+section(t('awards'),awards,'awards')
def person_name(t,key):
    return t('name' if key=='bio' else 'name-'+key)


def family(l,t,p):
    def node(key, role=None):
        title=person_name(t,key)
        subtitle=f'<small>{t(role)}</small>' if role else ''
        return link(path(l,key),subtitle+f'<bdi class="kin-name">{title}</bdi>','kin-node')

    if p=='family':
        def branch(parent,heading):
            grandparents=''
            for grand in PARENTS[parent]:
                ancestors=''.join('<li>'+node(key)+'</li>' for key in PARENTS.get(grand,()))
                if ancestors:
                    ancestors=f'<div class="kin-caption">{t("kinparents")}</div><ul class="twigs">{ancestors}</ul>'
                sibling=''
                if grand=='maternal-grandmother':
                    sibling=f'<div class="collateral">{node("aminollah-rezaei","siblingof")}</div>'
                grandparents+=f'<li>{node(grand,grand)}{ancestors}{sibling}</li>'
            return f'<section class="branch"><h2>{t(heading)}</h2>{node(parent,parent)}<div class="kin-caption">{t("kinparents")}</div><ul class="limbs">{grandparents}</ul></section>'
        canopy=branch('father','pbranch')+branch('mother','mbranch')
        return sub(t('familytitle'),t('familyintro'))+f'<div class="pedigree"><div class="generation"><h2>{t("familychildren")}</h2><div>{node("bio")}{node("sister")}</div></div><div class="canopy">{canopy}</div></div>'
    children=[key for key,parents in PARENTS.items() if p in parents]
    parents=PARENTS.get(p,())
    siblings=[key for key,family_parents in PARENTS.items() if key!=p and parents and family_parents==parents]
    relations=''
    for group,keys in [('kinparents',parents),('children',children),('siblings',siblings)]:
        if keys:
            relations+=f'<section class="relation"><h2>{t(group)}</h2><div>'+''.join(node(key) for key in keys)+'</div></section>'
    sources=''.join('<li>'+link(url,escape(title))+'</li>' for title,url in PEOPLE[p])
    references=f'<section class="references"><h2>{t("sources")}</h2><ul>{sources}</ul></section>' if sources else ''
    return sub(person_name(t,p),t('bio-'+p),t(ROLES.get(p,p)))+f'<p class="record-note">{t("familyrecord")}</p><div class="relations">{relations}</div>{references}<div class="actions">{button(path(l,"family"),t("familytitle"))}</div>'


def art_page(l,t):
    attribution=link('https://www.metmuseum.org/art/collection/search/453983',t('museumcredit'))
    image=f'<figure class="artwork"><img src="/assets/nastaliq-panel.webp" alt="{t("museumcredit")}" width="388" height="623"><figcaption>{attribution}</figcaption></figure>'
    text=f'<section><h2>{t("guild")}</h2><p>{t("guildtext")}</p>{link("https://www.linkedin.com/in/pouya-latifiyan/","LinkedIn ↗","quiet")}</section><section><h2>{t("exhibitions")}</h2><p>{t("exhibittext")}</p></section>'
    return sub(t('artisttitle'),t('artistintro'),t('art'))+f'<div class="atelier">{image}<div class="art-notes">{text}</div></div>'


def research_page(l,t):
    return sub(t('current'),t('identity'),t('scope'))+section('Alert','<h3>'+t('framework')+'</h3><p class="intro">'+t('alertintro')+'</p><p class="domains">'+t('domains')+'</p>','framework')+section(t('future'),entry(t('ai'),t('aitext'))+entry(t('quantum'),t('qtext')),'future')
def project_page(l,t):
    return sub(t('portfolio'),t('biotitle'),t('name'))+section('Alert',t('alertintro')+'<div class="actions">'+button(path(l,'research')+'#framework',t('current'))+'</div>','alert')+'<div class="cards">'+project_cards(l,t)+'</div><div class="actions">'+link('https://github.com/lunex-project-2025/NIVAS','NIVAS · GitHub '+arrow(),'quiet')+'</div>'
def page(l,p):
    def t(k): return escape(TEXT[k][l])
    url=BASE+path(l,p)
    title=(t('name')+' | '+t('field')+' · Beihang University') if p=='home' else ((person_name(t,p) if p in PEOPLE else t('home' if p=='research' else p))+' | '+t('name'))
    descr=t('bio-'+p) if p in PEOPLE else t({'home':'intro','bio':'story','docs':'docintro','family':'familyintro','art':'artistintro','research':'alertintro','portfolio':'identity','papers':'pub','notes':'noteTitle'}[p])
    alt=''.join(f'<link rel="alternate" hreflang="{a}" href="{BASE+path(a,p)}">' for a in LANGS)
    default_url=BASE+('/' if p=='home' else path('en',p))
    alt+=f'<link rel="alternate" hreflang="x-default" href="{default_url}">'
    langs=''.join(f'<a href="{path(a,p)}" hreflang="{a}" lang="{a}" dir="auto"'+(' aria-current="true"' if a==l else '')+f'>{NAMES[a]}</a>' for a in LANGS)
    def page_link(k):
        name=t({'home':'homepage','research':'home'}.get(k,k))
        return f'<a href="{path(l,k)}"'+(' aria-current="page"' if p==k else '')+f'>{name}</a>'
    nav=''.join(page_link(k) for k in ('home','research','portfolio','papers'))
    nav+=link(path(l,'home')+'#awards',t('awards'))
    more=''.join(page_link(k) for k in ('bio','docs','family','art','notes'))+link('#contact',t('contact'))
    theme='<label class="theme"><span aria-hidden="true">◐</span><select aria-label="'+t('theme')+'" id="theme">'+''.join(f'<option value="{k}">{t(k)}</option>' for k in ('system','light','dark'))+'</select></label>'
    search=f'<button type="button" class="search-toggle" hidden>{t("search")} <span aria-hidden="true">⌕</span></button>'
    dialog=f'<dialog id="search-dialog" aria-labelledby="search-label"><form method="dialog"><label id="search-label" for="query">{t("search")}</label><button aria-label="{t("close")}">×</button></form><input type="search" id="query" autocomplete="off"><div id="results" data-empty="{t("nothing")}"></div></dialog>'
    socials=''.join(link(u,n) for n,u in [('Google Scholar','https://scholar.google.com/citations?user=k05C_IgAAAAJ'),('ResearchGate','https://www.researchgate.net/profile/Pouya-Latifiyan'),('LinkedIn','https://www.linkedin.com/in/pouya-latifiyan/'),('GitHub','https://github.com/PouyaLatifiyan')])
    brand=f'<a class="brand" href="{path(l,"home")}"><span class="mark" aria-hidden="true">∿</span>{t("name")}</a>'
    head=f'''<header><div class="bar wrap">{brand}<details class="menu"><summary aria-label="{t("menu")}"><span class="hamburger" aria-hidden="true"><i></i><i></i><i></i></span></summary>
    <div class="menu-sheet"><nav aria-label="{t("menu")}">{nav}{more}</nav><section><h2>{t("settings")}</h2><div class="preferences">{theme}{search}</div></section><section><h2>{t("lang")}</h2><div class="menu-languages">{langs}</div></section></div></details></div></header>{dialog}'''
    footer=f'<footer id="contact"><div class="wrap"><div class="footrow"><div><span class="caption">{t("contact")}</span>{link("mailto:Pouya@BUAA.edu.cn","Pouya@BUAA.edu.cn")}</div><div class="footlinks">{socials}</div></div><nav class="footlinks footpages">{nav}{more}</nav><nav class="langs" aria-label="{t("lang")}">{langs}</nav></div></footer>'
    if p=='home': body=home(l,t)
    elif p=='research': body=research_page(l,t)
    elif p=='portfolio': body=project_page(l,t)
    elif p=='papers': body=sub(t('pub'),t('name'))+'<div class="paper-list">'+publications(t)+'</div>'
    elif p=='notes': body=sub(t('notes'),t('field'))+section(t('noteTitle'),t('noteBody')+'<div class="actions">'+button(path(l,'research')+'#framework',t('current'))+'</div>','timing')
    elif p=='bio': body=bio(l,t)
    elif p=='docs': body=docs(t)
    elif p=='art': body=art_page(l,t)
    else: body=family(l,t,p)
    person={'@context':'https://schema.org','@type':'Person','@id':BASE+'/#person','name':'Pouya Latifiyan','url':BASE+'/','image':BASE+'/assets/portrait.webp','affiliation':{'@type':'CollegeOrUniversity','name':'Beihang University'},'knowsAbout':['Signal processing','Communication systems','Detection reliability','Dynamical systems']}
    extra=''
    if p=='home':
        extra+='<script type="application/ld+json">'+json.dumps(person)+'</script>'
        if l=='en': extra+='<meta name="google-site-verification" content="google1af6c3eb30ceaa7e"><script defer src="/assets/legacy.js"></script>'
    return f'''<!doctype html>
<html lang="{l}" dir="{'rtl' if l in ('fa','ar') else 'ltr'}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>
<meta name="description" content="{descr}"><link rel="canonical" href="{url}">
{alt}<meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:title" content="{title}">
<meta property="og:description" content="{descr}"><meta property="og:image" content="{BASE}/assets/umbra.webp"><meta name="theme-color" content="#160f17">
<script src="/assets/theme.js?v=entrance"></script><link rel="stylesheet" href="/assets/site.css?v=heritage1"><script defer src="/assets/interaction.js?v=heritage1"></script>{extra}</head><body class="page-{p} {'profile-page' if p in PEOPLE else ''}"><a class="skip" href="#main">{t("skip")}</a>{head}<main id="main" class="wrap {'archive' if p!='home' else ''}">{body}</main>{footer}</body></html>
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
                title=TEXT['name-'+key if key in PEOPLE else {'home':'homepage','research':'home'}.get(key,key)][lang]
                parser=SearchText()
                parser.feed(html)
                search_index.append(dict(url=path(lang,key),title=title,text=' '.join(parser.words)))
        (ROOT/'assets'/f'search-{lang}.json').write_text(json.dumps(search_index,ensure_ascii=False),encoding='utf-8')
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{u}</loc></url>\n' for u in pages)+'</urlset>\n')
