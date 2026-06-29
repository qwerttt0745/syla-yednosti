<div align="center">

# 🛡️ Сила Єдності

### Інформаційна система волонтерського благодійного фонду

*Автоматизація збору, обробки та обліку заявок на матеріальну допомогу від військових підрозділів ЗСУ*

---

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=flat-square&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/Ліцензія-MIT-green?style=flat-square)

</div>

---

## 📋 Зміст

1. [Про проєкт](#1-про-проєкт)
2. [Стек технологій та обґрунтування вибору](#2-стек-технологій-та-обґрунтування-вибору)
3. [Архітектура системи](#3-архітектура-системи)
4. [Структура проєкту](#4-структура-проєкту)
5. [Моделі даних та база даних](#5-моделі-даних-та-база-даних)
6. [Модулі та компоненти](#6-модулі-та-компоненти).
7. [Бізнес-логіка та сценарії використання](#7-бізнес-логіка-та-сценарії-використання)
8. [Безпека системи](#8-безпека-системи)
9. [Середовище розробки та Docker](#9-середовище-розробки-та-docker)
10. [Швидкий старт](#10-швидкий-старт)
11. [Змінні оточення](#11-змінні-оточення)
12. [Команди Makefile](#12-команди-makefile)
13. [URL-маршрути](#13-url-маршрути)
14. [Ролі та права доступу](#14-ролі-та-права-доступу)
15. [Функціональні та нефункціональні вимоги](#15-функціональні-та-нефункціональні-вимоги)
16. [Управління базою даних](#16-управління-базою-даних)
17. [Розробник](#17-розробник)

---

## 1. Про проєкт

**«Сила Єдності»** — веб-орієнтована інформаційна система, розроблена для автоматизації діяльності волонтерського благодійного фонду, що надає матеріальну допомогу підрозділам Збройних Сил України.

### Проблема, яку вирішує система

До впровадження системи волонтерський фонд вів облік заявок у месенджерах (Telegram, Viber) та Excel-таблицях. Це призводило до:

- **Втрати заявок** — повідомлення губились у загальних чатах
- **Дублювання роботи** — кілька волонтерів брались за одну заявку
- **Відсутності звітності** — неможливо було автоматично формувати звіти для донорів
- **Непрозорості процесу** — жодного журналу хто, коли і що зробив
- **Відсутності зворотного зв'язку** — військовий не міг дізнатись статус свого запиту

### Що вирішує ця система

```
Заявка від військового → Унікальний код → Реєстр волонтерів → Закупівля → Звіт для донорів
   (публічна форма)      (A3F7-2B19)     (дашборд + фільтри)  (IN-BUY форма) (Excel .xlsx)
```

Система є **єдиним цифровим реєстром** усіх заявок із повним відстеженням статусів, автоматичним журналом аудиту, вбудованою звітністю та публічним трекінгом стану заявки.

### Ключові переваги

| Перевага | Опис |
|---|---|
| 📱 Мобільна доступність | Публічна форма оптимізована для смартфонів — військові заповнюють з поля |
| 🔒 Без реєстрації | Військовим не потрібен обліковий запис для подачі заявки |
| 🔑 Безпечний трекінг | Унікальний код доступу замість порядкового ID захищає від несанкціонованого перегляду |
| 📊 Автоматична звітність | Excel-звіт для донорів генерується в 1 клік |
| 🕵️ Повний аудит | Кожна зміна фіксується: хто, коли, що змінив |
| 🔄 Контроль дублювання | Система блокує взяття заявки якщо вона вже в роботі |

---

## 2. Стек технологій та обґрунтування вибору

### 2.1 Бекенд

#### Python 3.12
**Роль:** Основна мова програмування всієї системи.

**Чому обрано:**
- Найпопулярніша мова для веб-розробки у 2024–2025 роках
- Django написаний на Python — нативна підтримка без мостів
- Широка екосистема: `openpyxl` (Excel), `Pillow` (зображення), `psycopg2` (PostgreSQL), `secrets` (криптографічно стійка генерація кодів)
- Читабельний синтаксис — легко підтримувати та розширювати

#### Django 5.x
**Роль:** Full-stack MVT веб-фреймворк — основа всього застосунку.

**Чому обрано:**
- Принцип «batteries included»: вбудовані ORM, автентифікація, адмін-панель, форми, CSRF-захист, міграції БД — не потрібні десятки окремих бібліотек
- Зріла екосистема з активною спільнотою та LTS-підтримкою
- Django ORM захищає від SQL-ін'єкцій на рівні фреймворку
- Вбудована система міграцій — версіонування схеми БД «з коробки»
- Django Admin — безкоштовна адмін-панель без додаткового коду

**Ключові модулі Django:**
```
django.contrib.auth      → автентифікація, сесії, хешування паролів
django.contrib.admin     → адмін-панель
django.db                → ORM, міграції, транзакції
django.forms             → форми, валідація
django.contrib.messages  → flash-повідомлення
django.db.models.signals → реактивна логіка (AuditLog)
```

### 2.2 База даних

#### PostgreSQL 16
**Роль:** Основна СУБД системи.

**Чому обрано:**
- Повна підтримка ACID-транзакцій — цілісність даних гарантована
- Значно потужніший за SQLite для багатокористувацького режиму
- Офіційний Django-драйвер `psycopg2` — стабільна інтеграція
- Підтримка складних запитів, індексів, JSON-полів
- Запускається в Docker без конфігурації

### 2.3 Фронтенд

#### Bootstrap 5.3 + Bootstrap Icons
**Роль:** CSS/JS фреймворк для побудови інтерфейсу.

**Чому обрано:**
- Mobile-first підхід — критично важливо, бо військові заповнюють форму з телефону
- Готові компоненти: `navbar`, `table`, `badge`, `card`, `form` — не потрібно писати CSS з нуля
- Підключається через CDN — немає потреби у Node.js, Webpack, збірці
- Bootstrap Icons — 1900+ іконок у тому ж пакеті

#### Django Template Language (DTL)
**Роль:** Серверний рендеринг HTML-шаблонів.

**Чому обрано:**
- Нативна підтримка Django — не потрібен окремий фронтенд-фреймворк (React/Vue)
- Безпечний рендеринг: автоматичне екранування XSS
- Наслідування шаблонів (`{% extends %}`) — єдиний `base.html` без дублювання

### 2.4 Генерація звітів

#### openpyxl 3.1
**Роль:** Генерація Excel-файлів (.xlsx) для звітності.

**Чому обрано:**
- Єдина Python-бібліотека що повноцінно підтримує формат .xlsx
- Стилізація: шрифти, кольори, рамки, об'єднання клітинок
- Немає залежності від встановленого Microsoft Office
- Повертає bytes — Django відправляє напряму як HTTP-відповідь

#### Pillow 10
**Роль:** Обробка та валідація завантажених зображень (фото чеків).

**Чому обрано:**
- Стандартна Python-бібліотека для роботи із зображеннями
- Потрібна для `ImageField` у Django моделі `Purchase`

### 2.5 Безпека

#### secrets (стандартна бібліотека Python)
**Роль:** Криптографічно стійка генерація унікальних кодів доступу до заявок.

**Чому обрано:**
- Модуль зі стандартної бібліотеки Python — без зовнішніх залежностей
- `secrets.token_hex()` генерує байти з `/dev/urandom` (OS CSPRNG)
- На відміну від `random` — не піддається передбаченню навіть при знанні попередніх значень
- Використовується для генерації кодів виду `A3F7-2B19` (захист від перебору: 4 млрд+ варіантів)

### 2.6 Інфраструктура

#### Docker + Docker Compose v2
**Роль:** Контейнеризація та управління середовищем розробки.

**Чому обрано:**
- Однакове оточення на будь-якій машині — «у мене працює» перестає бути проблемою
- PostgreSQL у контейнері — не потрібно встановлювати локально
- Bind mount коду — hot reload при змінах файлів без перезапуску контейнера
- Ізоляція сервісів: `web` і `db` у власній мережі

#### Git
**Роль:** Система контролю версій.

**Практики:**
- `.gitignore` виключає: `__pycache__`, `.env`, `media/`, `staticfiles/`
- `.env.example` — шаблон для нових розробників (без реальних секретів)

### 2.7 Додаткові інструменти

#### python-decouple
Читає змінні оточення з `.env` файлу. Відокремлює конфігурацію від коду.

#### django-debug-toolbar *(тільки local)*
Панель налагодження: SQL-запити, час виконання, сесії. Тільки у режимі `DEBUG=True`.

---

## 3. Архітектура системи

### 3.1 Загальна схема (трирівнева архітектура)

```
┌─────────────────────────────────────────────────────────┐
│                  РІВЕНЬ ПРЕДСТАВЛЕННЯ                   │
│         Bootstrap 5 + Django Templates (DTL)            │
│   base.html → dashboard.html, create_request.html ...   │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP Request/Response
┌─────────────────────▼───────────────────────────────────┐
│                 РІВЕНЬ БІЗНЕС-ЛОГІКИ                    │
│                                                         │
│  Django Views             Services                      │
│  ┌───────────────────┐  ┌────────────────┐              │
│  │create_request     │  │ FilterService  │              │
│  │request_success    │  │ StatusService  │              │
│  │check_request_stat │  │RequestValidator│              │
│  │dashboard          │  │ ReportEngine   │              │
│  │request_detail     │  └────────────────┘              │
│  │export_report      │                                  │
│  └───────────────────┘                                  │
│                                                         │
│  Django Middleware: Security → Session → CSRF → Auth    │
└─────────────────────┬───────────────────────────────────┘
                      │ Django ORM
┌─────────────────────▼───────────────────────────────────┐
│                    РІВЕНЬ ДАНИХ                         │
│                                                         │
│  Models: CustomUser, Request (+ access_code),           │
│          Category, Comment, AuditLog, Purchase          │
│                                                         │
│              PostgreSQL 16                              │
└─────────────────────────────────────────────────────────┘
```

### 3.2 Патерн MVT (Model–View–Template)

Django реалізує власну варіацію класичного MVC, яка називається **MVT**:

| Шар | Файли | Відповідальність |
|---|---|---|
| **Model** | `apps/*/models.py` | Структура даних, зв'язки між таблицями, валідація на рівні БД |
| **View** | `apps/*/views.py` | Отримує HTTP-запит → викликає сервіси → формує контекст → повертає відповідь |
| **Template** | `templates/**/*.html` | HTML-розмітка з DTL-тегами, відображає дані з контексту |
| **Services** *(розширення)* | `apps/*/services/*.py` | Складна бізнес-логіка, ізольована від View |

### 3.3 Потік HTTP-запиту (детально)

```
1. Браузер → HTTP GET/POST → localhost:8000
2. Docker port mapping 8000:8000 → контейнер web
3. Django runserver приймає запит
4. Middleware-ланцюжок (в порядку виконання):
   a. SecurityMiddleware       — HTTPS-заголовки
   b. SessionMiddleware        — завантажує сесію
   c. CommonMiddleware         — URL-нормалізація
   d. CsrfViewMiddleware       — перевірка CSRF-токена (POST)
   e. AuthenticationMiddleware — прив'язує request.user
   f. MessageMiddleware        — flash-повідомлення
5. URL Router (config/urls.py) → матчить URL → викликає View
6. View:
   a. Перевіряє авторизацію (@login_required)
   b. Зчитує дані з request.GET / request.POST
   c. Викликає потрібний Service
7. Service → Django ORM → SQL → PostgreSQL → результат
8. View формує context dict
9. Template рендерить HTML з context
10. HttpResponse → браузер
```

---

## 4. Структура проєкту

```
syla-yednosti/
│
├── 📄 .env.example                    ← Шаблон змінних оточення (комітити можна)
├── 📄 .env                            ← Реальні секрети (у .gitignore!)
├── 📄 .gitignore
├── 📄 docker-compose.yml              ← Оголошення сервісів web + db
├── 📄 Dockerfile                      ← Образ Django-застосунку
├── 📄 Makefile                        ← Зручні команди розробника
├── 📄 manage.py                       ← Django CLI
├── 📄 README.md
│
├── 📁 config/                         ← Django-проєкт (налаштування)
│   ├── __init__.py
│   ├── urls.py                        ← Головний URL-роутер
│   ├── wsgi.py
│   ├── asgi.py
│   └── settings/
│       ├── __init__.py
│       ├── base.py                    ← Спільні налаштування (DB, APPS, AUTH...)
│       └── local.py                   ← Локальна розробка (DEBUG=True, toolbar)
│
├── 📁 apps/                           ← Django-застосунки
│   │
│   ├── 📁 accounts/                   ── Auth Module
│   │   ├── models.py                  ← CustomUser: email, role (VOLUNTEER/DIRECTOR)
│   │   ├── managers.py                ← CustomUserManager
│   │   ├── forms.py                   ← LoginForm, VolunteerCreateForm
│   │   ├── views.py                   ← login_view, logout_view, volunteer CRUD
│   │   └── urls.py                    ← /login/, /logout/, /volunteers/
│   │
│   ├── 📁 applications/               ── Ядро системи
│   │   ├── models.py                  ← Request (+access_code), Category, Comment, AuditLog
│   │   ├── forms.py                   ← RequestForm (публічна), CommentForm
│   │   ├── views.py                   ← create_request, request_success,
│   │   │                                 check_request_status, dashboard, request_detail
│   │   ├── signals.py                 ← pre_save → автозапис AuditLog
│   │   ├── urls.py                    ← /, /success/<code>/, /check/, /dashboard/...
│   │   ├── fixtures/
│   │   │   └── categories.json        ← Початкові дані: 7 категорій
│   │   └── services/
│   │       ├── filter_service.py      ← FilterService: фільтрація QuerySet
│   │       ├── status_service.py      ← StatusService: State Machine статусів
│   │       └── validator.py           ← RequestValidator: телефон, кількість
│   │
│   └── 📁 reports/                    ── Звітність
│       ├── models.py                  ← Purchase: дані закупівлі (IN-BUY)
│       ├── forms.py                   ← PurchaseForm
│       ├── views.py                   ← export_report, purchase_create
│       ├── urls.py                    ← /reports/export/, /reports/purchase/<pk>/
│       └── services/
│           └── excel_export.py        ← generate_report(): openpyxl → bytes
│
├── 📁 templates/                      ← HTML-шаблони (Bootstrap 5)
│   ├── base.html                      ← Базовий макет: navbar, messages, Bootstrap CDN
│   ├── partials/
│   │   ├── _navbar.html               ← Навігація (з посиланням "Перевірити статус")
│   │   └── _messages.html             ← Flash-повідомлення Django
│   ├── accounts/
│   │   ├── login.html
│   │   ├── volunteer_list.html
│   │   └── volunteer_form.html
│   ├── applications/
│   │   ├── create_request.html        ← Публічна форма заявки
│   │   ├── request_success.html       ← Показує унікальний код доступу
│   │   ├── check_status.html          ← Публічна перевірка статусу за кодом
│   │   └── dashboard.html / request_detail.html
│   └── reports/
│       ├── report_form.html
│       └── purchase_form.html
│
├── 📁 static/
│   ├── css/main.css
│   └── js/main.js
│
└── 📁 requirements/
    ├── base.txt                       ← Django, psycopg2, openpyxl, pillow, decouple
    └── local.txt                      ← + django-debug-toolbar
```

---

## 5. Моделі даних та база даних

### 5.1 ER-діаграма (текстова)

```
CustomUser ──┐
 email (UK)  │ assigned_to (FK, SET_NULL)
 role        ├──────────────────────────► Request
 is_active   │                            ├── access_code (unique, 9 chars)
 is_staff    │ changed_by (FK, SET_NULL)  ├── status (State Machine)
             │                            ├── priority
             │                    category (FK, PROTECT)
             │                             │
             │                         Category
             │                          name (UK) / slug (UK)
             │
             │ author (FK, CASCADE)
             ├──────────────────────────► Comment
             │
             │ changed_by (FK, SET_NULL)
             └──────────────────────────► AuditLog
                                           old_status → new_status

Purchase ──(OneToOne → Request)
  actual_cost / purchase_date / funding_source / receipt_photo / created_by
```

### 5.2 Опис моделей

#### `CustomUser` (apps/accounts)
Замінює стандартну Django User. Логін — email (не username).

| Поле | Тип | Опис |
|---|---|---|
| `email` | EmailField (unique) | Логін користувача |
| `role` | CharField (choices) | `VOLUNTEER` або `DIRECTOR` |
| `is_active` | BooleanField | Чи може входити в систему |
| `is_staff` | BooleanField | Доступ до Django Admin |

#### `Request` (apps/applications) — центральна модель

| Поле | Тип | Опис |
|---|---|---|
| `user_name` | CharField | ПІБ заявника |
| `phone` | CharField | Телефон +380XXXXXXXXX |
| `unit_name` | CharField | Підрозділ (72 ОМБр, 2 бат) |
| `category` | FK → Category | Категорія потреби |
| `item_name` | TextField | Опис що потрібно |
| `quantity` | PositiveIntegerField | Кількість |
| `priority` | CharField (choices) | `LOW` / `MEDIUM` / `CRITICAL` |
| `location` | CharField | Населений пункт |
| `post_dept` | CharField | Відділення Нової Пошти |
| `status` | CharField (choices) | `NEW` / `IN_PROGRESS` / `DONE` / `CANCELED` |
| `assigned_to` | FK → CustomUser | Відповідальний волонтер |
| `access_code` | CharField (9, unique) | **Публічний код доступу** (напр. `A3F7-2B19`) |
| `created_at` | DateTimeField | Дата/час створення (auto) |
| `updated_at` | DateTimeField | Дата/час останньої зміни (auto) |

**Генерація `access_code`** відбувається автоматично у `save()`:
```python
import secrets

def save(self, *args, **kwargs):
    if not self.access_code:
        while True:
            code = secrets.token_hex(2).upper() + "-" + secrets.token_hex(2).upper()
            if not Request.objects.filter(access_code=code).exists():
                self.access_code = code
                break
    super().save(*args, **kwargs)
```
Це гарантує унікальність коду та використання CSPRNG (`/dev/urandom`).

#### `AuditLog` (apps/applications)
Автоматичний журнал змін статусу через Django Signals (pre_save).

#### `Purchase` (apps/reports) — вхідний документ IN-BUY

| Поле | Тип | Опис |
|---|---|---|
| `request` | OneToOneField | Прив'язка до заявки |
| `actual_cost` | DecimalField | Фактична вартість (грн) |
| `purchase_date` | DateField | Дата чека |
| `funding_source` | CharField | Джерело фінансування |
| `receipt_photo` | ImageField | Фото чека (media/) |
| `created_by` | FK → CustomUser | Хто вніс дані |

---

## 6. Модулі та компоненти

### 6.1 Auth Module (`apps/accounts/`)

**`login_view`** — сценарій UC-03:
- `authenticate(request, username=email, password=password)`
- При успіху → `login(request, user)` → Session cookie
- Редирект на `/dashboard/`

**`director_required`** — декоратор для захисту директорських view:
```python
@login_required
@director_required
def volunteer_list(request): ...
```

### 6.2 RequestController (`apps/applications/views.py`)

**`create_request`** — публічна форма:
- GET: рендерить порожню `RequestForm`
- POST: валідує → `obj = form.save()` → `access_code` генерується автоматично → редирект на `request_success` з кодом

**`request_success`** — сторінка після подачі:
- Отримує `code` з URL
- Знаходить заявку по `access_code`
- Відображає код великим шрифтом з попередженням зберегти його

**`check_request_status`** — публічна перевірка *(нова функція)*:
- GET: відображає форму для введення коду
- POST: шукає заявку по `access_code.upper()`
- Показує статус, деталі, дату оновлення, відповідального волонтера
- При невалідному коді — повідомлення про помилку

**`dashboard`** — панель управління (`@login_required`):
- `select_related("category", "assigned_to")` для запобігання N+1
- `FilterService.apply()` для фільтрації
- `aggregate(Count(...))` — лічильники одним SQL-запитом

**`request_detail`** — деталі заявки (`@login_required`):
- POST `new_status` → `StatusService.transition()`
- POST comment → `Comment` з `author=request.user`

### 6.3 Сервісний шар

#### `StatusService` — State Machine статусів
```
NEW ──────────────────────────────────► IN_PROGRESS
 │                                           │
 └──────────► CANCELED ◄─────────────────────┤
                                             │
                                          DONE ✓
```

```python
ALLOWED_TRANSITIONS = {
    "NEW":         ["IN_PROGRESS", "CANCELED"],
    "IN_PROGRESS": ["DONE",        "CANCELED"],
    "DONE":        [],
    "CANCELED":    [],
}
```

При переході до `IN_PROGRESS`: `assigned_to = changed_by`.

#### `FilterService`
```python
FilterService.apply(queryset, status="NEW", category_slug="drones",
                    unit_name="72 ОМБр", search="Іванченко")
```

### 6.4 AuditLog через Django Signals

```python
@receiver(pre_save, sender=Request)
def log_status_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    old = Request.objects.get(pk=instance.pk)
    if old.status != instance.status:
        AuditLog.objects.create(
            request=instance,
            changed_by=getattr(instance, "_changed_by", None),
            old_status=old.status,
            new_status=instance.status,
        )
```

### 6.5 ReportEngine (`apps/reports/`)

**`generate_report(purchases, date_from, date_to)`:**
```
Workbook → Лист «Звіт»
  → Merged title «Звіт БФ «Сила Єдності» за період...»
  → Кольорова шапка (темно-синій фон, білий текст)
  → Рядки даних з Purchase
  → Footer: загальна сума та кількість виконаних заявок
→ BytesIO → HTTP response (Content-Disposition: attachment)
```

---

## 7. Бізнес-логіка та сценарії використання

### 7.1 UC-01: Подача заявки з отриманням коду доступу

**Актор:** Представник військового підрозділу (без авторизації)

```
Передумова: Немає (відкрита система)

Основний потік:
  1. Користувач відкриває localhost:8000
  2. Система відображає форму RequestForm (9 полів)
  3. Клієнтська валідація (main.js): формат телефону +380
  4. POST → серверна валідація → збереження Request
  5. При збереженні автоматично генерується access_code (напр. A3F7-2B19)
  6. Редирект → request_success/<access_code>/
  7. Сторінка відображає код великим шрифтом з попередженням:
     «Запишіть або сфотографуйте — код більше не відобразиться»

Альтернативний потік (помилка валідації):
  → Форма з підсвічуванням помилок, повторне заповнення
```

### 7.2 UC-NEW: Перевірка статусу заявки *(нова функція)*

**Актор:** Представник військового підрозділу (без авторизації)

```
Передумова: Заявку подано, є код доступу (напр. A3F7-2B19)

Основний потік:
  1. Користувач відкриває /check/ (або натискає «Перевірити статус» у навбарі)
  2. Вводить код у поле (великими чи малими літерами — однаково)
  3. POST → пошук Request.objects.get(access_code=raw.upper())
  4. Система відображає:
     — Статус з кольоровим бейджем та поясненням
     — Підрозділ, категорія, опис потреби, кількість
     — Дата подачі та дата останнього оновлення
     — ПІБ/email відповідального волонтера (якщо призначено)
  5. Статуси та їх значення для військового:
     ⬜ Нова          → «Заявку отримано, очікує на обробку»
     🔵 В обробці    → «Волонтери вже працюють над вашою заявкою»
     🟢 Виконано     → «Заявку виконано!»
     🔴 Скасовано    → «На жаль, заявку скасовано»

Альтернативний потік (невірний код):
  → «Заявку з кодом «XYZ» не знайдено. Перевірте правильність введення.»
```

### 7.3 UC-02: Обробка заявки волонтером

```
1. Волонтер відкриває /dashboard/
2. Бачить заявки зі статусом NEW
3. Відкриває деталі → «Взяти в роботу»
4. StatusService.transition(req, IN_PROGRESS, user)
   → assigned_to = поточний волонтер
   → AuditLog запис через Signal
5. Волонтер виконує закупівлю
6. Вносить дані закупівлі (IN-BUY форма)
7. Purchase збережено → автоматичний перехід → DONE
```

### 7.4 UC-07: Генерація звіту для донорів

```
1. Директор відкриває /reports/export/
2. Вибирає date_from та date_to
3. generate_report() → openpyxl → bytes
4. HTTP response → браузер завантажує .xlsx
```

---

## 8. Безпека системи

### 8.1 Захист публічного трекінгу (IDOR Prevention)

Класична вразливість **IDOR (Insecure Direct Object Reference)** — коли порядковий ID у URL дозволяє будь-кому переглянути чужі дані (заявка №7, №8, №9...).

**Рішення:** замість порядкового ID використовується `access_code` — криптографічно стійкий код формату `A3F7-2B19`.

```python
# Генерація через secrets (CSPRNG, /dev/urandom)
secrets.token_hex(2).upper() + "-" + secrets.token_hex(2).upper()
# → 2 байти = 65536 варіантів на частину
# → разом: 65536² ≈ 4 млрд варіантів для однієї пари
```

Порівняння підходів:

| Підхід | Варіантів | Ризик перебору |
|---|---|---|
| Порядковий ID (`/7/`) | ~1000 (реальні) | Критичний — переглянути всіх |
| Короткий код `A3F7-2B19` | ~4 млрд | Мінімальний (+ rate-limit) |
| UUID | ~2¹²² | Нульовий |

### 8.2 Автентифікація та сесії

- Session-based authentication з httpOnly cookie
- `@login_required` — захист всіх внутрішніх сторінок
- `@director_required` — власний декоратор для директорських view
- Публічні сторінки (`/`, `/check/`, `/success/<code>/`) — навмисно відкриті

### 8.3 CSRF-захист

```python
"django.middleware.csrf.CsrfViewMiddleware"  # у MIDDLEWARE
{% csrf_token %}  # у кожній формі
# POST без токена → HTTP 403 Forbidden
```

### 8.4 Захист від SQL-ін'єкцій

Всі запити — виключно через Django ORM (параметризовані запити). Рядкова конкатенація в SQL відсутня.

### 8.5 Хешування паролів

```
Алгоритм: PBKDF2 + SHA256 + сіль (Django default)
Зберігається: pbkdf2_sha256$600000$<сіль>$<хеш>
У відкритому вигляді: ніколи
```

### 8.6 Ролева модель доступу (RBAC)

| Ресурс | Без входу | Волонтер | Директор |
|---|---|---|---|
| Форма заявки `/` | ✅ | ✅ | ✅ |
| Перевірка статусу `/check/` | ✅ | ✅ | ✅ |
| Дашборд `/dashboard/` | ❌ | ✅ | ✅ |
| Деталі заявки | ❌ | ✅ | ✅ |
| Форма закупівлі | ❌ | ✅ | ✅ |
| Excel-звіт | ❌ | ❌ | ✅ |
| Управління волонтерами | ❌ | ❌ | ✅ |

---

## 9. Середовище розробки та Docker

### 9.1 Схема Docker Compose

```
┌─────────────────────────────────────────────┐
│              Docker Network                 │
│                                             │
│  ┌──────────────────┐  ┌─────────────────┐  │
│  │   web (Django)   │  │   db (Postgres) │  │
│  │                  │  │                 │  │
│  │ python:3.12-slim │  │ postgres:16-    │  │
│  │ port: 8000:8000  │  │ alpine          │  │
│  │                  │  │ port: 5432:5432 │  │
│  │ volumes:         │  │                 │  │
│  │  . → /app        │  │ volume:         │  │
│  │  media_data      │  │  postgres_data  │  │
│  │                  │  │                 │  │
│  │ depends_on: db   │  │ healthcheck:    │  │
│  │ (healthy)        │  │  pg_isready     │  │
│  └──────────────────┘  └─────────────────┘  │
│                                             │
│  Named volumes: postgres_data, media_data   │
└─────────────────────────────────────────────┘
         │
    localhost:8000
```

### 9.2 Health Check

```yaml
db:
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
    interval: 10s
    retries: 5

web:
  depends_on:
    db:
      condition: service_healthy  # web стартує тільки після готовності БД
```

---

## 10. Швидкий старт

### Передумови
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) — встановлено і запущено
- Git

### Встановлення

```bash
# 1. Клонувати репозиторій
git clone <url-репозиторію>
cd syla-yednosti

# 2. Налаштувати оточення
cp .env.example .env
# Відредагуй .env — змінити DJANGO_SECRET_KEY на довгий випадковий рядок

# 3. Запустити (перший раз ~3 хвилини)
docker compose up --build

# 4. У новому терміналі — міграції та початкові дані
docker compose exec web python manage.py migrate
docker compose exec web python manage.py loaddata categories

# 5. Створити директора фонду
docker compose exec web python manage.py createsuperuser
# → вводиш email і пароль
# → у Django Admin (/admin/) встанови role=DIRECTOR і is_staff=True

# 6. Відкрити в браузері
# http://localhost:8000/          — публічна форма заявки
# http://localhost:8000/check/    — перевірка статусу
# http://localhost:8000/login/    — вхід для волонтерів
# http://localhost:8000/admin/    — Django Admin
```

### Зупинка

```bash
docker compose down          # зупинити контейнери
docker compose down -v       # + видалити volumes (скидає БД!)
```

---

## 11. Змінні оточення

Файл `.env` (не комітити! є в `.gitignore`):

```dotenv
# Django
DJANGO_SECRET_KEY=замінити-на-випадковий-рядок-мінімум-50-символів
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SETTINGS_MODULE=config.settings.local

# PostgreSQL
DB_NAME=syla_yednosti
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

> **Генерація SECRET_KEY:**
> ```bash
> docker compose exec web python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

---

## 12. Команди Makefile

```bash
make run            # docker compose up
make build          # docker compose up --build
make stop           # docker compose down

make migrate        # python manage.py migrate
make makemigrations # python manage.py makemigrations
make superuser      # python manage.py createsuperuser
make shell          # python manage.py shell
make logs           # docker compose logs -f web
make test           # python manage.py test
```

---

## 13. URL-маршрути

| Метод | URL | View | Авторизація | Опис |
|---|---|---|---|---|
| GET/POST | `/` | `create_request` | Публічна | Форма заявки для військових |
| GET | `/success/<str:code>/` | `request_success` | Публічна | Показує код доступу після подачі |
| GET/POST | `/check/` | `check_request_status` | Публічна | **Перевірка статусу за кодом** |
| GET/POST | `/login/` | `login_view` | Публічна | Вхід у систему |
| GET | `/logout/` | `logout_view` | Авторизований | Вихід |
| GET | `/dashboard/` | `dashboard` | Волонтер+ | Реєстр заявок з фільтрами |
| GET/POST | `/requests/<pk>/` | `request_detail` | Волонтер+ | Деталі + зміна статусу |
| GET | `/volunteers/` | `volunteer_list` | Директор | Список волонтерів |
| GET/POST | `/volunteers/add/` | `volunteer_create` | Директор | Створення волонтера |
| POST | `/volunteers/<pk>/toggle/` | `volunteer_toggle` | Директор | Блок/розблок |
| GET | `/reports/export/` | `export_report` | Директор | Генерація Excel |
| GET/POST | `/reports/purchase/<pk>/` | `purchase_create` | Волонтер+ | Внесення IN-BUY |
| GET | `/admin/` | Django Admin | Superuser | Адмін-панель |

---

## 14. Ролі та права доступу

### Як створити директора

Тільки через термінал (один раз):
```bash
docker compose exec web python manage.py createsuperuser
# Потім у /admin/ → Users → встанови role=DIRECTOR, is_staff=True
```

### Як створити волонтера

**Через інтерфейс директора** (рекомендовано):
```
Увійти як директор → /volunteers/add/ → заповнити форму
```

**Через Django shell:**
```python
from apps.accounts.models import CustomUser
CustomUser.objects.create_user(
    email='volunteer@syla.ua',
    password='Volunteer2024!',
    role='VOLUNTEER'
)
```

### Таблиця доступу

| Ресурс | Без входу | Волонтер | Директор |
|---|---|---|---|
| Форма заявки | ✅ | ✅ | ✅ |
| Перевірка статусу `/check/` | ✅ | ✅ | ✅ |
| Дашборд | ❌ | ✅ | ✅ |
| Деталі + зміна статусу | ❌ | ✅ | ✅ |
| Форма закупівлі IN-BUY | ❌ | ✅ | ✅ |
| Excel-звіт | ❌ | ❌ | ✅ |
| Управління волонтерами | ❌ | ❌ | ✅ |

---

## 15. Функціональні та нефункціональні вимоги

### Функціональні вимоги

| Код | Вимога | Статус |
|---|---|---|
| FR-01 | Подача заявки через публічну форму | ✅ |
| FR-02 | Валідація: телефон +380, обов'язкові поля | ✅ |
| FR-03 | Авторизація волонтерів за email+пароль | ✅ |
| FR-04 | Дашборд із реєстром, сортування від нових | ✅ |
| FR-05 | Фільтрація за статусом, категорією, підрозділом | ✅ |
| FR-06 | Зміна статусу з перевіркою переходів (State Machine) | ✅ |
| FR-07 | Внутрішні коментарі волонтера | ✅ |
| FR-08 | Генерація Excel-звіту за довільний період | ✅ |
| FR-09 | Глобальний пошук по прізвищу/телефону | ✅ |
| FR-10 | **Генерація унікального коду доступу при подачі заявки** | ✅ |
| FR-11 | **Публічна перевірка статусу заявки за кодом** | ✅ |
| IN-BUY | Форма внесення даних закупівлі з фото чека | ✅ |
| UC-08 | Управління обліковими записами волонтерів | ✅ |

### Нефункціональні вимоги

| Код | Вимога | Реалізація |
|---|---|---|
| NFR-01 | **Захист від IDOR** (перегляд чужих заявок) | access_code через secrets (CSPRNG) |
| NFR-03 | Адаптивний інтерфейс (mobile-first) | Bootstrap 5 grid |
| NFR-05 | СУБД PostgreSQL | PostgreSQL 16 у Docker |
| NFR-06 | Час відповіді < 2 сек (локально) | select_related, індекси |
| NFR-07 | Хешування паролів | PBKDF2-SHA256 (Django) |
| NFR-08 | Захист від SQL-ін'єкцій | Django ORM виключно |
| NFR-09 | CSRF-захист усіх POST-форм | CsrfViewMiddleware |

---

## 16. Управління базою даних

### Очистити тестові дані

**Варіант А — тільки заявки (зберігає користувачів):**
```bash
docker compose exec web python manage.py shell
```
```python
from apps.applications.models import Request, Comment, AuditLog
AuditLog.objects.all().delete()
Comment.objects.all().delete()
Request.objects.all().delete()
```

**Варіант Б — повне очищення (включно з користувачами):**
```bash
docker compose exec web python manage.py flush
# Після цього потрібно знову createsuperuser + loaddata categories
```

**Варіант В — повне скидання через Docker:**
```bash
docker compose down -v       # видаляє PostgreSQL volume
docker compose up -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py loaddata categories
docker compose exec web python manage.py createsuperuser
```

### Підключення до PostgreSQL напряму

```bash
docker compose exec db psql -U postgres -d syla_yednosti
```

---

## 17. Розробник

**Слободянюк Олексій Вікторович**

Київський національний економічний університет імені Вадима Гетьмана
Навчально-науковий інститут «Інститут інформаційних технологій в економіці»
Кафедра інформаційних систем в економіці
Освітньо-професійна програма «Комп'ютерні науки»
4 курс, група ІН-403


---

<div align="center">

Зроблено з ❤️ для підтримки Збройних Сил України 🇺🇦

</div>