# Задание 1: Анализ и проектирование

## Подзадание 1.1: Анализ и планирование

1. Функциональность монолитного приложения:
- Управление отоплением:
    - Пользователи могут удалённо включать/выключать отопление в своих домах.
    - Пользователи могут устанавливать желаемую температуру.
    - Система автоматически поддерживает заданную температуру, регулируя подачу тепла.
- Мониторинг температуры:
    - Система получает данные о температуре с датчиков, установленных в домах.
    - Пользователи могут просматривать текущую температуру в своих домах через веб-интерфейс.

2. Архитектура монолитного приложения:
- Язык программирования: Java
- База данных: PostgreSQL
- Архитектура: Монолитная, все компоненты системы (обработка запросов, бизнес-логика, работа с данными) находятся в рамках одного приложения.
- Взаимодействие: Синхронное, запросы обрабатываются последовательно.
- Масштабируемость: Ограничена, так как монолит сложно масштабировать по частям.
- Развертывание: Требует остановки всего приложения.

3. Домены и границы контекстов:
- домен "Управление устройствами": хранит данные об устройствах, обрабатывает запросы на конфигурацию и управляет устройствами
- домен "Управление сценариями": хранит данные о сценариях и управляет в соответствии с ними конфигурацией устройств
- домен "Телеметрия": получает, обрабатывает и сохраняет телеметрические данные от устройств
- домен "Пользователи": управление учетными данными пользователей

4. Визуализация контекста системы

