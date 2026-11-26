# Deploy HeatGuard AI on Render

This repository is configured for a Render Web Service. The current Python backend returns rule-based mock advisory output; it is not connected to Gemini or a live weather service.

## Existing service
- Repository: https://github.com/ramanjaneyareddy15/heatguard-ai-g15
- Branch: `main`
- Service: `heatguard-ai-g15`
- Start command: `python backend.py`
- Build command: `pip install -r requirements.txt`
- Health route: `/health`

## Automatic deployment
The existing Render service is configured to deploy automatically when a new commit is pushed to its connected GitHub branch. After pushing changes, open the Render dashboard, select the service and check Deploys. Confirm the latest commit reaches **Live** before sharing the updated site.

## Local run
```bash
python backend.py
```
Open `http://127.0.0.1:8000`.

## Supported prompt options
The browser interface supports Baseline and Structured only. Do not document or expect a third prompt-selector option.

## Responsible use
Test the public URL after every deployment. Label the app as a rule-based mock prototype unless a model integration is implemented and tested. Never upload API keys or passwords to the repository.
