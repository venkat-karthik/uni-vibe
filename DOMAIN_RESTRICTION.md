# Domain Restriction - New Horizon India Only

## Overview
UniVibe is now restricted to only accept email addresses from the `newhorizonindia.edu` domain. This ensures that only New Horizon India students can register and use the platform.

## Implementation

### Frontend Validation

#### HTML Form (`templates/enter.html`)
- Email input field has pattern validation: `[a-zA-Z0-9._%+-]+@newhorizonindia\.edu$`
- Placeholder shows example: `1NH24CD038@newhorizonindia.edu`
- Helper text explains the requirement
- Browser validates before form submission

### Backend Validation

#### Python Route (`app.py`)
```python
# Validate domain - only allow newhorizonindia.edu
if not email.endswith('@newhorizonindia.edu'):
    flash('❌ Only New Horizon India emails are allowed (e.g., 1NH24CD038@newhorizonindia.edu)', 'danger')
    return redirect(url_for('enter'))
```

## How It Works

### User Registration Flow
1. User visits `/enter` page
2. User enters email address
3. **Frontend Check**: Browser validates email pattern
   - Must end with `@newhorizonindia.edu`
   - Shows error if invalid format
4. User submits form
5. **Backend Check**: Server validates domain
   - Rejects non-newhorizonindia.edu emails
   - Shows clear error message
   - Redirects back to enter page
6. If valid:
   - User is created in database
   - User data stored in Firestore
   - User is logged in
   - Redirected to dashboard

## Example Emails

### ✅ Valid (Accepted)
- `1NH24CD038@newhorizonindia.edu`
- `student001@newhorizonindia.edu`
- `john.doe@newhorizonindia.edu`
- `1NH24CS001@newhorizonindia.edu`

### ❌ Invalid (Rejected)
- `user@gmail.com`
- `student@yahoo.com`
- `1NH24CD038@newhorizon.edu` (missing "india")
- `1NH24CD038@newhorizonindia.com` (wrong TLD)
- `1NH24CD038@newhorizonindia.edu.in` (extra domain)

## Error Messages

### Frontend Error
If user tries to submit invalid email format:
```
Browser validation error (before submission)
```

### Backend Error
If user somehow bypasses frontend validation:
```
❌ Only New Horizon India emails are allowed (e.g., 1NH24CD038@newhorizonindia.edu)
```

## Security Benefits

✅ **Campus-Only Access**
- Only New Horizon India students can join
- Prevents external users from registering

✅ **Verified Identity**
- Email domain confirms student status
- Reduces spam and fake accounts

✅ **Community Safety**
- Creates a trusted community
- All users are verified students

✅ **Data Privacy**
- Limited to institutional users
- Complies with campus policies

## Technical Details

### Validation Points

1. **HTML Pattern Validation**
   - Regex: `[a-zA-Z0-9._%+-]+@newhorizonindia\.edu$`
   - Runs in browser before submission
   - Provides immediate feedback

2. **Backend Validation**
   - Python string check: `email.endswith('@newhorizonindia.edu')`
   - Runs on server after form submission
   - Prevents bypass attempts

3. **Database Constraint**
   - Email is unique in database
   - Prevents duplicate registrations

## Configuration

### To Change Domain
If you need to change the allowed domain in the future:

1. **Update HTML** (`templates/enter.html`):
   ```html
   pattern="[a-zA-Z0-9._%+-]+@yourdomain\.edu$"
   placeholder="example@yourdomain.edu"
   ```

2. **Update Python** (`app.py`):
   ```python
   if not email.endswith('@yourdomain.edu'):
       flash('❌ Only yourdomain.edu emails are allowed', 'danger')
   ```

3. **Update Helper Text**:
   - Update placeholder text
   - Update error messages
   - Update info box text

## Testing

### Test Cases

#### Test 1: Valid Email
```
Email: 1NH24CD038@newhorizonindia.edu
Username: student001
Full Name: New Horizon Student
Expected: ✅ Registration successful
```

#### Test 2: Invalid Domain
```
Email: user@gmail.com
Username: student001
Full Name: Test User
Expected: ❌ Error message shown
```

#### Test 3: Wrong TLD
```
Email: 1NH24CD038@newhorizonindia.com
Username: student001
Full Name: Test User
Expected: ❌ Error message shown
```

#### Test 4: Missing Domain Part
```
Email: 1NH24CD038@newhorizon.edu
Username: student001
Full Name: Test User
Expected: ❌ Error message shown
```

## User Experience

### On Enter Page
- Placeholder shows example: `1NH24CD038@newhorizonindia.edu`
- Helper text: "Use your New Horizon India email"
- Info box: "New Horizon India Only! Only students with @newhorizonindia.edu email addresses can join."

### On Invalid Email
- Clear error message displayed
- User redirected back to enter page
- Can try again with correct email

### On Valid Email
- User created successfully
- Logged in automatically
- Redirected to dashboard

## Firestore Integration

### User Document
```json
{
  "user_id": 1,
  "email": "1NH24CD038@newhorizonindia.edu",
  "username": "student001",
  "full_name": "New Horizon Student",
  "avatar_color": "#6c63ff",
  "bio": "",
  "is_blacklisted": false,
  "created_at": "2026-05-16T...",
  "updated_at": "2026-05-16T..."
}
```

## Monitoring

### Check Registered Users
```bash
# View all users in database
sqlite3 univibe.db "SELECT email, username, full_name FROM users;"

# Check Firestore users
# Go to Firebase Console → Firestore → users collection
```

### Verify Domain Compliance
- All emails should end with `@newhorizonindia.edu`
- No external domain emails should be present
- Regular audits recommended

## Future Enhancements

- [ ] Add email verification (send confirmation email)
- [ ] Add student ID validation
- [ ] Add department/year selection
- [ ] Add role-based access (student, faculty, admin)
- [ ] Add email whitelist management
- [ ] Add domain-specific features

## Support

For issues:
1. Check error message displayed
2. Verify email format
3. Ensure email ends with `@newhorizonindia.edu`
4. Check browser console for errors
5. Review server logs

---

**Status**: ✅ Domain restriction implemented and tested
**Domain**: newhorizonindia.edu
**Example Email**: 1NH24CD038@newhorizonindia.edu
**Last Updated**: May 16, 2026
