# UniVibe - Setup Complete ✅

## Current Status

The UniVibe project has been successfully cleaned up and reconfigured with a simple, secure Firestore-based email and username login system.

## What's Running

### Server
- **Status**: ✅ Running on `http://localhost:5000`
- **Framework**: Flask 3.0.0
- **Database**: SQLite (univibe.db)
- **Cloud Storage**: Firestore (optional)

### Features Implemented
- ✅ Simple email & username login
- ✅ User registration with validation
- ✅ Firestore integration for user data storage
- ✅ SQLite database for core application data
- ✅ Quiz matching system
- ✅ User profiles and connections
- ✅ Chat functionality
- ✅ Notifications system
- ✅ Review and rating system

## What Was Removed

- ❌ Firebase Google Sign-In
- ❌ Firebase Authentication module
- ❌ Firebase Analytics
- ❌ Complex OAuth flows
- ❌ Login/Register pages (replaced with unified `/enter` page)

## How to Use

### 1. Start the Server
```bash
cd /Users/venkatkarthik/Downloads/univibe_v3
source venv/bin/activate
python3 app.py
```

### 2. Access the Application
- **Home**: `http://localhost:5000/`
- **Enter/Login**: `http://localhost:5000/enter`
- **Dashboard**: `http://localhost:5000/dashboard` (after login)

### 3. Create an Account
1. Go to `http://localhost:5000/enter`
2. Enter your email address
3. Choose a unique username
4. Enter your full name
5. Click "Enter UniVibe"
6. You'll be redirected to the dashboard

### 4. Complete the Quiz
1. Click "Quiz" in the navigation
2. Answer 15 questions about your interests
3. Submit the quiz
4. View your top 5 matches

### 5. Connect with Others
1. Go to "Matches" to see your top matches
2. Click on a profile to view details
3. Send a connection request
4. Once accepted, you can chat and review

## Project Structure

```
univibe_v3/
├── app.py                          # Main Flask application
├── univibe.db                      # SQLite database
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── templates/
│   ├── base.html                   # Base template with navigation
│   ├── index.html                  # Home page
│   ├── enter.html                  # Login/Registration page
│   ├── dashboard.html              # User dashboard
│   ├── quiz.html                   # Quiz page
│   ├── results.html                # Match results
│   ├── profile.html                # User profile
│   ├── chat.html                   # Chat interface
│   └── notifications.html          # Notifications
├── static/
│   ├── css/
│   │   ├── style.css               # Main styles
│   │   ├── modern-style.css        # Modern design
│   │   └── animations.css          # Animations
│   └── js/
│       └── firebase-config.js      # Firestore configuration
└── public/
    └── index.html                  # Public index
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    full_name TEXT,
    bio TEXT,
    avatar_color TEXT,
    is_blacklisted INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
```

### Other Tables
- `quiz_answers` - User quiz responses
- `connections` - Connection requests between users
- `reviews` - User reviews and ratings
- `blacklist` - Blacklisted users
- `messages` - Chat messages
- `notifications` - User notifications
- `cookie_consent` - Cookie consent tracking

## Firestore Integration

### Collection: `users`
Each user document is stored with their email as the document ID:

```json
{
  "user_id": 1,
  "email": "user@example.com",
  "username": "username",
  "full_name": "Full Name",
  "avatar_color": "#6c63ff",
  "bio": "User biography",
  "is_blacklisted": false,
  "created_at": "2026-05-16T...",
  "updated_at": "2026-05-16T..."
}
```

## Configuration

### Environment Variables (`.env`)
```
FIREBASE_API_KEY=AIzaSyCDwaBMoEJvJO1NBS-uUzsMTirSSGz8Mcc
FIREBASE_AUTH_DOMAIN=univibe-c85c6.firebaseapp.com
FIREBASE_PROJECT_ID=univibe-c85c6
FIREBASE_STORAGE_BUCKET=univibe-c85c6.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=631710741538
FIREBASE_APP_ID=1:631710741538:web:49b43d32353d97bcc3467b
FIREBASE_MEASUREMENT_ID=G-1CXWWSRM61
```

### Python Dependencies
```
flask==3.0.0
scikit-learn==1.4.0
numpy>=1.24.0
python-dotenv==1.0.0
firebase-admin==6.2.0
```

## Key Features

### 1. Quiz Matching Algorithm
- 15 comprehensive questions
- Cosine similarity matching
- Top 5 matches based on compatibility

### 2. User Connections
- Send/receive connection requests
- Accept/reject connections
- Chat with connected users

### 3. Review System
- Rate other users (1-5 stars)
- Leave comments
- Auto-blacklist after 3 bad reviews

### 4. Notifications
- Connection requests
- Accepted connections
- Messages
- Reviews
- Real-time notification count

### 5. Chat System
- Direct messaging with connected users
- Message history
- Read/unread status
- Real-time updates

## Security Notes

⚠️ **Important Security Considerations**:

1. **Service Account Key**: Not included in repository
   - Download from Firebase Console
   - Set `FIREBASE_SERVICE_ACCOUNT` environment variable
   - Or place `serviceAccountKey.json` in project root

2. **Firestore Rules**: Set up security rules to prevent unauthorized access
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

3. **Password Hashing**: Passwords are hashed with SHA256
   - Consider upgrading to bcrypt for production

4. **Session Management**: Flask sessions are used
   - Configure secure session cookies for production

## Troubleshooting

### Server Won't Start
```bash
# Check Python version
python3 --version

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python3 app.py
```

### Database Issues
```bash
# Reset database
rm univibe.db
python3 app.py  # Will recreate database

# Check database
sqlite3 univibe.db ".tables"
```

### Firestore Connection Issues
- Ensure Firebase credentials are properly configured
- Check internet connection
- Verify Firebase project is active

## Next Steps

1. **Configure Firestore Service Account**
   - Download from Firebase Console
   - Set up environment variable

2. **Set Up Firestore Security Rules**
   - Protect user data
   - Prevent unauthorized access

3. **Deploy to Production**
   - Use production WSGI server (Gunicorn, uWSGI)
   - Set up HTTPS
   - Configure environment variables

4. **Add Features**
   - Email verification
   - Password reset
   - Social login (optional)
   - User search
   - Advanced filtering

## Support

For issues or questions:
1. Check the logs: `python3 app.py`
2. Review the documentation files
3. Check Firestore console for data
4. Verify SQLite database: `sqlite3 univibe.db`

---

**Project**: UniVibe - University Connection Platform
**Status**: ✅ Ready for Development
**Last Updated**: May 16, 2026
**Server**: Running on http://localhost:5000
