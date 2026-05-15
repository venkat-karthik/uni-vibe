# 🔍 Debugging Firebase Backend Error

## The Error
```
Sign-in failed: Backend error: [error message]
```

## How to See the Full Error

### Step 1: Open Browser Developer Tools
1. Press **F12** on your keyboard
2. Go to the **Console** tab
3. You should see error messages in red

### Step 2: Look for Error Messages
You'll see something like:
```
❌ Google Sign-In failed: Backend error: [ACTUAL ERROR HERE]
```

### Step 3: Common Backend Errors

#### Error 1: Database Error - UNIQUE constraint failed
```
Backend error: Database error: UNIQUE constraint failed: users.email
```
**Cause**: User with this email already exists
**Solution**: Use a different Google account or delete the user from database

#### Error 2: Database Error - no such table
```
Backend error: Database error: no such table: users
```
**Cause**: Database tables not initialized
**Solution**: Delete `univibe.db` and restart server

#### Error 3: Database Error - database is locked
```
Backend error: Database error: database is locked
```
**Cause**: Database file is locked by another process
**Solution**: 
- Close all other connections
- Delete `univibe.db`
- Restart server

#### Error 4: JSON Decode Error
```
Backend error: Expecting value: line 1 column 1
```
**Cause**: Backend returned invalid JSON
**Solution**: Check server logs for Python errors

#### Error 5: Connection Error
```
Backend error: Failed to fetch
```
**Cause**: Server is not running or unreachable
**Solution**: 
- Make sure server is running: `python3 app.py`
- Check that it's on http://localhost:5000

---

## How to Check Server Logs

### Step 1: Look at Terminal Running Server
The terminal where you ran `python3 app.py` should show:
```
🔐 Firebase auth request: user@gmail.com (google)
❌ Database error: [ERROR MESSAGE]
```

### Step 2: Common Server Errors

**Error**: `UNIQUE constraint failed: users.email`
```python
❌ Database error: UNIQUE constraint failed: users.email
```
**Fix**: User already exists. Try with different Google account.

**Error**: `no such table: users`
```python
❌ Database error: no such table: users
```
**Fix**: Delete `univibe.db` and restart server

**Error**: `database is locked`
```python
❌ Database error: database is locked
```
**Fix**: Close other connections, delete `univibe.db`, restart

---

## Step-by-Step Debugging

### 1. Check if Server is Running
```bash
curl http://localhost:5000/enter
```
Should return HTML. If not, server is not running.

### 2. Check if Firebase is Initialized
In browser console, you should see:
```
✅ Firebase Config loaded successfully!
✅ Firebase Auth module loaded
```

### 3. Check if Google Sign-In Button Works
Click "Sign in with Google" and see if Google popup appears.

### 4. Check Browser Console for Errors
Press F12 → Console tab → Look for red errors

### 5. Check Server Logs
Look at terminal running `python3 app.py` for error messages

### 6. Test Backend Endpoint Directly
```bash
curl -X POST http://localhost:5000/api/firebase_auth \
  -H "Content-Type: application/json" \
  -d '{
    "uid": "test123",
    "email": "test@gmail.com",
    "displayName": "Test User",
    "photoURL": "",
    "provider": "google"
  }'
```

---

## Most Common Issues & Fixes

### Issue 1: UNIQUE constraint failed: users.email
**Cause**: User already exists in database
**Fix**: 
- Option A: Use different Google account
- Option B: Delete `univibe.db` and restart server
- Option C: Delete user from database:
  ```bash
  sqlite3 univibe.db "DELETE FROM users WHERE email='your@email.com';"
  ```

### Issue 2: database is locked
**Cause**: Database file is locked
**Fix**:
```bash
# Stop server (Ctrl+C)
# Delete database
rm univibe.db
# Restart server
python3 app.py
```

### Issue 3: no such table: users
**Cause**: Database not initialized
**Fix**:
```bash
# Stop server (Ctrl+C)
# Delete database
rm univibe.db
# Restart server (it will auto-initialize)
python3 app.py
```

### Issue 4: Backend error with no message
**Cause**: Server crashed or returned invalid response
**Fix**:
1. Check server logs (terminal)
2. Look for Python error messages
3. Restart server

---

## Quick Checklist

- [ ] Server is running (`python3 app.py`)
- [ ] Browser console shows Firebase loaded successfully
- [ ] Google Sign-In popup appears when clicking button
- [ ] Check browser console for error messages (F12)
- [ ] Check server terminal for error messages
- [ ] Try with different Google account
- [ ] Delete `univibe.db` and restart server
- [ ] Check that localhost is in Firebase authorized domains

---

## Getting More Details

### Enable Debug Mode
Add this to browser console:
```javascript
// Enable detailed logging
window.debugMode = true;
```

### Check Network Tab
1. Press F12
2. Go to **Network** tab
3. Click "Sign in with Google"
4. Look for POST request to `/api/firebase_auth`
5. Click on it and check Response tab for error details

### Check Response
In Network tab, click the `/api/firebase_auth` request:
- **Status**: Should be 200 (success) or 500 (error)
- **Response**: Should show JSON with error message

---

## Still Stuck?

1. **Check browser console** (F12 → Console)
2. **Check server logs** (terminal running app.py)
3. **Try direct entry** (username/password) to verify database works
4. **Delete database** and restart
5. **Check Firebase Console** for authorized domains

---

## Example Error Scenarios

### Scenario 1: First Time Sign-In
```
Browser Console:
✅ Google Sign-In successful: user@gmail.com
✅ User created in Firestore

Server Logs:
🔐 Firebase auth request: user@gmail.com (google)
✅ User created in SQLite: user@gmail.com
✅ User stored in Firestore: user@gmail.com
✅ Firebase auth successful: user@gmail.com

Result: ✅ Redirected to dashboard
```

### Scenario 2: User Already Exists
```
Browser Console:
❌ Google Sign-In failed: Backend error: Database error: UNIQUE constraint failed: users.email

Server Logs:
🔐 Firebase auth request: user@gmail.com (google)
❌ Database error: UNIQUE constraint failed: users.email

Result: ❌ Error shown to user
```

### Scenario 3: Database Locked
```
Browser Console:
❌ Google Sign-In failed: Backend error: Database error: database is locked

Server Logs:
🔐 Firebase auth request: user@gmail.com (google)
❌ Database error: database is locked

Result: ❌ Error shown to user
```

---

## Next Steps

1. **Try signing in again** with the improved error messages
2. **Check browser console** (F12) for the full error
3. **Check server logs** (terminal) for backend error
4. **Share the error message** for further help

---

**Updated**: May 16, 2026
**Status**: Ready for debugging
