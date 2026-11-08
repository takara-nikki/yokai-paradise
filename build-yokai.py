# 把 fu-daoshi.html 包成自架網站 index.html（妖怪天国 / takara-nikki/yokai-paradise）
s=open('/home/claude/fu-daoshi.html',encoding='utf-8').read()
head=('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,user-scalable=no">'
 '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">'
 '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
 '<meta name="apple-mobile-web-app-title" content="タカラ妖怪天国"><meta name="theme-color" content="#161311">'
 '<meta name="description" content="Yokai Paradise — タカラ妖怪天国：N4 日文練習遊戲">'
 '<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="icon" href="icon-192.png">'
 '<style>:root{padding-top:env(safe-area-inset-top,0px);background:#161311}img{max-width:100%}[hidden]{display:none!important}html,body{overscroll-behavior:none}</style></head><body>')
open('/home/claude/yokai-paradise/index.html','w',encoding='utf-8').write(head+s+'</body></html>')
import json
m=json.load(open('/home/claude/yokai-paradise/manifest.webmanifest',encoding='utf-8'));m['name']='タカラ妖怪天国';m['short_name']='タカラ妖怪天国';m['description']='Yokai Paradise — タカラ妖怪天国：N4 日文練習遊戲';m['background_color']='#161311';m['theme_color']='#161311'
json.dump(m,open('/home/claude/yokai-paradise/manifest.webmanifest','w',encoding='utf-8'),ensure_ascii=False,indent=2)
