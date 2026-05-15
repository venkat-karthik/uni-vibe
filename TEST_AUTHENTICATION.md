# Authentication Testing Guide

## Quick Test Steps

### 1. Test Server Status
```bash
curl http://localhost:5000/test
# Expected: <h1 style="color:red;">Server is working!</h1>
```

### 2. Test Login Page
```
Visit: http://localhost:5000/login
Expected: Login page with:
- Email input field
- Password input field
- "Sign in with Google" button
- Organization email info box
- Link to register page
```

### 3. Test Register Page
```
Visit: http://localhost:5000/register
Expected: Register page with:
- Full name input
- Username input
- Email input
- Password input
- Bio textarea
- "Sign up with Google" button
- Link to login page
```

### 4. Test Email Validation (Frontend)
```
1. Go to login page
2. Type an email NOT ending with @newhorizonindia.edu
3. Expected: Red error message, Login button disabled
4. Type valid email: yourname@newhorizonindia.edu
5. Expected: Green success message, Login button enabled
```

### 5. Test Email/Password Registration
```
1. Go to register page
2. Fill in:
   - Full Name: Test User
   - Username: testuser123
   - Email: testuser@newhorizonindia.edu
   - Password: password123
   - Bio: Test bio
3. Click "Create My Account"
4. Expected: Redirected to login page with success message
```

### 6. Test Email/Password Login
```
1. Go to login page
2. Enter credentials from step 5
3. Click "Login"
4. Expected: Redirected to dashboard
```

### 7. Test Google Sign-In (if configured)
```
1. Go to login page
2. Click "Sign in with Google"
3. Expected: Google popup appears
4. Select your @newhorizonindia.edu Google account
5. Expected: Redirected to dashboard
```

### 8. Test Google Sign-Up (if configured)
```
1. Go to register page
2. Click "Sign up with Google"
3. Expected: Google popup appears
4. Select your @newhorizonindia.edu Google account
5. Expected: Redirected to dashboard
```

### 9. Test Firebase Auth Endpoint
```bash
curl -X POST http://localhost:5000/api/firebase_auth \
  -H "Content-Type: application/json" \
  -d '{
    "uid": "test-uid-123",
    "email": "test@newhorizonindia.edu",
    "displayName": "Test User",
    "photoURL": "",
    "provider": "google"
  }'

# Expected Response:
# {
#   "success": true,
#   "user_id": 1,
#   "message": "Welcome Test User!"
# }
```

### 10. Test Invalid Email Domain
```bash
curl -X POST http://localhost:5000/api/firebase_auth \
  -H "Content-Type: application/json" \
  -d '{
    "uid": "test-uid-456",
    "email": "test@gmail.com",
    "displayName": "Test User",
    "photoURL": "",
    "provider": "google"
  }'

# Expected Response:
# {
#   "error": "Only newhorizonindia.edu emails are allowed"
# }
# Status: 403
```

---

## Browser Console Tests

### Check Firebase Initialization
```javascript
// In browser console (F12)
console.log(window.firebaseAuth);
console.log(window.firebaseDb);
console.log(window.firebaseAuthEnhanced);

// Expected: All three should be defined (not undefined)
```

### Test Google Sign-In Function
```javascript
// In browser console
window.firebaseAuthEnhanced.signInWithGoogle()
  .then(result => console.log(result))
  .catch(error => console.error(error));
```

### Check Current User
```javascript
// In browser console
window.firebaseAuthEnhanced.getCurrentUser();
// Expected: User object or null
```

---

## Database Verification

### Check Users Table
```bash
sqlite3 univibe.db "SELECT id, username, email, full_name FROM users LIMIT 5;"
```

### Check Quiz Answers
```bash
sqlite3 univibe.db "SELECT user_id, submitted_at FROM quiz_answers LIMIT 5;"
```

### Check Connections
```bash
sqlite3 univibe.db "SELECT sender_id, receiver_id, status FROM connections LIMIT 5;"
```

---

## Common Test Scenarios

### Scenario 1: New User Registration
1. Register with new email
2. Verify user created in database
3. Login with same credentials
4. Verify session set correctly

### Scenario 2: Existing User Login
1. Login with existing credentials
2. Verify session set
3. Verify redirected to dashboard
4. Verify user info displayed in navbar

### Scenario 3: Invalid Email Domain
1. Try to register with @gmail.com
2. Verify error message shown
3. Verify user NOT created in database

### Scenario 4: Duplicate Username
1. Register with username "testuser"
2. Try to register again with same username
3. Verify error message
4. Try with different username
5. Verify success

### Scenario 5: Session Persistence
1. Login successfully
2. Refresh page
3. Verify still logged in
4. Verify user info still displayed

### Scenario 6: Logout
1. Login successfully
2. Click logout
3. Verify redirected to home page
4. Verify session cleared
5. Try to access dashboard
6. Verify redirected to login

---

## Performance Tests

### Load Test
```bash
# Test 10 concurrent requests
ab -n 10 -c 10 http://localhost:5000/test
```

### Response Time
```bash
# Measure login endpoint response time
time curl -X POST http://localhost:5000/login \
  -d "identifier=test@newhorizonindia.edu&password=password123"
```

---

## Security Tests

### SQL Injection Test
```
Email: test@newhorizonindia.edu' OR '1'='1
Expected: Should be rejected or handled safely
```

### XSS Test
```
Full Name: <script>alert('XSS')</script>
Expected: Should be escaped or sanitized
```

### CSRF Test
```
Try to submit form without CSRF token
Expected: Should be rejected (if CSRF protection enabled)
```

---

## Troubleshooting

### Issue: "Firebase not initialized"
- Check if Firebase SDK scripts are loading
- Check browser console for errors
- Verify script loading order in base.html

### Issue: "Email validation not working"
- Check if JavaScript is enabled
- Check browser console for errors
- Verify validateLoginEmail function exists

### Issue: "Google Sign-In not working"
- Verify Google Sign-In enabled in Firebase Console
- Check if domain is authorized
- Check browser console for popup blocked message

### Issue: "User not created in database"
- Check if /api/firebase_auth endpoint is working
- Check Flask server logs
- Verify database permissions

### Issue: "Session not persisting"
- Check if cookies are enabled
- Check if session secret key is set
- Verify Flask session configuration

---

## Success Indicators

✅ All pages load without errors
✅ Email validation works in real-time
✅ Users can register with valid emails
✅ Users can login with credentials
✅ Google Sign-In works (if configured)
✅ Users redirected to dashboard after login
✅ Session persists across page refreshes
✅ Logout clears session
✅ Invalid emails rejected
✅ Database records created correctly

---

**Last Updated**: May 15, 2026
**Status**: Ready for Testing
