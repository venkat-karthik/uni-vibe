# 📧 New Horizon India Email Integration Guide

## Quick Reference

### Organization Email Domain
```
@newhorizonindia.edu
```

### Valid Email Examples
- ✅ `john.doe@newhorizonindia.edu`
- ✅ `student123@newhorizonindia.edu`
- ✅ `faculty.name@newhorizonindia.edu`
- ✅ `admin@newhorizonindia.edu`

### Invalid Email Examples
- ❌ `john.doe@gmail.com`
- ❌ `student@griet.ac.in`
- ❌ `user@university.edu`
- ❌ `john.doe@newhorizon.edu` (missing "india")

---

## 🔐 Email Validation Process

### 1. Frontend Validation (Real-time)
When user types email in login/register form:
- ✅ Checks if email ends with `@newhorizonindia.edu`
- ✅ Shows green checkmark if valid
- ✅ Shows red error if invalid
- ✅ Disables submit button if invalid

### 2. Backend Validation (Server-side)
When form is submitted:
- ✅ Python validates email domain
- ✅ Rejects if not `@newhorizonindia.edu`
- ✅ Shows error message to user
- ✅ Prevents account creation/login

### 3. Firebase Validation
- ✅ Firebase Authentication verifies email
- ✅ Sends verification email to user
- ✅ Confirms email ownership

---

## 🚀 Getting Started

### For New Users

1. **Register:**
   - Go to: `http://localhost:5000/register`
   - Enter your New Horizon India email
   - Create password (min 6 characters)
   - Add full name and username
   - Click "Create My Account"

2. **Login:**
   - Go to: `http://localhost:5000/login`
   - Enter your New Horizon India email
   - Enter your password
   - Click "Login"

### Email Format
```
firstname.lastname@newhorizonindia.edu
```

---

## 🔧 Configuration

### Backend Configuration (Python)
File: `app.py`
```python
ALLOWED_EMAIL_DOMAIN = "newhorizonindia.edu"
```

### Frontend Configuration (JavaScript)
File: `templates/login.html` and `templates/register.html`
```javascript
const ALLOWED_EMAIL_DOMAIN = 'newhorizonindia.edu';
```

### Environment Configuration
File: `.env`
```
ALLOWED_EMAIL_DOMAIN=newhorizonindia.edu
```

---

## 📋 Validation Rules

### Email Must:
- ✅ End with `@newhorizonindia.edu`
- ✅ Be a valid email format
- ✅ Not already be registered
- ✅ Be verified by Firebase

### Email Cannot:
- ❌ Be from other domains
- ❌ Be empty or invalid format
- ❌ Already exist in database
- ❌ Be unverified

---

## 🎯 Use Cases

### Student Registration
```
Email: student.name@newhorizonindia.edu
Password: SecurePassword123
Full Name: Student Name
Username: studentname
```

### Faculty Registration
```
Email: faculty.name@newhorizonindia.edu
Password: SecurePassword123
Full Name: Faculty Name
Username: facultyname
```

### Admin Registration
```
Email: admin@newhorizonindia.edu
Password: SecurePassword123
Full Name: Admin Name
Username: adminname
```

---

## 🔍 Troubleshooting

### Problem: "Email must end with @newhorizonindia.edu"

**Cause:** Using wrong email domain

**Solution:** 
- Use your New Horizon India email
- Check spelling: `newhorizonindia.edu`
- Not: `newhorizon.edu` or `newhorizonindia.com`

### Problem: "Email already exists"

**Cause:** Account already created with this email

**Solution:**
- Use a different email address
- Or login with existing account
- Contact admin if you forgot password

### Problem: Email validation not working

**Cause:** JavaScript not loaded or browser cache

**Solution:**
1. Clear browser cache (Ctrl+Shift+Delete)
2. Refresh page (Ctrl+R)
3. Check browser console for errors
4. Try different browser

---

## 📞 Support

### For Email Issues:
1. Verify you're using `@newhorizonindia.edu` domain
2. Check email spelling
3. Ensure email is active in organization
4. Contact IT support if email not working

### For Account Issues:
1. Check if account already exists
2. Verify password is correct
3. Clear browser cache
4. Try incognito/private browsing
5. Contact admin for help

---

## 🔐 Security Notes

### Password Requirements
- Minimum 6 characters
- Should be strong and unique
- Don't share with anyone
- Change regularly

### Email Verification
- Check your email for verification link
- Click link to verify account
- May take a few minutes to arrive
- Check spam folder if not found

### Account Security
- Never share your password
- Logout when done
- Use strong passwords
- Report suspicious activity

---

## 📊 Statistics

### Supported Email Domains
- ✅ `@newhorizonindia.edu` - Primary domain

### Unsupported Domains
- ❌ `@gmail.com`
- ❌ `@yahoo.com`
- ❌ `@outlook.com`
- ❌ `@griet.ac.in`
- ❌ Any other domain

---

## 🎓 Organization Information

### Organization
- **Name:** New Horizon India
- **Email Domain:** `newhorizonindia.edu`
- **Type:** Educational Institution
- **Location:** India

### Contact
- **Website:** https://newhorizonindia.edu
- **Email:** info@newhorizonindia.edu
- **Support:** support@newhorizonindia.edu

---

## ✅ Checklist

Before registering, ensure you have:
- ✅ Valid New Horizon India email
- ✅ Email access (to verify account)
- ✅ Strong password ready
- ✅ Full name
- ✅ Desired username

---

## 📝 FAQ

**Q: Can I use a personal email?**  
A: No, only `@newhorizonindia.edu` emails are allowed.

**Q: What if I don't have an organization email?**  
A: Contact your organization's IT department to get one.

**Q: Can I change my email later?**  
A: Contact admin to update your email address.

**Q: What if I forgot my password?**  
A: Use the "Forgot Password" link on login page.

**Q: How long does email verification take?**  
A: Usually 1-5 minutes. Check spam folder if delayed.

---

## 🚀 Next Steps

1. ✅ Get your New Horizon India email
2. ✅ Go to registration page
3. ✅ Enter your email and create account
4. ✅ Verify your email
5. ✅ Login and start using UniVibe!

---

**Last Updated:** May 15, 2026  
**Organization Domain:** newhorizonindia.edu  
**Status:** ✅ ACTIVE

