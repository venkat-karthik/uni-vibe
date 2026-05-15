# Firebase Setup Guide - UniVibe

## Error: `auth/unauthorized-domain`

This error occurs because your localhost domain is not authorized in Firebase Console.

## Solution: Add Localhost to Authorized Domains

### Step 1: Go to Firebase Console
1. Visit [Firebase Console](https://console.firebase.google.com/)
2. Sign in with your Google account
3. Select the project: **univibe-c85c6**

### Step 2: Navigate to Authentication Settings
1. Click on **Authentication** in the left sidebar
2. Click on the **Settings** tab (gear icon)
3. Scroll down to **Authorized domains** section

### Step 3: Add Localhost Domains
Click **Add domain** and add these domains one by one:

1. **localhost**
2. **127.0.0.1**
3. **localhost:5000** (optional, but recommended)

### Step 4: Save Changes
- Firebase will automatically save the changes
- Wait a few seconds for the changes to propagate

### Step 5: Test Again
1. Refresh your browser (Ctrl+R or Cmd+R)
2. Go to `http://localhost:5000/enter`
3. Click "Sign in with Google"
4. You should now be able to authenticate

---

## Complete Setup Checklist

- [ ] Add localhost to authorized domains in Firebase Console
- [ ] Refresh browser after adding domains
- [ ] Test Google Sign-In on `/enter` page
- [ ] Verify user is created in Firestore
- [ ] Verify user is created in SQLite database
- [ ] Check that session is created and user is redirected to dashboard

---

## Troubleshooting

### Still getting `auth/unauthorized-domain` error?

1. **Clear browser cache**:
   - Press Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)
   - Clear all cache and cookies
   - Refresh the page

2. **Check Firebase Console**:
   - Make sure you're in the correct Firebase project
   - Verify the domains are listed under Authorized domains
   - Wait 5-10 minutes for changes to propagate

3. **Check browser console**:
   - Press F12 to open Developer Tools
   - Go to Console tab
   - Look for any error messages
   - Share the error message for debugging

4. **Try different localhost format**:
   - Try `http://127.0.0.1:5000` instead of `http://localhost:5000`
   - Or add both to authorized domains

### Google Sign-In button not working?

1. Check browser console (F12) for JavaScript errors
2. Make sure Firebase scripts are loaded:
   - Look for "✅ Firebase Config loaded successfully!" in console
   - Look for "✅ Firebase Auth module loaded" in console
3. Check that you're on the `/enter` page
4. Make sure JavaScript is enabled in your browser

### User not being created in Firestore?

1. Check that you have a Firebase service account key configured
2. Look at server logs for any Firestore errors
3. Check Firebase Console → Firestore → Data to see if collection exists
4. Verify Firestore security rules allow writes

---

## Firebase Console Quick Links

- **Project**: https://console.firebase.google.com/project/univibe-c85c6
- **Authentication**: https://console.firebase.google.com/project/univibe-c85c6/authentication/providers
- **Firestore**: https://console.firebase.google.com/project/univibe-c85c6/firestore
- **Settings**: https://console.firebase.google.com/project/univibe-c85c6/settings/general

---

## What Happens After Sign-In?

1. **Frontend**:
   - User authenticates with Google
   - User data is stored in Firestore
   - Authentication data is sent to backend

2. **Backend**:
   - User is created/updated in SQLite database
   - Flask session is created
   - User is redirected to `/dashboard`

3. **Database**:
   - **Firestore**: User document with email, name, profile picture
   - **SQLite**: User record with username, email, full name, avatar color

---

## Security Notes

- ✅ Google Sign-In is secure (handled by Google)
- ✅ Firebase handles password hashing
- ✅ Session is stored server-side
- ⚠️ Make sure to set up Firestore security rules in production
- ⚠️ Never commit Firebase service account key to version control

---

## Next Steps

After successfully signing in:

1. Complete the 15-question quiz on `/quiz`
2. Get matched with other users on `/results`
3. View user profiles on `/profile/<user_id>`
4. Connect with other users
5. Chat with connected users
6. Leave reviews for connected users

---

**Status**: Firebase integration ready, awaiting authorized domain configuration
**Last Updated**: May 16, 2026
