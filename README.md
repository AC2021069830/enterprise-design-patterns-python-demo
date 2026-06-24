# Enterprise Design Patterns in Python

This repository is a companion demo for a Medium article about enterprise design patterns from Martin Fowler's *Patterns of Enterprise Application Architecture*.

The example shows a realistic order placement flow with:

- `Domain Model` for the business object
- `Service Layer` for orchestration and validation
- `Repository` for persistence
- `Data Mapper` for translating domain objects to storage rows

## Run

```bash
python -m pytest
python -m src.main
```

## What to look for

The important part is not the amount of code. It is the separation:

- business rules stay in the domain
- workflow stays in the service
- storage details stay behind the repository
- mapping stays isolated in the mapper
