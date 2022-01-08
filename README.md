Чтобы все заработало, необходимо добавить эти строчки в свой hosts файл

На Linux и MacOS они находятся в `/etc/hosts`
На Windows они находятся в  `c:\Windows\System32\Drivers\etc\hosts`

```
127.0.0.1 hc-solutions.local
127.0.0.1 auth.hc-solutions.local
127.0.0.1 traefik.hc-solutions.local
127.0.0.1 api.hc-solutions.local
127.0.0.1 ms.hc-solutions.local
```

После этого можно поднимать все окружение через `docker-compose up -d`
Изменения во фронте автоматически будут подтягиваться в контейнер -> будут видны сразу

`hc-solutions.local` - фронтенд на NextJS
`auth.hc-solutions.local` - сервер авторизации на базе KeyCloak
`traefik.hc-solutions.local` - Reverse Proxy
`api.hc-solutions.local` - Бэкенд на Python
`ms.hc-solutions.local` - Поисковое ядро
