
# Output Format
Each Linear ticket is saved as a JSON file with additional `keywords` field`
```json
{
  "id": "1d20ef87-ef49-4b30-9359-445ee43e2f83",
  "title": "Do Weblog aggregation (hour->day) on MTN data",
  "description": "For a month's data it will take around a week as we have no certainty on the data format/file types etc. ",
  "state": {
    "name": "Todo"
  },
  "assignee": {
    "name": "Catherine da Graca"
  },
  "createdAt": "2025-02-18T18:42:42.280Z",
  "updatedAt": "2025-03-03T11:32:27.337Z",
  "url": "https://linear.app/intent-hq/issue/FWD-82/do-weblog-aggregation-hour-day-on-mtn-data",
  "keywords": [
    "Weblog aggregation",
    "MTN data",
    "hour to day",
    "data format",
    "file types"
  ]
}
```

# Usage
## Basic usage
```bash
python linear_keywords.py --input /path/to/tickets --output /path/to/output
```

## Specify a different model
```bash
python linear_keywords.py --input /path/to/tickets --output /path/to/output --model gpt-4-turbo
```

## Process only a limited number of tickets (for testing)
```bash
python linear_keywords.py --input /path/to/tickets --output /path/to/output --max-tickets 5
```

## Provide API key on command line
```bash
python linear_keywords.py --input /path/to/tickets --output /path/to/output --api-key sk-...
```
