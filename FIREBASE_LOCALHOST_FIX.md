# Fix: Firebase Unauthorized Domain Error

## The Problem
```
Sign-in failed: Firebase: Error (auth/unauthorized-domain).
```

This happens because Firebase doesn't recognize `localhost` as an authorized domain for your app.

---

## The Solution (3 Steps)

### Step 1️⃣: Open Firebase Console
Go to: https://console.firebase.google.com/project/univibe-c85c6/authentication/settings

### Step 2️⃣: Find "Authorized domains"
Scroll down on the Authentication Settings page until you see the **Authorized domains** section.

### Step 3️⃣: Add These Domains
Click **Add domain** and add:
- `localhost`
- `127.0.0.1`

**Screenshot of what to look for:**
```
┌─────────────────────────────────────────┐
│ Authorized domains                      │
├─────────────────────────────────────────┤
│ ✓ univibe-c85c6.firebaseapp.com        │
│ ✓ localhost                    [Add]    │
│ ✓ 127.0.0.1                   [Add]    │
└─────────────────────────────────────────┘
```

---

## After Adding Domains

1. **Wait 30 seconds** for Firebase to update
2. **Refresh your browser** (Ctrl+R or Cmd+R)
3. **Clear cache** (Ctrl+Shift+Delete)
4. **Try signing in again** at http://localhost:5000/enter

---

## What Should Happen

✅ Click "Sign in with Google"
✅ Google login popup appears
✅ You authenticate with your Google account
✅ You're redirected to the dashboard
✅ Your user is created in Firestore
✅ Your user is created in SQLite database

---

## If It Still Doesn't Work

### Option A: Use 127.0.0.1 Instead of localhost
- Change your URL from `http://localhost:5000` to `http://127.0.0.1:5000`
- Make sure `127.0.0.1` is in authorized domains

### Option B: Check Browser Console
1. Press **F12** to open Developer Tools
2. Go to **Console** tab
3. Look for error messages
4. Share the error for debugging

### Option C: Check Firebase Project
1. Make sure you're in the correct project: **univibe-c85c6**
2. Go to Settings → General
3. Verify the API Key matches: `AIzaSyCDwaBMoEJvJO1NBS-uUzsMTirSSGz8Mcc`

---

## Direct Firebase Console Link

**Authentication Settings:**
https://console.firebase.google.com/project/univibe-c85c6/authentication/settings

---

## Current Status

| Component | Status |
|-----------|--------|
| Firebase Project | ✅ Created |
| Google Sign-In | ✅ Configured |
| Firestore Database | ✅ Ready |
| Frontend Code | ✅ Implemented |
| Backend Code | ✅ Implemented |
| Localhost Authorization | ⏳ **PENDING** |

---

## Timeline

1. Add localhost to authorized domains (2 minutes)
2. Wait for Firebase to update (30 seconds)
3. Refresh browser and clear cache (1 minute)
4. Test Google Sign-In (1 minute)

**Total time: ~5 minutes**

---

## Questions?

If you're stuck:
1. Check the browser console (F12) for error messages
2. Verify you're in the correct Firebase project
3. Make sure the authorized domains are saved
4. Try clearing browser cache and cookies
5. Try using `127.0.0.1:5000` instead of `localhost:5000`

---

**Next Step**: Add localhost to authorized domains in Firebase Console