![PlantUML model](http://www.plantuml.com/plantuml/png/fPFHQXD158Rlzod6u4K2DhdnIX0ADTYBLej1l0pJPDekxCuiknFQtZK94aebVGHHNo1KLxD9ixx2p1lvdzdO97OLeHSXCtFE-Syt_zdPJZIFTIyCl4U-x0Izhc0dMaV9iqOZvgVrOr-Vz0vxYOWxIceXTRsZmaOKS4arMudk1lvXO-VfrW4TlTtVQuGyqIB6KNi75ToN8gv7fEzfNmU2jSuH3na5nPbcNPyVnpnaHofchH0eR5U5WkqhgGBqzhm34ITALWdX2QkOZoOtS_l1_C3_ZPdOWKbfN_b7Z9cfkJMf7TjBh39cXxPl1_O2MHcjA9UPdzX-CpCKZEq8XGkpi5ScPMQ669AdPewCxouojMCqVApF8_6yGcILckSL5wloA0hy3jU-ac0gkP93_U8q9sWzBnIfKmwM721tH-OMx0pmEUqfIY1OVsNO88pab7HmdQ6zi5ShgfOwqgSy_ktt2h3TFDFLn2q9v1Dq-qknoJq4U_qdhRr6ny7IGnmjdDSktQqpPcuOZCp9ScRxQ_88bZMeRO09cIWtwC_tx-Scaa7T7OpWnAoOEq8fzQHMcvZKUORQI_p6Tbnkst2TcPnw8uBb1xS-pVAn_SyTtHHHIOIKH5_V6Xl-ixyDjEPWDZ2AuJq0frJK6RzwHKCxkfCamultODz3hXIrCAwr-_fTUw_vildgHRNcRGlPnSl_1G00)

[Схема в формате PlantUML](diagrams\as_is\context.puml)

## Подзадание 1.2: Архитектура микросервисов

1. Декомпозиция на микросервисы

Основываясь на выделенных доменах и границах контекстов и бизнес-целях выделены следующие микросервисы:
- микросервис "Пользователи"
- микросервис "Управление устройствами"
- микросервис "Управление сценариями"
- микросервис "Телеметрия"

2. Определение взаимодействия

- пользователи взаимодействуют с веб приложением
- веб приложение взаимодействует с микросервисами через API Gateway
- веб приложение взаимодействуют с микросервисом "Пользователи" для авторизации\аутентификации и получения данных пользователей
- веб приложение взаимодействуют с микросервисом "Управление устройствами" для получения данных устройств и их конфигурирования
- веб приложение взаимодействуют с микросервисом "Управление сценариями" для конфигурирования сценариев желаемого поведения устройств
- веб приложение взаимодействуют с микросервисом "Телеметрия" для получения динамически изменяющихся данных устройств
- микросервис "Пользователи" взаимодействует с микросервисом "Управление устройствами" для удаления устройств при удалении пользователя из приложения
- микросервисом "Управление устройствами" взаимодействует с микросервисом "Телеметрия" для передачи данных устройств по которым требуется собирать данные телеметрии
- микросервисом "Управление устройствами" взаимодействует с микросервисом "Управление сценариями" для удаления сценариев при удалении устройства из приложения
- микросервис "Управление сценариями" взаимодействует с микросервисом "Управление устройствами" для установки требуемой конфигурации устройств

3. Визуализация архитектуры

- C4 — Уровень контейнеров (Containers)
![PlantUML model](http://www.plantuml.com/plantuml/png/fLF1RjD04BtxAvQ8GoBH-C892QbIYUYXXOe8SOosoRQrPEzQwutQtf9Mg495xISWu0UYGY1jqlGNPl-8Dt6eQyKW90wMPsTstdlpnbxFdBIkdyJ1eqXtutvFYGFdqknP65fvsDoFt45_jvyfspNQAUsQNPE4QImrzwnbhXT7k-76qxKTJhtTtWeJcJbbaUfiSCUHQwQC7hZ8nKgqZr5DnB8aUf7Sjp8HUyQATYAj4vicKMBRQ1E3EGXsbCsChhE09w96dsXEK_-HVk9zHID_GcC-r_vI4tJd1pIXAT8_aBgbYRz4msDtdAhdDKQkDO8W5rQNQHf7NUaYeu5P8Mb1zNM1EGBDD4UaiQ0v6ETqLwHe9cWYQ8Oipbnb8OY_2HnGnkKnKf3gJ_t0dnUgscRF7Khxswz2OATrvEhP8cGXdu4xN8ADLYJmd6Mr_XAC9m9qt3N2fVdz41nV2xeIz1tH32FvOG7FnIg2HacOqfcnpFbbTJwwzUV003edpk34JRutbCRCoLHbcSnyWzuFU2xyHRLjfmyrirDlLBpyOChRN5tRlyt8M-HEL8Py2Ro31zhmllxJGXiiflnHvSlx3pcLe6nyyOU0_UmUaWr72FVzUy1LIisDQs--VjVPQhrilNfHRmJhIlVmv_u2)

[Схема в формате PlantUML](diagrams\to_be\containers\smart_home.puml)

- C4 — Уровень компонентов (Components)
  - Пользователи

    ![PlantUML model](http://www.plantuml.com/plantuml/png/fPFHQXD158Rlzod6u4K2DhdnIX0ADTYBLej1l0pJPDekxCuiknFQtZK94aebVGHHNo1KLxD9ixx2p1lvdzdO97OLeHSXCtFE-Syt_zdPJZIFTIyCl4U-x0Izhc0dMaV9iqOZvgVrOr-Vz0vxYOWxIceXTRsZmaOKS4arMudk1lvXO-VfrW4TlTtVQuGyqIB6KNi75ToN8gv7fEzfNmU2jSuH3na5nPbcNPyVnpnaHofchH0eR5U5WkqhgGBqzhm34ITALWdX2QkOZoOtS_l1_C3_ZPdOWKbfN_b7Z9cfkJMf7TjBh39cXxPl1_O2MHcjA9UPdzX-CpCKZEq8XGkpi5ScPMQ669AdPewCxouojMCqVApF8_6yGcILckSL5wloA0hy3jU-ac0gkP93_U8q9sWzBnIfKmwM721tH-OMx0pmEUqfIY1OVsNO88pab7HmdQ6zi5ShgfOwqgSy_ktt2h3TFDFLn2q9v1Dq-qknoJq4U_qdhRr6ny7IGnmjdDSktQqpPcuOZCp9ScRxQ_88bZMeRO09cIWtwC_tx-Scaa7T7OpWnAoOEq8fzQHMcvZKUORQI_p6Tbnkst2TcPnw8uBb1xS-pVAn_SyTtHHHIOIKH5_V6Xl-ixyDjEPWDZ2AuJq0frJK6RzwHKCxkfCamultODz3hXIrCAwr-_fTUw_vildgHRNcRGlPnSl_1G00)

    [Схема в формате PlantUML](diagrams\to_be\components\users.puml)

  - Управление устройствами
  
    ![PlantUML model](http://www.plantuml.com/plantuml/png/fPFHQXD158Rlzod6u4K2DhdnIX0ADTYBLej1l0pJPDekxCuiknFQtZK94aebVGHHNo1KLxD9ixx2p1lvdzdO97OLeHSXCtFE-Syt_zdPJZIFTIyCl4U-x0Izhc0dMaV9iqOZvgVrOr-Vz0vxYOWxIceXTRsZmaOKS4arMudk1lvXO-VfrW4TlTtVQuGyqIB6KNi75ToN8gv7fEzfNmU2jSuH3na5nPbcNPyVnpnaHofchH0eR5U5WkqhgGBqzhm34ITALWdX2QkOZoOtS_l1_C3_ZPdOWKbfN_b7Z9cfkJMf7TjBh39cXxPl1_O2MHcjA9UPdzX-CpCKZEq8XGkpi5ScPMQ669AdPewCxouojMCqVApF8_6yGcILckSL5wloA0hy3jU-ac0gkP93_U8q9sWzBnIfKmwM721tH-OMx0pmEUqfIY1OVsNO88pab7HmdQ6zi5ShgfOwqgSy_ktt2h3TFDFLn2q9v1Dq-qknoJq4U_qdhRr6ny7IGnmjdDSktQqpPcuOZCp9ScRxQ_88bZMeRO09cIWtwC_tx-Scaa7T7OpWnAoOEq8fzQHMcvZKUORQI_p6Tbnkst2TcPnw8uBb1xS-pVAn_SyTtHHHIOIKH5_V6Xl-ixyDjEPWDZ2AuJq0frJK6RzwHKCxkfCamultODz3hXIrCAwr-_fTUw_vildgHRNcRGlPnSl_1G00)

    [Схема в формате PlantUML](diagrams\to_be\components\devices.puml)

  - Управление сценариями
  
    ![PlantUML model](http://www.plantuml.com/plantuml/png/fPFHQXD158Rlzod6u4K2DhdnIX0ADTYBLej1l0pJPDekxCuiknFQtZK94aebVGHHNo1KLxD9ixx2p1lvdzdO97OLeHSXCtFE-Syt_zdPJZIFTIyCl4U-x0Izhc0dMaV9iqOZvgVrOr-Vz0vxYOWxIceXTRsZmaOKS4arMudk1lvXO-VfrW4TlTtVQuGyqIB6KNi75ToN8gv7fEzfNmU2jSuH3na5nPbcNPyVnpnaHofchH0eR5U5WkqhgGBqzhm34ITALWdX2QkOZoOtS_l1_C3_ZPdOWKbfN_b7Z9cfkJMf7TjBh39cXxPl1_O2MHcjA9UPdzX-CpCKZEq8XGkpi5ScPMQ669AdPewCxouojMCqVApF8_6yGcILckSL5wloA0hy3jU-ac0gkP93_U8q9sWzBnIfKmwM721tH-OMx0pmEUqfIY1OVsNO88pab7HmdQ6zi5ShgfOwqgSy_ktt2h3TFDFLn2q9v1Dq-qknoJq4U_qdhRr6ny7IGnmjdDSktQqpPcuOZCp9ScRxQ_88bZMeRO09cIWtwC_tx-Scaa7T7OpWnAoOEq8fzQHMcvZKUORQI_p6Tbnkst2TcPnw8uBb1xS-pVAn_SyTtHHHIOIKH5_V6Xl-ixyDjEPWDZ2AuJq0frJK6RzwHKCxkfCamultODz3hXIrCAwr-_fTUw_vildgHRNcRGlPnSl_1G00)

    [Схема в формате PlantUML](diagrams\to_be\components\scenarios.puml)

  - Телеметрия

    ![PlantUML model](http://www.plantuml.com/plantuml/png/fPFHQXD158Rlzod6u4K2DhdnIX0ADTYBLej1l0pJPDekxCuiknFQtZK94aebVGHHNo1KLxD9ixx2p1lvdzdO97OLeHSXCtFE-Syt_zdPJZIFTIyCl4U-x0Izhc0dMaV9iqOZvgVrOr-Vz0vxYOWxIceXTRsZmaOKS4arMudk1lvXO-VfrW4TlTtVQuGyqIB6KNi75ToN8gv7fEzfNmU2jSuH3na5nPbcNPyVnpnaHofchH0eR5U5WkqhgGBqzhm34ITALWdX2QkOZoOtS_l1_C3_ZPdOWKbfN_b7Z9cfkJMf7TjBh39cXxPl1_O2MHcjA9UPdzX-CpCKZEq8XGkpi5ScPMQ669AdPewCxouojMCqVApF8_6yGcILckSL5wloA0hy3jU-ac0gkP93_U8q9sWzBnIfKmwM721tH-OMx0pmEUqfIY1OVsNO88pab7HmdQ6zi5ShgfOwqgSy_ktt2h3TFDFLn2q9v1Dq-qknoJq4U_qdhRr6ny7IGnmjdDSktQqpPcuOZCp9ScRxQ_88bZMeRO09cIWtwC_tx-Scaa7T7OpWnAoOEq8fzQHMcvZKUORQI_p6Tbnkst2TcPnw8uBb1xS-pVAn_SyTtHHHIOIKH5_V6Xl-ixyDjEPWDZ2AuJq0frJK6RzwHKCxkfCamultODz3hXIrCAwr-_fTUw_vildgHRNcRGlPnSl_1G00)

    [Схема в формате PlantUML](diagrams\to_be\components\telemetry.puml)

- C4 — Уровень кода (Code)

  ![PlantUML model](http://www.plantuml.com/plantuml/png/fPFHQXD158Rlzod6u4K2DhdnIX0ADTYBLej1l0pJPDekxCuiknFQtZK94aebVGHHNo1KLxD9ixx2p1lvdzdO97OLeHSXCtFE-Syt_zdPJZIFTIyCl4U-x0Izhc0dMaV9iqOZvgVrOr-Vz0vxYOWxIceXTRsZmaOKS4arMudk1lvXO-VfrW4TlTtVQuGyqIB6KNi75ToN8gv7fEzfNmU2jSuH3na5nPbcNPyVnpnaHofchH0eR5U5WkqhgGBqzhm34ITALWdX2QkOZoOtS_l1_C3_ZPdOWKbfN_b7Z9cfkJMf7TjBh39cXxPl1_O2MHcjA9UPdzX-CpCKZEq8XGkpi5ScPMQ669AdPewCxouojMCqVApF8_6yGcILckSL5wloA0hy3jU-ac0gkP93_U8q9sWzBnIfKmwM721tH-OMx0pmEUqfIY1OVsNO88pab7HmdQ6zi5ShgfOwqgSy_ktt2h3TFDFLn2q9v1Dq-qknoJq4U_qdhRr6ny7IGnmjdDSktQqpPcuOZCp9ScRxQ_88bZMeRO09cIWtwC_tx-Scaa7T7OpWnAoOEq8fzQHMcvZKUORQI_p6Tbnkst2TcPnw8uBb1xS-pVAn_SyTtHHHIOIKH5_V6Xl-ixyDjEPWDZ2AuJq0frJK6RzwHKCxkfCamultODz3hXIrCAwr-_fTUw_vildgHRNcRGlPnSl_1G00)

  [Схема в формате PlantUML](diagrams\to_be\code.puml)


## Подзадание 1.3: ER-диаграмма

1. Идентификация сущностей
2. Определение атрибутов
3. Описание связей
4. ER-диаграмма

## Подзадание 1.4: Создание и документирование API
1. Выбор типов API



2. API для микросервиса «Управление устройствами»
3. API для микросервиса «Телеметрия»
4. API для микросервиса «Пользователи»
5. Описание контрактов взаимодействия
6. Документирование API

# Базовая настройка

## Запуск minikube

[Инструкция по установке](https://minikube.sigs.k8s.io/docs/start/)

```bash
minikube start
```


## Добавление токена авторизации GitHub

[Получение токена](https://github.com/settings/tokens/new)

```bash
kubectl create secret docker-registry ghcr --docker-server=https://ghcr.io --docker-username=<github_username> --docker-password=<github_token> -n default
```


## Установка API GW kusk

[Install Kusk CLI](https://docs.kusk.io/getting-started/install-kusk-cli)

```bash
kusk cluster install
```


## Настройка terraform

[Установите Terraform](https://yandex.cloud/ru/docs/tutorials/infrastructure-management/terraform-quickstart#install-terraform)


Создайте файл ~/.terraformrc

```hcl
provider_installation {
  network_mirror {
    url = "https://terraform-mirror.yandexcloud.net/"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
```

## Применяем terraform конфигурацию 

```bash
cd terraform
terraform apply
```

## Настройка API GW

```bash
kusk deploy -i api.yaml
```

## Проверяем работоспособность

```bash
kubectl port-forward svc/kusk-gateway-envoy-fleet -n kusk-system 8080:80
curl localhost:8080/hello
```


## Delete minikube

```bash
minikube delete
```
