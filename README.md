# ML-сервис классификации ирисов с CI/CD

Проект включает в себя: обучение модели, контейнеризацию, стратегию Blue‑Green и автоматический пайплайн CI/CD на GitHub Actions.

## Используемые технологии

- Python 3.11
- scikit‑learn, numpy, pandas
- Docker & Docker Compose
- GitHub Actions

## Стратегия деплоя

Выбрана стратегия Blue‑Green, зафиксированная в [ADR](./docs/adr/001-blue-green-deployment.md).

**Реализация**:
- docker-compose.yaml поднимает две идентичные среды (blue и green).
- Переключение между blue и green осуществляется сменой апстрима в конфигурации nginx.

## Структура проекта
├── .github/workflows/ci.yml # GitHub Actions CI/CD пайплайн

├── ml_pipeline.py # Скрипт обучения модели и сохранения артефактов

├── docker-compose.yaml # Описание сервисов Blue‑Green

├── Dockerfile # образ ML-сервиса

├── requirements.txt # Зависимости Python

├── README.md

└── docs/adr/ # Архитектурные решения (ADR)


## Локальный запуск

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. **Установка зависимостей**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt

 3. **Запустите обучение модели**:
    ```bash
    python ml_pipeline.py

**CI/CD пайплайн**
Workflow описан в .github/workflows/ci.yml и запускается при каждом push или pull request.

Шаги пайплайна:

- Установка Python и зависимостей.

- Запуск ml_pipeline.py – обучение модели и сохранение артефактов.

- Проверка воспроизводимости – загрузка модели, вывод гиперпараметров, подтверждение целостности артефактов.

- Публикация артефактов – model.pkl, hyperparameters.json, requirements.txt сохраняются в GitHub Artifacts.

Текущий статус:
https://github.com/your-username/your-repo/actions/workflows/ci.yml/badge.svg
