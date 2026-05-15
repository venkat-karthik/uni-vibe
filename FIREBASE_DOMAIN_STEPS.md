# Firebase Domain Authorization - Step-by-Step Guide 📋

## The Problem
When you try to sign in with Google, you get this error:
```
❌ Firebase: This domain is not authorized for OAuth operations for your 
Firebase project. Edit the list of authorized domains from the Firebase 
console. (auth/unauthorized-domain).
```

## The Solution
Add `localhost:5000` to your Firebase project's authorized domains list.

---

## Step-by-Step Instructions

### STEP 1️⃣: Open Firebase Console

**Action:**
1. Open your browser
2. Go to: https://console.firebase.google.com/
3. You should see your Firebase projects

**What you should see:**
- List of Firebase projects
- Your project "unvibe-54ae1" should be visible

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ Firebase Console                        │
├─────────────────────────────────────────┤
│ Projects:                               │
│ • unvibe-54ae1  ← Click this            │
│ • Other projects...                     │
└─────────────────────────────────────────┘
```

---

### STEP 2️⃣: Select Your Project

**Action:**
1. Click on "unvibe-54ae1" project
2. Wait for the project dashboard to load

**What you should see:**
- Project overview
- Left sidebar with options
- "Authentication" option in the sidebar

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ unvibe-54ae1 Project Dashboard          │
├─────────────────────────────────────────┤
│ Left Sidebar:                           │
│ • Build                                 │
│   • Authentication  ← Click this        │
│   • Firestore Database                  │
│   • Storage                             │
│ • Release & Monitor                     │
└─────────────────────────────────────────┘
```

---

### STEP 3️⃣: Go to Authentication

**Action:**
1. In the left sidebar, click "Authentication"
2. Wait for the Authentication page to load

**What you should see:**
- Authentication dashboard
- Tabs at the top: "Users", "Sign-in method", "Templates", "Settings"
- Settings tab with a gear icon (⚙️)

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ Authentication                          │
├─────────────────────────────────────────┤
│ Tabs:                                   │
│ [Users] [Sign-in method] [Templates] [Settings ⚙️]
│                                         │
│ Click on "Settings" tab ↑               │
└─────────────────────────────────────────┘
```

---

### STEP 4️⃣: Click Settings Tab

**Action:**
1. Click the "Settings" tab (gear icon ⚙️)
2. Wait for settings page to load

**What you should see:**
- Settings page
- Various configuration options
- Scroll down to find "Authorized domains"

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ Authentication Settings                 │
├─────────────────────────────────────────┤
│ Settings Options:                       │
│ • User account control                  │
│ • Email/Password                        │
│ • Authorized domains  ← Scroll to this  │
│ • Authorized redirect URIs              │
└─────────────────────────────────────────┘
```

---

### STEP 5️⃣: Find Authorized Domains

**Action:**
1. Scroll down on the Settings page
2. Look for "Authorized domains" section
3. You should see a list of domains

**What you should see:**
- "Authorized domains" heading
- List of currently authorized domains
- "Add domain" button

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ Authorized domains                      │
├─────────────────────────────────────────┤
│ Current domains:                        │
│ • localhost                             │
│ • 127.0.0.1                             │
│ • yourdomain.com                        │
│                                         │
│ [Add domain] button ← Click this        │
└─────────────────────────────────────────┘
```

---

### STEP 6️⃣: Click "Add domain" Button

**Action:**
1. Click the "Add domain" button
2. A text input field should appear

**What you should see:**
- Text input field appears
- Cursor ready for input
- "Add" button next to the input

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ Authorized domains                      │
├─────────────────────────────────────────┤
│ Current domains:                        │
│ • localhost                             │
│ • 127.0.0.1                             │
│                                         │
│ [Input field: ____________] [Add]       │
│                                         │
│ Type here ↑                             │
└─────────────────────────────────────────┘
```

---

### STEP 7️⃣: Type the Domain

**Action:**
1. Click in the text input field
2. Type exactly: `localhost:5000`
3. Make sure there are no extra spaces

**What you should type:**
```
localhost:5000
```

