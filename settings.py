﻿OBSERVATION_FOLDER = r'\\LAPTOP-JUJULQU5\test'  # какую папку сканировать на новые файлы
MOVE_FOLDER = r'\\LAPTOP-JUJULQU5\test1'  # в какую папку перемещать
SCAN_SUBFOLDERS = False  # сканировать или нет подпапки (True/False)
PAUSE_REFRESH_FOLDER = 60*1  # пауза между просмотром папки на новые файлы. в секундах  (3600 - 1 час)
MAX_DELTA_DAYS = 7  # если дата создания файла больше этого числа в днях, то подлежит удалению
MAX_ERRORS_COUNT = 3  # если количество подряд идущих ошибок превысит лимит, то отправит уведомление на почту

FROM_EMAIL = 'report.ap@mail.ru'  # с какой почты отправлять уведомление
FROM_PASSWORD = 'V9Z2cpLL3ckCHmjXfeeh'  # пароль от этой почты
TO_EMAIL = 'aryadnov@rbc.ru'  # на какую почту отправлять уведомление