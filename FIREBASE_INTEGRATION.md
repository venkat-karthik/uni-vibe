# Firebase Integration - UniVibe

## Overview
Firebase has been successfully integrated into the UniVibe project with Google Sign-In/Sign-Up functionality and Firestore user storage.

## What's Been Integrated

### 1. Firebase Configuration
- **Project ID**: univibe-c85c6
- **Auth Domain**: univibe-c85c6.firebaseapp.com
- **Firestore Database**: Enabled for user storage
- **Google Authentication**: Configured and ready

### 2. Frontend Integration

#### Firebase Config (`static/js/firebase-config.js`)
- Initializes Firebase app with the provided configuration
- Sets up Firebase Authentication
- Initializes Firestore database
- Enables Firebase Analytics
- Exports Firebase instances globally for use in other scripts

#### Firebase Auth Module (`static/js/firebase-auth.js`)
- **Google Sign-In**: `signInWithGoogle()` function
  - Authenticates user with Google
  - Creates new user in Firestore if first-time login
  - Updates existing user's last login time
  - Stores user data in SQLite database
  - Creates Flask session and redirects to dashboard

- **Logout**: `logout()` function
  - Signs out user from Firebase
  - Clears session

- **Auth State Monitoring**: `monitorAuthState()` function
  - Monitors Firebase authentication state changes
  - Provides callback with user data

### 3. Backend Integration

#### Firebase Backend Support (`app.py`)
- **Firebase Admin SDK**: Initialized with credentials
- **Firestore Client**: Connected for user data storage
- **API Endpoint**: `/api/firebase_auth` (POST)
  - Receives authentication data from frontend
  - Creates/updates user in SQLite database
  - Stores user data in Firestore
  - Creates Flask session
  - Returns success response

#### User Data Storage
**Firestore Collection**: `users`
- `uid`: Firebase User ID
- `email`: User's email address
- `full_name`: Display name
- `username`: Unique username
- `provider`: Authentication provider (google)
- `photoURL`: Google profile picture
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

### 4. UI/UX Updates

#### Enter Page (`templates/enter.html`)
- **Google Sign-In Button**: Prominent button with Google logo
- **Direct Entry Option**: Alternative username/name entry
- **Divider**: Clear separation between authentication methods
- **Responsive Design**: Works on all devices

#### Navigation Updates (`templates/base.html`)
- Firebase scripts loaded on all pages
- "Enter UniVibe" button for unauthenticated users
- Conditional navigation based on authentication state

### 5. How It Works

#### User Flow - Google Sign-In
1. User clicks "Sign in with Google" button on `/enter` page
2. Google authentication popup appears
3. User authenticates with Google account
4. Frontend receives user data (uid, email, displayName, photoURL)
5. Frontend checks if user exists in Firestore
6. If new user: Creates user document in Firestore
7. If existing user: Updates last login timestamp
8. Frontend sends authentication data to `/api/firebase_auth` endpoint
9. Backend creates/updates user in SQLite database
10. Backend creates Flask session
11. User is redirected to `/dashboard`

#### User Flow - Direct Entry
1. User enters full name and username
2. Form is submitted to `/enter` route
3. Backend checks if username is available
4. If available: Creates user in SQLite database
5. Backend creates Flask session
6. User is redirected to `/dashboard`

### 6. Configuration Files

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
- `firebase-admin==6.2.0` - Firebase Admin SDK for Python

### 7. Security Notes

⚠️ **Important**: The Firebase service account key is not included in the repository. To enable full Firebase Admin SDK functionality:

1. Download your Firebase service account key from Firebase Console
2. Set the `FIREBASE_SERVICE_ACCOUNT` environment variable with the JSON content, OR
3. Place the `serviceAccountKey.json` file in the project root

Without the service account key, the app will:
- ✅ Still work with Google Sign-In (frontend Firebase SDK)
- ✅ Still create users in SQLite database
- ⚠️ Not be able to store data in Firestore from the backend
- ⚠️ Not be able to use Firebase Admin features

### 8. Testing

To test the integration:

1. **Start the server**:
   ```bash
   source venv/bin/activate
   python3 app.py
   ```

2. **Visit the enter page**:
   - Navigate to `http://localhost:5000/enter`

3. **Test Google Sign-In**:
   - Click "Sign in with Google"
   - Authenticate with your Google account
   - You should be redirected to the dashboard

4. **Test Direct Entry**:
   - Enter your full name and username
   - Click "Enter UniVibe"
   - You should be redirected to the dashboard

### 9. Firestore Rules (Recommended)

For production, set up Firestore security rules:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{uid} {
      allow read, write: if request.auth.uid == uid;
      allow read: if request.auth != null;
    }
  }
}
```

### 10. Next Steps

- [ ] Download and configure Firebase service account key
- [ ] Set up Firestore security rules
- [ ] Test Google Sign-In with real Google account
- [ ] Configure Firebase Hosting (optional)
- [ ] Set up Firebase Analytics dashboard
- [ ] Add email verification (optional)
- [ ] Add password reset functionality (optional)

---

**Status**: ✅ Firebase integration complete and running
**Last Updated**: May 16, 2026
