# Vercel Deployment Guide - UniVibe

## Overview
This guide explains how to deploy UniVibe to Vercel with proper serverless configuration.

## What Was Fixed

### Issues Resolved
- ✅ 500 Internal Server Error on `/enter` endpoint
- ✅ SQLite database path issues in serverless environment
- ✅ Missing error handling in routes
- ✅ Vercel configuration for Flask apps

### Changes Made
1. **vercel.json** - Serverless configuration
2. **wsgi.py** - WSGI entry point for Vercel
3. **app.py** - Added error handling and /tmp database path
4. **requirements.txt** - Added gunicorn

## Deployment Steps

### 1. Prerequisites
- GitHub account with the repository pushed
- Vercel account (https://vercel.com)
- Firebase project configured

### 2. Deploy to Vercel

#### Option A: Using Vercel CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

#### Option B: Using Vercel Dashboard
1. Go to https://vercel.com/dashboard
2. Click "Add New..." → "Project"
3. Select your GitHub repository
4. Click "Import"
5. Configure environment variables (see below)
6. Click "Deploy"

### 3. Configure Environment Variables

In Vercel Dashboard:
1. Go to Project Settings → Environment Variables
2. Add the following variables:

```
FIREBASE_API_KEY=AIzaSyCDwaBMoEJvJO1NBS-uUzsMTirSSGz8Mcc
FIREBASE_AUTH_DOMAIN=univibe-c85c6.firebaseapp.com
FIREBASE_PROJECT_ID=univibe-c85c6
FIREBASE_STORAGE_BUCKET=univibe-c85c6.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=631710741538
FIREBASE_APP_ID=1:631710741538:web:49b43d32353d97bcc3467b
FIREBASE_MEASUREMENT_ID=G-1CXWWSRM61
FIREBASE_SERVICE_ACCOUNT=<your-service-account-json>
```

### 4. Firebase Service Account Setup

To enable Firestore storage on Vercel:

1. **Get Service Account Key**:
   - Go to Firebase Console → Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Copy the entire JSON content

2. **Add to Vercel**:
   - In Vercel Dashboard, go to Environment Variables
   - Add `FIREBASE_SERVICE_ACCOUNT` variable
   - Paste the entire JSON as the value
   - Make sure it's available in Production environment

### 5. Verify Deployment

After deployment:

1. **Test Home Page**:
   ```
   https://your-app.vercel.app/
   ```

2. **Test Enter Page**:
   ```
   https://your-app.vercel.app/enter
   ```

3. **Test Server**:
   ```
   https://your-app.vercel.app/test
   ```

## How It Works on Vercel

### Serverless Architecture
- **wsgi.py** - Entry point for Vercel
- **vercel.json** - Configuration file
- **/tmp** - Temporary database storage
- **Firestore** - Persistent user data storage

### Database Behavior
- SQLite database is stored in `/tmp` (temporary)
- Data persists during a single deployment
- For persistent data, use Firestore
- Each new deployment gets a fresh database

### Environment Detection
```python
if os.environ.get('VERCEL'):
    DB_PATH = '/tmp/univibe.db'  # Vercel
else:
    DB_PATH = 'univibe.db'       # Local
```

## Troubleshooting

### 500 Error on /enter
**Cause**: Database initialization failure
**Solution**: 
- Check Vercel logs: `vercel logs`
- Ensure database path is writable
- Check Firebase credentials

### Firestore Not Storing Data
**Cause**: Missing service account key
**Solution**:
- Add `FIREBASE_SERVICE_ACCOUNT` environment variable
- Verify JSON format is correct
- Check Firebase project is active

### Database Not Persisting
**Cause**: Using /tmp (temporary storage)
**Solution**:
- This is expected behavior on Vercel
- Use Firestore for persistent data
- SQLite is only for session data

### Build Fails
**Cause**: Missing dependencies
**Solution**:
```bash
# Ensure all dependencies are in requirements.txt
pip freeze > requirements.txt

# Push to GitHub
git add requirements.txt
git commit -m "Update dependencies"
git push origin main

# Redeploy on Vercel
```

## Vercel Logs

To view deployment logs:

```bash
# Using Vercel CLI
vercel logs

# Or in Vercel Dashboard
# Project → Deployments → Select deployment → Logs
```

## Performance Optimization

### Cold Starts
- First request may take 5-10 seconds
- Subsequent requests are faster
- Consider using Vercel Pro for faster cold starts

### Database Optimization
- Use Firestore for persistent data
- SQLite is for temporary session data
- Minimize database queries

## Security Considerations

⚠️ **Important**:

1. **Never commit secrets**:
   - Don't commit `serviceAccountKey.json`
   - Use environment variables only

2. **Firestore Security Rules**:
   ```
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /users/{email} {
         allow read: if request.auth != null;
         allow write: if false;
       }
     }
   }
   ```

3. **HTTPS Only**:
   - Vercel automatically provides HTTPS
   - All traffic is encrypted

## Monitoring

### Vercel Analytics
- Go to Project → Analytics
- Monitor:
  - Response times
  - Error rates
  - Request volume

### Firebase Console
- Monitor Firestore usage
- Check authentication logs
- Review security rules

## Rollback

If deployment has issues:

```bash
# View deployment history
vercel list

# Rollback to previous deployment
vercel rollback
```

## Custom Domain

To add a custom domain:

1. Go to Vercel Dashboard → Project Settings → Domains
2. Add your domain
3. Update DNS records (instructions provided by Vercel)
4. Wait for DNS propagation (up to 48 hours)

## Environment-Specific Configuration

### Local Development
```bash
python3 app.py
# Uses: univibe.db
```

### Vercel Production
```
Uses: /tmp/univibe.db
Firestore: Enabled
```

## Deployment Checklist

- [ ] All code committed and pushed to GitHub
- [ ] vercel.json configured
- [ ] wsgi.py created
- [ ] requirements.txt updated
- [ ] Environment variables set in Vercel
- [ ] Firebase service account key added
- [ ] Firestore security rules configured
- [ ] Test deployment successful
- [ ] All routes responding correctly
- [ ] Firestore storing user data

## Support

For issues:
1. Check Vercel logs: `vercel logs`
2. Check Firebase console
3. Review error messages in browser console
4. Check GitHub issues

## Next Steps

1. Deploy to Vercel
2. Test all features
3. Monitor performance
4. Set up custom domain
5. Configure analytics

---

**Status**: ✅ Ready for Vercel deployment
**Last Updated**: May 16, 2026
