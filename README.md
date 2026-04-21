# agentforge-matcher-plugin

Test rig for the AgentForge hybrid matcher (TAP-769). Provides three semantically
distinct agent domains — fruits, vehicles, weather — so BM25 + embedding routing
can be exercised with clear, non-overlapping signal.

## Agents

| Agent | Namespace | Domain |
|---|---|---|
| fruits-agent | project.matcher-test.fruits-agent | Fruit queries (apples, bananas, oranges) |
| vehicles-agent | project.matcher-test.vehicles-agent | Transport queries (taxi, car, cab, ride) |
| weather-agent | project.matcher-test.weather-agent | Weather queries (forecast, rain, temperature) |

## Routes

- `GET /api/matcher-test/status` — health check
- `POST /api/matcher-test/score` — BM25 score all three agents against a prompt

### Score request

```json
{"prompt": "I want some oranges"}
```

### Score response

```json
{"scores": {"fruits-agent": 2.4, "vehicles-agent": 0.0, "weather-agent": 0.0}, "top": "fruits-agent"}
```

The `/score` endpoint uses BM25-only scoring (no fastembed download required) so
it stays fast in CI.

## Installation

```bash
pip install -e /path/to/agentforge-matcher-plugin
```

Then register via the plugin API:

```bash
curl -X POST http://localhost:8000/api/plugins/register \
  -H 'Content-Type: application/json' \
  -d '{"package_name": "agentforge_matcher_test"}'
```

## Running the smoke test

Install the plugin into the AgentForge dev environment, then:

```bash
cd /path/to/AgentForge
uv run pytest backend/tests/test_matcher_smoke.py -v
```

The test is skipped automatically when the plugin is not installed.
