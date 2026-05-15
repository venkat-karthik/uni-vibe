# 🔧 Fix: Firebase Unauthorized Domain Error

## ❌ The Error You're Seeing
```
Sign-in failed: Firebase: Error (auth/unauthorized-domain).
```

---

## ✅ The Fix (Takes 2 Minutes)

### Step 1: Open Firebase Console
Click this link:
```
https://console.firebase.google.com/project/univibe-c85c6/authentication/settings
```

Or manually:
1. Go to https://console.firebase.google.com/
2. Select project: **univibe-c85c6**
3. Click **Authentication** (left sidebar)
4. Click **Settings** tab

### Step 2: Find Authorized Domains
Scroll down until you see this section:

```
┌─────────────────────────────────────────────────────┐
│ Authorized domains                                  │
├─────────────────────────────────────────────────────┤
│ ✓ univibe-c85c6.firebaseapp.com                    │
│                                                     │
│ [Add domain]                                        │
└─────────────────────────────────────────────────────┘
```

### Step 3: Add Localhost
1. Click **[Add domain]** button
2. Type: `localhost`
3. Press Enter or click Add
4. Click **[Add domain]** again
5. Type: `127.0.0.1`
6. Press Enter or click Add

**Result should look like:**
```
┌─────────────────────────────────────────────────────┐
│ Authorized domains                                  │
├─────────────────────────────────────────────────────┤
│ ✓ univibe-c85c6.firebaseapp.com                    │
│ ✓ localhost                                         │
│ ✓ 127.0.0.1                                        │
│                                                     │
│ [Add domain]                                        │
└─────────────────────────────────────────────────────┘
```

### Step 4: Wait & Refresh
1. Wait **30 seconds** for Firebase to update
2. Go back to your browser
3. Press **Ctrl+R** (or **Cmd+R** on Mac) to refresh
4. Press **Ctrl+Shift+Delete** to clear cache
5. Try signing in again

---

## 🎯 Test It

1. Go to: http://localhost:5000/enter
2. Click **"Sign in with Google"**
3. A Google login popup should appear
4. Sign in with your Google account
5. You should be redirected to the dashboard ✅

---

## 🐛 Still Not Working?

### Try This:
1. **Use 127.0.0.1 instead of localhost**
   - Change URL to: `http://127.0.0.1:5000/enter`
   - Make sure `127.0.0.1` is in authorized domains

2. **Check browser console for errors**
   - Press **F12** to open Developer Tools
   - Go to **Console** tab
   - Look for red error messages
   - Share the error message

3. **Verify you're in the right project**
   - Check Firebase Console URL contains: `univibe-c85c6`
   - Check Settings → General for API Key: `AIzaSyCDwaBMoEJvJO1NBS-uUzsMTirSSGz8Mcc`

4. **Clear everything and try again**
   - Close browser completely
   - Clear browser cache (Ctrl+Shift+Delete)
   - Reopen browser
   - Go to http://localhost:5000/enter
   - Try signing in

---

## 📋 Checklist

- [ ] Opened Firebase Console
- [ ] Found Authentication Settings
- [ ] Added `localhost` to authorized domains
- [ ] Added `127.0.0.1` to authorized domains
- [ ] Waited 30 seconds
- [ ] Refreshed browser (Ctrl+R)
- [ ] Cleared cache (Ctrl+Shift+Delete)
- [ ] Tried signing in again
- [ ] ✅ Success!

---

## 🔗 Quick Links

| Link | Purpose |
|------|---------|
| https://console.firebase.google.com/project/univibe-c85c6/authentication/settings | Add authorized domains |
| http://localhost:5000/enter | Test Google Sign-In |
| http://localhost:5000 | Home page |

---

## 💡 Why This Happens

Firebase has security restrictions to prevent unauthorized apps from using your credentials. When you try to sign in from `localhost`, Firebase doesn't recognize it as an authorized domain, so it blocks the request.

By adding `localhost` and `127.0.0.1` to the authorized domains list, you're telling Firebase: "It's OK to allow sign-ins from these local addresses."

---

## ✨ What Happens After Sign-In

1. ✅ Google authentication popup appears
2. ✅ You sign in with your Google account
3. ✅ Your user is created in Firestore
4. ✅ Your user is created in SQLite database
5. ✅ You're redirected to the dashboard
6. ✅ You can now use all UniVibe features!

---

## 🆘 Need Help?

1. Check the browser console (F12) for error messages
2. Make sure you added both `localhost` and `127.0.0.1`
3. Try using `http://127.0.0.1:5000` instead of `http://localhost:5000`
4. Clear browser cache completely
5. Try a different browser
6. Check that Firebase project is `univibe-c85c6`

---

**Status**: Ready to fix! Just add localhost to authorized domains.
