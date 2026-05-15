# UniVibe Authentication Guide

## Overview
UniVibe now supports **three authentication methods**:
1. ✅ **Password Login** - Email + Password authentication
2. ✅ **Google Sign-In** - OAuth 2.0 with Google
3. ✅ **Firestore Storage** - All user data persisted in cloud

## Authentication Methods

### 1. Password Authentication

#### Registration with Password
```
User enters:
- Email (must be @newhorizonindia.edu)
- Password (minimum 6 characters)
- Username (unique, alphanumeric + underscore)
- Full Name

Process:
1. Validate email domain
2. Check if email/username already exists
3. Hash password using SHA-256
4. Store in SQLite
5. Store in Firestore with auth_method: "password"
6. Create session
7. Redirect to dashboard
```

#### Login with Password
```
User enters:
- Email
- Password

Process:
1. Check if email exists in database
2. Hash provided password
3. Compare with stored hash
4. If match: Create session → Redirect to dashboard
5. If no match: Show error message
```

#### Password Security
- ✅ Passwords hashed with SHA-256
- ✅ Never stored in plain text
- ✅ Minimum 6 characters required
- ✅ Stored in both SQLite and Firestore

### 2. Google Sign-In

#### How It Works
```
User clicks "Sign in with Google"
        ↓
Google OAuth 2.0 popup
        ↓
User authenticates with Google
        ↓
Google returns ID token
        ↓
Backend verifies token with Firebase
        ↓
Check if email ends with @newhorizonindia.edu
        ↓
If new user: Create account automatically
If existing user: Login directly
        ↓
Create session → Redirect to dashboard
```

#### Google Sign-In Setup

**Step 1: Get Google Client ID**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google+ API
4. Create OAuth 2.0 credentials (Web application)
5. Add authorized redirect URIs:
   - `http://localhost:5000`
   - `https://your-vercel-domain.vercel.app`
6. Copy the Client ID

**Step 2: Configure in UniVibe**

For local development:
```bash
export GOOGLE_CLIENT_ID="your-client-id-here"
python3 app.py
```

For Vercel:
1. Go to Vercel Dashboard
2. Settings → Environment Variables
3. Add: `GOOGLE_CLIENT_ID` = your client ID
4. Redeploy

**Step 3: Update enter.html**
The template already includes Google Sign-In script. Just ensure `google_client_id` is passed from backend.

#### Google User Data
When a user signs in with Google:
```json
{
  "user_id": 8,
  "email": "student@newhorizonindia.edu",
  "username": "student1234",
  "full_name": "Student Name",
  "avatar_color": "#6c63ff",
  "bio": "",
  "is_blacklisted": false,
  "auth_method": "google",
  "google_uid": "google-unique-id",
  "created_at": "2026-05-16T...",
  "updated_at": "2026-05-16T..."
}
```

## Firestore Data Structure

### Users Collection
**Path:** `users/{email}`

**Document Fields:**
```json
{
  "user_id": 1,
  "email": "1NH24CD038@newhorizonindia.edu",
  "username": "student123",
  "full_name": "Student Name",
  "avatar_color": "#6c63ff",
  "bio": "",
  "is_blacklisted": false,
  "auth_method": "password" | "google",
  "google_uid": "optional-google-id",
  "created_at": "2026-05-16T01:57:58.123456",
  "updated_at": "2026-05-16T01:57:58.123456"
}
```

## Database Schema

### SQLite users table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,  -- SHA-256 hash
    full_name TEXT,
    bio TEXT,
    avatar_color TEXT,
    is_blacklisted INTEGER DEFAULT 0,
    is_demo INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
```

## API Endpoints

### POST /enter
**Register or Login**

**Request (Registration):**
```json
{
  "action": "register",
  "email": "1NH24CD038@newhorizonindia.edu",
  "password": "SecurePassword123",
  "username": "student123",
  "full_name": "Student Name"
}
```

**Request (Login):**
```json
{
  "action": "login",
  "email": "1NH24CD038@newhorizonindia.edu",
  "password": "SecurePassword123"
}
```

**Response:**
- Success: Redirect to `/dashboard`
- Error: Flash message with error details

### POST /auth/google
**Google Sign-In**

**Request:**
```json
{
  "token": "google-id-token"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login successful" | "Registration successful"
}
```

**Error Response:**
```json
{
  "error": "Only New Horizon India emails allowed" | "Invalid token"
}
```

### GET /logout
**Logout**
- Clears session
- Redirects to home page

## Frontend Implementation

### Login/Register Form
Located in `templates/enter.html`

**Features:**
- Tab-based UI (Login / Register)
- Email validation (must be @newhorizonindia.edu)
- Password strength requirements
- Google Sign-In button
- Real-time validation

### Google Sign-In Button
```html
<button id="google-signin-btn" class="btn w-100">
  <i class="bi bi-google me-2"></i>Sign in with Google
