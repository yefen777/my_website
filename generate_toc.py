import os
import yaml

content_dir = "content"

toc = [{"file": "content/index.md"}]

for root, dirs, files in os.walk(content_dir):
    if root == content_dir:
        for d in dirs:
            children = []
            path = os.path.join(root, d)

            for f in os.listdir(path):
                if f.endswith(".ipynb") or f.endswith(".md"):
                    children.append({"file": f"{path}/{f}"})

            toc.append({
                "title": d,
                "children": children
            })

config = {
    "version": 1,
    "site": {"title": "算法笔记"},
    "project": {
        "toc": toc,
        "numbering": {"headings": True}
    }
}

with open("myst.yml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, allow_unicode=True)