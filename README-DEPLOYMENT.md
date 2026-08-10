# Deployment & PR previews

This repo's site is built with Jekyll and published to `gh-pages` via
[.github/workflows/main.yml](.github/workflows/main.yml). That workflow has
three jobs:

- **build** — always runs (push to `main`, pull requests, manual dispatch).
  Builds the Jekyll site and uploads it as a workflow artifact named `site`.
- **publish** — runs on pushes to `main` (or a manual dispatch with
  "publish" checked). Downloads the `site` artifact and pushes it to the
  `gh-pages` branch, which serves the live site.
- **preview** — runs on pull requests opened from a branch of this
  repository (not a fork). Downloads the `site` artifact and deploys it to
  [Cloudflare Pages](https://pages.cloudflare.com/) as a per-PR preview,
  then posts (or updates) a comment on the PR with the preview link.

Forked PRs never run the `preview` job's deploy step, since forks don't have
access to repository secrets — that's a GitHub Actions security boundary,
not a bug.

## One-time Cloudflare Pages setup

You need a Cloudflare account and an API token before the `preview` job can
deploy anything.

1. **Create the Cloudflare API token.**
   In the Cloudflare dashboard: **My Profile → API Tokens → Create Token**,
   using the **"Edit Cloudflare Workers"** template (or a custom token with
   `Account.Cloudflare Pages: Edit` permission). Copy the token value — it's
   only shown once.

2. **Find your Cloudflare Account ID.**
   It's shown on the right-hand sidebar of any zone/domain overview page in
   the Cloudflare dashboard, or via `wrangler whoami` if you have Wrangler
   installed locally.

3. **Set both as GitHub Actions secrets on this repo**, using the `gh` CLI
   (run from the repo root, or add `--repo AEADataEditor/aeadataeditor.github.io`
   from elsewhere):

   ```bash
   gh secret set CLOUDFLARE_API_TOKEN --body "<paste the API token>"
   gh secret set CLOUDFLARE_ACCOUNT_ID --body "<paste the account ID>"
   ```

   Or omit `--body` to be prompted / pipe the value in:

   ```bash
   gh secret set CLOUDFLARE_API_TOKEN
   echo -n "<account id>" | gh secret set CLOUDFLARE_ACCOUNT_ID
   ```

4. **Create the Cloudflare Pages project**, if it doesn't already exist.
   The workflow deploys to a project named `aeadataeditor-preview`
   (see the `--project-name` flag in the `preview` job). Create it once with
   [Wrangler](https://developers.cloudflare.com/workers/wrangler/) (requires
   Node.js):

   ```bash
   npx wrangler login
   npx wrangler pages project create aeadataeditor-preview
   ```

   If you'd rather not install anything locally, you can instead just open a
   PR — `wrangler pages deploy` in CI will create the project automatically
   on first run if it doesn't exist yet.

5. **Verify the secrets are set:**

   ```bash
   gh secret list
   ```

   You should see `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` listed
   (values are never shown, only names and update times).

## After setup

Once the secrets exist, every PR from a repo branch (not a fork) will get:

- A live preview at a Cloudflare Pages URL specific to that PR
  (`--branch=pr-<PR number>`), rebuilt on every push to the PR.
- A PR comment with the preview link, edited in place on each new commit
  rather than re-posted.

## Changing the project name

If you rename the Cloudflare Pages project, update `--project-name` in the
`preview` job of [.github/workflows/main.yml](.github/workflows/main.yml) to
match.
