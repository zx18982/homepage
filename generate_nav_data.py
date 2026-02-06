#!/usr/bin/env python3
import json

# 所有数据
all_data = []

# ============ Home (menu_id=1) ============
home_cards = [
    {"name": "Notification", "url": "https://notification.eooce.xx.kg", "icon": "https://img.icons8.com/ios-filled/150/228BE6/reminders.png"},
    {"name": "Youtube", "url": "https://www.youtube.com", "icon": "https://img.icons8.com/ios-filled/100/ff1d06/youtube-play.png"},
    {"name": "Gmail", "url": "https://mail.google.com", "icon": "https://img.icons8.com/fluency/48/gmail-new.png"},
    {"name": "GitHub", "url": "https://github.com", "icon": "https://img.icons8.com/ios-filled/50/github.png"},
    {"name": "ip.sb", "url": "https://ip.ssss.nyc.mn", "icon": "https://ip.sb/favicon-32x32.png"},
    {"name": "Cloudflare", "url": "https://dash.cloudflare.com", "icon": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/50/external-cloudflare-provides-content-delivery-network-services-ddos-mitigation-logo-color-tal-revivo.png"},
    {"name": "指纹浏览器", "url": "https://www.adspower.net/share/laowang", "icon": "https://www.adspower.net/favicon.svg"},
    {"name": "Huggingface", "url": "https://huggingface.co", "icon": "https://img.icons8.com/fluency/48/hugging-face_app.png"},
    {"name": "ITDOG - 在线ping", "url": "https://www.itdog.cn/tcping", "icon": "https://www.itdog.cn/favicon.ico"},
    {"name": "Ping0", "url": "https://ping0.cc", "icon": "https://ping0.cc/favico.ico"},
    {"name": "浏览器指纹", "url": "https://www.browserscan.net/zh", "icon": "https://www.browserscan.net/favicon-32x32.png"},
    {"name": "nezha面板", "url": "https://ssss.nyc.mn", "icon": "https://nezha.wiki/logo.png"},
    {"name": "Api测试", "url": "https://hoppscotch.io", "icon": "https://hoppscotch.io/favicon.ico"},
    {"name": "域名检查", "url": "https://who.cx", "icon": "https://who.cx/favicon.ico"},
    {"name": "域名比价", "url": "https://www.nazhumi.com", "icon": "https://www.nazhumi.com/favicon.ico"},
    {"name": "NodeSeek", "url": "https://www.nodeseek.com", "icon": "https://www.nodeseek.com/static/image/favicon/favicon-32x32.png"},
    {"name": "Linux do", "url": "https://linux.do", "icon": "https://linux.do/uploads/default/optimized/3X/9/d/9dd49731091ce8656e94433a26a3ef36062b3994_2_32x32.png"},
    {"name": "在线音乐", "url": "https://music.eooce.com", "icon": "https://p3.music.126.net/tBTNafgjNnTL1KlZMt7lVA==/18885211718935735.jpg"},
    {"name": "Nodeloc", "url": "https://www.nodeloc.com", "icon": "https://s.rmimg.com/optimized/1X/660236e67b776cefea8b2df2276659af2f4eda2a_2_32x32.png"},
    {"name": "Moontv", "url": "https://moontv.cfapps.jp10.hana.ondemand.com", "icon": "https://moontv.cfapps.jp10.hana.ondemand.com/favicon.ico"},
    {"name": "订阅转换", "url": "https://sublink.eooce.com", "icon": "https://img.icons8.com/color/96/link--v1.png"},
    {"name": "webssh", "url": "https://ssh.eooce.com", "icon": "https://img.icons8.com/fluency/240/ssh.png"},
    {"name": "文件快递柜", "url": "https://filebox.nnuu.nyc.mn", "icon": "https://img.icons8.com/nolan/256/document.png"},
    {"name": "真实地址生成", "url": "https://address.nnuu.nyc.mn", "icon": "https://static11.meiguodizhi.com/favicon.ico"}
]

all_data.extend([{"category": "Home", **card} for card in home_cards])

print(f"Home: {len(home_cards)} items")

# 输出统计信息
print(f"Total items: {len(all_data)}")

# 保存到文件
with open("/Users/goodin/coding/homepage/nav_eooce_com_complete.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print("Data saved to nav_eooce_com_complete.json")
