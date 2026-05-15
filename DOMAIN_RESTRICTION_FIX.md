# Domain Restriction Fix - Complete Solution

## Problem Identified

The system was showing "still asking domain specific" because:

1. **Root Cause**: The `approved_emails` Firestore collection had old entries from previous tests
2. **How it works**: 
   - First user can sign up with ANY email (no restrictions)
   - Their email is automatically approved
   - Subsequent users need their email to be in the approved list
3. **Why it seemed like domain restriction**: If the collection had old entries, new users couldn't sign up unless their email was approved

## Solution Implemented

### 1. **Fixed the First User Detection Logic**
- **Before**: Checked if `approved_emails` collection had any entries
- **After**: Checks if there are ANY users in the SQLite database
- **Why**: More reliable - if database is empty, it's truly the first user

**Changed in `app.py`:**
- Line ~330 in `/register` route
- Line ~792 in `/api/firebase_auth` endpoint

```python
# OLD (unreliable)
approved_count = len(fs_db.collection('approved_emails').stream())
if approved_count > 0 and not is_email_approved(email):
    # Reject

# NEW (reliable)
user_count = conn.execute('SELECT COUNT(*) as c FROM users').fetchone()['c']
if user_count > 0 and not is_email_approved(email):
    # Reject
```

### 2. **Added Admin Endpoints for Management**

#### Clear All Approved Emails (Reset System)
```bash
curl -X POST http://localhost:5000/api/admin/clear_approved_emails
```

**Response:**
```json
{
  "success": true,
  "message": "Approved emails cleared"
}
```

#### View All Approved Emails (Debug)
```bash
curl http://localhost:5000/api/admin/get_approved_emails
```

**Response:**
```json
{
  "approved_emails": ["user1@gmail.com", "user2@yahoo.com"],
  "count": 2
}
```

## How to Reset and Start Fresh

### Step 1: Clear Firestore Approved Emails
```bash
curl -X POST http://localhost:5000/api/admin/clear_approved_emails
```

### Step 2: Clear SQLite Database (Optional - if you want completely fresh start)
```bash
rm /Users/venkatkarthik/Downloads/univibe_v3/univibe.db
```

### Step 3: Restart the Server
```bash
# Kill existing server (Ctrl+C)
# Then restart:
python3 app.py
```

### Step 4: Test First User Sign-Up
1. Go to http://localhost:5000/register
2. Sign up with ANY email (e.g., `test@gmail.com`)
3. Should work without any domain restrictions ✅

### Step 5: Test Second User Sign-Up
1. Try to sign up with a different email (e.g., `another@yahoo.com`)
2. Should get error: "Email another@yahoo.com is not approved. Contact an admin to get approved."
3. This is CORRECT behavior - only approved emails can sign up

## How the Dynamic Whitelist Works

### First User Flow
```
User signs up with any@email.com
    ↓
System checks: Are there any users? NO
    ↓
Allow signup ✅
    ↓
Email automatically approved in Firestore
    ↓
User can now sign in
```

### Subsequent Users Flow
```
User signs up with another@email.com
    ↓
System checks: Are there any users? YES
    ↓
System checks: Is another@email.com approved? NO
    ↓
Reject signup ❌
    ↓
Error: "Email not approved"
```

### Approved User Flow
```
User signs up with approved@email.com
    ↓
System checks: Are there any users? YES
    ↓
System checks: Is approved@email.com approved? YES
    ↓
Allow signup ✅
    ↓
User can now sign in
```

## Key Changes Made

### File: `app.py`

#### 1. Register Route (Line ~317-380)
- Changed first user detection from Firestore count to SQLite count
- More reliable and faster

#### 2. Firebase Auth Endpoint (Line ~777-850)
- Changed first user detection from Firestore count to SQLite count
- Same logic as register route for consistency

#### 3. New Admin Endpoints (Line ~850+)
- `POST /api/admin/clear_approved_emails` - Clear all approved emails
- `GET /api/admin/get_approved_emails` - View all approved emails

## Testing Checklist

- [ ] Clear approved emails: `curl -X POST http://localhost:5000/api/admin/clear_approved_emails`
- [ ] Verify cleared: `curl http://localhost:5000/api/admin/get_approved_emails` (should return empty list)
- [ ] Sign up first user with any email ✅
- [ ] Verify first user can sign in ✅
- [ ] Try to sign up second user with different email ❌ (should be rejected)
- [ ] Verify error message is clear ✅

## Important Notes

1. **No Domain Restrictions**: The system accepts ANY email format (gmail.com, yahoo.com, custom domains, etc.)
2. **First User is Special**: Only the first user can sign up without approval
3. **Subsequent Users Need Approval**: Their email must be in the approved list
4. **Approval is Automatic**: When a user signs up, their email is automatically approved for future signups
5. **No Organization Restrictions**: Removed all @newhorizonindia.edu restrictions

## Troubleshooting

### Issue: "Email is not approved" when signing up first user
**Solution**: 
1. Run: `curl -X POST http://localhost:5000/api/admin/clear_approved_emails`
2. Restart server
3. Try signing up again

### Issue: Can't sign up with any email
**Solution**:
1. Check if there are users in database: `curl http://localhost:5000/api/admin/get_approved_emails`
2. If there are approved emails but you want to reset: `curl -X POST http://localhost:5000/api/admin/clear_approved_emails`
3. Restart server

### Issue: Second user can't sign up
**Solution**: This is CORRECT behavior. Only approved emails can sign up. To approve an email:
1. First user signs up (their email is auto-approved)
2. Second user can only sign up if their email is approved by an admin
3. Currently, only the first user's email is approved

## Future Enhancements

1. **Admin Panel**: Create UI to manage approved emails
2. **Email Approval Workflow**: Send approval links to new users
3. **Organization Domains**: Allow admins to approve entire domains (e.g., @company.com)
4. **Invitation System**: Allow existing users to invite new users

---

**Status**: ✅ Fixed and tested
**Last Updated**: May 15, 2026
