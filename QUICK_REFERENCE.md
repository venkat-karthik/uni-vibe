# UniVibe - Quick Reference Guide

## 🚀 Quick Start

### Start Server
```bash
cd /Users/venkatkarthik/Downloads/univibe_v3
/Users/venkatkarthik/Downloads/univibe_v3/venv/bin/python app.py
```

### Access Application
- **Home**: http://localhost:5000
- **Login**: http://localhost:5000/login
- **Register**: http://localhost:5000/register

---

## 🔐 Authentication

### Email Requirements
- Must use: `@newhorizonindia.edu`
- Example: `student@newhorizonindia.edu`

### Login Methods
1. **Email/Password** - Traditional login
2. **Google Sign-In** - OAuth 2.0 with Google

### Register Methods
1. **Email/Password** - Create account with credentials
2. **Google Sign-Up** - Create account with Google

---

## 📁 Key Files

### Frontend
- `templates/login.html` - Login page
- `templates/register.html` - Register page
- `static/js/firebase-auth-enhanced.js` - Auth functions
- `static/js/firebase-config.js` - Firebase setup
- `static/css/modern-style.css` - Modern design
- `static/css/animations.css` - 50+ animations

### Backend
- `app.py` - Main Flask application
- `firebase_helpers.py` - Firestore operations
- `univibe.db` - SQLite database

### Configuration
- `.env.example` - Environment variables template
- `requirements.txt` - Python dependencies

---

## 🔧 API Endpoints

### Authentication
```
POST /api/firebase_auth
- uid: string
- email: string (must be @newhorizonindia.edu)
- displayName: string
- photoURL: string
- provider: 'google' | 'email'
```

### Messages
```
POST /api/send_message
GET /api/get_messages/<uid>
```

### Notifications
```
GET /api/notifications/count
POST /api/cookie_consent
```

---

## 🗄️ Database

### SQLite Tables
- `users` - User profiles
- `quiz_answers` - Quiz responses
- `connections` - User connections
- `messages` - Chat messages
- `reviews` - User reviews
- `notifications` - Notifications
- `cookie_consent` - Cookie consent
- `blacklist` - Blacklisted users

### Firestore Collections
- `users` - User profiles
- `quiz_answers` - Quiz responses
- `connections` - User connections
- `messages` - Chat messages
- `reviews` - User reviews
- `notifications` - Notifications
- `blacklist` - Blacklisted users

---

## 🧪 Testing

### Test Server
```bash
curl http://localhost:5000/test
```

### Test Firebase Auth
```bash
curl -X POST http://localhost:5000/api/firebase_auth \
  -H "Content-Type: application/json" \
  -d '{
    "uid": "test-user",
    "email": "test@newhorizonindia.edu",
    "displayName": "Test User",
    "photoURL": "",
    "provider": "google"
  }'
```

### Test Invalid Email
```bash
curl -X POST http://localhost:5000/api/firebase_auth \
  -H "Content-Type: application/json" \
  -d '{
    "uid": "test-user",
    "email": "test@gmail.com",
    "displayName": "Test User",
    "photoURL": "",
    "provider": "google"
  }'
# Expected: Error - Only newhorizonindia.edu emails are allowed
```

---

## 🔍 Debugging

### Check Server Logs
```bash
# Server output shows in terminal
# Look for errors or warnings
```

### Check Browser Console
```javascript
// Press F12 to open developer tools
console.log(window.firebaseAuth);
console.log(window.firebaseDb);
console.log(window.firebaseAuthEnhanced);
```

### Check Database
```bash
sqlite3 univibe.db "SELECT * FROM users LIMIT 5;"
```

### Check Routes
```bash
curl -s http://localhost:5000/login | grep -i "sign in"
```

---

## 🐛 Common Issues

### Port Already in Use
```bash
lsof -ti:5000 | xargs kill -9
```

### Dependencies Missing
```bash
pip install -r requirements.txt
```

### Firebase Not Initializing
- Check internet connection
- Verify Firebase credentials
- Check browser console for errors

### Email Validation Not Working
- Verify JavaScript is enabled
- Check browser console
- Verify email format

---

## 📊 Project Structure

```
univibe_v3/
├── app.py                    # Main Flask app
├── firebase_helpers.py       # Firestore operations
├── requirements.txt          # Dependencies
├── univibe.db               # SQLite database
├── .env.example             # Environment template
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── modern-style.css
│   │   └── animations.css
│   └── js/
│       ├── firebase-config.js
│       └── firebase-auth-enhanced.js
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── quiz.html
│   ├── results.html
│   ├── profile.html
│   ├── chat.html
│   └── notifications.html
│
└── Documentation/
    ├── README.md
    ├── QUICK_START.md
    ├── FIREBASE_AUTH_COMPLETE.md
    ├── TEST_AUTHENTICATION.md
    ├── CURRENT_STATUS.md
    ├── IMPLEMENTATION_COMPLETE.md
    └── QUICK_REFERENCE.md (this file)
```

---

## 🎯 Features

### Authentication ✅
- Email/Password login
- Email/Password registration
- Google Sign-In
- Google Sign-Up
- Email domain validation
- Session management

### Social Features ✅
- Connection requests
- User profiles
- Personality quiz
- Match recommendations
- User reviews
- Real-time messaging
- Notifications

### UI/UX ✅
- Modern design system
- 50+ animations
- Responsive layout
- Dark theme
- Professional typography
- Smooth transitions

---

## 📞 Support

### Documentation
- [README.md](README.md) - Project overview
- [QUICK_START.md](QUICK_START.md) - Getting started
- [FIREBASE_AUTH_COMPLETE.md](FIREBASE_AUTH_COMPLETE.md) - Auth details
- [TEST_AUTHENTICATION.md](TEST_AUTHENTICATION.md) - Testing guide
- [CURRENT_STATUS.md](CURRENT_STATUS.md) - Project status
- [IMPLEMENTATION_COMPLETE.md](IMPLEMENTATION_COMPLETE.md) - Implementation details

### Firebase Console
- Project: https://console.firebase.google.com/project/unvibe-54ae1
- Auth: Enable Google Sign-In
- Firestore: Check collections

---

## ✅ Status

**Server**: Running ✅  
**Authentication**: Working ✅  
**Database**: Synced ✅  
**UI/UX**: Modern ✅  
**Production Ready**: Yes ✅

---

**Last Updated**: May 15, 2026  
**Version**: 3.0  
**Status**: Production Ready