</button>
```

### JavaScript Integration
```javascript
google.accounts.id.initialize({
  client_id: 'YOUR_CLIENT_ID',
  callback: handleCredentialResponse
});

function handleCredentialResponse(response) {
  // Send token to backend
  fetch('/auth/google', {
    method: 'POST',
    body: JSON.stringify({ token: response.credential })
  });
}
```

## Security Features

### Password Security
- ✅ SHA-256 hashing
- ✅ Minimum 6 characters
- ✅ Never logged or exposed
- ✅ Stored securely in Firestore

### Google OAuth
- ✅ Token verification with Firebase
- ✅ Domain validation (@newhorizonindia.edu)
- ✅ Secure token exchange
- ✅ No password stored for Google users

### Session Management
- ✅ Server-side sessions
- ✅ Secure session cookies
- ✅ Session timeout on logout
- ✅ User ID stored in session

### Domain Restriction
- ✅ Only @newhorizonindia.edu emails allowed
- ✅ Validated on both frontend and backend
- ✅ Works for both password and Google auth

## Testing

### Test Password Registration
```bash
curl -X POST http://localhost:5000/enter \
  -d "action=register" \
  -d "email=test@newhorizonindia.edu" \
  -d "password=TestPassword123" \
  -d "username=testuser" \
  -d "full_name=Test User"
```

### Test Password Login
```bash
curl -X POST http://localhost:5000/enter \
  -d "action=login" \
  -d "email=test@newhorizonindia.edu" \
  -d "password=TestPassword123"
```

### Test Google Sign-In
1. Go to http://localhost:5000/enter
2. Click "Sign in with Google"
3. Authenticate with Google account
4. Should redirect to dashboard

## Troubleshooting

### Issue: "Only New Horizon India emails allowed"
**Solution:** Use email ending with @newhorizonindia.edu

### Issue: "Email already registered"
**Solution:** Use different email or login instead

### Issue: "Incorrect password"
**Solution:** Check password is correct (case-sensitive)

### Issue: Google Sign-In not working
**Solution:**
1. Verify GOOGLE_CLIENT_ID is set
2. Check Google Cloud Console for correct Client ID
3. Verify authorized redirect URIs include your domain
4. Check browser console for errors

### Issue: User data not in Firestore
**Solution:**
1. Verify Firebase credentials are loaded
2. Check Firestore is initialized
3. Verify user email in Firestore Console

## Production Deployment

### Vercel Setup

**Step 1: Add Environment Variables**
```
GOOGLE_CLIENT_ID=your-client-id
FIREBASE_SERVICE_ACCOUNT=your-json-credentials
```

**Step 2: Update Google OAuth**
1. Add Vercel domain to authorized redirect URIs
2. Format: `https://your-project.vercel.app`

**Step 3: Deploy**
```bash
git push
```

### Firestore Security Rules
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{document=**} {
      allow read, write: if request.auth != null;
    }
  }
}
```

## User Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    UniVibe Entry Page                        │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
   ┌────▼─────┐            ┌─────▼──────┐
   │  Login   │            │  Register  │
   └────┬─────┘            └─────┬──────┘
        │                        │
   ┌────▼──────────────────────┐ │
   │ Password or Google Auth   │ │
   └────┬──────────────────────┘ │
        │                        │
   ┌────▼────────────────────────▼──┐
   │  Validate Email Domain         │
   │  (@newhorizonindia.edu)        │
   └────┬─────────────────────────────┘
        │
   ┌────▼──────────────────────────┐
   │  Store in SQLite + Firestore  │
   └────┬─────────────────────────────┘
        │
   ┌────▼──────────────────────────┐
   │  Create Session               │
   └────┬─────────────────────────────┘
        │
   ┌────▼──────────────────────────┐
   │  Redirect to Dashboard        │
   └───────────────────────────────┘
```

## Next Steps

1. ✅ Password authentication implemented
2. ✅ Google Sign-In integrated
3. ✅ Firestore storage enabled
4. ⏭️ Add password reset functionality
5. ⏭️ Add two-factor authentication
6. ⏭️ Add social login (GitHub, Microsoft)

---

**Status:** ✅ Authentication System Complete
**Last Updated:** May 16, 2026
**Supported Methods:** Password + Google OAuth
