"""Unit tests for the three deterministic agent runners."""

from agentforge_matcher_test.agents.fruits_agent.runner import FruitsRunner
from agentforge_matcher_test.agents.vehicles_agent.runner import VehiclesRunner
from agentforge_matcher_test.agents.weather_agent.runner import WeatherRunner


def test_fruits_runner() -> None:
    assert FruitsRunner().run("anything") == "fruits:ok"


def test_vehicles_runner() -> None:
    assert VehiclesRunner().run("anything") == "vehicles:ok"


def test_weather_runner() -> None:
    assert WeatherRunner().run("anything") == "weather:ok"
