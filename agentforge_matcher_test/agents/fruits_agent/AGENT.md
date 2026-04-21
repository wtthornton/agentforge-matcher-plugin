---
name: fruits-agent
namespace: project.matcher-test.fruits-agent
description: Handles fruit-related queries.
keywords: [apples, bananas, oranges, fruit]
utterances:
  - I want apples
  - find me bananas
  - looking for oranges
  - need some fruit
runner: agentforge_matcher_test.agents.fruits_agent.runner:FruitsRunner
---

# Fruits Agent

Handles fruit-related queries. Used as a matcher test fixture for the TAP-769 test rig.
