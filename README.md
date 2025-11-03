# CrewAI AgentCore Template

This is a template repository for deploying CrewAI agents on AWS AgentCore.

## Generated for Team: testteam
- **Agent Name**: test
- **Model**: us.anthropic.claude-3-5-sonnet-20241022-v2:0

## Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python src/agent.py

# Test the agent
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, how can you help me?"}'
```

### Deploy to AgentCore
```bash
# Configure AgentCore
agentcore configure --entrypoint src/agent.py

# Deploy to production
agentcore launch
```

## Customization

### Modify Agent Behavior
Edit `src/agent.py` to customize:
- Agent role and backstory
- Task processing logic
- Error handling
- Additional tools

### Environment Variables
Set in `agentcore.yaml` or during deployment:
- `AWS_REGION`: AWS region for Bedrock
- `TEAM_NAME`: Your team identifier
- `MODEL_ID`: Bedrock model to use

### CI/CD Pipeline
The GitHub Actions workflow in `.github/workflows/deploy.yml` automatically:
1. Installs dependencies
2. Runs tests (add your own in `tests/`)
3. Deploys to AgentCore on push to main

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GitHub Repo   │───▶│  GitHub Actions  │───▶│   AgentCore     │
│                 │    │                  │    │                 │
│ - Agent Code    │    │ - Build & Test   │    │ - Auto-scaling  │
│ - Configuration │    │ - Deploy         │    │ - Monitoring    │
│ - CI/CD Config  │    │ - Notifications  │    │ - Load Balancer │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │  Amazon Bedrock │
                                               │                 │
                                               │ - Claude Models │
                                               │ - Usage Tracking│
                                               └─────────────────┘
```

## Support

- **Documentation**: [AgentCore Docs](https://aws.github.io/bedrock-agentcore-starter-toolkit/)
- **Issues**: Contact your platform team
- **Monitoring**: Check AgentCore dashboard for metrics

## Next Steps

1. Customize the agent in `src/agent.py`
2. Add tests in `tests/` directory
3. Push changes to trigger deployment
4. Monitor performance in AgentCore dashboard
