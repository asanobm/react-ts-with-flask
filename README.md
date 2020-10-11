# React TypeScript with Flask Application

this repository use react (TypeScript) and Flask API Server.

```
.
├── Pipfile                   # Python virtual environments
├── Pipfile.lock              # Python virtual environments
├── README.md
├── api
│   ├── __init__.py
│   └── controllers           # API Controller
├── build.sh                  # run watch
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── server.py                 # Flask server
├── src                       # React source code
│   ├── App.test.tsx
│   ├── App.tsx
│   ├── index.tsx
│   ├── react-app-env.d.ts
│   ├── serviceWorker.ts
│   └── setupTests.ts
├── tsconfig.json
└── yarn.lock
```

## Local

### install

- front end package install

```
yarn install
```

- api package install

```
pipenv install
```

### Run Local developemnt environments

```
yarn serve
```
