# UniVibe Data Storage Architecture

## Overview
User data is stored in a **dual-storage system** for redundancy and cloud persistence:

```
┌─────────────────────────────────────────────────────────────┐
│                    User Registration                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                    ┌────▼────┐
                    │ Validate │
                    │  Email   │
                    └────┬────┘
                         │
        ┌────────────────┴────────────────┐
        │                                 │
   ┌────▼─────┐                    ┌─────▼──────┐
   │  SQLite  │                    │ Firestore  │
   │ (Primary)│                    │ (Cloud)    │
   └──────────┘                    └────────────┘
```

## Storage Details

### 1. SQLite Database (`univibe.db`)
**Location:** Local file system
- **Local Development:** `univibe.db` in project root
- **Vercel Production:** `/tmp/univibe.db` (temporary, recreated on each deployment)

**Tables:**
- `users` - User profiles and account info
- `quiz_answers` - Quiz responses
- `connections` - User connections/matches
- `messages` - Direct messages
- `notifications` - User notifications
- `reviews` - User reviews/ratings
- `blacklist` - Blacklisted users

**User Data Stored:**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT,
    full_name TEXT,
    bio TEXT,
    avatar_color TEXT,
    is_blacklisted INTEGER,
    is_demo INTEGER,
    created_at TEXT
);
```

### 2. Firestore (Google Cloud)
**Location:** Cloud Firestore database
**Collection:** `users`
**Document ID:** User's email address

**User Data Stored:**
```json
{
  "user_id": 1,
  "email": "1NH24CD038@newhorizonindia.edu",
  "username": "student123",
  "full_name": "Student Name",
  "avatar_color": "#6c63ff",
  "bio": "",
  "is_blacklisted": false,
  "created_at": "2026-05-16T...",
  "updated_at": "2026-05-16T..."
}
```

## Registration Flow

### Step 1: Validation
```python
# Check email format and domain
if not email.endswith('@newhorizonindia.edu'):
    flash('❌ Only New Horizon India emails allowed')
    return
```

### Step 2: SQLite Storage
```python
# Insert into SQLite
conn.execute(
    'INSERT INTO users (username, email, password, full_name, avatar_color) VALUES (?,?,?,?,?)',
    (username, email, hashed_password, full_name, color)
)
conn.commit()
```

### Step 3: Firestore Storage (if available)
```python
if db:  # If Firebase is initialized
    user_data = {
        'user_id': user_id,
        'email': email,
        'username': username,
        'full_name': full_name,
        'avatar_color': color,
        'bio': '',
        'is_blacklisted': False,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }
    db.collection('users').document(email).set(user_data)
    print(f"✅ User stored in Firestore: {email}")
```

### Step 4: Session Management
```python
session['user_id'] = user_id
session['username'] = username
session['full_name'] = full_name
session['email'] = email
session['avatar_color'] = color
```

## Current Status

### ✅ Working
- SQLite storage: **Always active**
- User registration: **Fully functional**
- Session management: **Working**
- Demo users: **5 demo users with quiz answers**

### ⚠️ Firestore Status
- **Currently Disabled** (no Firebase credentials available)
- **When Enabled:** Requires `serviceAccountKey.json` or `FIREBASE_SERVICE_ACCOUNT` environment variable
- **Fallback:** App works fine without Firestore - SQLite is the primary storage

## Enabling Firestore Storage

To enable Firestore cloud storage:

### Option 1: Local Development
1. Download `serviceAccountKey.json` from Firebase Console
2. Place it in the project root directory
3. Restart the server

### Option 2: Vercel Deployment
1. Add `FIREBASE_SERVICE_ACCOUNT` environment variable in Vercel settings
2. Set value to the JSON content of your service account key
3. Redeploy

## Data Persistence

### Local Development
- SQLite: ✅ Persistent (stored in `univibe.db`)
- Firestore: ✅ Persistent (if enabled)

### Vercel Production
- SQLite: ⚠️ Temporary (lost on redeploy - use Firestore for persistence)
- Firestore: ✅ Persistent (recommended for production)

## Recommendations

1. **For Development:** SQLite is sufficient
2. **For Production:** Enable Firestore for data persistence across deployments
3. **For Backup:** Both storages provide redundancy
4. **For Scaling:** Firestore handles better than SQLite for high traffic

## Demo Users
5 demo users are automatically created on database initialization:
- `demo_coder@newhorizonindia.edu`
- `demo_designer@newhorizonindia.edu`
- `demo_gamer@newhorizonindia.edu`
- `demo_student@newhorizonindia.edu`
- `demo_entrepreneur@newhorizonindia.edu`

Each demo user has pre-filled quiz answers for testing the matching algorithm.
