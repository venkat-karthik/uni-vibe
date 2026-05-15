# UniVibe - Quick Start Guide

## 🚀 Start the Server

```bash
cd /Users/venkatkarthik/Downloads/univibe_v3
source venv/bin/activate
python3 app.py
```

Server will run on: **http://localhost:5000**

## 📍 Key URLs

| Page | URL | Purpose |
|------|-----|---------|
| Home | `http://localhost:5000/` | Landing page |
| Enter/Login | `http://localhost:5000/enter` | Create account or login |
| Dashboard | `http://localhost:5000/dashboard` | User home (after login) |
| Quiz | `http://localhost:5000/quiz` | Take the matching quiz |
| Matches | `http://localhost:5000/results` | View top 5 matches |
| Profile | `http://localhost:5000/profile/<id>` | View user profile |
| Chat | `http://localhost:5000/chat/<id>` | Chat with connected user |
| Notifications | `http://localhost:5000/notifications` | View notifications |

## 📝 How to Create an Account

1. Go to `http://localhost:5000/enter`
2. Fill in the form:
   - **Email**: Your email address (e.g., `user@example.com`)
   - **Username**: Unique username (e.g., `john_doe`)
   - **Full Name**: Your name (e.g., `John Doe`)
3. Click "Enter UniVibe"
4. You'll be logged in and redirected to dashboard

## 🎯 How to Use the App

### Step 1: Take the Quiz
- Click "Quiz" in the navigation
- Answer 15 questions about your interests
- Submit the quiz

### Step 2: View Your Matches
- Click "Matches" in the navigation
- See your top 5 compatible users
- Click on a profile to view details

### Step 3: Connect with Others
- Click "Connect" on a profile
- Wait for them to accept your request
- Once accepted, you can chat

### Step 4: Chat & Review
- Click on a connected user to chat
- Leave a review and rating
- Build your reputation

## 🔧 Project Structure

```
univibe_v3/
├── app.py                    # Main application
├── univibe.db               # SQLite database
├── requirements.txt         # Dependencies
├── templates/               # HTML templates
│   ├── enter.html          # Login page
│   ├── dashboard.html      # User dashboard
│   ├── quiz.html           # Quiz page
│   ├── results.html        # Matches page
│   ├── profile.html        # User profile
│   ├── chat.html           # Chat page
│   └── ...
├── static/
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript files
└── venv/                   # Virtual environment
```

## 📊 Database

**SQLite Database**: `univibe.db`

Main tables:
- `users` - User accounts
- `quiz_answers` - Quiz responses
- `connections` - User connections
- `messages` - Chat messages
- `reviews` - User reviews
- `notifications` - Notifications

## 🔐 Login System

**Simple Email & Username Login**
- No password required
- Email must be unique
- Username must be unique
- Data stored in SQLite + Firestore

## 🌐 Firestore Integration

**Optional Cloud Storage**
- User data backed up in Firestore
- Requires Firebase service account key
- Set `FIREBASE_SERVICE_ACCOUNT` environment variable

## 🛠️ Troubleshooting

### Server won't start?
```bash
# Check if port 5000 is in use
lsof -i :5000

# Kill the process if needed
kill -9 <PID>

# Try again
python3 app.py
```

### Database error?
```bash
# Reset database
rm univibe.db

# Restart server (will recreate database)
python3 app.py
```

### Can't login?
- Make sure email is unique
- Make sure username is unique
- Check browser console for errors

## 📱 Features

✅ User registration with email & username
✅ 15-question compatibility quiz
✅ Cosine similarity matching algorithm
✅ Top 5 match recommendations
✅ User profiles with bio
✅ Connection requests
✅ Direct messaging/chat
✅ User reviews & ratings
✅ Notification system
✅ Auto-blacklist after 3 bad reviews
✅ Cookie consent management

## 🎨 UI/UX

- Modern gradient design
- Responsive layout
- Bootstrap 5 framework
- Smooth animations
- Dark mode ready

## 📚 Documentation

- `SETUP_COMPLETE.md` - Full setup guide
- `FIRESTORE_LOGIN_SETUP.md` - Login system details
- `README.md` - Project overview

## 🚀 Next Steps

1. Create an account
2. Take the quiz
3. View your matches
4. Connect with others
5. Start chatting!

## 💡 Tips

- Use a real email for testing Firestore integration
- Try creating multiple accounts to test matching
- Check notifications for connection requests
- Leave reviews to build your reputation

---

**Ready to go!** 🎉

Start the server and visit `http://localhost:5000`
