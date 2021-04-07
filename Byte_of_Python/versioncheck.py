import sys
import warnings

if sys.version_info[0] < 3:
    warnings.warn('Для выполнения данной программы необходим как минимум Python 3.0', RuntimeWarning)
else:
    print('Всё хорошо')