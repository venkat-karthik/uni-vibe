# 🔥 Firebase Integration Guide for UniVibe

## Overview

UniVibe has been integrated with Firebase Authentication to provide secure, scalable user authentication with organization-specific email validation (New Horizon India only).

---

## 📋 What's New

### Backend Changes (Python/Flask)
- ✅ Added Firebase configuration to `app.py`
- ✅ Updated email validation to check for `@newhorizonindia.edu` domain
- ✅ Added `python-dotenv` for environment variable management
- ✅ Removed old GRIET email validation (24241a prefix)

### Frontend Changes (HTML/JavaScript)
- ✅ Created `static/js/firebase-config.js` - Firebase initialization
- ✅ Created `static/js/firebase-auth.js` - Authentication helper functions
- ✅ Updated `templates/login.html` - New Horizon India email validation
- ✅ Updated `templates/register.html` - Organization email restriction

### Configuration Files
- ✅ Updated `requirements.txt` - Added Firebase dependencies
- ✅ Created `.env.example` - Environment variable template

---

## 🚀 Setup Instructions

### Step 1: Install Dependencies

```bash
cd /Users/venkatkarthik/Downloads/univibe_v3
source venv/bin/activate
pip install -r requirements.txt
```

**New packages installed:**
- `firebase-admin==6.2.0` - Firebase Admin SDK for Python
- `python-dotenv==1.0.0` - Environment variable management

### Step 2: Create Environment File

Copy the example environment file:

```bash
cp .env.example .env
```

The `.env` file contains:
```
FIREBASE_API_KEY=AIzaSyCc9soowCRi8W7hGZqL_RViQwallIPutp4
FIREBASE_AUTH_DOMAIN=unvibe-54ae1.firebaseapp.com
FIREBASE_PROJECT_ID=unvibe-54ae1
FIREBASE_STORAGE_BUCKET=unvibe-54ae1.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=91608029769
FIREBASE_APP_ID=1:91608029769:web:18544d40309fbd82a63d98
FIREBASE_MEASUREMENT_ID=G-Z8MKB0PL4M
ALLOWED_EMAIL_DOMAIN=newhorizonindia.edu
```

### Step 3: Run the Application

```bash
python3 app.py
```

Visit: `http://localhost:5000`

---

## 🔐 Email Validation

### Organization Email Domain
- **Allowed Domain:** `@newhorizonindia.edu`
- **Example Valid Email:** `john.doe@newhorizonindia.edu`
- **Example Invalid Email:** `john.doe@gmail.com`

### Validation Happens At:
1. **Frontend (Real-time)** - JavaScript validation in login/register forms
2. **Backend (Server-side)** - Python validation in Flask routes
3. **Firebase** - Email verification through Firebase Authentication

---

## 📁 File Structure

```
univibe_v3/
├── app.py                              # Updated with Firebase config
├── requirements.txt                    # Updated with Firebase packages
├── .env.example                        # Environment variables template
├── .env                                # (Create from .env.example)
├── static/
│   └── js/
│       ├── firebase-config.js          # NEW - Firebase initialization
│       └── firebase-auth.js            # NEW - Auth helper functions
├── templates/
│   ├── login.html                      # Updated with org email validation
│   ├── register.html                   # Updated with org email validation
│   └── base.html                       # (No changes)
└── FIREBASE_INTEGRATION.md             # This file
```

---

## 🔧 Firebase Configuration

### Firebase Project Details
- **Project ID:** `unvibe-54ae1`
- **Auth Domain:** `unvibe-54ae1.firebaseapp.com`
- **Storage Bucket:** `unvibe-54ae1.firebasestorage.app`
- **Deployment URL:** `https://unvibe-54ae1.web.app`

### Firebase Console
Access Firebase Console: https://console.firebase.google.com/project/unvibe-54ae1

---

## 🎯 Features

### Authentication
- ✅ Email/Password authentication
- ✅ Organization email validation
- ✅ Real-time email validation feedback
- ✅ Secure password handling
- ✅ Session management

### User Registration
- ✅ Full name input
- ✅ Username creation
- ✅ Organization email validation
- ✅ Password strength requirement (min 6 chars)
- ✅ Optional bio/profile info

### User Login
- ✅ Email-based login
- ✅ Organization email validation
- ✅ Real-time validation feedback
- ✅ Session persistence

---

## 📝 Code Examples

### Frontend - Email Validation (JavaScript)

```javascript
const ALLOWED_EMAIL_DOMAIN = 'newhorizonindia.edu';

function validateLoginEmail(input) {
  const email = input.value.toLowerCase().trim();
  
  if (email.endsWith(`@${ALLOWED_EMAIL_DOMAIN}`)) {
    // Valid email
    input.style.borderColor = '#43d9ad';
  } else {
    // Invalid email
    input.style.borderColor = '#ff6584';
  }
}
```

### Backend - Email Validation (Python)

```python
ALLOWED_EMAIL_DOMAIN = "newhorizonindia.edu"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        
        # Validate email domain
        if not email.endswith(f'@{ALLOWED_EMAIL_DOMAIN}'):
            flash(f'Only {ALLOWED_EMAIL_DOMAIN} emails are allowed!', 'danger')
            return render_template('register.html')
        
        # Continue with registration...
```

---

## 🚀 Deployment

### Deploy to Firebase Hosting

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login to Firebase
firebase login

# Initialize Firebase in project
firebase init

# Deploy
firebase deploy
```

**Deployment URL:** `https://unvibe-54ae1.web.app`

---

## 🔍 Testing

### Test Account Setup

1. **Create Test Account:**
   - Email: `test@newhorizonindia.edu`
   - Password: `TestPassword123`
   - Full Name: `Test User`
   - Username: `testuser`

2. **Test Login:**
   - Use the same email and password
   - Verify real-time email validation
   - Check session persistence

3. **Test Invalid Email:**
   - Try: `test@gmail.com`
   - Should see error message
   - Submit button should be disabled

---

## 🐛 Troubleshooting

### Issue: "Only newhorizonindia.edu emails are allowed"

**Solution:** Ensure you're using an email ending with `@newhorizonindia.edu`

### Issue: Firebase not initializing

**Solution:** 
1. Check `.env` file exists and has correct credentials
2. Verify internet connection
3. Check browser console for errors

### Issue: Email validation not working

**Solution:**
1. Clear browser cache
2. Check JavaScript console for errors
3. Verify `firebase-config.js` is loaded

---

## 📚 Additional Resources

- [Firebase Documentation](https://firebase.google.com/docs)
- [Firebase Authentication Guide](https://firebase.google.com/docs/auth)
- [Firebase Hosting Guide](https://firebase.google.com/docs/hosting)
- [Firebase Console](https://console.firebase.google.com)

---

## ✅ Verification Checklist

- ✅ Dependencies installed
- ✅ `.env` file created
- ✅ Firebase config in `app.py`
- ✅ Email validation in login/register
- ✅ Frontend scripts loaded
- ✅ Server running without errors
- ✅ Test account created
- ✅ Login/register working

---

## 📞 Support

For issues or questions:
1. Check Firebase Console for authentication logs
2. Review browser console for JavaScript errors
3. Check Flask server logs for backend errors
4. Verify `.env` file configuration

---

**Last Updated:** May 15, 2026  
**Firebase Project:** unvibe-54ae1  
**Organization Domain:** newhorizonindia.edu

