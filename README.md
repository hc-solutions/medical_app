Сервис будет предоставлять возможность вести учет анализов пациентов, сроки их исследований и предупреждать персонал 
лечебного учреждения о необходимости пересдать анализы. 
Однако, база данных, разработанная в рамках данного проекта позволяет модернизировать проект и использовать его для 
управления небольшим лечебным учреждением.

---

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

`hc-solutions.local` - фронтенд на VueJS \
`auth.hc-solutions.local` - сервис авторизации на базе KeyCloak \
`traefik.hc-solutions.local` - Reverse Proxy \
`api.hc-solutions.local` - Бэкенд на Python \
`ms.hc-solutions.local` - Поисковое ядро 


Первичная настройка keycloak:
1. Запустить все через docker-compose up -d
2. Открыть auth.hc-solutions.local
3. Зайти в административную-консоль
4. Создать realm с названием backend-realm
5. Создавть в realm "client": backend-client-id, root-url: http://api.hc-solutions.local
6. Добавить пользователя с именем admin@hc-solution.com и паролем "querty", поставить галочку email-verified
7. Готово, теперь можно отправлять запросы к бэкенду. Токен можно получать у keycloak