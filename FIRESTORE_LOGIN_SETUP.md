# Firestore Email & Username Login - UniVibe

## Overview
Firebase Google Sign-In has been removed. The project now uses a simple, clean email and username-based login system with Firestore storage for user data.

## What's Implemented

### 1. Simple Login Form
**Location**: `/enter` route and `templates/enter.html`

Users enter:
- **Email Address**: Unique email for account identification
- **Username**: Unique username for profile display
- **Full Name**: Display name visible to other users

### 2. Frontend Integration

#### Firebase Config (`static/js/firebase-config.js`)
- Initializes Firestore database only (no Authentication)
- Exports Firestore instance globally
- Minimal, lightweight setup

#### No Firebase Auth Module
- Removed `firebase-auth.js` (Google Sign-In code)
- All authentication handled by backend

### 3. Backend Integration

#### Entry Route (`app.py` - `/enter`)
```python
@app.route('/enter', methods=['GET', 'POST'])
def enter():
    # Validates email, username, full_name
    # Checks for duplicates in SQLite
    # Creates user in SQLite database
    # Stores user data in Firestore
    # Creates Flask session
    # Redirects to dashboard
```

#### User Data Storage

**Firestore Collection**: `users`
- Document ID: User's email address
- Fields:
  - `user_id`: SQLite user ID
  - `email`: User's email
  - `username`: Unique username
  - `full_name`: Display name
  - `avatar_color`: Avatar color
  - `bio`: User biography
  - `is_blacklisted`: Blacklist status
  - `created_at`: Account creation timestamp
  - `updated_at`: Last update timestamp

**SQLite Database**: `users` table
- `id`: Primary key
- `username`: Unique username
- `email`: User's email
- `password`: Hashed password
- `full_name`: Display name
- `bio`: User biography
- `avatar_color`: Avatar color
- `is_blacklisted`: Blacklist status
- `created_at`: Creation timestamp

### 4. User Flow

1. User visits `/enter` page
2. User enters email, username, and full name
3. Form is submitted to `/enter` route (POST)
4. Backend validates:
   - All fields are provided
   - Email format is valid
   - Email is not already registered
   - Username is not already taken
5. If validation passes:
   - User is created in SQLite database
   - User data is stored in Firestore
   - Flask session is created
   - User is redirected to `/dashboard`
6. If validation fails:
   - Flash message is displayed
   - User is redirected back to `/enter`

### 5. Validation Rules

- **Email**: Must be valid email format (contains @)
- **Username**: Letters, numbers, and underscores only
- **Full Name**: Any text allowed
- **Email Uniqueness**: No duplicate emails allowed
- **Username Uniqueness**: No duplicate usernames allowed

### 6. Error Handling

Users receive clear feedback for:
- Missing fields: "Please provide email, username, and full name."
- Invalid email: "Please enter a valid email address."
- Duplicate email: "Email already registered. Please use a different email."
- Duplicate username: "Username already taken. Please choose another."

### 7. Session Management

After successful login, Flask session contains:
- `user_id`: SQLite user ID
- `username`: User's username
- `full_name`: User's full name
- `email`: User's email
- `avatar_color`: Avatar color

### 8. Firestore Setup

To enable Firestore storage:

1. **Download Service Account Key**:
   - Go to Firebase Console → Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Save as `serviceAccountKey.json` in project root

2. **Or Set Environment Variable**:
   ```bash
   export FIREBASE_SERVICE_ACCOUNT='{"type":"service_account",...}'
   ```

3. **Firestore Security Rules** (Recommended):
   ```
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /users/{email} {
         allow read: if request.auth != null;
         allow write: if false;
       }
     }
   }
   ```

### 9. Configuration

#### `.env.example`
```
FIREBASE_API_KEY=AIzaSyCDwaBMoEJvJO1NBS-uUzsMTirSSGz8Mcc
FIREBASE_AUTH_DOMAIN=univibe-c85c6.firebaseapp.com
FIREBASE_PROJECT_ID=univibe-c85c6
FIREBASE_STORAGE_BUCKET=univibe-c85c6.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=631710741538
FIREBASE_APP_ID=1:631710741538:web:49b43d32353d97bcc3467b
FIREBASE_MEASUREMENT_ID=G-1CXWWSRM61
```

#### `requirements.txt`
- `firebase-admin==6.2.0` - For Firestore backend storage

### 10. Testing

1. **Start the server**:
   ```bash
   source venv/bin/activate
   python3 app.py
   ```

2. **Visit the enter page**:
   - Navigate to `http://localhost:5000/enter`

3. **Test Registration**:
   - Enter email: `test@example.com`
   - Enter username: `testuser`
   - Enter full name: `Test User`
   - Click "Enter UniVibe"
   - Should redirect to dashboard

4. **Test Duplicate Prevention**:
   - Try registering with same email/username
   - Should see error message

### 11. Files Modified

- ✅ `app.py` - Updated `/enter` route, removed Firebase auth endpoint
- ✅ `templates/enter.html` - Simplified to email/username form
- ✅ `templates/base.html` - Removed Firebase auth imports
- ✅ `static/js/firebase-config.js` - Firestore only (no Auth)
- ❌ `static/js/firebase-auth.js` - DELETED (Google Sign-In removed)
- ✅ `requirements.txt` - Firebase admin included
- ✅ `.env.example` - Firebase config included

### 12. What Was Removed

- ❌ Google Sign-In button
- ❌ Firebase Authentication module
- ❌ Firebase Analytics
- ❌ `/api/firebase_auth` endpoint
- ❌ Google OAuth popup flow

### 13. Benefits of This Approach

✅ **Simple**: No complex OAuth flows
✅ **Secure**: Email/username stored in Firestore
✅ **Fast**: Minimal dependencies
✅ **Flexible**: Easy to add password reset later
✅ **Scalable**: Firestore handles user data
✅ **Clean**: No third-party authentication complexity

### 14. Future Enhancements

- [ ] Add password-based login
- [ ] Add email verification
- [ ] Add password reset functionality
- [ ] Add login history tracking
- [ ] Add two-factor authentication
- [ ] Add social login (optional)

---

**Status**: ✅ Simple Firestore email/username login implemented and running
**Last Updated**: May 16, 2026