**Important:**
- ✅ Correct: `localhost:5000`
- ❌ Wrong: `localhost: 5000` (space before 5000)
- ❌ Wrong: `localhost:5000/` (trailing slash)
- ❌ Wrong: `http://localhost:5000` (don't include http://)

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ Authorized domains                      │
├─────────────────────────────────────────┤
│ [Input field: localhost:5000] [Add]     │
│                                         │
│ You typed ↑                             │
└─────────────────────────────────────────┘
```

---

### STEP 8️⃣: Click "Add" Button

**Action:**
1. Click the "Add" button next to the input field
2. Wait for the domain to be added

**What you should see:**
- Input field disappears
- `localhost:5000` appears in the authorized domains list
- Success message (optional)

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ Authorized domains                      │
├─────────────────────────────────────────┤
│ Current domains:                        │
│ • localhost                             │
│ • 127.0.0.1                             │
│ • localhost:5000  ← NEW! ✅             │
│                                         │
│ [Add domain] button                     │
└─────────────────────────────────────────┘
```

---

### STEP 9️⃣: Wait for Propagation

**Action:**
1. Wait 5-10 seconds
2. Firebase needs time to update its systems
3. Don't close the page

**Why wait?**
- Firebase servers need to sync the changes
- Changes don't take effect immediately
- Waiting ensures the change is propagated

**What to do:**
- ✅ Wait 5-10 seconds
- ✅ Don't close the page
- ✅ Don't refresh yet

---

### STEP 🔟: Clear Browser Cache

**Action (Mac):**
1. Press: **Cmd + Shift + Delete**
2. Select "All time"
3. Check: "Cookies and other site data"
4. Check: "Cached images and files"
5. Click: "Clear data"

**Action (Windows):**
1. Press: **Ctrl + Shift + Delete**
2. Select "All time"
3. Check: "Cookies and other site data"
4. Check: "Cached images and files"
5. Click: "Clear data"

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ Clear browsing data                     │
├─────────────────────────────────────────┤
│ Time range: [All time ▼]                │
│                                         │
│ ☑ Cookies and other site data           │
│ ☑ Cached images and files               │
│ ☐ Download history                      │
│ ☐ Browsing history                      │
│                                         │
│ [Clear data] button                     │
└─────────────────────────────────────────┘
```

---

### STEP 1️⃣1️⃣: Hard Refresh Page

**Action (Mac):**
1. Press: **Cmd + Shift + R**

**Action (Windows):**
1. Press: **Ctrl + Shift + F5**

**What this does:**
- Clears the page cache
- Reloads all resources fresh
- Ensures you get the latest Firebase config

---

### STEP 1️⃣2️⃣: Test Google Sign-In

**Action:**
1. Go to: http://localhost:5000/login
2. Click: "Sign in with Google"
3. A Google popup should appear

**What you should see:**
- ✅ Google sign-in popup appears (NO ERROR)
- ✅ You can select your Google account
- ✅ After selection, redirected to dashboard

**What you should NOT see:**
- ❌ "This domain is not authorized" error
- ❌ Any Firebase errors

**Screenshot description:**
```
┌─────────────────────────────────────────┐
│ UniVibe Login Page                      │
├─────────────────────────────────────────┤
│ [Sign in with Google] button            │
│                                         │
│ Click this ↑                            │
│                                         │
│ Google popup should appear ✅           │
└─────────────────────────────────────────┘
```

---

## Verification Checklist

After completing all steps, verify:

- ☑ Firebase Console opened
- ☑ unvibe-54ae1 project selected
- ☑ Authentication section opened
- ☑ Settings tab clicked
- ☑ Authorized domains found
- ☑ "Add domain" button clicked
- ☑ "localhost:5000" typed
- ☑ "Add" button clicked
- ☑ Domain appears in list
- ☑ Waited 5-10 seconds
- ☑ Browser cache cleared
- ☑ Page hard refreshed
- ☑ Google Sign-In tested
- ☑ No error appears ✅

---

## If It Still Doesn't Work

### Issue: Still Getting the Error

**Solution:**
1. Wait another 10-15 seconds (Firebase can be slow)
2. Close browser completely
3. Reopen browser
4. Go to http://localhost:5000/login
5. Try again

### Issue: Domain Not in List

**Solution:**
1. Go back to Firebase Console
2. Check if domain is really there
3. If not, try adding again
4. Make sure you clicked "Add" button

### Issue: Different Error

**Solution:**
1. Open browser console (F12)
2. Look for error messages
3. Check if Firebase is initialized
4. Check if internet connection is working

---

## Success Indicators

When it's working, you should see:

**In browser console (F12):**
```
✅ Firebase initialized successfully!
✅ Firebase Auth Enhanced module loaded
🔐 Google Sign-In initiated...
✅ Google Sign-In successful: yourname@newhorizonindia.edu
```

**In browser:**
```
✅ Google popup appears
✅ Can select account
✅ Redirected to dashboard
✅ No errors
```

---

## Summary

| Step | Action | Result |
|------|--------|--------|
| 1 | Open Firebase Console | See projects |
| 2 | Select unvibe-54ae1 | See project dashboard |
| 3 | Click Authentication | See auth options |
| 4 | Click Settings | See settings page |
| 5 | Scroll to Authorized domains | See domain list |
| 6 | Click "Add domain" | See input field |
| 7 | Type "localhost:5000" | Domain typed |
| 8 | Click "Add" | Domain added to list |
| 9 | Wait 5-10 seconds | Firebase syncs |
| 10 | Clear browser cache | Cache cleared |
| 11 | Hard refresh | Page reloaded |
| 12 | Test Google Sign-In | Works! ✅ |

---

## Status

✅ **Follow these 12 steps to fix the Firebase domain error**

After completing all steps, Google Sign-In should work perfectly!
