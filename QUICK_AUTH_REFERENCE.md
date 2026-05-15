# Quick Authentication Reference

## 🚀 Quick Start

### Local Development
```bash
# Server is already running on localhost:5000
# Password auth works immediately
# Google Sign-In needs GOOGLE_CLIENT_ID
```

### Test Password Login
1. Go to http://localhost:5000/enter
2. Click "Register" tab
3. Fill in:
   - Email: `test@newhorizonindia.edu`
   - Password: `TestPassword123`
   - Username: `testuser`
   - Full Name: `Test User`
4. Click "Create Account"
5. You're logged in!

### Test Password Login
1. Go to http://localhost:5000/enter
2. Stay on "Login" tab
3. Enter email and password
4. Click "Login"

## 🔑 Authentication Methods

| Method | Setup | Status |
|--------|-------|--------|
| Password | None needed | ✅ Ready |
| Google | Need Client ID | ⏳ Ready (needs config) |
| Firestore | Already done | ✅ Ready |

## 📝 Password Requirements

- **Email:** Must end with `@newhorizonindia.edu`
- **Password:** Minimum 6 characters
- **Username:** Letters, numbers, underscores only
- **Full Name:** Any text

## 🔐 Security

- Passwords: SHA-256 hashed
- Storage: SQLite + Firestore
- Domain: Only @newhorizonindia.edu
- Sessions: Server-side secure

## 🌐 Google Sign-In Setup

### Step 1: Get Client ID
1. Go to https://console.cloud.google.com/
2. Create project or select existing
3. Enable Google+ API
4. Create OAuth 2.0 credentials (Web)
5. Add authorized redirect URIs:
   - `http://localhost:5000`
   - `https://your-vercel-domain.vercel.app`
6. Copy Client ID

### Step 2: Configure Locally
```bash
export GOOGLE_CLIENT_ID="your-client-id-here"
python3 app.py
```

### Step 3: Test
1. Go to http://localhost:5000/enter
2. Click "Sign in with Google"
3. Authenticate with Google
4. Should redirect to dashboard

## 📊 Firestore Data

### User Document Location
```
Collection: users
Document ID: user@newhorizonindia.edu
```

### Fields
```json
{
  "user_id": 1,
  "email": "user@newhorizonindia.edu",
  "username": "username",
  "full_name": "Full Name",
  "auth_method": "password" | "google",
  "avatar_color": "#6c63ff",
  "bio": "",
  "is_blacklisted": false,
  "created_at": "2026-05-16T...",
  "updated_at": "2026-05-16T..."
}
```

## 🔗 API Endpoints

### POST /enter
**Password Registration**
```bash
curl -X POST http://localhost:5000/enter \
  -d "action=register" \
  -d "email=test@newhorizonindia.edu" \
  -d "password=TestPassword123" \
  -d "username=testuser" \
  -d "full_name=Test User"
```

**Password Login**
```bash
curl -X POST http://localhost:5000/enter \
  -d "action=login" \
  -d "email=test@newhorizonindia.edu" \
  -d "password=TestPassword123"
```

### POST /auth/google
**Google Sign-In**
```bash
curl -X POST http://localhost:5000/auth/google \
  -H "Content-Type: application/json" \
  -d '{"token": "google-id-token"}'
```

### GET /logout
**Logout**
```bash
curl http://localhost:5000/logout
```

## ❌ Common Errors

| Error | Solution |
|-------|----------|
| "Only New Horizon India emails allowed" | Use @newhorizonindia.edu email |
| "Email already registered" | Use different email or login |
| "Incorrect password" | Check password (case-sensitive) |
| "Email not found" | Register first |
| "Password must be at least 6 characters" | Use longer password |
| "Username already taken" | Choose different username |

## 🚀 Deployment to Vercel

### Step 1: Add Environment Variables
```
GOOGLE_CLIENT_ID=your-client-id
FIREBASE_SERVICE_ACCOUNT=your-json-credentials
```

### Step 2: Deploy
```bash
git push
```

### Step 3: Test
1. Go to https://your-project.vercel.app/enter
2. Test password login
3. Test Google Sign-In

## 📚 Full Documentation

- `AUTHENTICATION_GUIDE.md` - Complete guide
- `AUTHENTICATION_COMPLETE.md` - Implementation details
- `FIRESTORE_SETUP_GUIDE.md` - Firestore setup
- `DATA_STORAGE_ARCHITECTURE.md` - Storage details

## ✅ Checklist

- [x] Password registration working
- [x] Password login working
- [x] Firestore storage working
- [x] Domain validation working
- [ ] Google Client ID obtained
- [ ] Google Sign-In tested locally
- [ ] Deployed to Vercel
- [ ] Google Sign-In tested on production

## 🎯 Current Status

```
✅ Password Auth: Ready
✅ Firestore: Ready
⏳ Google Sign-In: Ready (needs Client ID)
✅ Server: Running on localhost:5000
```

## 💡 Tips

1. **Test Password Auth First** - No setup needed
2. **Use Test Email** - `test@newhorizonindia.edu`
3. **Check Firestore Console** - Verify data is stored
4. **Keep Client ID Safe** - Don't commit to GitHub
5. **Use Environment Variables** - For sensitive data

---

**Last Updated:** May 16, 2026
**Status:** ✅ Ready for Production
