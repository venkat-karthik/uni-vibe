# Google OAuth Setup Guide

## Error: "The OAuth client was not found"

This error occurs when the `GOOGLE_CLIENT_ID` in the code doesn't match your actual Google OAuth credentials.

## Step-by-Step Setup

### Step 1: Go to Google Cloud Console
1. Visit: https://console.cloud.google.com/
2. Sign in with your Google account
3. Create a new project or select existing one

### Step 2: Enable Google+ API
1. Click on "APIs & Services" in the left sidebar
2. Click "Enable APIs and Services"
3. Search for "Google+ API"
4. Click on it and press "Enable"

### Step 3: Create OAuth 2.0 Credentials
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted, configure OAuth consent screen first:
   - User Type: External
   - Fill in app name: "UniVibe"
   - Add your email
   - Save and continue
4. Back to credentials, click "Create Credentials" → "OAuth client ID"
5. Choose "Web application"
6. Name it: "UniVibe Web Client"

### Step 4: Add Authorized Redirect URIs
In the OAuth client creation form, add these URIs:

**For Local Development:**
```
http://localhost:5000
http://localhost:5000/enter
http://127.0.0.1:5000
```

**For Vercel Production:**
```
https://your-project.vercel.app
https://your-project.vercel.app/enter
```

### Step 5: Copy Your Client ID
1. After creating the OAuth client, you'll see a popup with:
   - Client ID
   - Client Secret
2. **Copy the Client ID** (it looks like: `123456789-abc123def456.apps.googleusercontent.com`)
3. Click "Download JSON" to save credentials

### Step 6: Update UniVibe Configuration

#### For Local Development:
```bash
# Set environment variable
export GOOGLE_CLIENT_ID="your-client-id-here"

# Restart server
python3 app.py
```

#### For Vercel:
1. Go to Vercel Dashboard
2. Select your project
3. Settings → Environment Variables
4. Add new variable:
   - Name: `GOOGLE_CLIENT_ID`
   - Value: Your Client ID
5. Redeploy

### Step 7: Test Google Sign-In

1. Go to http://localhost:5000/enter
2. Click "Sign in with Google"
3. You should see Google login popup
4. Authenticate with your Google account
5. Should redirect to dashboard

## Troubleshooting

### Issue: "The OAuth client was not found"
**Solution:**
- Verify Client ID is correct
- Check authorized redirect URIs include your domain
- Make sure Google+ API is enabled
- Try creating a new OAuth client

### Issue: "Redirect URI mismatch"
**Solution:**
- Add the exact URI you're using to authorized list
- Include protocol (http/https)
- Include port number (5000)

### Issue: "Invalid client"
**Solution:**
- Double-check Client ID spelling
- Regenerate OAuth client if needed
- Clear browser cache and cookies

### Issue: "Access blocked"
**Solution:**
- Check if OAuth consent screen is configured
- Verify app is not in restricted mode
- Try with different Google account

## Finding Your Client ID

If you already created OAuth credentials:

1. Go to https://console.cloud.google.com/
2. APIs & Services → Credentials
3. Look for "OAuth 2.0 Client IDs"
4. Click on "Web application"
5. Copy the Client ID

## Security Notes

⚠️ **Important:**
- Never commit Client ID to GitHub (it's public, but good practice)
- Use environment variables for sensitive data
- Keep Client Secret safe (don't share)
- Regenerate credentials if compromised

## Complete Setup Checklist

- [ ] Google Cloud project created
- [ ] Google+ API enabled
- [ ] OAuth consent screen configured
- [ ] OAuth 2.0 credentials created
- [ ] Authorized redirect URIs added
- [ ] Client ID copied
- [ ] GOOGLE_CLIENT_ID environment variable set
- [ ] Server restarted
- [ ] Google Sign-In tested locally
- [ ] Works on localhost:5000

## Next Steps

1. ✅ Get Client ID from Google Cloud Console
2. ✅ Set GOOGLE_CLIENT_ID environment variable
3. ✅ Restart Flask server
4. ✅ Test Google Sign-In
5. ✅ Deploy to Vercel
6. ✅ Test on production

---

**Status:** Follow this guide to fix the OAuth error
**Last Updated:** May 16, 2026
