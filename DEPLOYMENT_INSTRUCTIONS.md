# UniVibe - Deployment Instructions

## Current Status
✅ **All fixes have been implemented and pushed to GitHub**

## What Was Fixed

### The 500 Error Issue
You were getting a 500 error on `https://uni-vibe-b7dj.vercel.app/enter`

**Root Cause**: Flask app wasn't properly configured for Vercel's serverless environment

**Solution**: 
- Added `vercel.json` configuration
- Created `wsgi.py` entry point
- Added error handling to all routes
- Fixed database path for serverless environment

## Files Added/Modified

### New Files
- ✅ `vercel.json` - Vercel serverless configuration
- ✅ `wsgi.py` - WSGI entry point for Vercel
- ✅ `VERCEL_DEPLOYMENT.md` - Comprehensive deployment guide
- ✅ `VERCEL_FIX_SUMMARY.md` - Fix summary

### Modified Files
- ✅ `app.py` - Added error handling and Vercel detection
- ✅ `requirements.txt` - Added gunicorn

## How to Redeploy on Vercel

### Option 1: Automatic Redeploy (Recommended)
1. Go to Vercel Dashboard: https://vercel.com/dashboard
2. Select your project: `uni-vibe`
3. Click the "Redeploy" button
4. Wait for deployment to complete (2-5 minutes)

### Option 2: Manual Redeploy via CLI
```bash
cd /Users/venkatkarthik/Downloads/univibe_v3
vercel --prod
```

### Option 3: Automatic via GitHub
- The code is already pushed to GitHub
- Vercel will automatically redeploy on next push
- Just push any changes to trigger redeploy

## Verify Deployment

After redeployment, test these URLs:

1. **Home Page**:
   ```
   https://uni-vibe-b7dj.vercel.app/
   ```
   Expected: Landing page loads

2. **Enter Page**:
   ```
   https://uni-vibe-b7dj.vercel.app/enter
   ```
   Expected: Login form loads (no 500 error)

3. **Test Endpoint**:
   ```
   https://uni-vibe-b7dj.vercel.app/test
   ```
   Expected: "✅ Server is working!" message

## Environment Variables

Make sure these are set in Vercel Dashboard (Project Settings → Environment Variables):

```
FIREBASE_API_KEY=AIzaSyCDwaBMoEJvJO1NBS-uUzsMTirSSGz8Mcc
FIREBASE_AUTH_DOMAIN=univibe-c85c6.firebaseapp.com
FIREBASE_PROJECT_ID=univibe-c85c6
FIREBASE_STORAGE_BUCKET=univibe-c85c6.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=631710741538
FIREBASE_APP_ID=1:631710741538:web:49b43d32353d97bcc3467b
FIREBASE_MEASUREMENT_ID=G-1CXWWSRM61
```

### Optional: Firestore Backend Storage
To enable Firestore data storage on Vercel:

1. Get Firebase Service Account Key:
   - Go to Firebase Console → Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Copy the entire JSON

2. Add to Vercel:
   - In Vercel Dashboard, add environment variable
   - Name: `FIREBASE_SERVICE_ACCOUNT`
   - Value: Paste the entire JSON
   - Make sure it's available in Production

## How It Works

### Local Development
```bash
python3 app.py
# Uses: univibe.db (local SQLite)
# Database: Persistent
```

### Vercel Production
```
Uses: /tmp/univibe.db (temporary)
Database: Fresh on each deployment
Firestore: Persistent user data storage
```

## Database Behavior

### SQLite on Vercel
- Stored in `/tmp` (temporary storage)
- Persists during a single deployment
- Fresh database on each new deployment
- Good for session data

### Firestore
- Persistent across deployments
- Stores user profiles and data
- Requires service account key
- Recommended for production

## Troubleshooting

### Still Getting 500 Error?
1. Check Vercel logs:
   ```bash
   vercel logs
   ```

2. Verify environment variables are set

3. Check Firebase credentials

4. Try manual redeploy

### Database Issues?
- This is expected on Vercel (temporary storage)
- Use Firestore for persistent data
- Check Firestore console for user data

### Firestore Not Storing Data?
- Add `FIREBASE_SERVICE_ACCOUNT` environment variable
- Verify Firebase project is active
- Check Firestore security rules

## Performance Tips

### Cold Starts
- First request: 5-10 seconds
- Subsequent requests: <1 second
- Consider Vercel Pro for faster cold starts

### Optimization
- Use Firestore for persistent data
- Minimize database queries
- Cache frequently accessed data

## Monitoring

### Vercel Dashboard
- Project → Analytics
- Monitor response times and errors

### Firebase Console
- Monitor Firestore usage
- Check authentication logs

## Next Steps

1. ✅ Code is fixed and pushed
2. 🔄 Redeploy on Vercel
3. 🧪 Test all endpoints
4. 📊 Monitor performance
5. 🎉 Done!

## Quick Checklist

- [ ] Code pushed to GitHub
- [ ] Vercel redeploy triggered
- [ ] Environment variables set
- [ ] Home page loads
- [ ] Enter page loads (no 500 error)
- [ ] Test endpoint works
- [ ] Can create account
- [ ] Firestore storing data

## Support

For issues:
1. Check Vercel logs: `vercel logs`
2. Check Firebase console
3. Review error messages
4. Check GitHub issues

## Documentation

For more details, see:
- `VERCEL_DEPLOYMENT.md` - Comprehensive deployment guide
- `VERCEL_FIX_SUMMARY.md` - Detailed fix explanation
- `SETUP_COMPLETE.md` - Full setup guide
- `QUICK_START.md` - Quick reference

---

**Status**: ✅ Ready for deployment
**Last Updated**: May 16, 2026
**Repository**: https://github.com/venkat-karthik/uni-vibe
