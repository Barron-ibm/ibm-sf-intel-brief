# SE Horizon — Site Setup Guide

> Do this once. After this, every new edition publishes automatically when Bob pushes to the repo.

---

## Step 1 — Create the GitHub Repo

1. Go to [github.com/new](https://github.com/new)
2. Name it `se-horizon` (or any name you like)
3. Set visibility to **Private**
4. Do NOT initialize with a README (you'll push this folder instead)
5. Click **Create repository**

---

## Step 2 — Push This Folder to GitHub

From your terminal, inside this `se-horizon-site/` folder:

```bash
git init
git add .
git commit -m "Initial scaffold — SE Horizon site"
git branch -M main
git remote add origin https://github.com/YOUR-ORG/se-horizon.git
git push -u origin main
```

---

## Step 3 — Enable GitHub Pages

1. Go to your repo on GitHub → **Settings** → **Pages**
2. Under **Source**, select **GitHub Actions**
3. Save

GitHub will now deploy the site on every push to `main`. The URL will be:
`https://YOUR-ORG.github.io/se-horizon/`

> **Private Pages note:** On a free personal account, GitHub Pages for private repos is
> publicly accessible by URL. Use **Step 4 (Cloudflare Access)** to gate it.
> On a **GitHub Team plan ($4/user/mo)**, you can restrict Pages to org members natively
> under Settings → Pages → Access → "Only organization members".

---

## Step 4 — Gate the URL with Cloudflare Access (Free, up to 50 users)

This puts a login wall in front of the GitHub Pages URL so only your team can read it.
No code changes needed. Free for up to 50 users.

### 4a — Add your domain to Cloudflare (or use a subdomain)

If you don't have a custom domain, the easiest path is to use **Cloudflare Tunnel**
to proxy the GitHub Pages URL through a domain you own on Cloudflare.

Alternatively: set a custom domain in GitHub Pages settings first
(e.g. `horizon.yourcompany.com`) and point it to Cloudflare.

### 4b — Activate Cloudflare Zero Trust

1. Go to [one.dash.cloudflare.com](https://one.dash.cloudflare.com)
2. Click **Zero Trust** → set a team name → select **Free plan**

### 4c — Add your team's identity provider

Go to **Settings → Authentication → Login methods → Add new**. Choose one:

| Option | Best for |
|--------|----------|
| **One-time PIN (email OTP)** | Quickest setup — Cloudflare emails a code, no app needed |
| **Google Workspace** | If your team uses `@yourcompany.com` Google accounts |
| **GitHub** | If your team already has GitHub accounts |

### 4d — Create an Access Application

1. **Access → Applications → Add an Application → Self-hosted**
2. Fill in:
   - **Application name:** SE Horizon
   - **Application domain:** `YOUR-ORG.github.io/se-horizon` (or your custom domain)
3. Click **Next**
4. Under **Policy**, add a rule:
   - Rule name: `Team access`
   - Action: **Allow**
   - Include: **Emails ending in** `@ibm.com` (or your team's domain)
5. Save

From now on, anyone hitting the URL gets a Cloudflare login screen. They enter their
IBM email, receive a one-time code, and are in. Session lasts 24 hours by default.

---

## Step 5 — Add Team Members to the Repo (optional)

If team members need to VIEW the GitHub Pages site only, Cloudflare Access handles
all of that — they never need a GitHub account.

If someone needs to CONTRIBUTE (e.g. drop a file into the repo):
Go to **Settings → Collaborators and teams → Add people**

---

## That's it.

Every time Bob finishes a new newsletter edition and pushes to `main`, GitHub Actions
deploys it in ~30 seconds. The new issue appears at the top of the archive page
automatically.

---

*SE Horizon · IBM South Florida SE Team · Internal Use Only*
