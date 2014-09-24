#!/usr/bin/env python

import sys
import yaml
from jinja2 import Template
from asciidocapi import AsciiDocAPI
from StringIO import StringIO

t_content = ""
with open(sys.argv[1], 'r') as f:
    t_content = f.read().decode('utf8')
template = Template(t_content)
obj = yaml.load(sys.stdin)
sys.stderr.write(str(obj))

in_data = StringIO(template.render(obj).encode('utf8'))
out_data = StringIO()
asciidoc = AsciiDocAPI()
asciidoc.options('--no-header-footer')
asciidoc.execute(in_data, out_data, backend='xhtml11')
sys.stdout.write(out_data.getvalue())
