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

[Схема в формате PlantUML](diagrams\as_is\context.puml)

<details>
<summary>Показать схему</summary>

![PlantUML model](http://www.plantuml.com/plantuml/png/fPFHQXD158Rlzod6u4K2DhdnIX0ADTYBLej1l0pJPDekxCuiknFQtZK94aebVGHHNo1KLxD9ixx2p1lvdzdO97OLeHSXCtFE-Syt_zdPJZIFTIyCl4U-x0Izhc0dMaV9iqOZvgVrOr-Vz0vxYOWxIceXTRsZmaOKS4arMudk1lvXO-VfrW4TlTtVQuGyqIB6KNi75ToN8gv7fEzfNmU2jSuH3na5nPbcNPyVnpnaHofchH0eR5U5WkqhgGBqzhm34ITALWdX2QkOZoOtS_l1_C3_ZPdOWKbfN_b7Z9cfkJMf7TjBh39cXxPl1_O2MHcjA9UPdzX-CpCKZEq8XGkpi5ScPMQ669AdPewCxouojMCqVApF8_6yGcILckSL5wloA0hy3jU-ac0gkP93_U8q9sWzBnIfKmwM721tH-OMx0pmEUqfIY1OVsNO88pab7HmdQ6zi5ShgfOwqgSy_ktt2h3TFDFLn2q9v1Dq-qknoJq4U_qdhRr6ny7IGnmjdDSktQqpPcuOZCp9ScRxQ_88bZMeRO09cIWtwC_tx-Scaa7T7OpWnAoOEq8fzQHMcvZKUORQI_p6Tbnkst2TcPnw8uBb1xS-pVAn_SyTtHHHIOIKH5_V6Xl-ixyDjEPWDZ2AuJq0frJK6RzwHKCxkfCamultODz3hXIrCAwr-_fTUw_vildgHRNcRGlPnSl_1G00)
</details>

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
  [Схема в формате PlantUML](diagrams\to_be\containers\smart_home.puml)

  <details>
  <summary>Показать схему</summary>

  ![PlantUML model](http://www.plantuml.com/plantuml/png/dPNVRXj55CRlzoa6Ymj7QkCRhf2G2cdKL0fWwbJSLB8stgcpqlwnPiQa5a9gGccfGB50N2AGu0KSW-dMTZUlCFj6V6TscMxNQpPA92ixCzzyvpVddDcz8vKhr3WCdFVyQ12CFSvEb1h93piTuPxk3drrCZuUIou6SQHuf7O7STWP1Mv4UsvBvGN-SMVlWzjTcdhuwM4dTANY0bFzFUnm_OYBtH7vEyfN0MUOTVDfvldkKBWXUnmBrWk1mGxYa3jEbmiPHssAUekrzEywrQliH_qA_-Twbfth1OrR_xF6z5NsL2TwXUb_CFL69zaK6zvNan7_g4NEhHt7wKt06lO_YSUHvuf9MvenVD_Ij7ROrmx3dprDU-WgVkfE8FkuUv_ToqT44mtzw8d1-XKeJxFlyViMI8b-XV5pOc3qQE3Ix8oOcLuolOPaMSmjy7yEwHbqQq2-6_knC6NmACZFEDXbpKdrWXW4TmUgLT8b-Wsb1qpFCF4wEsFwRxqYfBc1Ie2HOigiGJdFUQ_gCamY1eUwu3NKb6-vjLmw8SpHH9t4aG7-qzZEe5ZzPygGo1U0FySXVg1y4VmCQtQubNE3nkDV-GCkjqUYurCrR29GYMj14iTIfu1wXl5VS49sy3D4M-qt0EM0HwxmjoDYttCpc9a0q-lYNTNVbkmCr0cPr3jN-HGFUCYLc52WFueyhwaw-QOAoc_wqg1Seh_F4Mb6jKie1hbJMNC0HXU5V92_QNQHlSoPW3IjL1j4xoBTFMvxnttRPZz1Z9OkxSg-8vHkBDLGyDuNXmRi5-kvQEoVQYpRH3U8rjW4DehjX9l5gPGJJrlYs8hUDCvvjGjCaRwnhzZz9wguTwOvDsvOMctQR4fEHQ9CfDJsCZs_PdfEX2c5n3brGa8YeCLRZ3nnYZdvePDckHi9bl1yYT_5vbtDNz8N82zXInx9M1Gd1lOBo9VvnmTR5iIGCvQm8I7V589rxahXKkBCnIc4k9JvUyowwXbrzWCU5D--qjl-eUIIWXuS7NLxK97exRBz9DNgx2gvoegegichrAIoZTcWiurLg-iVsfTnWx9Te9Tk-GFkUioDF7OgVCL9VhJNVNI_ii7wDuHlE93LbQz-4qB9itAN6pQMSb6vd0qRBLh-K3dBew8fgZ5iXzUAdTx1vr_s3_VlxNzsjxtZt473ZSFWNm00)
  </details>

- C4 — Уровень компонентов (Components)
  - Пользователи

    [Схема в формате PlantUML](diagrams\to_be\components\users.puml)

    <details>
    <summary>Показать схему</summary>

    ![PlantUML model](http://www.plantuml.com/plantuml/png/ZPHHRz9G5CVV-ockF44YuyKddwPisKnGSMpnaHHw0qtABMalJc9CO3WrmMJHcFXYzC4lq36QiI7iAvpxZVoVTAmGmRYaMSzfp-_yp_-UiXrgEz2TbcVTSrNTwpXIDBLkXmyBXS0-tcgukjcfTK8Pr7sbfT9RTRzLQ7ksuffyg1tFhHMA3_9bJXqzBHLQTgXbW5IrwBVQlkAQDlEj8WYsgsIGRTXQ7jlT-oBpgFn4x2LH1g5gkEertz1tYapFVCGrC2SqeKl4xsbYpWJVqetfqTpqQKuZGTU2VkELwzjSZFyZlDetWqnkgQiZNxbr6JBz5mE06T6KOfgXE1PcW8eJPj0Lt-5Xn5oMq-xgfgyocqff0X6ecvbtY2z0wj64ISpOY8UuL5triTzHZXrqisnsc5YmPYP1Do1CpIUwJF0WnJI5p9nuOra2VtU-PqqV-C3tF1a0U0Gm7YuoF0rVz8FEUI8wPnZcYFwo64fNmI2nbmje9GdlY9_vm6W6rVqyJK6uG09WS5P1ExMiKwik9aPTnAq5ZTass3aqfmmi-w5k1BBoeiGHVLqyfNY37RYk5iqEfBTgH2gUlfXXKiWR5ADsJkDqO2wjbj9XbwN-vBOuqmyKSI6l07jbJjbAQ3jBikF_blhMij0k_JHMpuw-fITYXWBC21krPXNNDu4SR3ABPCaiZJLnxlQiURMIbzZX_SF3CZJn-0Vf-2lV3mRxvxUpKSWItwhiFtzPBUtkxJxRoUQiRQaS_g7u0m00)
    </details>

  - Управление устройствами

    [Схема в формате PlantUML](diagrams\to_be\components\devices.puml)

    <details>
    <summary>Показать схему</summary>

    ![PlantUML model](http://www.plantuml.com/plantuml/png/dLNVJXfF6BtVfvWVLvYetFokUcMBHflGbefDBpSBJ91asIMxIvKqJGIhhR6Hs3JfZR59VG54IP4_-0epRzJppU8kJD7ODjbqPfZldFETEJEk-87b1RMARVnNTWfshSZPTX1K_IUfb6VjB9VAmNOjN_EvLt2TW3l1Si6jfAgsvL3DaXyKxN8-bVv_AKjBRrvaKXNB3xY79JFjLggkGpLLmZVIGB3A3lUI9IlWErPzaIMUPf-pzN2MmDGfbPrT6eWpqPPxyZE-VTaKFV4ByqFHaor6Gt4hzyHODiHOT9ZeCp74blvahOl_EzZQaFk9XIbMly0TookxFk5VA8WsDWv4LunGtcMeE5GJK1CLePAOQZtOTft4VMNY5Z86yWk4GGwAc_W9SqZfOmD0vYBFQ0kupIiyyCWJyPFgyGtHIZCiq6ISYqibun8DDy7IPk8QLC0dPFa9XOgSAUU6H2rRyaGUXNeWfuKAx1xXX-C_rD1vAvT-pEliKQR8VQMYUOUlqTrZ6huRA8cbhEQJnRnPvE_A1QuKdG850PY2amSa8klwGSdZkTSP9UbRHAQaDCX74DtGI7I88bT7JYlcscwG3E5L9_fECTOxb2rgQmAgMCPHupI-OHJ9Quo6AbBARMfkI3ykCi941nt2mtcq5PhQq0Vc4RuJ95gC8VuZdBp2mjua-oSprfZFt9fJjBnwSigUitdt06Br4vAjERPWWqe2UsyO3F-Y2voK3R1whcrp3ooh8HzBHujaaXRCTXXC_Rh2UmqRMIEuATnSk1A1dgeKZoZKIs80a2ii05k7kZF2B3nIxLSbhgUEvbfq8n_2ns2UGpXLi2hQJMxF-X8r0c1v70QRXPTOuSVDezJCn8t72O_l7AxF91lg-O1x1yhOqIH_m7ieuJ5HJ3F7dOUb6XyC0mZnSpqR0_4zFbbvpEZrmRMEr4VFOq_Fdrg_Ft-0tjZQoa80o2TlaKvzGVq_23OBOsx6Fipy7T20j9SQeyvVOS-yu-Uo6VNTrzuicWpe5ZRrnrxq7i4uD-hXshy5MxVUo6syUcjcrjRNNguc5umLxXHh5Vit)
    </details>
  
  - Управление сценариями
    
    [Схема в формате PlantUML](diagrams\to_be\components\scenarios.puml)

    <details>
    <summary>Показать схему</summary>

    ![PlantUML model](http://www.plantuml.com/plantuml/png/bLJ1RjD04BtxAvQS4eaq5qwS2cdL8WK8JH57ox5NYILd7TaRIeIGafGMf20Y418IGd3e3xXjh8QcQNvXzu-OMMExJXg5LggoEzvvxytRcTtqkU7nJilHxjdCT3eM9KtEs_x3Kiap3ZOQDczswXsVUgRBE6LymtHRfRPZCCmf-jnox7gf_A1OnT3BfvLIo_0vzI2abzrMssMOqqPyhGm8XisebsyOd1uOtViazwZwXEn4knniMSDcRt0XVef0zkH7-3-K0p4H5x0_5XCv8hWKSzaJrx8lhiKP4PT4NC6Hot-n47xFu6XV7kOADrWj-jesgO_e9meWW6DJ4OeP98S4YFfoW1ZY3wxWOu2uAAVTvKsNvLQbYWc8WBoPV0_xSq3g0JyW8SPAU11tmnJziTjXbk5ry-YshpouhIW2oSUAEK0Mq5SWRpMDm5zYU5xs0TPp7OTw05GpAJCys_NXH1p6MbGzlyIfgkSKy0PGHR1aCEZCeeC-T3A3N8jY2UmNTMSpqDqlYYd0d4C0q9V0JCzb6IGC931VvL3C8NkAKEYa72qQ468Bm1c2PO3YEReKsIu_0vtYIspUgkUjkkx7R97K04icOgooPd8eZv2ywlgyuT7QYugIyYt-Ai9R9CH4UzJ9kf-QfOgvY5hs2emPm7AS6eofUYKrTr7cRxG1kkY3230PcmxlHnvXtQ1h54N7QsGcAXCYDFp_vAdBMgzilGRjdQOXNl8GP1jMV4yxK0u99iFyB0xU4hWSnVEwkxzV1HgWIAP-aU84LQw4IheA2liKkQBc8uJzACkWxyMsfE_BZxi_1YccLjjz_aglREziFzlA5xHDoYnyF_y2)
    </details>
  
  - Телеметрия

    [Схема в формате PlantUML](diagrams\to_be\components\telemetry.puml)

    <details>
    <summary>Показать схему</summary>

    ![PlantUML model](http://www.plantuml.com/plantuml/png/fLJTIXj15BxVfvZcAa8rDxtgbQsA5j8sDPPUXaqonC1cDknEgg4KZDQs83Iq2BqfIkaBh3_1LCtw2cVUgD-PPDrkY5Ie89cPdE_dV6SoYw5s0zrfUSw3fgfvdReKcrgtmyU5Gk1kBJIQUhDJxOGogFbAIwKNQdwhqFPSnPZvKDUzPhMmz6Y-n4UldnSBBJVKCi1HPSbljNt5c3RpEqjWS9jA1lc6g-MMstqeSazApyJgU9V3LZMQQfiNz8CYisC-ut_FxDAGBh3_I4FJ5xoa6xD3iUbHJAU2BWLTe-HoSZR0vobAUsOlD_UNQbs-RTPaoEo_B464iYiQq0ZWWO1Gp-mo1_tc5RwCc9VjjBjwqrUvkw0qX0dWHkO3zcTWse4-c9ZZJdgOSyfTfDMgh6phV2XLw0SiSKWHAZznIrRo6AW1dLDiSLRQzD7cBeIjPeo2wqb0NmJ5mlGcnJ4AMHy6prDMYg2T9bDvwdTKtGswUHvqQEEVbQS0uS2sVStgjib-RawySno1lzjvvqqFr87lUPBxsP2UR4aTT56H77DVjhSZEh5ndh0xTZOzNuufomwFFCWCStbyTalxrLwP4Mpsvk4ufhEaxocoMk2h31CVfEuI8zduxAsxuPnX7IvlE1sUDESF2Qjn6-zoDL-lLdIYCBONSPlCogYHEJ3xB5ZoGzq8PFbLqSeV9j_IO4RsD4oargMNpJoDYBu1VJ5sR95OdgUnChHIJ2ETDdgCqYkpXxuZ1iFmFoobj2afHte_AvDnJBluYH7iSzOGxj_RX_FUSS2PlZRPQqdVqtjc3WJO8WmrwJVvRMT6D5i9N6iR6oKeGYrzPQRKZe1DNexBgT5Zmp_fcVIp7ewCOcLzabhwW1p_LnTEUUtbcqfnPNNbnN9-pbcKgixlzny0T)
    </details>

- C4 — Уровень кода (Code)

    [Схема в формате PlantUML](diagrams\to_be\code\code.puml)

    <details>
    <summary>Показать схему</summary>

    ![PlantUML model](http://www.plantuml.com/plantuml/png/vLN1QXin4BtlLqptv59CBpdL9QHiBeKMIbEVGbccqiGLrKggD4en8V_UtNf5nxkEsMCWkXZclJTwUXfhhn9ZvDpPwfLnocPDyBwvUDjSj8tlWdVa-BAg0gfVk2Eeh-dUA88RYiDl3GyLz4jPJ0aEMECTHsyjnG4SrvillVhsGFXAgU-Rw3liY5kqTlNwF--OCZ1Ms-t7Qy5GaP1fLOY_CoKMSB_zdTdb-A_7eOagfLK1p-h4tgrnTtvgG9Cb9b5zh6OXZFc81DPwD1nyCkpZVbEzq7Ha27944juNupVg9tKekkQWaPz4PVbKA9zCubj94k5kdZ9PZYmlKLw0p6xYR7FknjeYGZRUpOLJCmANupGS4OpUJ2evKMoFoeaZEEneKk9zc9Oq9HLD66nDaDwo8pK0hKR6KpRbmC73yt4bqt--yPLXMvAWB1yUbRbZCMEBDfK1BUuo-pElr_xu_Ni7TIJKy2SQ9j0_wb4dHlgKPfj8Cekz9ToItrdg_E1BwUURbrW40kjB-4QMEkAu_n0mCCMUtQ2rmAKEqMUcL9-KJv-ZNlqPdGdP8jCu058gFy15BNpEjQ2HiQuUgojoEdVsBm00)
    </details>

## Подзадание 1.3: ER-диаграмма

1. Идентификация сущностей

- Пользователь (User)
- Дом (House)
- Устройство (Device)
- Тип устройства (DeviceType)
- Конфигурация устройства (DeviceConfiguration)
- Датчик (Sensor)
- Телеметрия (TelemetryData)
- Сценарий (Scenario)

2. Определение атрибутов

- Сущность "Пользователь":
  - id
  - username
  - password
  - email
- Сущность "Дом":
  - id
  - user_id
  - address
- Сущность "Устройство":
  - id
  - type_id
  - house_id
  - user_id
  - serial_number
  - name
  - description
  - connection_data
- Сущность "Тип устройства":
  - id
  - name
  - description
- Сущность "Конфигурация устройства":
  - device_id
  - configuration
- Сущность "Датчик":
  - id
  - user_id
  - device_id
  - name
  - description
  - connection_data
- Сущность "Телеметрия":
  - id
  - sensor_id
  - timestamp
  - data
- Сущность "Сценарий":
  - id
  - user_id
  - device_id
  - scheduler_data
  - configuration

3. Описание связей

- Пользователь — Дом: один пользователь может иметь доступ к нескольким домам, но каждый дом связан только с одним пользователем.
- Дом — Устройство: один дом может содержать несколько устройств, и каждое устройство принадлежит только одному дому.
- Устройство - Тип устройства: одно устройство может быть только одного типа, но тип может быть связан с несколькими устройствами.
- Устройство - Конфигурация устройства: одно устройство может иметь только одну конфигурацию и наоборот
- Устройство - Датчик: одно устройство может иметь несколько датчиков, датчик может принадлежать только одному устройству.
- Датчик — Телеметрия: одно устройство может генерировать множество записей телеметрии.
- Пользователь - Сценарий: пользователь может завести несколько сценариев.
- Устройство - Сценарий: устройство может иметь множество сценариев 

4. ER-диаграмма

  [Схема в формате PlantUML](diagrams\to_be\er.puml)
  <details>
  <summary>Показать схему</summary>

  ![PlantUML model](http://www.plantuml.com/plantuml/png/bLF1ReCm3Btp5L6Fa_Y1dIgjXss7xT3sZ3BYWYMIe2IiGgN_FeTaQkXIfDtiznv-jcEsrd7Z1jaL7PmSSvePR5h711ge7MfL5A0Skf5jZXRCXd7BV70f67jYADWpEnxVTdCs4Awu1CBspg1gPhJdrfwr4KiK9CVk1brlDg-Qwim-S_J8g4AH85m80zPc2-xW6-jGCOIvacxieSgwf52h2Rp3I8MygzGWly0iX_ox306sDjZxnIw9MYiL5bu9xlZA88UnJuUXzF50gmsiUBneTS9cCDph4hC57bo59-vtKgSw8jxtdn-fonwKrU6OGfYP8Acy_YYhG_vxoGVeG88puuuKSuSB9DUezIFST-LGWdLSzWGUVkEPyTQvdTIWk44TjXAJrUjVtvHjGGmTILE_Xu-JQSp_vcoQob9Vmgz8d3uhMuGaCF4mYAAoZYFH4Rdgifocv4f9WxRYWO_VJxd38c7BxK9tYNSIgPW4Qlb0f6X00LK2qiKr-cQCxuPc2ZLIBcqqaiKMb1XazmC0)
  </details>

## Подзадание 1.4: Создание и документирование API
1. Выбор типов API

Для взаимодействия с микросервисами и между микросервисами выбран REST API


2. API для микросервиса «Управление устройствами»

- Получение информации об устройстве:
  - Эндпойнт: /devices/{device_id}
  - Метод: GET
  - Описание: Возвращает подробную информацию о конкретном устройстве по его ID.

3. API для микросервиса «Телеметрия»

- Получение последних данных телеметрии:
  - Эндпойнт: /telemetry/{sensor_id}
  - Метод: GET
  - Описание: Возвращает исторические данные телеметрии для устройства за определённый период времени.

4. Описание контрактов взаимодействия

- GET /devices/{device_id}
  - Формат ответа:
    <details>
    <summary>Показать</summary>

    ```json
    {
      "properties": {
        "type_id": {
          "format": "uuid",
          "title": "Type Id",
          "type": "string"
        },
        "house_id": {
          "format": "uuid",
          "title": "House Id",
          "type": "string"
        },
        "serial_number": {
          "maxLength": 255,
          "minLength": 1,
          "title": "Serial Number",
          "type": "string"
        },
        "name": {
          "maxLength": 255,
          "minLength": 1,
          "title": "Name",
          "type": "string"
        },
        "description": {
          "anyOf": [
            {
              "maxLength": 255,
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Description"
        },
        "connection_data": {
          "maxLength": 255,
          "minLength": 1,
          "title": "Connection Data",
          "type": "string"
        },
        "id": {
          "format": "uuid",
          "title": "Id",
          "type": "string"
        }
      },
      "required": [
        "type_id",
        "house_id",
        "serial_number",
        "name",
        "connection_data",
        "id"
      ],
      "title": "DevicePublic",
      "type": "object"
    }
       ```  
    
    </details>
    
  - Коды ответа: 200 — успех, 401 — не авторизован, 403 — нет доступа, 404 — устройство не найдено, 500 — ошибка сервера.
  - Пример ответа:
    ```json
       {
         "type_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
         "house_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
         "serial_number": "12554324224-ser",
         "name": "Система отопления",
         "description": "Двухконтураная система отопления",
         "connection_data": "http://device.domen.com?params=123",
         "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
       }
       ```
- GET /telemetry/{sensor_id}
  - Формат ответа:
    <details>
    <summary>Показать</summary>

    ```json
    {
        "$defs": {
            "TelemetryBase": {
                "properties": {
                    "sensor_id": {
                        "format": "uuid",
                        "title": "Sensor Id",
                        "type": "string"
                    },
                    "timestamp": {
                        "format": "date-time",
                        "title": "Timestamp",
                        "type": "string"
                    },
                    "data": {
                        "title": "Data",
                        "type": "object"
                    }
                },
                "required": [
                    "sensor_id",
                    "timestamp",
                    "data"
                ],
                "title": "TelemetryBase",
                "type": "object"
            }
        },
        "properties": {
            "data": {
                "items": {
                    "$ref": "#/$defs/TelemetryBase"
                },
                "title": "Data",
                "type": "array"
            }
        },
        "required": [
            "data"
        ],
        "title": "TelemetryPublic",
        "type": "object"
    }
       ```  
    
    </details>
  - Коды ответа: 200 — успех, 401 — не авторизован, 403 — нет доступа, 404 — устройство не найдено, 500 — ошибка сервера.
  - Пример ответа:
    ```json
    {
        "data": [
            {
                "sensor_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "timestamp": "2024-09-30T22:16:42.557Z",
                "data": {}
            }
        ]
    }
       ```

5. Документирование API
- [OpenAPI документация для микросервиса Управление устройствами](openapi\devices\openapi.json)
- [OpenAPI документация для микросервиса Телеметрия](openapi\telemetry\openapi.json)


# Задание 2: Разработка MVP

## Подзадание 2.1: Новые микросервисы и интеграция с монолитом

1. Выбор языка программирования

Для микросервисов выбран язык программирования Python, фреймворк FastAPI

2. Создание проекта

- Проект микросервис Управление устройствами расположен в папке [devices](devices)
- Проект микросервис Управление устройствами расположен в папке [telemetry](telemetry)

3. Разработка API

Используя спецификацию OpenAPI, определены эндпойнты, методы запросов, форматы данных и коды ответов для API каждого микросервиса.
После запуска микросервисов, перейдя по адресу `http://hostname:port/docs` можно посмотреть интерактивную документацию по API микросервисов. 


4. Реализация логики микросервисов

Реализован код для обработки запросов к API и выполнения бизнес логики по взаимодействию с устройствами и сбору телеметрии с датчиков. 
Реализовано взаимодействие с базой данных Postgres. Для первоначального развертывания базы данных используется Alembic, соответсвующие миграции
находятся в папках проектов микросервисов.

5. Интеграция с монолитом

Настроена интеграция с монолитом через REST API.

- Микросервис «Управление устройствами» предоставляет REST endpoint /devices/{device_id}/status, который принимает HTTP PUT-запросы с JSON-телом, содержащим новое состояние устройства ({"status": "on/off"}). Монолит может вызывать этот endpoint для изменения состояния устройства.
- Микросервис «Управление телеметрией» предоставляет REST endpoint /telemetry, который принимает HTTP POST-запросы с JSON-телом, содержащим данные телеметрии. Монолит, получая данные от датчиков, может отправлять их на этот endpoint для сохранения.


## Подзадание 2.2: Подготовка 3rd party сервисов для связи микросервисов

1. Развертывание Kafka (опционально)
2. Настройка Kafka (опционально)
3. Развертывание API Gateway

Развернут API Gateway nginx.
4. Настройка API Gateway

Настроена маршрутизация запросов к микросервисам.
http://hostname/devices - запросы попадают в микросервис Управление устройствами
http://hostnmae/telemetry - запросы попадают в микросервис Телеметрия


# Запуск

Запустить приложение:

```shell
docker compose up -d
```

## Документация по API:
- микросервис Управление устройствами: `http://localhost:8001/docs`
- микросервис Телеметрия: `http://localhost:8002/docs`

Для выполнения запросов к микросервисам необходим JWT токен, который должен получаться от микросервиса Пользователи.
Для выполнения тестовых запросов можно использовать debug токен, который наделен правами администратора и работает с настройками по умолчанию:
'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjJlYjUzYmZlLTQzMWEtNGY4Mi05MWFjLWM1ZGZkN2ZhNmY1MiIsImlzX3N1cGVydXNlciI6dHJ1ZX0.xbUVkbe4cm8hrqiTi4dOZ4FhGDLAeCLLHg8yyFXyJtA'

## Примеры запросов:

Создать тип датчика:
```shell
curl -X 'POST' \
  'http://localhost/devices/api/v1/device_types/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjJlYjUzYmZlLTQzMWEtNGY4Mi05MWFjLWM1ZGZkN2ZhNmY1MiIsImlzX3N1cGVydXNlciI6dHJ1ZX0.xbUVkbe4cm8hrqiTi4dOZ4FhGDLAeCLLHg8yyFXyJtA' \
  -H 'Content-Type: application/json' \
  -d '{
  "type_name": "Система отопления",
  "description": "Стандартная система отопления"
}'
```

Посмотреть имеемые типы датчиков:
```shell
curl -X 'GET' \
  'http://localhost/api/v1/device_types/?skip=0&limit=100' \
  -H 'accept: application/json'
```

Посмотреть имеемые типы датчиков:
```shell
curl -X 'GET' \
  'http://localhost/api/v1/device_types/?skip=0&limit=100' \
  -H 'accept: application/json'
```

Запрос от монолита для конфигурации датчика (датчик должен быть добавлен в микросервисе):
```shell
curl -X 'PUT' \
  'http://localhost/devices/3fa85f64-5717-4562-b3fc-2c963f66afa6/status' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "status": "on"
}'
```

Сохранить данные телеметрии от монолита (соответствующй сенсор должен быть создан):
```shell
curl -X 'POST' \
  'http://localhost/telemetry/' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "sensor_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "data": {"temperature": 21}
}'
```