"""Generate crawlable store pages: python3 tools/build_stores.py."""
from pathlib import Path
from html import escape as esc
import json
import re
from urllib.parse import urlsplit
ROOT = Path(__file__).resolve().parents[1]
TODO = 'TODO: 正式情報確認'
data = json.loads((ROOT / 'data/stores.json').read_text())
assets = json.loads((ROOT / 'data/assets.json').read_text())
site_url = data.get('site_url')
if site_url and (urlsplit(site_url).scheme != 'https' or not urlsplit(site_url).netloc or urlsplit(site_url).path not in ('', '/') or urlsplit(site_url).query or urlsplit(site_url).fragment):
    raise ValueError('site_url must be the confirmed HTTPS origin, without a path')
slugs = [s['slug'] for s in data['stores']]
if len(slugs) != len(set(slugs)) or any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', v) for v in slugs):
    raise ValueError('Store slugs must be unique URL-safe path components')
def e(value): return esc(str(value), quote=True)
def link(value, label):
    return f'<a class="button" href="{e(value)}">{e(label)}</a>' if value else f'<p>{e(label)}：{TODO}</p>'
reports=[]
for s in data['stores']:
    path=f"/stores/{s['slug']}/"
    canonical=data['site_url'].rstrip('/')+path if data['site_url'] else None
    schema={'@context':'https://schema.org','@type':'Restaurant','name':s['name'],'servesCuisine':['もんじゃ焼き','鉄板焼き']}
    if canonical: schema.update(url=canonical, **{'@id':canonical+'#restaurant'})
    if s['address']: schema['address']={'@type':'PostalAddress',**s.get('address_parts', {'streetAddress':s['address']}),'addressCountry':'JP'}
    if s['telephone']: schema['telephone']=s['telephone']
    if s.get('opening_hours'):
        schema['openingHoursSpecification']=[{'@type':'OpeningHoursSpecification','dayOfWeek':['https://schema.org/'+d for d in h['days']],'opens':h['opens'],'closes':h['closes']} for h in s['opening_hours']]
    if s['map_url']: schema['hasMap']=s['map_url']
    if s['instagram']: schema['sameAs']=[s['instagram']]
    if canonical and s['photos']: schema['image']=[data['site_url'].rstrip('/')+p['src'] if p['src'].startswith('/') else p['src'] for p in s['photos']]
    metadata=f'<link rel="canonical" href="{e(canonical)}"><meta property="og:url" content="{e(canonical)}">' if canonical else f'<!-- canonical / og:url: {TODO}（公式ドメイン） -->'
    if canonical:
        share_image = schema['image'][0] if s['photos'] else data['site_url'].rstrip('/')+assets['logo']
        metadata+=f'<meta property="og:image" content="{e(share_image)}"><meta property="og:image:alt" content="{e(s["photos"][0]["alt"] if s["photos"] else "もんじゃ駒と ロゴ")}">'
    else: metadata+=f'<!-- og:image: {TODO}（公式ドメイン） -->'
    breadcrumb_schema = {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'TOP','item':data['site_url'].rstrip('/')+'/'},{'@type':'ListItem','position':2,'name':s['name'],'item':canonical}]} if canonical else None
    breadcrumb_json = '<script type="application/ld+json">'+json.dumps(breadcrumb_schema,ensure_ascii=False).replace('<',chr(92)+'u003c')+'</script>' if breadcrumb_schema else ''
    info=''.join(f'<dt>{label}</dt><dd>{e(s.get(key)) if s.get(key) else TODO}</dd>' for label,key in [('住所','address'),('電話番号','telephone'),('営業時間','hours'),('定休日','closed_days'),('ラストオーダー','last_order'),('最寄駅・アクセス','access')])
    if s['telephone']: info+=f'<dt>電話でのお問い合わせ</dt><dd><a href="tel:{e(s["telephone"])}">電話する</a></dd>'
    photos=''.join(f'<figure><img loading="lazy" src="{e(p["src"])}" alt="{e(p["alt"])}"></figure>' for p in s['photos']) or f'<div class="placeholder">店舗外観・店内写真<br>{TODO}</div>'
    faq=''.join(f'<details><summary>{e(f["question"])}</summary><p>{e(f["answer"]) if f.get("answer") else TODO}</p></details>' for f in s['faq'])
    siblings=''.join(f'<a href="/stores/{v["slug"]}/">{e(v["name"])}</a>' for v in data['stores'] if v['slug']!=s['slug'])
    map_html=f'<iframe title="{e(s["name"])}のGoogleマップ" src="{e(s["map_embed_url"])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>' if s['map_embed_url'] else f'<p>Googleマップ：{TODO}</p>'
    menus=''.join(f'<li>{e(m)}</li>' for m in s['popular_menu']) or f'<li>店舗別の人気メニュー：{TODO}</li>'
    html=f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(s['title'])}</title><meta name="description" content="{e(s['description'])}">
{metadata}<meta property="og:type" content="website"><meta property="og:locale" content="ja_JP"><meta property="og:site_name" content="もんじゃ駒と"><meta property="og:title" content="{e(s['title'])}"><meta property="og:description" content="{e(s['description'])}">
<link rel="stylesheet" href="/assets/stores/stores.css">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False).replace('<',chr(92)+'u003c')}</script>{breadcrumb_json}</head>
<body><a class="skip" href="#main">本文へ</a><header><div class="wrap nav"><a href="/"><img class="logo" src="{assets['logo']}" alt="もんじゃ駒と TOP"></a><nav aria-label="メイン"><a href="/monja_komato_menu_final.html">メニュー</a><a class="button" href="#reservation">予約案内</a></nav></div></header>
<main id="main" class="wrap"><nav class="breadcrumb" aria-label="パンくず"><ol><li><a href="/">TOP</a></li><li aria-current="page">{e(s['name'])}</li></ol></nav>
<section class="hero"><div><p class="kicker">MONJA KOMATO / {e(s['area'])}</p><h1>{e(s['name'])}</h1><p>{e(s['description'])}</p><a class="button" href="#reservation">ご予約・お問い合わせ</a><a class="text-link" href="#access">店舗情報・アクセス</a></div><figure><img src="{assets['food']}" alt="もんじゃ駒との料理イメージ（共通メニュー写真）"><figcaption>共通メニューの料理イメージ。店舗別の提供内容：{TODO}</figcaption></figure></section>
<section><p class="kicker">SCENES</p><h2>{e(s['area'])}でのお食事を計画する方へ</h2><div class="cards">{''.join(f'<article><h3>{e(v)}</h3><p>{e(s["scene_descriptions"].get(v, TODO))}</p></article>' for v in s['scenes'])}</div></section>
<section id="access"><p class="kicker">INFORMATION & ACCESS</p><h2>店舗情報・アクセス</h2><div class="panel"><dl>{info}</dl><p class="note">営業時間はご提供のTOP完成版に基づきます。祝日は上記の土日祝の時間をご確認ください。臨時休業・祝日の個別日程：{TODO}</p>{map_html}<p class="note">地図は店名・住所による検索表示です。正確な店舗ピン・Place ID：{TODO}</p>{link(s['map_url'],'Googleマップで確認')}{link(s['instagram'],'公式Instagram')}</div></section>
<section><p class="kicker">GALLERY</p><h2>店舗写真</h2><div class="cards">{photos}</div></section>
<section><p class="kicker">MENU</p><h2>人気メニュー</h2><div class="panel"><ul>{menus}</ul><p>共通メニュー掲載：明太もちチーズもんじゃ・こまとスペシャルもんじゃ。店舗別の提供・価格・人気順位：{TODO}</p><a class="text-link" href="/monja_komato_menu_final.html">メニューを見る</a></div></section>
<section><p class="kicker">FAQ</p><h2>よくあるご質問</h2>{faq}</section>
<section id="reservation" class="reservation"><h2>{e(s['name'])}のご予約・お問い合わせ</h2>{link('tel:'+s['telephone'] if s['telephone'] else None,'電話で予約・問い合わせ')}{link(s['reservation'],'オンライン予約')}<p>電話予約の受付条件・受付時間：{TODO}</p></section>
<section><h2>ほかの店舗を探す</h2><nav class="store-links" aria-label="ほかの店舗">{siblings}</nav></section></main>
<footer class="wrap"><p>© MONJA KOMATO / SUMIKOMA Inc.</p></footer></body></html>'''
    dest=ROOT/path.strip('/')/'index.html'; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(html)
    reports.append({'url':path,'title':s['title'],'h1':s['name'],'meta_description':s['description'],'canonical':canonical or TODO,'og_url':canonical or TODO,'og_image':share_image if canonical else TODO,'json_ld':schema,'breadcrumb_json_ld':breadcrumb_schema})
(ROOT/'data/seo-report.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
print(f"Generated {len(reports)} store pages")
