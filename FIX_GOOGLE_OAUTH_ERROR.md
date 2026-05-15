# Fix: "The OAuth client was not found" Error

## Problem
You're getting this error when trying to use Google Sign-In:
```
Access blocked: Authorization Error
The OAuth client was not found.
Error 401: invalid_client
```

## Root Cause
The `GOOGLE_CLIENT_ID` in the code is a placeholder and doesn't match your actual Google OAuth credentials.

## Solution

### Quick Fix (5 minutes)

#### Step 1: Get Your Real Google Client ID

1. Go to https://console.cloud.google.com/
2. Sign in with your Google account
3. Create a new project or select existing one
4. Go to "APIs & Services" → "Credentials"
5. Click "Create Credentials" → "OAuth client ID"
6. Choose "Web application"
7. Add authorized redirect URIs:
   ```
   http://localhost:5000
   http://localhost:5000/enter
   http://127.0.0.1:5000
   ```
8. Click "Create"
9. **Copy the Client ID** (looks like: `123456789-abc123def456.apps.googleusercontent.com`)

#### Step 2: Set Environment Variable

**Option A: Using the setup script (easiest)**
```bash
cd /Users/venkatkarthik/Downloads/univibe_v3
./setup_google_oauth.sh
# Enter your Client ID when prompted
```

**Option B: Manual setup**
```bash
export GOOGLE_CLIENT_ID="your-client-id-here"
python3 app.py
```

**Option C: Add to shell profile (permanent)**

For zsh (~/.zshrc):
```bash
echo 'export GOOGLE_CLIENT_ID="your-client-id-here"' >> ~/.zshrc
source ~/.zshrc
```

For bash (~/.bashrc):
```bash
echo 'export GOOGLE_CLIENT_ID="your-client-id-here"' >> ~/.bashrc
source ~/.bashrc
```

#### Step 3: Restart Server
```bash
# Kill current server (Ctrl+C)
# Then restart:
python3 app.py
```

#### Step 4: Test Google Sign-In
1. Go to http://localhost:5000/enter
2. Click "Sign in with Google"
3. You should see Google login popup
4. Authenticate with your Google account
5. Should redirect to dashboard

## Detailed Setup Guide

### Create Google Cloud Project

1. **Visit Google Cloud Console**
   - URL: https://console.cloud.google.com/
   - Sign in with your Google account

2. **Create New Project**
   - Click project dropdown at top
   - Click "New Project"
   - Name: "UniVibe"
   - Click "Create"

3. **Enable Google+ API**
   - Go to "APIs & Services" → "Library"
   - Search for "Google+ API"
   - Click on it
   - Click "Enable"

4. **Configure OAuth Consent Screen**
   - Go to "APIs & Services" → "OAuth consent screen"
   - Choose "External" for User Type
   - Fill in:
     - App name: "UniVibe"
     - User support email: your email
     - Developer contact: your email
   - Click "Save and Continue"
   - Skip scopes (click "Save and Continue")
   - Add test users if needed
   - Click "Back to Dashboard"

5. **Create OAuth 2.0 Credentials**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth client ID"
   - Choose "Web application"
   - Name: "UniVibe Web Client"
   - Add Authorized redirect URIs:
     ```
     http://localhost:5000
     http://localhost:5000/enter
     http://127.0.0.1:5000
     ```
   - Click "Create"

6. **Copy Client ID**
   - You'll see a popup with Client ID and Client Secret
   - **Copy the Client ID** (the long string)
   - Click "Download JSON" to save (optional)

### Set Environment Variable

**For macOS/Linux:**

```bash
# Temporary (current session only)
export GOOGLE_CLIENT_ID="your-client-id-here"

# Permanent (add to ~/.zshrc or ~/.bashrc)
echo 'export GOOGLE_CLIENT_ID="your-client-id-here"' >> ~/.zshrc
source ~/.zshrc
```

**For Windows (PowerShell):**

```powershell
$env:GOOGLE_CLIENT_ID="your-client-id-here"
```

### Verify Setup

```bash
# Check if environment variable is set
echo $GOOGLE_CLIENT_ID

# Should output your Client ID
# If empty, variable is not set
```

## Troubleshooting

### Issue: Still getting "OAuth client was not found"

**Solution:**
1. Verify Client ID is correct (copy-paste again)
2. Check authorized redirect URIs include `http://localhost:5000`
3. Make sure Google+ API is enabled
4. Try creating a new OAuth client
5. Clear browser cache and cookies

### Issue: "Redirect URI mismatch"

**Solution:**
- Add the exact URI to authorized list
- Include protocol: `http://` or `https://`
- Include port: `:5000`
- Example: `http://localhost:5000/enter`

### Issue: "Invalid client"

**Solution:**
- Double-check Client ID spelling
- No extra spaces or characters
- Regenerate OAuth client if needed

### Issue: Google button is disabled

**Solution:**
- Check browser console for errors
- Verify GOOGLE_CLIENT_ID is set
- Restart server
- Clear browser cache

## For Vercel Deployment

Once you have your Client ID:

1. Go to Vercel Dashboard
2. Select your project
3. Settings → Environment Variables
4. Add new variable:
   - Name: `GOOGLE_CLIENT_ID`
   - Value: Your Client ID
5. Click "Save"
6. Redeploy project
7. Test on production URL

## Security Notes

⚠️ **Important:**
- Client ID is public (safe to share)
- Client Secret should be kept private
- Never commit credentials to GitHub
- Use environment variables for sensitive data
- Regenerate credentials if compromised

## Quick Reference

| Item | Value |
|------|-------|
| Google Cloud Console | https://console.cloud.google.com/ |
| OAuth Credentials | APIs & Services → Credentials |
| Redirect URI (Local) | http://localhost:5000 |
| Redirect URI (Vercel) | https://your-project.vercel.app |
| Environment Variable | GOOGLE_CLIENT_ID |

## Testing Checklist

- [ ] Google Client ID obtained
- [ ] GOOGLE_CLIENT_ID environment variable set
- [ ] Server restarted
- [ ] Google Sign-In button visible
- [ ] Google Sign-In button not disabled
- [ ] Google login popup appears
- [ ] Can authenticate with Google
- [ ] Redirects to dashboard
- [ ] User data in Firestore

## Still Having Issues?

1. Check browser console for errors (F12)
2. Check server logs for errors
3. Verify authorized redirect URIs
4. Try incognito/private browsing
5. Try different Google account
6. Regenerate OAuth credentials

---

**Status:** Follow this guide to fix the OAuth error
**Last Updated:** May 16, 2026
