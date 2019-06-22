# secure-flow-prototype

## Structure

```
.
├── LICENSE
├── README.md
├── auction
│   ├── addr.py
│   ├── auction.py
│   ├── auction_event.py
│   ├── bid.py
│   ├── card.py
│   ├── item.py
│   ├── name.py
│   └── user.py
├── auction-event-test.py
├── auction-test.py
└── gen-cfg.py
```

## Usage

See `auction-test.py` and `auction-event-test.py` for usages and unit tests.

Execute `python3 auction-test.py` (tests on a single auction) and `python3 auction-event-test.py` (tests on auction events) to run all tests

Execute `python3 gen-cfg.py` to generate cfg for `./auction/bid.py` and `./auction/auction.py`.

## Known issues

* CFG generation is not working for `./auction/auction_event.py` due to unsupported strings in the CFG generation process.

## Disclaimer

This project is simply a test project to prove an idea. Such that it might lack crucial features such as countdown, expiry dates, payments and etc. Be mindful when using this project.

Many thanks to [Staticfg](https://github.com/coetaur0/staticfg) for CFG extractions and generations

