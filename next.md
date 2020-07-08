---
title: next update
---

<ul>
{% for n in site.next %}
  <li>
    <a href="{{ n.url }}">
      {{ n.title }}
    </a>
  </li>
{% endfor %}
</ul>

