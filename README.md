# UniVibe - Find Your Vibe, Find Your People

A modern web application for connecting students based on personality compatibility using cosine similarity matching.

## Quick Start

### Prerequisites
- Python 3.8+
- Firebase project
- pip

### Installation

```bash
# Clone repository
git clone https://github.com/venkat-karthik/unvibe.git
cd unvibe

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python3 app.py
```

Visit http://localhost:5000

## Features

✅ Email/Password authentication
✅ Google Sign-In/Sign-Up
✅ Personality quiz (15 questions)
✅ Smart matching algorithm (cosine similarity)
✅ Real-time chat
✅ Connection requests
✅ User reviews and ratings
✅ Notifications
✅ Modern glassmorphism UI
✅ Firestore integration
✅ Auto-blacklist on bad reviews

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite + Firestore
- **Authentication**: Firebase Auth
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Bootstrap 5 + Custom CSS

## Project Structure

```
univibe/
├── app.py                      # Main Flask application
├── firebase_helpers.py         # Firebase integration
├── requirements.txt            # Dependencies
├── templates/                  # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── quiz.html
│   ├── results.html
│   ├── profile.html
│   ├── chat.html
│   └── notifications.html
├── static/
│   ├── css/
│   │   ├── modern-style.css
│   │   ├── animations.css
│   │   └── style.css
│   └── js/
│       ├── firebase-config.js
│       └── firebase-auth-enhanced.js
└── univibe.db                  # SQLite database
```

## Database Schema

- **users**: User profiles and authentication
- **quiz_answers**: User quiz responses
- **connections**: Connection requests and status
- **messages**: Chat messages
- **reviews**: User reviews and ratings
- **notifications**: User notifications
- **blacklist**: Blacklisted users

## API Endpoints

### Auth
- `POST /register` - Register user
- `POST /login` - Login user
- `GET /logout` - Logout user
- `POST /api/firebase_auth` - Firebase auth

### User
- `GET /dashboard` - Dashboard
- `GET /profile/<uid>` - User profile
- `POST /api/cookie_consent` - Cookie consent

### Quiz & Matching
- `GET /quiz` - Quiz page
- `POST /quiz` - Submit quiz
- `GET /results` - View matches

### Connections
- `POST /connect/<uid>` - Send request
- `GET /connection/respond/<conn_id>/<action>` - Respond

### Chat
- `GET /chat/<uid>` - Chat page
- `POST /api/send_message` - Send message
- `GET /api/get_messages/<uid>` - Get messages

### Notifications
- `GET /notifications` - View notifications
- `GET /api/notifications/count` - Unread count

### Reviews
- `POST /review/<uid>` - Submit review

## Configuration

### Firebase Console Setup

1. Go to https://console.firebase.google.com/
2. Select project: **unvibe-54ae1**
3. Go to **Authentication → Settings → Authorized domains**
4. Add:
   - `localhost:5000`
   - `127.0.0.1:5000`
5. Remove any old domains

### Environment Variables

Create `.env` file with Firebase credentials:
```
FIREBASE_API_KEY=your_api_key
FIREBASE_AUTH_DOMAIN=your_auth_domain
FIREBASE_PROJECT_ID=your_project_id
```

## Documentation

- `IMMEDIATE_ACTION_REQUIRED.md` - Firebase Console setup
- `FIREBASE_CONSOLE_FIX.md` - Detailed Firebase configuration
- `FINAL_FIX_SUMMARY.md` - System overview
- `DYNAMIC_EMAIL_WHITELIST.md` - Email approval system

## License

MIT License

## Author

Venkat Karthik
