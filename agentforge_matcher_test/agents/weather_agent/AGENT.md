---
name: weather-agent
namespace: project.matcher-test.weather-agent
description: Handles weather and forecast queries.
keywords: [weather, forecast, rain, temperature, climate]
utterances:
  - what's the forecast
  - will it rain
  - chance of precipitation
  - is it going to be sunny
  - temperature tomorrow
runner: agentforge_matcher_test.agents.weather_agent.runner:WeatherRunner
---

# Weather Agent

Handles weather and forecast queries. Used as a matcher test fixture for the TAP-769 test rig.
