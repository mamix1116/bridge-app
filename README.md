# bridge app

日本全国の橋梁及び点検データを登録してAPIとして公開するプロジェクトです。

# 開発環境

## docker-compose

```sh
docker-compose -f docker-compose.development.yml
docker-compose -f docker-compose.development.yml run app python manage.py flush --no-input
docker-compose -f docker-compose.development.yml run app python manage.py migrate
docker-compose -f docker-compose.development.yml run app python manage.py init_data
```

entry point: http://localhost:1337
