"""
主要将plantuml的mindmap写法转为vega可用的json文件
"""
import sys
import re
import json


def converter(puml_path: str):
    """
    传入puml文件路径进行解析转化
    1. 标题都是以*开头, 且一个*的都是根节点
    2. 父级节点只会比子级节点少一个*，如果当前节点比下一个节点少于超过一个*，puml就无法通过
    3. 如果下一个节点比上一个节点少*，就去对应列表里面找最后一个
    :param puml_path:
    :return:
    """
    print(f"开始处理{puml_path}...")
    levels = {}
    json_results = []
    with open(puml_path, 'r') as f:
        notes = extract_notes(f.read())

    with open(puml_path, 'r') as f:
        lines = [line for line in f.readlines()]
        title_index = 1
        for index, line in enumerate(lines):
            # 标题的*后面只会出现三种情况：空格、:、[
            if line.startswith('*'):
                stars, name, color, links = extract_stars_name_links_color(line)
                levels[stars] = (line, title_index)
                parent = levels.get(stars[:-1])
                node = {
                    "id": title_index,
                    "name": name,
                    # "size": len(name)
                    # "link": 'https://www.google.com'
                }
                if parent:
                    node["parent"] = parent[1]
                if links:
                    # 如果是有链接，就变成子节点
                    link_count = 1
                    for link_name, link in links.items():
                        title_index += 1
                        wrap_link_name = get_wrap_name(f"链接{link_count}: {link_name}")
                        child_node = {
                            "id": title_index,
                            "name": wrap_link_name,
                            "link": link,
                            "parent": node['id'],
                            "note": f'来自{node["name"]}的链接'
                        }
                        json_results.append(child_node)
                        link_count += 1
                if color:
                    node["color"] = '#' + color
                if index < len(lines) and lines[index + 1].startswith('<code>'):
                    note = notes.pop(0)
                    # print(f"弹出的注释：{note}")
                    node['note'] = note
                json_results.append(node)
                title_index += 1
    with open('test.json', 'w') as f:
        f.write(json.dumps(json_results))


def extract_stars_name_links_color(line=''):
    color = None
    links = re.findall('\[\[(.*?)\]\]', line)
    link_dict = {}
    for link in links:
        href, title = link.split(' ', 1)
        line = line.replace(f"[[{href} {title}]]", f" {title}")
        link_dict[title] = href
    try:
        stars = re.split('[ :\[]', line)[0]
        name = line[len(stars):]
        if name.startswith('[#'):  # 如果有颜色
            color = re.findall('\[#(.*?)\]', name)[0]
            name = name.split(']')[1]
        if name.startswith(':'):  # 如果有注释
            name = name[1:]
    except:
        print(line)
    wrap_name = get_wrap_name(name)
    return stars, wrap_name, color, link_dict


def get_wrap_name(name):
    # 统一添加换行符
    wrap_name = []
    space_count = 0
    for char in name:
        if char == ' ':
            space_count += 1
        if space_count == 3:
            char = '\n'
            space_count = 0
        wrap_name.append(char)
    return ''.join(wrap_name)


def extract_notes(text=''):
    #     text = '''
    #         ****:tail -n 80 customSpec.json
    # <code>
    #
    # 此命令显示 Wasm 二进制字段后面的最后部分，
    # 包括运行时使用的几个托盘的详细信息，
    # 例如 sudo 和 balances 托盘。
    # </code>;
    # ****:Modify the name field to identify this chain specification as a custom chain specification.
    # <code>
    #
    # "name": "My Custom Testnet",
    # </code>
    # ****:Modify aura field to specify the nodes
    # <code>
    #     '''
    # 同时匹配换行符
    # (?:pattern) 来解决方括号不适用的场景
    # [正则匹配所有字符（包括换行）_尐东东的博客-CSDN博客_正则匹配所有字符](https://blog.csdn.net/u011158908/article/details/105666329)
    notes = re.findall('\<code\>((?:.|\n)*?)\</code\>', text)
    return notes


def extract_links(text=''):
    links = re.findall('\[\[(.*?)\]\]', text)
    link_dict = {}
    for link in links:
        href, title = link.split(' ', 1)
        link_dict[title] = href
    return link_dict


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("请传入puml文件路径...")
    else:
        puml_path = sys.argv[1]
        if not puml_path.endswith('.puml'):
            print("请传入puml文件...")
    converter(puml_path)
