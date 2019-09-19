---
lang: ja-JP
permalink: /var/
---

# var

var|val
---|---
site.url|{{site.url}}
site.time|{{site.time}}
title|{{title}}
name|{{name}}
path|{{path}}
lang|{{lang}}
:title|{{:title}}
:name|{{:name}}
:path|{{:path}}
:lang|{{::lang}}
page.url|{{page.url}}
page.title|{{page.title}}
page.name|{{page.name}}
page.path|{{page.path}}
page.lang|{{page.lang}}

## pages

{% for page in site.html_pages %}
- {{page.date}}: [{{ page.title }}]({{site.url}}{{ page.url }})
{% endfor %}
