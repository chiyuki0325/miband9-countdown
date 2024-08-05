import json

charset = {}

with open('8105.dict.yaml', 'r') as f:
    for line in f.readlines():
        if line.strip().startswith('#'):
            continue

        if '\t' in line:
            line_split = line.split('\t')

            if len(line_split) != 3:
                continue

            char, pinyin, weight = line_split
            weight = int(weight[:-1])
            char_obj = {"char": char, "weight": weight}

            if pinyin not in charset:
                charset[pinyin] = [char_obj]
                continue

            if weight > charset[pinyin][0]['weight']:
                charset[pinyin].insert(0, char_obj)
            else:
                charset[pinyin].append(char_obj)

new_charset = {}

for k in charset:
    v = charset[k]
    new_v = ""
    for item in v:
        new_v += item["char"]
    new_charset[k] = new_v

with open("converted_dict.json", "w") as g:
    g.write(json.dumps(new_charset, ensure_ascii=False, separators=(',', ':')))
