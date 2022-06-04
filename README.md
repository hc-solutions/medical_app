This is an open source service for healthcare.

This app will help to create appointments and notify hospital staff and patients about them,
track analysis and medicine expiration time and notify about it.
App will help to manage electronic health records, track all prescriptions, diagnoses and so on.

Later we will work to create fully functional and secure application to manage a tiny hospital / private medical practice

---

## Installation for local development

To make this project work you should add some DNS-records to your hosts file
In linux and Mac OS it is located at `/etc/hosts` and at `c:\Windows\System32\Drivers\etc\hosts` for Windows

```
127.0.0.1 hc-solutions.local
127.0.0.1 app.hc-solutions.local
127.0.0.1 traefik.hc-solutions.local
127.0.0.1 api.hc-solutions.local
127.0.0.1 ms.hc-solutions.local
```

After that you could run project with docker-compose: `docker-compose up -d`
Hot-reload for frontend and backend is enabled by default and work well on Linux and MacOS,
but you could face some troubles when installing same project on Windows.

**Please check your git settings and be aware of proper CR and LF DOS line endings!**

`hc-solutions.local` - VueJS Frontend with Argon libraries \
`app.hc-solutions.local` - VueJS Admin panel with Argon libraries \
`traefik.hc-solutions.local` - Reverse Proxy for local development \
`api.hc-solutions.local` - FastAPI Backend in Python \
`ms.hc-solutions.local` - Meilisearch, fast and tiny search engine
