---
layout: reference
title: "상한론"
desc: "송본 상한론1 〔서문 ∽ 辨痓濕暍〕"
tags: [상한금궤원문, 송본]
---



[刻《仲景全書》序]({{site.baseurl}}/reference/Books/Sinipets/조개미_중경전서_서)

[《傷寒論》序]({{site.baseurl}}/reference/Books/Sinipets/임억_상한론_서)

[《傷寒卒病論》集]({{site.baseurl}}/reference/Books/Sinipets/상한잡병론_집론)

[醫林列傳]({{site.baseurl}}/reference/Books/Sinipets/의림열전)

[國子監]({{site.baseurl}}/reference/Books/Sinipets/국자감_상서)


## 辨脉法第一

{% for idx in (1..37) %}

{% assign nooTail = idx | prepend: '000' | slice: -3, 3 %}
{% assign noo = "01-" | append: nooTail %}
{% include clause.md book="SHL_SongBM" noo=noo %}

{% endfor %}



## 平脉法第二

{% for idx in (1..50) %}

{% assign nooTail = idx | prepend: '000' | slice: -3, 3 %}
{% assign noo = "02-" | append: nooTail %}
{% include clause.md book="SHL_SongPM" noo=noo %}

{% endfor %}

## 傷寒例第三

{% for idx in (1..43) %}

{% assign nooTail = idx | prepend: '000' | slice: -3, 3 %}
{% assign noo = "03-" | append: nooTail %}
{% include clause.md book="SHL_SongL" noo=noo %}

{% endfor %}


## 辨痓濕暍脉證第四 <small>痙音◍又作痙去郢切下同</small>

{% for idx in (1..16) %}

{% assign nooTail = idx | prepend: '000' | slice: -3, 3 %}
{% assign noo = "04-" | append: nooTail %}
{% include clause.md book="SHL_SongCSG" noo=noo %}

{% endfor %}