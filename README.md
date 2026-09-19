# Legal Market Intelligence

A compact decision engine that turns case demand, revenue, location, and local talent supply into an explainable market opportunity ranking.

## The decision problem

Where should a legal practice expand, and which expertise should it recruit there? Raw case records contain the answer, but leaders need a clear view of demand, commercial value, and local supply.

The opportunity score uses:

- **40% demand:** relative case volume
- **40% value:** relative revenue
- **20% undersupply:** inverse local lawyer availability

The output also identifies the most common case type in each city to guide targeted recruiting.

## Run it

```bash
python market_intelligence.py
python -m unittest test_market_intelligence.py
```

## Example output

| Rank | City | Cases | Revenue | Top demand | Local lawyers | Score |
|---:|---|---:|---:|---|---:|---:|
| 1 | Mombasa | 4 | $44,700 | Maritime | 12 | 93.7 |
| 2 | Nakuru | 3 | $27,700 | Commercial | 10 | 69.5 |

## Engineering choices

- Standard-library Python keeps the analysis portable
- Dataclasses make the domain model explicit
- The scoring formula remains explainable to decision makers
- Tests cover ranking behavior and empty datasets
- Markdown output works in GitHub, reports, and automated workflows

## Next steps

- Add time-series demand and seasonality
- Validate weights with historical expansion outcomes
- Serve scores through FastAPI
- Add a Power BI or Streamlit decision dashboard

The included dataset is fictional and intended for demonstration only.
