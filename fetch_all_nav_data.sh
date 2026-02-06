#!/bin/bash

# 获取所有菜单数据
OUTPUT_FILE="/Users/goodin/coding/homepage/nav_eooce_com_all_data.json"

echo "[" > "$OUTPUT_FILE"

# 菜单列表
menus=(1 2 3 4 5 6 8 11)

# 子菜单列表 (menu_id:sub_menu_id)
submenus=(
  "8:1"
  "4:5"
  "4:3"
  "5:6"
  "5:7"
)

first=true

# 获取主菜单数据
for menu_id in "${menus[@]}"; do
  echo "Fetching menu $menu_id..."
  data=$(curl -s "https://nav.eooce.com/api/cards/$menu_id")
  
  if [ "$first" = true ]; then
    first=false
  else
    echo "," >> "$OUTPUT_FILE"
  fi
  
  # 提取并格式化数据
  echo "$data" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for card in data:
    print(json.dumps({
        'name': card['title'],
        'url': card['url'],
        'icon': card['display_logo'],
        'category': f'menu_{card[\"menu_id\"]}'
    }, ensure_ascii=False))
" | sed '$ ! s/$/,/' | sed '1 ! s/^/    /' >> "$OUTPUT_FILE"
done

# 获取子菜单数据
for submenu in "${submenus[@]}"; do
  menu_id=$(echo $submenu | cut -d: -f1)
  sub_id=$(echo $submenu | cut -d: -f2)
  
  echo "Fetching submenu $menu_id:$sub_id..."
  data=$(curl -s "https://nav.eooce.com/api/cards/$menu_id?subMenuId=$sub_id")
  
  echo "," >> "$OUTPUT_FILE"
  
  echo "$data" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for card in data:
    print(json.dumps({
        'name': card['title'],
        'url': card['url'],
        'icon': card['display_logo'],
        'category': f'menu_{card[\"menu_id\"]}',
        'sub_category': f'submenu_{card[\"sub_menu_id\"]}'
    }, ensure_ascii=False))
" | sed '$ ! s/$/,/' | sed '1 ! s/^/    /' >> "$OUTPUT_FILE"
done

echo "" >> "$OUTPUT_FILE"
echo "]" >> "$OUTPUT_FILE"

echo "Data saved to $OUTPUT_FILE"
