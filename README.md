# PythonStudy
DRF(Django REST framework)框架学习

# 重点
1.根据零时区转化获取上海时区当日零时
```python
import pytz
from django.utils import temezone

date_0_shanghai = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0, second=0)
```
