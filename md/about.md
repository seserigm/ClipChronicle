---
lang: ja-JP
permalink: /about/
---

# About

var|val
---|---
Name|{{site.title}}
URL|{{site.url}}{{site.baseurl}}
Update|{{site.time}}

## Pages

Title|Path
---|---
{% for page in site.html_pages %}
[{{page.title}}]({{site.baseurl}}{{page.url}})|[{{site.baseurl}}{{page.url}}]({{site.baseurl}}{{ page.url}})
{% endfor %}

<style>
  thead { display: none; }
</style>
