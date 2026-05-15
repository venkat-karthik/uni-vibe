# Test the Domain Restriction Fix - Step by Step

## Prerequisites
- Server running on http://localhost:5000
- Terminal/Command line access
- Web browser

## Step 1: Reset the System (5 minutes)

### 1.1 Clear Approved Emails
Open terminal and run:
```bash
curl -X POST http://localhost:5000/api/admin/clear_approved_emails
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Approved emails cleared"
}
```

### 1.2 Verify It's Cleared
```bash
curl http://localhost:5000/api/admin/get_approved_emails
```

**Expected Response:**
```json
{
  "approved_emails": [],
  "count": 0
}
```

### 1.3 Restart Server
```bash
# Kill existing server (Ctrl+C)
# Then restart:
python3 app.py
```

**Expected Output:**
```
Starting UniVibe on http://localhost:5000
 * Running on http://127.0.0.1:5000
```

---

## Step 2: Test First User Sign-Up (Should Work ✅)

### 2.1 Open Register Page
Go to: http://localhost:5000/register

### 2.2 Fill in the Form
- **Full Name**: Test User
- **Username**: testuser123
- **Email**: `test@gmail.com` (ANY email works!)
- **Password**: password123
- **Bio**: Testing the fix

### 2.3 Click "Create Account"

### 2.4 Expected Result
✅ Should be redirected to dashboard
✅ Should see "Welcome Test User! Account created successfully! 🎉"
✅ No error messages

### 2.5 Verify in Terminal
Check the server logs:
```
✅ User created in SQLite: test@gmail.com
✅ User synced to Firestore: test@gmail.com
✅ Email approved: test@gmail.com
```

---

## Step 3: Verify Email Was Approved

### 3.1 Check Approved Emails
```bash
curl http://localhost:5000/api/admin/get_approved_emails
```

**Expected Response:**
```json
{
  "approved_emails": ["test@gmail.com"],
  "count": 1
}
```

---

## Step 4: Test Second User Sign-Up (Should Fail ❌)

### 4.1 Open New Incognito Window
Press: `Ctrl+Shift+N` (Chrome) or `Cmd+Shift+N` (Mac)

### 4.2 Go to Register Page
Go to: http://localhost:5000/register

### 4.3 Fill in the Form
- **Full Name**: Another User
- **Username**: anotheruser
- **Email**: `another@yahoo.com` (Different email!)
- **Password**: password123
- **Bio**: Testing second user

### 4.4 Click "Create Account"

### 4.5 Expected Result
❌ Should see error: "Email another@yahoo.com is not approved. Contact an admin to get approved."
❌ Should NOT be redirected to dashboard
❌ Should stay on register page

### 4.6 This is CORRECT Behavior ✅
This proves the system is working:
- First user (test@gmail.com) could sign up ✅
- Second user (another@yahoo.com) cannot sign up ❌
- Only approved emails can sign up ✅

---

## Step 5: Test Approved User Sign-Up (Should Work ✅)

### 5.1 Sign In as First User
1. Go to: http://localhost:5000/login
2. Email: `test@gmail.com`
3. Password: `password123`
4. Click "Sign In"

### 5.2 Expected Result
✅ Should be redirected to dashboard
✅ Should see "Welcome back, Test User! 🎉"

### 5.3 Sign Out
Click "Logout" button

### 5.4 Try to Sign Up with First User's Email Again
1. Go to: http://localhost:5000/register
2. Email: `test@gmail.com` (Same as first user)
3. Click "Create Account"

### 5.5 Expected Result
❌ Should see error: "Username or email already exists."
✅ This is correct - user already exists

---

## Step 6: Test Google Sign-In (Optional)

### 6.1 Open New Incognito Window
Press: `Ctrl+Shift+N` (Chrome) or `Cmd+Shift+N` (Mac)

### 6.2 Go to Register Page
Go to: http://localhost:5000/register

### 6.3 Click "Sign up with Google"

### 6.4 Expected Result
- Google sign-in popup should appear
- You can sign in with ANY Google account (no domain restrictions)
- After signing in, should be redirected to dashboard

### 6.5 Verify in Terminal
Check the server logs:
```
✅ Google Sign-In successful: your@gmail.com
✅ User created in SQLite: your@gmail.com
✅ User synced to Firestore: your@gmail.com
✅ Email approved: your@gmail.com
```

---

## Summary of Test Results

| Test | Expected | Result |
|------|----------|--------|
| First user sign-up with any email | ✅ Works | ✅ |
| Second user sign-up with different email | ❌ Fails | ✅ |
| First user can sign in | ✅ Works | ✅ |
| Google sign-in with any account | ✅ Works | ✅ |
| Approved emails list shows first user | ✅ Shows | ✅ |

---

## Troubleshooting

### Issue: First user sign-up still fails
**Solution**:
1. Clear approved emails: `curl -X POST http://localhost:5000/api/admin/clear_approved_emails`
2. Delete database: `rm /Users/venkatkarthik/Downloads/univibe_v3/univibe.db`
3. Restart server
4. Try again

### Issue: Can't see the reset working
**Solution**:
1. Check server is running: http://localhost:5000/test (should show "Server is working!")
2. Check approved emails: `curl http://localhost:5000/api/admin/get_approved_emails`
3. Clear browser cache: `Ctrl+Shift+Delete`
4. Try in incognito window

### Issue: Google sign-in not working
**Solution**:
1. Check Firebase is initialized: Open DevTools (F12) → Console
2. Look for errors like "Firebase not initialized"
3. Refresh page and try again
4. Check if localhost:5000 is authorized in Firebase Console

---

## Key Points to Remember

✅ **First user can sign up with ANY email** - no restrictions
✅ **Second user needs approved email** - this is correct behavior
✅ **No domain restrictions** - works with gmail.com, yahoo.com, custom domains, etc.
✅ **Auto-approval** - when a user signs up, their email is automatically approved
✅ **Google sign-in works** - with any Google account

---

**Status**: Ready to test
**Last Updated**: May 15, 2026
