# Experiment 19: Full CI/CD Pipeline Using GitHub Actions

## Files in this Folder
- `app.py`: Flask application.
- `test_app.py`: Automated pytest test cases (tests routes and JSON schema).
- `requirements.txt`: Package dependencies (`flask`, `pytest`).
- `Dockerfile`: Container image specification.
- `.github/workflows/cicd.yml`: Two-stage automated pipeline (`test` $\rightarrow$ `build-and-push`).

## Steps for You to Complete on GitHub:
1. **Publish to GitHub:**
   - In Antigravity IDE / VS Code: Open this folder.
   - Click the **Source Control (Ctrl+Shift+G)** panel $\rightarrow$ click **Initialize Repository**.
   - Stage all files (`+`), write commit message `Initial Flask CI/CD setup`, and click **Publish Branch to GitHub**.
2. **Add GitHub Secrets (via Web GUI):**
   - Go to your repo on GitHub $\rightarrow$ **Settings** $\rightarrow$ **Secrets and variables** $\rightarrow$ **Actions**.
   - Add:
     - `DOCKERHUB_USERNAME`: your Docker Hub username
     - `DOCKERHUB_TOKEN`: your Docker Hub token
3. **Watch Automated Pipeline:**
   - Push any commit to `main`.
   - In the **Actions** tab on GitHub, watch `Run Automated Tests` (pytest) run and pass, automatically unlocking the `Build & Push Docker Image` job!

