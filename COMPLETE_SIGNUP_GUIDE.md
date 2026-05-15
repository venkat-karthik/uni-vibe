# Complete Sign-Up & Sign-In Guide ✅

## IMPORTANT: Email Requirements

### ✅ ALLOWED Emails
- `1NH24CD038@newhorizonindia.edu` ✅
- `yourname@newhorizonindia.edu` ✅
- Any email ending with `@newhorizonindia.edu` ✅

### ❌ NOT ALLOWED Emails
- `yourname@gmail.com` ❌
- `user@yahoo.com` ❌
- `student@college.edu` ❌
- **Gmail is NOT supported** ❌

**Why?** The system is restricted to New Horizon India organization emails only.

---

## Sign-Up Methods

### Method 1: Email/Password Sign-Up (Recommended for @newhorizonindia.edu)

**Steps:**
1. Go to http://localhost:5000/register
2. Fill in the form:
   - **Full Name**: Your full name (e.g., "Arjun Sharma")
   - **Username**: Your username (e.g., "arjun_v")
   - **Email**: Your @newhorizonindia.edu email (e.g., "1NH24CD038@newhorizonindia.edu")
   - **Password**: Min 6 characters
   - **Bio**: Optional
3. Click "Create My Account"
4. ✅ **Automatically logged in and redirected to dashboard**

**What Happens:**
- Account created in SQLite database
- User data synced to Firestore
- Session created automatically
- Redirected to dashboard
- You're ready to use the app!

**Email Validation:**
- As you type, you'll see:
  - ✅ Green checkmark if email ends with `@newhorizonindia.edu`
  - ❌ Red error if email doesn't match

---

### Method 2: Google Sign-Up (For @newhorizonindia.edu Google Accounts)

**Steps:**
1. Go to http://localhost:5000/register
2. Click "Sign up with Google"
3. Google popup appears
4. Select your Google account with `@newhorizonindia.edu` email
5. ✅ **Automatically logged in and redirected to dashboard**

**What Happens:**
- Account created in Firebase Auth
- Account created in SQLite database
- User data synced to Firestore
- Session created automatically
- Redirected to dashboard
- You're ready to use the app!

**Important:**
- Your Google account MUST have a `@newhorizonindia.edu` email
- If you use a Gmail account, it will be rejected

---

## Sign-In Methods

### Method 1: Email/Password Sign-In

**Steps:**
1. Go to http://localhost:5000/login
2. Enter your email: `1NH24CD038@newhorizonindia.edu`
3. Enter your password
4. Click "Login"
5. ✅ **Redirected to dashboard**

**What Happens:**
- Credentials verified
- Session created
- Redirected to dashboard

---

### Method 2: Google Sign-In

**Steps:**
1. Go to http://localhost:5000/login
2. Click "Sign in with Google"
3. Google popup appears
4. Select your Google account with `@newhorizonindia.edu` email
5. ✅ **Redirected to dashboard**

**What Happens:**
- Google authentication verified
- Email domain validated
- Session created
- Redirected to dashboard

---

## Data Storage & Sync

### Where Your Data Is Stored

**1. SQLite Database** (Local)
- User account information
- Quiz answers
- Connections
- Messages
- Reviews
- Notifications

**2. Firestore** (Cloud)
- User profile
- Quiz data
- Connections
- Messages
- Reviews
- Notifications

### How Sync Works

**When you sign up:**
1. Account created in SQLite
2. Account created in Firestore
3. Both databases stay in sync

**When you sign in:**
1. Session created
2. User data available from both databases
3. Real-time sync with Firestore

**When you update profile:**
1. SQLite updated
2. Firestore updated
3. Both stay in sync

---

## Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    SIGN-UP FLOW                             │
└─────────────────────────────────────────────────────────────┘

Option 1: Email/Password
├─ Go to /register
├─ Fill form with @newhorizonindia.edu email
├─ Click "Create My Account"
├─ Account created in SQLite
├─ Data synced to Firestore
├─ Session created
└─ Redirected to /dashboard ✅

Option 2: Google Sign-Up
├─ Go to /register
├─ Click "Sign up with Google"
├─ Select @newhorizonindia.edu Google account
├─ Account created in Firebase Auth
├─ Account created in SQLite
├─ Data synced to Firestore
├─ Session created
└─ Redirected to /dashboard ✅

┌─────────────────────────────────────────────────────────────┐
│                    SIGN-IN FLOW                             │
└─────────────────────────────────────────────────────────────┘

Option 1: Email/Password
├─ Go to /login
├─ Enter @newhorizonindia.edu email
├─ Enter password
├─ Click "Login"
├─ Credentials verified
├─ Session created
└─ Redirected to /dashboard ✅

Option 2: Google Sign-In
├─ Go to /login
├─ Click "Sign in with Google"
├─ Select @newhorizonindia.edu Google account
├─ Email domain validated
├─ Session created
└─ Redirected to /dashboard ✅
```

---

## Firestore Collections

Your data is stored in these Firestore collections:

1. **users** - User profiles
2. **quiz_answers** - Quiz responses
3. **connections** - Friend connections
4. **messages** - Chat messages
5. **reviews** - User reviews
6. **notifications** - Notifications
7. **blacklist** - Blacklisted users

---

## Troubleshooting

### Issue: "Only @newhorizonindia.edu emails are allowed"
**Solution:**
- Make sure your email ends with `@newhorizonindia.edu`
- Check for typos
- Gmail accounts are NOT supported

### Issue: "Username or email already exists"
**Solution:**
- Choose a different username
- Or use a different email
- Or sign in if you already have an account

### Issue: "Firebase not initialized"
**Solution:**
1. Clear browser cache (Cmd+Shift+Delete on Mac)
2. Hard refresh (Cmd+Shift+R on Mac)
3. Try again

### Issue: Redirects to login instead of dashboard
**Solution:**
1. Clear browser cache
2. Hard refresh
3. Try again

### Issue: Data not syncing to Firestore
**Solution:**
- Check Firebase project is configured correctly
- Check Firestore database is active
- Check service account key is valid
- Check internet connection

---

## What You Can Do After Sign-Up

✅ Complete your profile
✅ Take the personality quiz
✅ Find matches based on interests
✅ Connect with other students
✅ Send messages
✅ Leave reviews
✅ Get notifications
✅ Chat with friends

---

## Security

- ✅ Email domain validation (frontend + backend)
- ✅ Password hashing (SQLite)
- ✅ Firebase Auth security
- ✅ Session management
- ✅ Firestore security rules
- ✅ HTTPS ready

---

## Summary

| Feature | Email/Password | Google |
|---------|---|---|
| Sign-Up | ✅ | ✅ |
| Sign-In | ✅ | ✅ |
| Email Required | @newhorizonindia.edu | @newhorizonindia.edu |
| Auto-Login | ✅ | ✅ |
| Firestore Sync | ✅ | ✅ |
| Session | ✅ | ✅ |
| Dashboard Access | ✅ | ✅ |

---

## Status

✅ **FULLY WORKING AND READY TO USE**

- Email/Password Sign-Up: ✅ Working
- Email/Password Sign-In: ✅ Working
- Google Sign-Up: ✅ Working
- Google Sign-In: ✅ Working
- Firestore Sync: ✅ Working
- Auto-Login: ✅ Working
- Dashboard Access: ✅ Working

---

## Next Steps

1. Go to http://localhost:5000/register
2. Sign up with your @newhorizonindia.edu email
3. You'll be automatically logged in
4. Start using UniVibe!

**Remember:** Only @newhorizonindia.edu emails are allowed. Gmail is NOT supported.
