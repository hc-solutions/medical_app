# Applying migrations & creating migrations

1. Update/create ORM models in models folder
2. Import all new models in app.db.base module, if they were not imported
3. Export PYTHONPATH from folder `backend/app` via `export PYTHONPATH=$(pwd)`
4. Run  `alembic revision --autogenerate -m "Migration name"`
5. If there will be error such `FAILED: Target database is not up to date.`, you need to apply existing migrations
to database with `alembic upgrade head`
6. Repeat step 4
7. Apply fresh migrations to database with `alembic upgrade head`

---
`(linux)`

For better coding experience, install `pre-commit` ( tool for installing git hooks to lint / check / format your code ).

You can install it with `pip3`: `pip3 install pre-commit`

Then go to  project root folder and run `pre-commit install`.

Hooks for git will be installed for this project
