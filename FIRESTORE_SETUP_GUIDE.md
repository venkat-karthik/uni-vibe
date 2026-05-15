# Firestore Setup Guide

## Step 1: Get Firebase Service Account Key

### From Firebase Console:
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: **univibe-c85c6**
3. Click **Settings** (gear icon) → **Project Settings**
4. Go to **Service Accounts** tab
5. Click **Generate New Private Key**
6. A JSON file will download - this is your `serviceAccountKey.json`

## Step 2: Local Development Setup

### Option A: Using Service Account Key File (Recommended for Local)

1. **Download the key** from Firebase Console (see Step 1)
2. **Place the file** in your project root:
   ```
   /Users/venkatkarthik/Downloads/univibe_v3/serviceAccountKey.json
   ```
3. **Restart the Flask server**
4. The app will automatically detect and use the credentials

### Option B: Using Environment Variable (Recommended for Vercel)

1. **Get the service account key** (see Step 1)
2. **Convert to environment variable:**
   - Open the downloaded JSON file
   - Copy the entire content
   - Create environment variable: `FIREBASE_SERVICE_ACCOUNT`
   - Set value to the JSON content

## Step 3: Verify Firestore Connection

After placing the credentials, restart the server and check:

```bash
python3 app.py
```

You should see:
```
🔄 Loading Firebase credentials from file...
✅ Firebase initialized with file credentials
✅ Firestore initialized
```

## Step 4: Test User Registration with Firestore

Once Firestore is enabled, new user registrations will automatically:
1. Save to SQLite (local database)
2. Save to Firestore (cloud database)

You'll see in the logs:
```
✅ User stored in Firestore: user@newhorizonindia.edu
```

## Firestore Data Structure

When a user registers, their data is stored in Firestore at:
```
Collection: users
Document ID: user@newhorizonindia.edu
```

Document content:
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

## Vercel Deployment with Firestore

### Step 1: Get Service Account Key
Follow Step 1 above to download the JSON file

### Step 2: Add to Vercel Environment Variables
1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Go to **Settings** → **Environment Variables**
4. Add new variable:
   - **Name:** `FIREBASE_SERVICE_ACCOUNT`
   - **Value:** Paste the entire JSON content from the service account key
5. Click **Save**

### Step 3: Redeploy
```bash
git push
```
Vercel will automatically redeploy with the new environment variable.

## Troubleshooting

### Issue: "Service account key not found"
**Solution:** 
- Make sure `serviceAccountKey.json` is in the project root
- Or set `FIREBASE_SERVICE_ACCOUNT` environment variable
- Restart the server

### Issue: "Firebase initialization error"
**Solution:**
- Check that the JSON file is valid
- Verify the project ID matches your Firebase project
- Check that Firestore is enabled in Firebase Console

### Issue: "Firestore initialization warning"
**Solution:**
- Ensure Firebase Admin SDK is initialized first
- Check internet connection
- Verify Firebase credentials are correct

## Checking Firestore Data

### Via Firebase Console:
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Go to **Firestore Database**
4. View the `users` collection
5. See all registered users and their data

### Via Python Script:
```python
from firebase_admin import firestore

db = firestore.client()
users = db.collection('users').stream()

for user in users:
    print(f"Email: {user.id}")
    print(f"Data: {user.to_dict()}")
```

## Security Rules (Optional)

To restrict Firestore access, set security rules in Firebase Console:

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

## Next Steps

1. ✅ Download service account key from Firebase Console
2. ✅ Place `serviceAccountKey.json` in project root OR set environment variable
3. ✅ Restart the Flask server
4. ✅ Test by registering a new user
5. ✅ Verify data appears in Firestore Console
6. ✅ For production, deploy to Vercel with environment variable
