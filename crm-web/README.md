# CRM-Web

## Tip!, Jupyter를 사용해서 Query를 확인하는 방법

```
import os

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

import django
django.setup()
```
