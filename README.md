Build the site

```bash
./build_app_yaml.sh
cd gwax_nikola
nikola build
```

Type guessing for app.yaml building:

```python
import collections
import itertools
import mimetypes
import os

import magic  # pip install python-magic

ext_to_mime = collections.defaultdict(set)
ext_to_magic = collections.defaultdict(set)
for root, _, filenames in os.walk('static'):
    for filename in filenames:
        _, ext = os.path.splitext(filename)
        mime_guess = mimetypes.guess_type(filename, strict=False)
        ext_to_mime[ext].add(mime_guess)

        magic_guess = magic.from_file(os.path.join(root, filename), mime=True)
        ext_to_magic[ext].add(magic_guess)

print ext_to_mime
print ext_to_magic
```
