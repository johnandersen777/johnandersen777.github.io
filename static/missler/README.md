```bash
cat 24Hours.json | jq -r 'to_entries[] | .value'
```
