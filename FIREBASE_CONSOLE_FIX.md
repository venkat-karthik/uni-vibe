# Firebase Console Configuration Fix

## Problem
The system is still asking for "newhorizon" domain and not accepting new email sign-ups. This is likely because:

1. **Firebase Console has domain restrictions** configured for OAuth
2. **Old domain (newhorizonindia.edu) is still authorized** in Firebase settings
3. **localhost:5000 is not authorized** for OAuth operations

## Solution: Update Firebase Console Settings

### Step 1: Go to Firebase Console
1. Open: https://console.firebase.google.com/
2. Select project: **unvibe-54ae1**
3. Go to: **Authentication** → **Settings** → **Authorized domains**

### Step 2: Remove Old Domain
1. Find and delete: `newhorizonindia.edu`
2. Find and delete: Any other old domains

### Step 3: Add Authorized Domains

#### For Local Development (localhost)
Add these domains:
- `localhost:5000`
- `127.0.0.1:5000`
- `localhost`

#### For Production (when deployed)
Add your production domain:
- `yourdomain.com`
- `www.yourdomain.com`

### Step 4: Save Changes
Click "Save" and wait for changes to propagate (usually 5-10 minutes)

### Step 5: Test
1. Clear browser cache: `Ctrl+Shift+Delete`
2. Go to http://localhost:5000/register
3. Try to sign up with any email
4. Should work without domain restrictions ✅

## Visual Guide

```
Firebase Console
    ↓
Authentication
    ↓
Settings
    ↓
Authorized domains
    ↓
Remove: newhorizonindia.edu
Add: localhost:5000
Add: 127.0.0.1:5000
    ↓
Save
    ↓
Wait 5-10 minutes
    ↓
Test on http://localhost:5000/register
```

## What We Fixed in Code

### Deleted
- `static/js/firebase-auth.js` - Old file with hardcoded domain restrictions

### Verified
- ✅ `firebase-auth-enhanced.js` - No domain restrictions
- ✅ `firebase-config.js` - No domain restrictions
- ✅ `app.py` - No domain restrictions
- ✅ `templates/login.html` - No domain restrictions
- ✅ `templates/register.html` - No domain restrictions

## Common Issues and Solutions

### Issue 1: "This domain is not authorized for OAuth operations"
**Solution**:
1. Go to Firebase Console → Authentication → Settings
2. Add `localhost:5000` to Authorized domains
3. Wait 5-10 minutes
4. Refresh browser and try again

### Issue 2: Still seeing "newhorizon" error
**Solution**:
1. Check if old `firebase-auth.js` is being loaded (we deleted it)
2. Clear browser cache: `Ctrl+Shift+Delete`
3. Try in incognito window
4. Check Firebase Console for old domain entries

### Issue 3: Google Sign-In not working
**Solution**:
1. Make sure `localhost:5000` is in Authorized domains
2. Check if Google OAuth credentials are configured
3. Open DevTools (F12) → Console for error messages
4. Refresh page and try again

## Firebase Console Checklist

- [ ] Go to https://console.firebase.google.com/
- [ ] Select project: unvibe-54ae1
- [ ] Go to Authentication → Settings
- [ ] Check Authorized domains section
- [ ] Remove: newhorizonindia.edu (if present)
- [ ] Remove: Any other old domains
- [ ] Add: localhost:5000
- [ ] Add: 127.0.0.1:5000
- [ ] Add: localhost (optional)
- [ ] Click Save
- [ ] Wait 5-10 minutes for changes to propagate
- [ ] Clear browser cache: Ctrl+Shift+Delete
- [ ] Test on http://localhost:5000/register

## Testing After Firebase Console Update

### Test 1: Email Sign-Up
1. Go to http://localhost:5000/register
2. Sign up with any email (e.g., test@gmail.com)
3. Should work ✅

### Test 2: Google Sign-In
1. Go to http://localhost:5000/register
2. Click "Sign up with Google"
3. Should work with any Google account ✅

### Test 3: Email Sign-In
1. Go to http://localhost:5000/login
2. Sign in with email and password
3. Should work ✅

## Important Notes

1. **Authorized domains are global** - They apply to all authentication methods
2. **Changes take time** - Wait 5-10 minutes after saving
3. **Cache matters** - Clear browser cache after making changes
4. **localhost vs 127.0.0.1** - Both should be added for compatibility
5. **No domain restrictions in code** - All code has been cleaned

## Firebase Console URL
https://console.firebase.google.com/project/unvibe-54ae1/authentication/settings

## Next Steps

1. Update Firebase Console settings (steps above)
2. Wait 5-10 minutes
3. Clear browser cache
4. Test sign-up and sign-in
5. If still not working, check browser console for errors (F12)

---

**Status**: Code is clean, Firebase Console needs update
**Last Updated**: May 15, 2026
