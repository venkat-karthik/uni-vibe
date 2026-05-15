# Firebase Web SDK Setup Guide

## Overview
This guide explains how to use Firebase Web SDK for authentication in UniVibe frontend.

## What's Included

### 1. Firebase Initialization (`firebase-init.js`)
- Initializes Firebase app
- Sets up Authentication
- Sets up Firestore
- Sets up Analytics
- Configures Google Auth Provider

### 2. Authentication Helper (`firebase-auth-helper.js`)
- Email/Password registration
- Email/Password login
- Google Sign-In
- Session management
- User profile management
- Error handling
- Input validation

## Installation

### Step 1: Include Firebase SDK in HTML

Add this to your HTML file (e.g., `templates/base.html`):

```html
<!-- Firebase Web SDK -->
<script type="module" src="{{ url_for('static', filename='js/firebase-init.js') }}"></script>
```

### Step 2: Use Authentication Functions

In your JavaScript files, import the functions:

```javascript
import { 
  registerWithEmail, 
  loginWithEmail, 
  signInWithGoogle,
  getCurrentUser,
  logoutUser,
  validateEmail,
  validatePassword
} from '/static/js/firebase-auth-helper.js';
```

## Usage Examples

### Email & Password Registration

```javascript
import { registerWithEmail, validateEmail, validatePassword } from '/static/js/firebase-auth-helper.js';

async function handleRegister(email, password, username, fullName) {
  // Validate inputs
  const emailValidation = validateEmail(email);
  if (!emailValidation.valid) {
    alert(emailValidation.error);
    return;
  }
  
  const passwordValidation = validatePassword(password);
  if (!passwordValidation.valid) {
    alert(passwordValidation.error);
    return;
  }
  
  // Register user
  const result = await registerWithEmail(email, password, {
    username: username,
    full_name: fullName,
    avatar_color: '#6c63ff'
  });
  
  if (result.success) {
    console.log("✅ Registration successful!");
    // Redirect to dashboard
    window.location.href = '/dashboard';
  } else {
    alert("Registration failed: " + result.error);
  }
}
```

### Email & Password Login

```javascript
import { loginWithEmail, validateEmail } from '/static/js/firebase-auth-helper.js';

async function handleLogin(email, password) {
  // Validate email
  const emailValidation = validateEmail(email);
  if (!emailValidation.valid) {
    alert(emailValidation.error);
    return;
  }
  
  // Login user
  const result = await loginWithEmail(email, password);
  
  if (result.success) {
    console.log("✅ Login successful!");
    // Redirect to dashboard
    window.location.href = '/dashboard';
  } else {
    alert("Login failed: " + result.error);
  }
}
```

### Google Sign-In

```javascript
import { signInWithGoogle } from '/static/js/firebase-auth-helper.js';

async function handleGoogleSignIn() {
  const result = await signInWithGoogle();
  
  if (result.success) {
    console.log("✅ Google sign-in successful!");
    if (result.isNewUser) {
      console.log("New user created");
    }
    // Redirect to dashboard
    window.location.href = '/dashboard';
  } else {
    alert("Google sign-in failed: " + result.error);
  }
}
```

### Check Authentication State

```javascript
import { onAuthChange, getCurrentUser } from '/static/js/firebase-auth-helper.js';

// Listen to auth state changes
onAuthChange((user) => {
  if (user) {
    console.log("✅ User logged in:", user.email);
    // Show dashboard
  } else {
    console.log("❌ User logged out");
    // Show login page
  }
});

// Get current user
const user = await getCurrentUser();
if (user) {
  console.log("Current user:", user.email);
}
```

### Logout

```javascript
import { logoutUser } from '/static/js/firebase-auth-helper.js';

async function handleLogout() {
  const result = await logoutUser();
  
  if (result.success) {
    console.log("✅ Logged out successfully");
    // Redirect to home
    window.location.href = '/';
  }
}
```

### Get User Profile

```javascript
import { getUserProfile } from '/static/js/firebase-auth-helper.js';

async function loadUserProfile(email) {
  const result = await getUserProfile(email);
  
  if (result.success) {
    console.log("User profile:", result.data);
    // Display user data
  } else {
    console.log("Error:", result.error);
  }
}
```

### Update User Profile

```javascript
import { updateUserProfile } from '/static/js/firebase-auth-helper.js';

async function updateProfile(email, updates) {
  const result = await updateUserProfile(email, {
    bio: "New bio",
    avatar_color: "#ff6584"
  });
  
  if (result.success) {
    console.log("✅ Profile updated");
  } else {
    console.log("Error:", result.error);
  }
}
```

