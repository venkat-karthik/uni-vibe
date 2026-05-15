# Quick Reset Guide - Get Started Fresh

## The Issue
The system was checking an old `approved_emails` list from Firestore, which had entries from previous tests. This made it seem like there were domain restrictions.

## The Fix (Already Applied)
✅ Changed the system to check if there are ANY users in the database instead of checking Firestore
✅ Now the first user can sign up with ANY email without restrictions
✅ Added admin endpoints to clear and view approved emails

## How to Reset and Test

### Option 1: Quick Reset (Recommended)
```bash
# 1. Clear the approved emails list
curl -X POST http://localhost:5000/api/admin/clear_approved_emails

# 2. Verify it's cleared
curl http://localhost:5000/api/admin/get_approved_emails

# 3. Restart your server (Ctrl+C and run again)
python3 app.py
```

### Option 2: Complete Fresh Start
```bash
# 1. Delete the database
rm /Users/venkatkarthik/Downloads/univibe_v3/univibe.db

# 2. Clear approved emails
curl -X POST http://localhost:5000/api/admin/clear_approved_emails

# 3. Restart server
python3 app.py
```

## Test the Fix

### Test 1: First User Sign-Up (Should Work ✅)
1. Go to http://localhost:5000/register
2. Sign up with ANY email: `test@gmail.com`
3. Should work without any restrictions
4. You should be redirected to dashboard

### Test 2: Second User Sign-Up (Should Fail ❌)
1. Go to http://localhost:5000/register
2. Try to sign up with different email: `another@yahoo.com`
3. Should get error: "Email another@yahoo.com is not approved"
4. This is CORRECT - only approved emails can sign up

### Test 3: Approved User Sign-Up (Should Work ✅)
1. The first user's email is automatically approved
2. If you want to approve another email, you need to:
   - Have the first user approve it (future feature)
   - Or manually add it to Firestore `approved_emails` collection

## What Changed

### Before
- System checked if `approved_emails` Firestore collection had entries
- If it had old entries, new users couldn't sign up
- Seemed like domain restrictions were still active

### After
- System checks if there are ANY users in SQLite database
- If database is empty → first user can sign up with ANY email
- If database has users → only approved emails can sign up
- Much more reliable and predictable

## Key Points

✅ **No Domain Restrictions**: Accept any email format (gmail.com, yahoo.com, custom, etc.)
✅ **First User is Special**: Can sign up with any email
✅ **Subsequent Users Need Approval**: Their email must be approved
✅ **Auto-Approval**: When a user signs up, their email is automatically approved
✅ **No Organization Restrictions**: Removed all @newhorizonindia.edu restrictions

## Commands Reference

```bash
# Clear all approved emails
curl -X POST http://localhost:5000/api/admin/clear_approved_emails

# View all approved emails
curl http://localhost:5000/api/admin/get_approved_emails

# Example response:
# {
#   "approved_emails": ["test@gmail.com"],
#   "count": 1
# }
```

## Still Having Issues?

1. **Check if server is running**: http://localhost:5000/test (should show "Server is working!")
2. **Check approved emails**: `curl http://localhost:5000/api/admin/get_approved_emails`
3. **Clear and restart**: 
   ```bash
   curl -X POST http://localhost:5000/api/admin/clear_approved_emails
   # Restart server (Ctrl+C and run again)
   ```
4. **Check browser console**: Open DevTools (F12) and look for errors

---

**Status**: ✅ Ready to test
**Last Updated**: May 15, 2026
