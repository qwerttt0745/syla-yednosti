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
6. [Модулі та компоненти](#6-модулі-та-компоненти)
7. [Бізнес-логіка та сценарії використання](#7-бізнес-логіка-та-сценарії-використання)
8. [Безпека системи](#8-безпека-системи)
9. [Середовище розробки та Docker](#9-середовище-розробки-та-docker)
10. [Швидкий старт](#10-швидкий-старт)
11. [Змінні оточення](#11-змінні-оточення)
12. [Команди Makefile](#12-команди-makefile)
13. [URL-маршрути](#13-url-маршрути)
14. [Ролі та права доступу](#14-ролі-та-права-доступу)
15. [Функціональні та нефункціональні вимоги](#15-функціональні-та-нефункціональні-вимоги)
16. [Розробник](#16-розробник)

---

## 1. Про проєкт

**«Сила Єдності»** — веб-орієнтована інформаційна система, розроблена для автоматизації діяльності волонтерського благодійного фонду, що надає матеріальну допомогу підрозділам Збройних Сил України.

### Проблема, яку вирішує система

До впровадження системи волонтерський фонд вів облік заявок у месенджерах (Telegram, Viber) та Excel-таблицях. Це призводило до:

- **Втрати заявок** — повідомлення губились у загальних чатах
- **Дублювання роботи** — кілька волонтерів брались за одну заявку
- **Відсутності звітності** — неможливо було автоматично формувати звіти для донорів
- **Непрозорості процесу** — жодного журналу хто, коли і що зробив

### Що вирішує ця система

```
Заявка від військового → Реєстр волонтерів → Закупівля → Звіт для донорів
       (публічна форма)     (дашборд + фільтри)  (IN-BUY форма)   (Excel .xlsx)
```

Система є **єдиним цифровим реєстром** усіх заявок із повним відстеженням статусів, автоматичним журналом аудиту та вбудованою звітністю.

### Ключові переваги

| Перевага | Опис |
|---|---|
| 📱 Мобільна доступність | Публічна форма оптимізована для смартфонів — військові заповнюють з поля |
| 🔒 Без реєстрації | Військовим не потрібен обліковий запис для подачі заявки |
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
- Широка екосистема: `openpyxl` (Excel), `Pillow` (зображення), `psycopg2` (PostgreSQL)
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

### 2.5 Інфраструктура

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
- Гілки: `main` — стабільна версія

### 2.6 Додаткові інструменти

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
│  Django Views          Services                         │
│  ┌──────────────┐  ┌────────────────┐                   │
│  │create_request│  │ FilterService  │                   │
│  │  dashboard   │  │ StatusService  │                   │
│  │request_detail│  │RequestValidator│                   │
│  │export_report │  │ ReportEngine   │                   │
│  │purchase_creat│  └────────────────┘                   │
│  └──────────────┘                                       │
│                                                         │
│  Django Middleware: Security → Session → CSRF → Auth    │
└─────────────────────┬───────────────────────────────────┘
                      │ Django ORM
┌─────────────────────▼───────────────────────────────────┐
│                    РІВЕНЬ ДАНИХ                         │
│                                                         │
│  Models: CustomUser, Request, Category,                 │
│          Comment, AuditLog, Purchase                    │
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

### 3.4 Діаграма компонентів системи

```
┌──────────────────────────────────────────────────────────────┐
│                        Django App                            │
│                                                              │
│  ┌─────────────┐   ┌──────────────────┐   ┌──────────────┐  │
│  │ Auth Module │   │ RequestController│   │ ReportEngine │  │
│  │             │   │                  │   │              │  │
│  │ CustomUser  │   │ create_request   │   │ export_report│  │
│  │ login_view  │   │ dashboard        │   │ purchase_    │  │
│  │ volunteer   │   │ request_detail   │   │   create     │  │
│  │   CRUD      │   │                  │   │ excel_export │  │
│  └──────┬──────┘   └────────┬─────────┘   └──────┬───────┘  │
│         │                   │                    │           │
│         └─────────┬─────────┘                    │           │
│                   │                              │           │
│         ┌─────────▼──────────────────────────────▼─────────┐ │
│         │              Service Layer                        │ │
│         │  FilterService  StatusService  RequestValidator   │ │
│         └─────────────────────┬─────────────────────────── ┘ │
│                               │ Django ORM                   │
│         ┌─────────────────────▼──────────────────────────┐   │
│         │           Models / Database Layer               │   │
│         │  CustomUser  Request  Category  Comment         │   │
│         │  AuditLog    Purchase                           │   │
│         └────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
                              │
                     ┌────────▼────────┐
                     │  PostgreSQL 16  │
                     │  (Docker: db)   │
                     └─────────────────┘
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
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py                   ← CustomUserAdmin
│   │   ├── managers.py                ← CustomUserManager (create_user, create_superuser)
│   │   ├── models.py                  ← CustomUser: email, role (VOLUNTEER/DIRECTOR)
│   │   ├── forms.py                   ← LoginForm, VolunteerCreateForm
│   │   ├── views.py                   ← login_view, logout_view, volunteer CRUD
│   │   ├── urls.py                    ← /login/, /logout/, /volunteers/
│   │   └── migrations/
│   │
│   ├── 📁 applications/               ── Ядро системи
│   │   ├── __init__.py
│   │   ├── apps.py                    ← ready(): реєстрація сигналів
│   │   ├── admin.py                   ← RequestAdmin, CategoryAdmin, AuditLogAdmin
│   │   ├── models.py                  ← Request, Category, Comment, AuditLog
│   │   ├── forms.py                   ← RequestForm (публічна), CommentForm
│   │   ├── views.py                   ← create_request, dashboard, request_detail
│   │   ├── signals.py                 ← pre_save → автозапис AuditLog
│   │   ├── urls.py                    ← /, /dashboard/, /requests/<pk>/
│   │   ├── migrations/
│   │   ├── fixtures/
│   │   │   └── categories.json        ← Початкові дані: 7 категорій
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── filter_service.py      ← FilterService: фільтрація QuerySet
│   │       ├── status_service.py      ← StatusService: State Machine статусів
│   │       └── validator.py           ← RequestValidator: телефон, кількість
│   │
│   └── 📁 reports/                    ── Звітність
│       ├── __init__.py
│       ├── apps.py
│       ├── admin.py
│       ├── models.py                  ← Purchase: дані закупівлі (IN-BUY)
│       ├── forms.py                   ← PurchaseForm
│       ├── views.py                   ← export_report, purchase_create
│       ├── urls.py                    ← /reports/export/, /reports/purchase/<pk>/
│       ├── migrations/
│       └── services/
│           ├── __init__.py
│           └── excel_export.py        ← generate_report(): openpyxl → bytes
│
├── 📁 templates/                      ← HTML-шаблони (Bootstrap 5)
│   ├── base.html                      ← Базовий макет: navbar, messages, Bootstrap CDN
│   ├── partials/
│   │   ├── _navbar.html               ← Навігаційна панель (адаптивна, з ролями)
│   │   └── _messages.html             ← Flash-повідомлення Django
│   ├── accounts/
│   │   ├── login.html                 ← /login/ — форма входу
│   │   ├── volunteer_list.html        ← /volunteers/ — список волонтерів
│   │   └── volunteer_form.html        ← /volunteers/add/ — форма створення
│   ├── applications/
│   │   ├── create_request.html        ← / — публічна форма заявки (UC-01)
│   │   ├── request_success.html       ← Підтвердження після відправки
│   │   ├── dashboard.html             ← /dashboard/ — реєстр + фільтри (UC-02)
│   │   └── request_detail.html        ← /requests/<pk>/ — деталі + дії
│   └── reports/
│       ├── report_form.html           ← /reports/export/ — форма вибору дат
│       └── purchase_form.html         ← /reports/purchase/<pk>/ — IN-BUY форма
│
├── 📁 static/
│   ├── css/
│   │   └── main.css                   ← Кастомні стилі поверх Bootstrap
│   └── js/
│       └── main.js                    ← Клієнтська валідація форм (FR-02)
│
├── 📁 media/                          ← Завантажені файли (у .gitignore)
│   └── receipts/                      ← Фото чеків Purchase.receipt_photo
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
 is_active   │ changed_by (FK, SET_NULL) ──┤
 is_staff    │                             │
             │                    category (FK, PROTECT)
             │                             │
             │                         Category
             │                          name (UK)
             │                          slug (UK)
             │
             │ author (FK, CASCADE)
             ├──────────────────────────► Comment
             │                            text
             │                            created_at
             │
             │ changed_by (FK, SET_NULL)
             └──────────────────────────► AuditLog
                                           old_status
                                           new_status
                                           changed_at

Purchase ──(OneToOne → Request)──► Request
  actual_cost
  purchase_date
  funding_source
  receipt_photo (ImageField)
  created_by (FK → CustomUser)
```

### 5.2 Опис моделей

#### `CustomUser` (apps/accounts)
Замінює стандартну Django User модель. Логін — email (не username).

| Поле | Тип | Опис |
|---|---|---|
| `email` | EmailField (unique) | Логін користувача |
| `role` | CharField (choices) | `VOLUNTEER` або `DIRECTOR` |
| `is_active` | BooleanField | Чи може входити в систему |
| `is_staff` | BooleanField | Доступ до Django Admin |

#### `Category` (apps/applications)
Довідник категорій потреб.

| Поле | Тип | Опис |
|---|---|---|
| `name` | CharField (unique) | Назва: «Дрони та БПЛА» |
| `slug` | SlugField (unique) | URL-ідентифікатор: `drones` |

#### `Request` (apps/applications) — центральна модель
Заявка від підрозділу. Відповідає вхідному документу **IN-REQ** з курсової.

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
| `post_dept` | PositiveIntegerField | Відділення Нової Пошти |
| `status` | CharField (choices) | `NEW` / `IN_PROGRESS` / `DONE` / `CANCELED` |
| `assigned_to` | FK → CustomUser | Відповідальний волонтер |
| `created_at` | DateTimeField | Дата/час створення (auto) |
| `updated_at` | DateTimeField | Дата/час останньої зміни (auto) |

#### `Comment` (apps/applications)
Внутрішні нотатки волонтерів. Військові їх не бачать.

#### `AuditLog` (apps/applications)
Автоматичний журнал змін статусу через Django Signals.

#### `Purchase` (apps/reports) — вхідний документ IN-BUY

| Поле | Тип | Опис |
|---|---|---|
| `request` | OneToOneField | Прив'язка до заявки |
| `actual_cost` | DecimalField | Фактична вартість (грн) |
| `purchase_date` | DateField | Дата чека |
| `funding_source` | CharField | Джерело фінансування |
| `receipt_photo` | ImageField | Фото чека (зберігається у media/) |
| `created_by` | FK → CustomUser | Хто вніс дані |

### 5.3 Індекси та оптимізація

```python
# Request.status — найчастіший фільтр на дашборді
status = models.CharField(..., db_index=True)

# Request.category — фільтрація по категорії
category = models.ForeignKey(..., db_index=True)

# CustomUser.email — unique автоматично створює індекс
email = models.EmailField(unique=True)

# Запобігання N+1 у dashboard view
Request.objects.select_related("category", "assigned_to").all()
```

---

## 6. Модулі та компоненти

### 6.1 Auth Module (`apps/accounts/`)

Відповідає за автентифікацію та управління обліковими записами.

**`CustomUserManager`** — кастомний менеджер:
```python
create_user(email, password, **extra_fields)      # Для волонтерів
create_superuser(email, password, **extra_fields)  # role=DIRECTOR автоматично
```

**`login_view`** — сценарій UC-03:
1. `authenticate(request, username=email, password=password)`
2. При успіху → `login(request, user)` → Session cookie встановлюється
3. Редирект на `/dashboard/`

**`director_required`** — декоратор для захисту директорських view:
```python
@login_required
@director_required
def volunteer_list(request): ...
```

### 6.2 RequestController (`apps/applications/views.py`)

Три основні view-функції:

**`create_request`** — публічна (без `@login_required`):
- GET: рендерить порожню `RequestForm`
- POST: валідує → зберігає → редирект на success

**`dashboard`** — панель управління (`@login_required`):
- Завантажує всі `Request` з `select_related`
- Передає через `FilterService.apply(qs, request.GET)`
- Рахує агреговані лічильники одним SQL-запитом через `aggregate(Count(...))`

**`request_detail`** — деталі заявки (`@login_required`):
- GET: рендерить деталі + форму коментаря + журнал AuditLog
- POST (new_status): викликає `StatusService.transition()`
- POST (comment): зберігає `Comment` з `author=request.user`

### 6.3 Сервісний шар (`apps/applications/services/`)

#### `FilterService`
Фільтрація QuerySet за параметрами GET-запиту:
```python
FilterService.apply(queryset, {
    "status":    "NEW",
    "category":  "drones",
    "unit_name": "72 ОМБр",
    "search":    "Іванченко",
})
```

#### `StatusService`
Кінцевий автомат (State Machine) статусів заявки:

```
NEW ──────────────────────────────────────► IN_PROGRESS
 │                                               │
 └──────────► CANCELED ◄─────────────────────────┤
                                                 │
                                              DONE ✓
```

```python
ALLOWED_TRANSITIONS = {
    "NEW":         ["IN_PROGRESS", "CANCELED"],
    "IN_PROGRESS": ["DONE",        "CANCELED"],
    "DONE":        [],   # фінальний — без переходів
    "CANCELED":    [],   # фінальний — без переходів
}

StatusService.transition(request_obj, "IN_PROGRESS", changed_by=request.user)
```

При переході до `IN_PROGRESS`:
- `assigned_to` = `changed_by` (поточний волонтер)
- `_changed_by` встановлюється для Django Signal

#### `RequestValidator`
Серверна валідація (доповнює форму):
```python
RequestValidator.validate_phone("+380991234567")  # → True/False (regex)
RequestValidator.validate_quantity(0)              # → False (має бути > 0)
```

### 6.4 AuditLog через Django Signals

```python
# apps/applications/signals.py
@receiver(pre_save, sender=Request)
def log_status_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # нова заявка — нічого логувати
    old = Request.objects.get(pk=instance.pk)
    if old.status != instance.status:
        AuditLog.objects.create(
            request=instance,
            changed_by=getattr(instance, "_changed_by", None),
            old_status=old.status,
            new_status=instance.status,
        )
```

Реєстрація у `apps/applications/apps.py`:
```python
def ready(self):
    import apps.applications.signals  # noqa
```

### 6.5 ReportEngine (`apps/reports/`)

**`purchase_create`** — внесення даних закупівлі (IN-BUY):
- Доступний тільки для заявок зі статусом `IN_PROGRESS`
- Блокує якщо `Purchase` вже існує (OneToOne)
- Після збереження автоматично переводить заявку → `DONE`

**`generate_report(purchases, date_from, date_to)`** — генерація OUT-REP:
```
Workbook → Лист «Звіт»
  → Рядок 1: Merged title «Звіт БФ «Сила Єдності» за період...»
  → Рядок 3: Кольорова шапка (темно-синій фон, білий текст)
  → Рядки 4+: Дані з Purchase (дата, підрозділ, що передано, категорія, сума)
  → Footer:   «Всього заявок виконано: N» + «Загальна сума витрат: X грн»
→ BytesIO → HTTP response (Content-Disposition: attachment)
```

---

## 7. Бізнес-логіка та сценарії використання

### 7.1 UC-01: Подача заявки

**Актор:** Представник військового підрозділу (без авторизації)

```
Передумова: Немає (відкрита система)

Основний потік:
  1. Користувач відкриває localhost:8000
  2. Система відображає форму RequestForm (9 полів)
  3. Користувач заповнює всі обов'язкові поля
  4. Клієнтська валідація (main.js): формат телефону +380
  5. POST-запит → серверна валідація (RequestForm.clean_phone())
  6. Збереження Request зі статусом NEW
  7. Редирект → request_success.html

Альтернативний потік А1 (помилка валідації):
  3а. Невірний формат телефону → is-invalid підсвічування
  3б. Порожнє обов'язкове поле → форма не відправляється
  → Повернення до кроку 3
```

### 7.2 UC-02: Обробка заявки

**Актор:** Волонтер (авторизований)

```
Передумова: Волонтер авторизований, є заявки зі статусом NEW

Основний потік:
  1. Волонтер відкриває /dashboard/
  2. Бачить заявки зі статусом NEW (червоний бейдж)
  3. Застосовує фільтри за потребою (FR-05)
  4. Відкриває деталі → натискає «Взяти в роботу»
  5. StatusService.transition(req, IN_PROGRESS, user)
     → assigned_to = поточний волонтер
     → AuditLog запис створюється через Signal
  6. Волонтер виконує закупівлю (поза системою)
  7. Повертається → натискає «Внести дані закупівлі»
  8. Заповнює PurchaseForm: вартість, дата, джерело, фото чека
  9. Збереження Purchase → автоматичний перехід → DONE

Виняткова ситуація (блокування):
  4а. Заявку вже взяв інший волонтер (assigned_to != None)
  → Кнопки зміни статусу замінюються на попередження:
     «Заявка заблокована: [email волонтера]»
```

### 7.3 UC-03: Авторизація

**Актор:** Волонтер або Директор

```
1. Відкриває /login/
2. Вводить email + пароль
3. authenticate() → перевіряє хеш PBKDF2-SHA256
4а. Успіх → login() → session cookie → редирект /dashboard/
4б. Помилка → «Невірний email або пароль» всередині картки
```

### 7.4 UC-07: Генерація звіту

**Актор:** Директор (role=DIRECTOR)

```
1. Директор відкриває /reports/export/
2. Вибирає date_from та date_to
3. GET-запит → фільтрація Purchase за датами
4. generate_report() → openpyxl Workbook → bytes
5. HTTP response з Content-Disposition: attachment
6. Браузер завантажує .xlsx файл
```

### 7.5 UC-08: Управління волонтерами

**Актор:** Директор

```
1. Директор відкриває /volunteers/
2. Бачить список всіх користувачів з ролями та статусами
3. Натискає «Додати волонтера» → /volunteers/add/
4. Заповнює VolunteerCreateForm: email, role, password
5. Перевірка: email унікальний, паролі співпадають
6. Збереження → CustomUser.objects.create_user()
7а. «Заблокувати» → user.is_active = False → волонтер не може увійти
7б. «Активувати» → user.is_active = True → доступ відновлено
```

---

## 8. Безпека системи

### 8.1 Автентифікація та сесії

- Django session-based authentication
- Session ID у `httpOnly` cookie — недоступний для JavaScript (XSS-захист)
- `@login_required` — неавторизованих автоматично редиректить на `/login/`
- `@director_required` — власний декоратор для сторінок директора
- Публічна форма `/` — навмисно відкрита без авторизації (вимога системи)

### 8.2 CSRF-захист

```python
# Активовано у MIDDLEWARE:
"django.middleware.csrf.CsrfViewMiddleware"

# Кожна форма містить:
{% csrf_token %}

# POST без токена → HTTP 403 Forbidden
```

### 8.3 Захист від SQL-ін'єкцій

**Всі запити — виключно через Django ORM:**
```python
# ✅ Безпечно — ORM параметризує значення
Request.objects.filter(unit_name__icontains=unit_name)

# ❌ Такого коду в проєкті немає
cursor.execute(f"SELECT * FROM requests WHERE unit = '{unit_name}'")
```

### 8.4 Хешування паролів

```
Алгоритм: PBKDF2 + SHA256 + сіль (Django default)
Зберігається: pbkdf2_sha256$600000$<сіль>$<хеш>
У відкритому вигляді: ніде не зберігається, не логується
```

### 8.5 Ролева модель доступу (RBAC)

| Ресурс | Без входу | Волонтер | Директор |
|---|---|---|---|
| Форма заявки `/` | ✅ | ✅ | ✅ |
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

### 9.2 Bind Mount та Hot Reload

Директорія проєкту монтується у контейнер як bind mount:
```yaml
volumes:
  - .:/app  # локальна директорія → /app у контейнері
```

Django `runserver` автоматично перезавантажується при зміні `.py` файлів — не потрібно перезапускати контейнер.

### 9.3 Health Check

```yaml
db:
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
    interval: 10s
    timeout: 5s
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
# Відредагуй .env: змінити DJANGO_SECRET_KEY на будь-який довгий рядок

# 3. Запустити (перший раз ~3 хвилини)
docker compose up --build

# 4. У новому терміналі — міграції та дані
docker compose exec web python manage.py migrate
docker compose exec web python manage.py loaddata categories

# 5. Створити директора фонду
docker compose exec web python manage.py createsuperuser
# → вводиш email і пароль

# 6. Відкрити в браузері
# http://localhost:8000/
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
make run            # docker compose up (запуск)
make build          # docker compose up --build (перебудова)
make stop           # docker compose down

make migrate        # python manage.py migrate
make makemigrations # python manage.py makemigrations
make superuser      # python manage.py createsuperuser
make shell          # python manage.py shell (інтерактивна консоль)
make logs           # docker compose logs -f web
make test           # python manage.py test
```

---

## 13. URL-маршрути

| Метод | URL | View | Авторизація | Опис |
|---|---|---|---|---|
| GET/POST | `/` | `create_request` | Публічна | Форма заявки для військових |
| GET | `/success/` | `request_success` | Публічна | Підтвердження після відправки |
| GET/POST | `/login/` | `login_view` | Публічна | Вхід у систему |
| GET | `/logout/` | `logout_view` | Авторизований | Вихід |
| GET | `/dashboard/` | `dashboard` | Волонтер+ | Реєстр заявок |
| GET/POST | `/requests/<pk>/` | `request_detail` | Волонтер+ | Деталі + зміна статусу |
| GET | `/volunteers/` | `volunteer_list` | Директор | Список волонтерів |
| GET/POST | `/volunteers/add/` | `volunteer_create` | Директор | Створення волонтера |
| POST | `/volunteers/<pk>/toggle/` | `volunteer_toggle` | Директор | Блок/розблок |
| GET | `/reports/export/` | `export_report` | Директор | Генерація Excel |
| GET/POST | `/reports/purchase/<pk>/` | `purchase_create` | Волонтер+ | Внесення IN-BUY |
| GET | `/admin/` | Django Admin | Superuser | Адмін-панель |

---

## 14. Ролі та права доступу

### Волонтер (`role = VOLUNTEER`)
Стандартний обліковий запис співробітника фонду.

**Може:**
- Переглядати всі заявки на дашборді
- Фільтрувати та шукати заявки
- Взяти заявку в роботу (стає `assigned_to`)
- Додавати внутрішні коментарі
- Вносити дані закупівлі (IN-BUY)
- Змінювати статуси в межах дозволених переходів

**Не може:**
- Генерувати Excel-звіти
- Керувати обліковими записами

### Директор (`role = DIRECTOR`)
Керівник фонду. Всі права волонтера + додаткові.

**Додатково може:**
- Генерувати Excel-звіти для донорів
- Переглядати список всіх волонтерів
- Додавати нових волонтерів/директорів
- Блокувати/розблоковувати доступ

### Як створити волонтера

**Через адмін-панель:**
```
http://localhost:8000/admin/ → Users → Add User
Email: volunteer@syla.ua | Role: VOLUNTEER
```

**Через Django Shell:**
```bash
docker compose exec web python manage.py shell
```
```python
from apps.accounts.models import CustomUser
CustomUser.objects.create_user(
    email='volunteer@syla.ua',
    password='Volunteer2024!',
    role='VOLUNTEER'
)
```

**Через інтерфейс директора:**
```
http://localhost:8000/volunteers/add/
```

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
| FR-06 | Зміна статусу з перевіркою переходів | ✅ |
| FR-07 | Внутрішні коментарі волонтера | ✅ |
| FR-08 | Генерація Excel-звіту за довільний період | ✅ |
| FR-09 | Глобальний пошук по прізвищу/телефону | ✅ |
| IN-BUY | Форма внесення даних закупівлі з фото | ✅ |
| UC-08 | Управління обліковими записами волонтерів | ✅ |

### Нефункціональні вимоги

| Код | Вимога | Реалізація |
|---|---|---|
| NFR-03 | Адаптивний інтерфейс (mobile-first) | Bootstrap 5 grid |
| NFR-05 | СУБД PostgreSQL | PostgreSQL 16 у Docker |
| NFR-06 | Час відповіді < 2 сек (локально) | select_related, індекси |
| NFR-07 | Хешування паролів | PBKDF2-SHA256 (Django) |
| NFR-08 | Захист від SQL-ін'єкцій | Django ORM (тільки) |
| NFR-09 | CSRF-захист усіх POST-форм | CsrfViewMiddleware |

---

## 16. Розробник

**Слободянюк Олексій Вікторович**

Київський національний економічний університет імені Вадима Гетьмана
Навчально-науковий інститут «Інститут інформаційних технологій в економіці»
Кафедра інформаційних систем в економіці
Освітньо-професійна програма «Комп'ютерні науки»
4 курс, група ІН-403

**Бакалаврська робота, 2025**

---

<div align="center">

Зроблено з ❤️ для підтримки Збройних Сил України 🇺🇦

</div>