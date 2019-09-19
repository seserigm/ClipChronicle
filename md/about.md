---
lang: ja-JP
permalink: /about/
---

# About

var|val
---|---
name|{{site.title}}
url|{{site.url}}{{site.baseurl}}
update|{{site.time}}

## Pages

{% for page in site.html_pages %}
- [
    {{page.title}}  
    {{site.baseurl}}{{page.url}}
  ]({{site.baseurl}}{{ page.url}})  
{% endfor %}

<style>
  thead { display: none; }
</style>
