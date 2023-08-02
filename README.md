# DDoSer
Небольшой скрипт на Python для проведения тестирования сайта на DDoS/DoS атаки

## Установка

1. Клонируйте репозиторий

```bash
git clone https://github.com/OkulusDev/ddoser.git
```

2. Установите make, python3, python3-pip

```bash
sudo apt install make python3 python-pip
```

3. Создайте виртуальное окружение

```bash
make create_venv
```

4. Войдите в виртуальное окружение

```bash
source venv/bin/activate
```

5. Установите зависимости

```bash
make install
```

6. Запустите DDoSer

```bash
make run
```