## Firebase Configuration

Your Firebase config is already set up:

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyCDwaBMoEJvJO1NBS-uUzsMTirSSGz8Mcc",
  authDomain: "univibe-c85c6.firebaseapp.com",
  projectId: "univibe-c85c6",
  storageBucket: "univibe-c85c6.firebasestorage.app",
  messagingSenderId: "631710741538",
  appId: "1:631710741538:web:49b43d32353d97bcc3467b",
  measurementId: "G-1CXWWSRM61"
};
```

## Firestore Data Structure

### Users Collection

```
Collection: users
Document ID: user@email.com

Fields:
{
  uid: "firebase-uid",
  email: "user@newhorizonindia.edu",
  username: "username",
  full_name: "Full Name",
  avatar_color: "#6c63ff",
  bio: "User bio",
  auth_method: "email" | "google",
  google_uid: "optional-google-id",
  photo_url: "optional-photo-url",
  created_at: Timestamp,
  updated_at: Timestamp
}
```

## Authentication Methods

### Email & Password
- Registration with email, password, username, full name
- Login with email and password
- Password validation (minimum 6 characters)
- Email domain validation (@newhorizonindia.edu)

### Google Sign-In
- One-click Google authentication
- Auto-registration for new users
- Profile data from Google (name, photo)
- Domain validation

## Error Handling

The helper includes user-friendly error messages:

```javascript
import { getErrorMessage } from '/static/js/firebase-auth-helper.js';

try {
  // Some auth operation
} catch (error) {
  const message = getErrorMessage(error.code);
  alert(message);
}
```

Common errors:
- `auth/email-already-in-use` - Email already registered
- `auth/invalid-email` - Invalid email format
- `auth/weak-password` - Password too short
- `auth/user-not-found` - Email not found
- `auth/wrong-password` - Incorrect password
- `auth/too-many-requests` - Too many login attempts

## Validation Functions

### Email Validation
```javascript
import { validateEmail } from '/static/js/firebase-auth-helper.js';

const result = validateEmail('user@newhorizonindia.edu');
if (result.valid) {
  // Email is valid
} else {
  console.log(result.error);
}
```

### Password Validation
```javascript
import { validatePassword } from '/static/js/firebase-auth-helper.js';

const result = validatePassword('MyPassword123');
if (result.valid) {
  // Password is valid
} else {
  console.log(result.error);
}
```

### Username Validation
```javascript
import { validateUsername } from '/static/js/firebase-auth-helper.js';

const result = validateUsername('myusername');
if (result.valid) {
  // Username is valid
} else {
  console.log(result.error);
}
```

## Security Best Practices

1. **Never expose API keys** - Already handled (keys are public for web SDK)
2. **Use HTTPS** - Always use HTTPS in production
3. **Validate on frontend and backend** - Both layers validate input
4. **Use secure passwords** - Minimum 6 characters enforced
5. **Domain restriction** - Only @newhorizonindia.edu emails allowed
6. **Firestore security rules** - Configure in Firebase Console

## Firestore Security Rules

Add these rules in Firebase Console:

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

## Testing

### Test Email Registration
```javascript
const result = await registerWithEmail(
  'test@newhorizonindia.edu',
  'TestPassword123',
  { username: 'testuser', full_name: 'Test User' }
);
```

### Test Email Login
```javascript
const result = await loginWithEmail(
  'test@newhorizonindia.edu',
  'TestPassword123'
);
```

### Test Google Sign-In
```javascript
const result = await signInWithGoogle();
```

## Troubleshooting

### Issue: "Firebase is not defined"
**Solution:** Make sure `firebase-init.js` is loaded before using auth functions

### Issue: "Module not found"
**Solution:** Check file paths are correct relative to HTML file

### Issue: "CORS error"
**Solution:** This shouldn't happen with Firebase Web SDK, check browser console

### Issue: "Auth/firestore not initialized"
**Solution:** Wait for Firebase to initialize before using functions

## Next Steps

1. ✅ Firebase Web SDK configured
2. ✅ Authentication helper created
3. ⏭️ Update HTML forms to use Firebase auth
4. ⏭️ Add frontend validation
5. ⏭️ Test all authentication flows
6. ⏭️ Deploy to production

## Files

- `static/js/firebase-init.js` - Firebase initialization
- `static/js/firebase-auth-helper.js` - Authentication helper functions
- `FIREBASE_WEB_SDK_SETUP.md` - This guide

---

**Status:** ✅ Firebase Web SDK Ready
**Last Updated:** May 16, 2026
