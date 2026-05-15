# Fix Firebase Domain Authorization Error ✅

## Error Message
```
❌ Firebase: This domain is not authorized for OAuth operations for your Firebase project. 
Edit the list of authorized domains from the Firebase console. (auth/unauthorized-domain).
```

## Root Cause
Firebase doesn't recognize `localhost:5000` as an authorized domain for OAuth operations.

---

## Solution: Add localhost to Authorized Domains

### Step 1: Go to Firebase Console
1. Open https://console.firebase.google.com/
2. Select your project: **unvibe-54ae1**

### Step 2: Navigate to Authentication Settings
1. Click **Authentication** in the left sidebar
2. Click **Settings** tab (gear icon at the top)
3. Scroll down to **Authorized domains**

### Step 3: Add localhost:5000
1. Click **Add domain** button
2. Enter: `localhost:5000`
3. Click **Add**

### Step 4: Also Add Other Domains (Optional)
If you plan to deploy, add these too:
- `127.0.0.1:5000`
- `localhost:3000` (if using different port)
- Your production domain (when ready)

### Step 5: Save and Verify
1. The domain should appear in the authorized domains list
2. Wait 5-10 seconds for changes to propagate
3. Refresh your browser
4. Try signing in again

---

## Step-by-Step Screenshots Guide

### Step 1: Firebase Console
```
1. Go to: https://console.firebase.google.com/
2. Select project: unvibe-54ae1
3. You should see the project dashboard
```

### Step 2: Authentication Settings
```
1. Left sidebar → Authentication
2. Top menu → Settings (gear icon)
3. Scroll down to "Authorized domains"
```

### Step 3: Add Domain
```
1. Click "Add domain" button
2. Type: localhost:5000
3. Click "Add"
```

### Step 4: Verify
```
1. You should see "localhost:5000" in the list
2. Status should show as authorized
3. Wait 5-10 seconds for propagation
```

---

## Complete List of Domains to Add

### For Local Development
- ✅ `localhost:5000`
- ✅ `127.0.0.1:5000`
- ✅ `localhost` (without port)

### For Production (When Ready)
- ✅ `yourdomain.com`
- ✅ `www.yourdomain.com`
- ✅ `api.yourdomain.com`

---

## After Adding Domain

### Clear Browser Cache
1. Press **Cmd+Shift+Delete** (Mac) or **Ctrl+Shift+Delete** (Windows)
2. Select "All time"
3. Check "Cookies and other site data"
4. Click "Clear data"

### Hard Refresh
1. Press **Cmd+Shift+R** (Mac) or **Ctrl+Shift+R** (Windows)

### Test Again
1. Go to http://localhost:5000/login
2. Click "Sign in with Google"
3. Should work now ✅

---

## Troubleshooting

### Issue: Still Getting the Error
**Solution:**
1. Wait 10-15 seconds for Firebase to propagate changes
2. Clear browser cache completely
3. Close and reopen browser
4. Try again

### Issue: Domain Not Appearing in List
**Solution:**
1. Make sure you clicked "Add" button
2. Check for typos (should be exactly: `localhost:5000`)
3. Try refreshing the Firebase console page
4. Try adding again

### Issue: Can't Find Authorized Domains Section
**Solution:**
1. Make sure you're in Authentication section
2. Click Settings (gear icon) at the top
3. Scroll down - it should be there
4. If not visible, try different browser

### Issue: Getting Different Error
**Solution:**
1. Check browser console (F12)
2. Look for error messages
3. Check Firebase project ID is correct
4. Verify Firebase SDK is loading

---

## Firebase Console Navigation

### Quick Path
```
1. https://console.firebase.google.com/
2. Select "unvibe-54ae1" project
3. Left sidebar → Authentication
4. Top menu → Settings (⚙️ icon)
5. Scroll to "Authorized domains"
6. Click "Add domain"
7. Enter "localhost:5000"
8. Click "Add"
```

---

## What Each Domain Does

| Domain | Purpose |
|--------|---------|
| `localhost:5000` | Local development on port 5000 |
| `127.0.0.1:5000` | Local development using IP |
| `localhost` | Local development (any port) |
| `yourdomain.com` | Production domain |
| `www.yourdomain.com` | Production with www |

---

## After Fix - What Should Work

✅ Google Sign-In
✅ Google Sign-Up
✅ Email/Password Sign-In
✅ Email/Password Sign-Up
✅ Firestore sync
✅ Dashboard access
✅ All features

---

## Testing After Fix

### Test 1: Google Sign-In
1. Go to http://localhost:5000/login
2. Click "Sign in with Google"
3. Should open Google popup (not error)
4. Select account
5. Should redirect to dashboard ✅

### Test 2: Google Sign-Up
1. Go to http://localhost:5000/register
2. Click "Sign up with Google"
3. Should open Google popup (not error)
4. Select account
5. Should redirect to dashboard ✅

### Test 3: Email/Password
1. Go to http://localhost:5000/register
2. Fill form with @newhorizonindia.edu email
3. Click "Create My Account"
4. Should redirect to dashboard ✅

---

## Browser Console Check

After adding domain, you should see:
```
✅ Firebase initialized successfully!
✅ Firebase Auth Enhanced module loaded
🔐 Google Sign-In initiated...
✅ Google Sign-In successful: yourname@newhorizonindia.edu
```

NOT:
```
❌ Firebase: This domain is not authorized for OAuth operations...
```

---

## Summary

1. ✅ Go to Firebase Console
2. ✅ Select unvibe-54ae1 project
3. ✅ Go to Authentication → Settings
4. ✅ Add domain: `localhost:5000`
5. ✅ Wait 5-10 seconds
6. ✅ Clear browser cache
7. ✅ Hard refresh
8. ✅ Test again

---

## Status

After completing these steps:
✅ Domain error should be fixed
✅ Google Sign-In should work
✅ Google Sign-Up should work
✅ All auth methods should work
✅ Firestore sync should work

---

## Need Help?

If you're still having issues:
1. Check Firebase console for the domain in the list
2. Verify project ID is correct (unvibe-54ae1)
3. Check browser console for errors (F12)
4. Try different browser
5. Check internet connection

---

**Status**: Follow these steps to fix the domain authorization error ✅
