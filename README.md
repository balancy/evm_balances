# App to check balances of EVM-compatible wallet

Web-app helps to check balances of a wallet in different evm-compatible networks.
It's build using litestar python framework for backend and svelte.js for frontend.

## Install

1. Clone the repository

```sh
git clone https://github.com/balancy/evm_balances.git
```

## Run locally
You should have docker-compose installed on your computer.

Run docker-compose by:
```sh
make
```

## Run on server
Define the file with environment variables

```sh
cp .env.example .env
```

Define your host inside `.env`
- HOST=your_hostname

Run docker-compose by:
```sh
make prod
```

## Use in dev version
The app will be available on http://localhost:5173/