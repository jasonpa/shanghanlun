

<!--원문인용 시작. 상위에서 from, noo 지정 필요-->

{% assign itemms = site.data.compare.SHLtext | where: include.from, include.noo %}

{% assign targets = itemms | map: 'GGYL' %}

{% for ts in targets %}
{% for t in ts %}
{% if t %}

{% include clause.md book="GGYL" noo=t %}

{% endif %}
{% endfor %}
{% endfor %}

<!--원문인용 끝-->