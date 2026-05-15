# UniVibe - Quick Start Guide

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual environment (venv)
- Firebase account with project: **univibe-c85c6**

### Installation

1. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server**:
   ```bash
   python3 app.py
   ```

4. **Open in browser**:
   ```
   http://localhost:5000
   ```

---

## 🔐 Firebase Setup (IMPORTANT!)

### ⚠️ Current Issue
You're getting: `Sign-in failed: Firebase: Error (auth/unauthorized-domain)`

### ✅ Fix (Takes 2 minutes)

1. Go to: https://console.firebase.google.com/project/univibe-c85c6/authentication/settings
2. Scroll to **Authorized domains**
3. Click **Add domain**
4. Add: `localhost`
5. Click **Add domain** again
6. Add: `127.0.0.1`
7. Refresh your browser
8. Try signing in again

---

## 📱 Features

### Entry Page (`/enter`)
- ✅ Google Sign-In button
- ✅ Direct entry with username
- ✅ No password required

### Dashboard (`/dashboard`)
- ✅ View pending connection requests
- ✅ See accepted connections
- ✅ Access quiz and matches

### Quiz (`/quiz`)
- ✅ 15 personality questions
- ✅ Covers interests, goals, habits
- ✅ Results saved automatically

### Matches (`/results`)
- ✅ Top 5 compatible users
- ✅ Compatibility score
- ✅ Common interests highlighted

### Profile (`/profile/<user_id>`)
- ✅ View user information
- ✅ See quiz answers
- ✅ Leave reviews and ratings
- ✅ Send connection requests

### Chat (`/chat/<user_id>`)
- ✅ Real-time messaging
- ✅ Message history
- ✅ Only with connected users

### Notifications (`/notifications`)
- ✅ Connection requests
- ✅ Accepted connections
- ✅ Messages and reviews
- ✅ System notifications

---

## 🗄️ Database

### SQLite (Local)
- User profiles
- Quiz answers
- Connections
- Messages
- Reviews
- Notifications

### Firestore (Cloud)
- User emails (for sign-in)
- User profiles (backup)
- Authentication records

---

## 🔑 Authentication Methods

### Method 1: Google Sign-In
1. Click "Sign in with Google"
2. Authenticate with your Google account
3. Automatically creates user account
4. Stores email in Firestore

### Method 2: Direct Entry
1. Enter your full name
2. Choose a username
3. Click "Enter UniVibe"
4. Account created instantly

---

## 📁 Project Structure

```
univibe_v3/
├── app.py                          # Main Flask app
├── univibe.db                      # SQLite database
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables
├── templates/
│   ├── base.html                   # Base template
│   ├── index.html                  # Home page
│   ├── enter.html                  # Entry/Sign-in page
│   ├── dashboard.html              # User dashboard
│   ├── quiz.html                   # Quiz page
│   ├── results.html                # Match results
│   ├── profile.html                # User profile
│   ├── chat.html                   # Chat page
│   └── notifications.html          # Notifications
├── static/
│   ├── css/
│   │   ├── style.css               # Main styles
│   │   ├── modern-style.css        # Modern design
│   │   └── animations.css          # Animations
│   └── js/
│       ├── firebase-config.js      # Firebase setup
│       └── firebase-auth.js        # Google Sign-In
└── venv/                           # Virtual environment
```

---

## 🛠️ Troubleshooting

### Issue: `auth/unauthorized-domain`
**Solution**: Add localhost to Firebase authorized domains (see Firebase Setup above)

### Issue: `ModuleNotFoundError: No module named 'firebase_admin'`
**Solution**: Run `pip install -r requirements.txt`

### Issue: Port 5000 already in use
**Solution**: Change port in `app.py` line 747: `app.run(port=5001)`

### Issue: Database locked
**Solution**: Delete `univibe.db` and restart the server

### Issue: Firebase scripts not loading
**Solution**: Check browser console (F12) for errors, make sure JavaScript is enabled

---

## 📊 User Flow

```
┌─────────────────┐
│   Visit /       │
│  (Home Page)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Click "Enter"  │
└────────┬────────┘
         │
    ┌────┴────┐
    │          │
    ▼          ▼
┌────────┐  ┌──────────────┐
│ Google │  │ Direct Entry │
│Sign-In │  │ (Username)   │
└────┬───┘  └──────┬───────┘
     │             │
     └──────┬──────┘
            │
            ▼
    ┌──────────────┐
    │  Dashboard   │
    └──────┬───────┘
           │
    ┌──────┴──────┐
    │             │
    ▼             ▼
┌────────┐   ┌────────┐
│  Quiz  │   │ Matches│
└────┬───┘   └────┬───┘
     │            │
     └──────┬─────┘
            │
            ▼
    ┌──────────────┐
    │   Profile    │
    │  & Connect   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │     Chat     │
    │   & Review   │
    └──────────────┘
```

---

## 🎯 Next Steps

1. ✅ Add localhost to Firebase authorized domains
2. ✅ Test Google Sign-In
3. ✅ Create a user account
4. ✅ Complete the 15-question quiz
5. ✅ View your matches
6. ✅ Connect with other users
7. ✅ Start chatting!

---

## 📞 Support

For issues or questions:
1. Check the browser console (F12) for error messages
2. Check the server logs for backend errors
3. Review the FIREBASE_SETUP_GUIDE.md
4. Check FIREBASE_LOCALHOST_FIX.md for common issues

---

## 📝 Notes

- All data is stored locally in SQLite (except Firestore backup)
- No real emails are required for direct entry
- Usernames must be unique
- Quiz answers are used for matching algorithm
- Connections are mutual (both users must accept)
- Reviews can only be left by connected users

---

**Status**: ✅ Ready to use (after Firebase setup)
**Last Updated**: May 16, 2026
