# Quick Fix - Firebase Not Initialized ⚡

**If you're seeing "Firebase not initialized" error, follow these steps:**

---

## Step 1: Clear Browser Cache (Most Important!)

### Chrome/Edge:
1. Press **Ctrl+Shift+Delete** (Windows) or **Cmd+Shift+Delete** (Mac)
2. Select "All time"
3. Check:
   - ☑️ Cookies and other site data
   - ☑️ Cached images and files
4. Click "Clear data"

### Firefox:
1. Press **Ctrl+Shift+Delete** (Windows) or **Cmd+Shift+Delete** (Mac)
2. Click "Clear Now"

### Safari:
1. Click "Safari" → "Preferences"
2. Click "Privacy"
3. Click "Manage Website Data"
4. Select all
5. Click "Remove"

---

## Step 2: Hard Refresh Page

Press **Ctrl+Shift+R** (Windows) or **Cmd+Shift+R** (Mac)

This clears cache AND reloads the page fresh.

---

## Step 3: Restart Server

Open terminal and run:

```bash
pkill -f "python.*app.py"
sleep 1
/Users/venkatkarthik/Downloads/univibe_v3/venv/bin/python /Users/venkatkarthik/Downloads/univibe_v3/app.py
```

---

## Step 4: Check Browser Console

1. Press **F12** to open DevTools
2. Click **Console** tab
3. Look for these messages:

✅ **Good** - You should see:
```
✅ Firebase initialized successfully!
✅ Firebase Auth Enhanced module loaded
```

❌ **Bad** - If you see:
```
❌ Firebase initialization error: ...
```

---

## Step 5: Test Google Sign-In

1. Go to http://localhost:5000/login
2. Click "Sign in with Google"
3. Check console (F12) for messages
4. Should see:
   ```
   🔐 Google Sign-In initiated...
   ✅ Google Sign-In successful: yourname@newhorizonindia.edu
   ```

---

## If Still Not Working

### Check Network Tab

1. Open DevTools (F12)
2. Click **Network** tab
3. Reload page
4. Look for Firebase scripts:
   - firebase-app-compat.js
   - firebase-auth-compat.js
   - firebase-firestore-compat.js
   - firebase-analytics-compat.js

All should show **200** status (green).

If any show **404** or **failed**:
- Your internet might be down
- CDN might be blocked
- Try different network

### Check Internet Connection

1. Open https://www.google.com
2. If it doesn't load, internet is down
3. Try different WiFi or mobile hotspot

### Try Different Browser

1. Try Chrome, Firefox, Safari, or Edge
2. Some browsers might work better

### Disable Extensions

1. Open DevTools (F12)
2. Check if any extensions are blocking scripts
3. Try disabling ad blockers or popup blockers

---

## Complete Restart (Nuclear Option)

If nothing works:

1. **Close browser completely**
2. **Kill server**:
   ```bash
   pkill -f "python.*app.py"
   ```
3. **Wait 5 seconds**
4. **Restart server**:
   ```bash
   /Users/venkatkarthik/Downloads/univibe_v3/venv/bin/python /Users/venkatkarthik/Downloads/univibe_v3/app.py
   ```
5. **Open fresh browser window**
6. **Go to http://localhost:5000**
7. **Press Ctrl+Shift+R** (hard refresh)

---

## Verify Everything Works

### Check 1: Firebase Initialized
- Console shows "✅ Firebase initialized successfully!"

### Check 2: Firebase Objects Available
Run in console:
```javascript
console.log(window.firebaseAuth);  // Should show Auth object
console.log(window.firebaseDb);    // Should show Firestore object
```

### Check 3: Google Sign-In Works
1. Click "Sign in with Google"
2. Google popup appears
3. Select account
4. Redirected to dashboard

### Check 4: Email/Password Works
1. Go to register page
2. Fill form with @newhorizonindia.edu email
3. Create account
4. Login with credentials

### Check 5: Firestore Synced
1. Go to https://console.firebase.google.com/project/unvibe-54ae1
2. Click "Firestore Database"
3. Click "Collections"
4. Click "users"
5. See your user document

---

## Still Stuck?

1. **Read the full debugging guide**: `FIREBASE_INITIALIZATION_DEBUG.md`
2. **Check server logs**: Look at terminal where server is running
3. **Check browser console**: F12 → Console tab
4. **Check network tab**: F12 → Network tab
5. **Verify Firebase project**: https://console.firebase.google.com/project/unvibe-54ae1

---

## Quick Commands

```bash
# Kill server
pkill -f "python.*app.py"

# Start server
/Users/venkatkarthik/Downloads/univibe_v3/venv/bin/python /Users/venkatkarthik/Downloads/univibe_v3/app.py

# Test server
curl http://localhost:5000/test

# Test Firebase auth endpoint
curl -X POST http://localhost:5000/api/firebase_auth \
  -H "Content-Type: application/json" \
  -d '{
    "uid": "test-user",
    "email": "test@newhorizonindia.edu",
    "displayName": "Test User",
    "photoURL": "",
    "provider": "google"
  }'
```

---

**Status**: ✅ Should be working now!

If not, follow the full debugging guide: `FIREBASE_INITIALIZATION_DEBUG.md`
