---
layout: default
title: Compatibility
description: "Which Maya and 3ds Max versions and renderers each LP Tools script and plugin supports, and which versions it has been tested in."
permalink: /compatibility/
---
<h1>Compatibility</h1>
<p class="lead">Which app versions each tool supports, and where it has been tested.</p>
<p>Maya 2026 runs the same Python as Maya 2025, so a tool tested in 2025 runs the same code in 2026. I test in Maya 2025 and 2027. The 3ds Max importer is tested in 3ds Max 2027.</p>
<div class="table-wrap"><table class="compat">
<thead><tr><th>Tool</th><th>App versions</th><th>Tested in</th><th>Notes</th></tr></thead>
<tbody>{% assign ts = site.tools | sort_natural: "name" %}{% for t in ts %}
<tr><td data-label="Tool"><a href="{{ t.url }}">{{ t.name }}</a></td><td data-label="App versions">{{ t.maya_versions }}</td><td data-label="Tested in">{{ t.maya_tested }}</td><td data-label="Notes">{{ t.compat_note }}</td></tr>{% endfor %}
</tbody></table></div>
<p class="note">Using a version or renderer that isn't listed, or something doesn't work? Email <a href="mailto:{{ site.support_email }}">{{ site.support_email_display }}</a> with the tool name and your app version. Requests help decide what gets tested and added next.</p>
