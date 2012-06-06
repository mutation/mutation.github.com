#!/usr/bin/python

import os

html = "<html><head></head><body>%(body)s<br /></body></html>"

for p, d, f in os.walk(os.getcwd()):
    d[:] = [x for x in d if not x.startswith('.')] # hide hidden dirs
    if p == os.getcwd():
        continue

    body = "<ul>"
    body += "<br />".join(["<li><a href=\"%s\">%s</a></li>" % \
            (x, x.replace("-", " ").title())  for x in sorted(f) if x != "index.html"])
    body += "</ul>"

    with open("%s/index.html" % p, "w") as indexfile:
        indexfile.write(html % {"body": body})
