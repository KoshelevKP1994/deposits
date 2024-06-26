# deposits

## application

simple rest api project for calculating deposits profitability scheduler

## API Endpoints

`GET health` 
return status code 200 if application is OK

`POST /deposits/v1/profitability_scheduler` 
calculate deposit scheduler

## test

`sh run_tests.sh`

## запуск прилождения

Запуск через докер

`sh build.sh` - первый запуск и пересборка приложения

`sh start.sh` - последующие запуски приложения

`sh stop.sh` - остановка приложения

приложения будет доступно на `http://0.0.0.0:8000/`


