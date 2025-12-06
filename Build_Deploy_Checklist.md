# Build & Deploy Checklist (GitHub Pages)

## Local Development & Build

- [ ] **Dependencies**: `npm install` completes successfully without errors.
- [ ] **Local Server**: `npm run start` launches the Docusaurus development server.
- [ ] **Navigation**: Verify all sidebar links, internal links, and external links are functional.
- [ ] **Search**: Confirm the search functionality (if enabled) works as expected.
- [ ] **Build Process**: `npm run build` completes without errors.
- [ ] **Local Build Preview**: Serve the static build output locally to verify everything (`npx serve build`).
- [ ] **Linting & Formatting**: `npm run lint` and `npm run format` (if configured) pass without issues.

## GitHub Pages Deployment

- [ ] **Repository Setup**: GitHub repository is public and correctly initialized.
- [ ] **Docusaurus Config**: `docusaurus.config.ts` is configured for GitHub Pages:
    - `baseUrl`: Set to `'/your-repo-name/'` (e.g., `'/ai-humanoid-robotics-book/'`).
    - `projectName`: Set to your GitHub repository name (e.g., `'ai-humanoid-robotics-book'`).
    - `organizationName`: Set to your GitHub username or organization (e.g., `'your-github-username'`).
- [ ] **Deployment Script**: Add `deploy` script to `package.json`:
    ```json
    {
      "scripts": {
        "deploy": "docusaurus deploy"
      }
    }
    ```
- [ ] **GitHub Actions Workflow (Example `deploy.yml`)**:

    ```yaml
    name: Deploy to GitHub Pages

    on:
      push:
        branches:
          - main # Deploy on pushes to the main branch

    jobs:
      deploy:
        name: Deploy
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
            with:
              fetch-depth: 0 # Not required for Docusaurus, but good for historical context

          - uses: actions/setup-node@v3
            with:
              node-version: 18 # Or your preferred Node.js version

          - name: Install dependencies
            run: npm install

          - name: Build Docusaurus website
            run: npm run build

          - name: Deploy to GitHub Pages
            uses: peaceiris/actions-gh-pages@v3
            with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
              publish_dir: ./build # The folder that Docusaurus builds to
              # cname: example.com # Uncomment if you're using a custom domain
              # user_name: 'github-actions[bot]' # Optional: use a bot name for commits
              # user_email: 'github-actions[bot]@users.noreply.github.com' # Optional: bot email
    ```

- [ ] **Initial Deployment**: Run `npm run deploy` locally (if `GIT_USER` env var is set, or configure `docusaurus.config.ts` with `deploymentBranch: 'gh-pages'`). Alternatively, push to `main` and let GitHub Actions trigger the deployment.
- [ ] **Site Reachability**: Verify the deployed site is accessible at `https://<your-github-username>.github.io/<your-repo-name>/`.
- [ ] **Broken Links/Images**: Check the deployed site for any broken links or missing images.
- [ ] **Search Functionality (Deployed)**: Confirm search works correctly on the live site.

