# HTTP сервер для отображения достижений пользователя

Программа собирает и отображает статистику пользователя с трёх платформ:
- **GitHub**: информация об аккаунте
- **Lichess**: данные шахматного профиля
- **Stepik**: информация об учётной записи на образовательной платформе

Данные обновляются по запросу и сохраняются в файл `data.json`. Веб-интерфейс доступен по адресу `http://localhost:5000`.

## Требования
- Python 3.8+
- Установленные зависимости из `requirements.txt`

## Установка и запуск
1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение:
Для Windows:
```bash
venv\Scripts\activate
```
Для Linux/macOS:
```bash
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Настройте конфигурационный файл (см. раздел **"Настройка конфигурации"**)

5. Запустите приложение:
```bash
python main.py
```

Приложение будет доступно по адресу: http://localhost:5000

---

## Настройка конфигурации

### 1. Создание конфигурационного файла
Создайте файл `config.json` в корне проекта и заполните по шаблону:
```json
{
  "github_username": "ВАШ_GITHUB_ЛОГИН",
  "github_token": "ВАШ_GITHUB_ТОКЕН",
  "user_name": "ВАШ_LICHESS_ЛОГИН",
  "user_id": "ВАШ_STEPIK_ID"
}
```

### 2. Получение токенов и идентификаторов
**GitHub Token**:
1. Перейдите в [Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
2. Создайте новый токен с правами:
   - `repo` (полный доступ к репозиториям)
   - `user` (чтение информации профиля)

**Lichess Username**:
- Используйте логин из профиля Lichess (например, из URL: `https://lichess.org/@/ваш_логин`)

**Stepik User ID**:
1. Откройте профиль на [Stepik.org](https://stepik.org)
2. Скопируйте ID из адресной строки:
   ```
   https://stepik.org/users/12345 → ID: 12345
   ```

---

## Обновление данных
- **Автоматическое**: при первом запуске и переходе на `/update`
- **Ручное обновление**:
  1. Перейдите по адресу: http://localhost:5000/update
  2. Или удалите файл `data.json` и перезапустите приложение

---

## Обновление версий пакетов
Для синхронизации зависимостей:

1. Обновите пакеты:
```bash
pip install --upgrade flask requests
```

2. Зафиксируйте изменения:
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Обновление версий пакетов"
```

---

## Структура проекта
```
├── main.py
├── config.json         # Конфиг 
├── data.json           # Кешированные данные
├── requirements.txt
└── templates/
    └── index.html     # HTML-шаблон
```

