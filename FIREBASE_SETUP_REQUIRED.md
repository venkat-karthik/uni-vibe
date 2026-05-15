# ⚠️ FIREBASE CONSOLE SETUP REQUIRED

## The Problem
When you click "Sign up with Google" or "Sign in with Google", you get an error about domain restrictions. This is because **Firebase Console doesn't recognize localhost:5000 as an authorized domain**.

## The Solution (5 minutes)

### Step 1: Open Firebase Console
Go to: https://console.firebase.google.com/project/unvibe-54ae1/authentication/settings

### Step 2: Find "Authorized domains" Section
Look for the list of authorized domains in the Authentication settings.

### Step 3: Add localhost:5000
Click "Add domain" and add:
```
localhost:5000
```

### Step 4: Add 127.0.0.1:5000 (Optional but recommended)
Click "Add domain" again and add:
```
127.0.0.1:5000
```

### Step 5: Remove Old Domains (if any)
If you see `newhorizonindia.edu` or any other old domains, delete them.

### Step 6: Save
Click Save button.

### Step 7: Wait
Wait 5-10 minutes for changes to propagate.

### Step 8: Test
1. Clear browser cache: `Ctrl+Shift+Delete`
2. Go to http://localhost:5000/register
3. Click "Sign up with Google"
4. Should work now ✅

## Visual Steps

```
1. Open: https://console.firebase.google.com/project/unvibe-54ae1/authentication/settings

2. Find: "Authorized domains" section

3. Click: "Add domain"

4. Enter: localhost:5000

5. Click: "Add domain" again

6. Enter: 127.0.0.1:5000

7. Remove: Any old domains (newhorizonindia.edu, etc.)

8. Click: Save

9. Wait: 5-10 minutes

10. Clear cache: Ctrl+Shift+Delete

11. Test: http://localhost:5000/register → Click "Sign up with Google"
```

## What's Happening

### Before (Current Issue)
```
User clicks "Sign up with Google"
    ↓
Firebase checks: Is localhost:5000 authorized? NO
    ↓
Firebase rejects: "This domain is not authorized"
    ↓
Error shown to user ❌
```

### After (After Firebase Console Update)
```
User clicks "Sign up with Google"
    ↓
Firebase checks: Is localhost:5000 authorized? YES
    ↓
Google OAuth popup appears
    ↓
User signs in with any Google account
    ↓
User created in system ✅
```

## Important Notes

⚠️ **This is a Firebase Console setting, NOT a code issue**
⚠️ **Changes take 5-10 minutes to propagate**
⚠️ **Clear browser cache after making changes**
⚠️ **Add both localhost:5000 and 127.0.0.1:5000 for compatibility**

## If Still Not Working

1. **Double-check Firebase Console**
   - Make sure localhost:5000 is in the list
   - Make sure you clicked Save
   - Make sure you waited 5-10 minutes

2. **Clear everything**
   - Clear browser cache: `Ctrl+Shift+Delete`
   - Try in incognito window
   - Restart server

3. **Check browser console**
   - Open DevTools: F12
   - Go to Console tab
   - Look for error messages
   - Screenshot and share the error

## Firebase Console URL
https://console.firebase.google.com/project/unvibe-54ae1/authentication/settings

---

**This is the ONLY thing preventing Google Sign-In/Sign-Up from working.**
**Once you add localhost:5000 to authorized domains, everything will work.**
