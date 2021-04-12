# CRM

## Use Jupyter

```
import os

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

import django
django.setup()
```
