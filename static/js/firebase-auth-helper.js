// Firebase Authentication Helper Functions
// Provides clean, reusable functions for authentication

import { 
  auth, 
  db,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  signInWithPopup,
  googleProvider
} from './firebase-init.js';

import { doc, setDoc, getDoc } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";

// ─── EMAIL & PASSWORD AUTHENTICATION ───────────────────────────────────────

/**
 * Register user with email and password
 * @param {string} email - User email
 * @param {string} password - User password
 * @param {object} userData - Additional user data (username, full_name, etc.)
 * @returns {Promise} User credential
 */
export async function registerWithEmail(email, password, userData) {
  try {
    // Create user in Firebase Auth
    const userCredential = await createUserWithEmailAndPassword(auth, email, password);
    const user = userCredential.user;
    
    console.log("✅ User registered in Firebase Auth:", user.uid);
    
    // Store user data in Firestore
    await setDoc(doc(db, "users", email), {
      uid: user.uid,
      email: email,
      username: userData.username || email.split('@')[0],
      full_name: userData.full_name || '',
      avatar_color: userData.avatar_color || '#6c63ff',
      bio: userData.bio || '',
      auth_method: 'email',
      created_at: new Date(),
      updated_at: new Date()
    });
    
    console.log("✅ User data stored in Firestore");
    
    return { success: true, user: user };
  } catch (error) {
    console.error("❌ Registration error:", error.message);
    return { success: false, error: error.message };
  }
}

/**
 * Login user with email and password
 * @param {string} email - User email
 * @param {string} password - User password
 * @returns {Promise} User credential
 */
export async function loginWithEmail(email, password) {
  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    const user = userCredential.user;
    
    console.log("✅ User logged in:", user.uid);
    
    return { success: true, user: user };
  } catch (error) {
    console.error("❌ Login error:", error.message);
    return { success: false, error: error.message };
  }
}

// ─── GOOGLE AUTHENTICATION ─────────────────────────────────────────────────

/**
 * Sign in with Google
 * @returns {Promise} User credential
 */
export async function signInWithGoogle() {
  try {
    const result = await signInWithPopup(auth, googleProvider);
    const user = result.user;
    
    console.log("✅ User signed in with Google:", user.uid);
    
    // Check if user exists in Firestore
    const userDoc = await getDoc(doc(db, "users", user.email));
    
    if (!userDoc.exists()) {
      // New user - create profile
      await setDoc(doc(db, "users", user.email), {
        uid: user.uid,
        email: user.email,
        username: user.displayName?.split(' ')[0] || user.email.split('@')[0],
        full_name: user.displayName || '',
        avatar_color: '#6c63ff',
        bio: '',
        auth_method: 'google',
        google_uid: user.uid,
        photo_url: user.photoURL || '',
        created_at: new Date(),
        updated_at: new Date()
      });
      
      console.log("✅ New Google user created in Firestore");
    } else {
      console.log("✅ Existing Google user logged in");
    }
    
    return { success: true, user: user, isNewUser: !userDoc.exists() };
  } catch (error) {
    console.error("❌ Google sign-in error:", error.message);
    return { success: false, error: error.message };
  }
}

// ─── SESSION MANAGEMENT ────────────────────────────────────────────────────

/**
 * Get current authenticated user
 * @returns {Promise} Current user or null
 */
export function getCurrentUser() {
  return new Promise((resolve, reject) => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      unsubscribe();
      resolve(user);
    }, reject);
  });
}

/**
 * Listen to authentication state changes
 * @param {function} callback - Function to call when auth state changes
 * @returns {function} Unsubscribe function
 */
export function onAuthChange(callback) {
  return onAuthStateChanged(auth, callback);
}

/**
 * Logout user
 * @returns {Promise} Logout result
 */
export async function logoutUser() {
  try {
    await signOut(auth);
    console.log("✅ User logged out");
    return { success: true };
  } catch (error) {
    console.error("❌ Logout error:", error.message);
    return { success: false, error: error.message };
  }
}

// ─── USER DATA MANAGEMENT ──────────────────────────────────────────────────

/**
 * Get user profile from Firestore
 * @param {string} email - User email
 * @returns {Promise} User profile data
 */
export async function getUserProfile(email) {
  try {
    const userDoc = await getDoc(doc(db, "users", email));
    if (userDoc.exists()) {
      return { success: true, data: userDoc.data() };
    } else {
      return { success: false, error: "User not found" };
    }
  } catch (error) {
    console.error("❌ Error getting user profile:", error.message);
    return { success: false, error: error.message };
  }
}

/**
 * Update user profile
 * @param {string} email - User email
 * @param {object} updates - Fields to update
 * @returns {Promise} Update result
 */
export async function updateUserProfile(email, updates) {
  try {
    await setDoc(doc(db, "users", email), {
      ...updates,
      updated_at: new Date()
    }, { merge: true });
    
    console.log("✅ User profile updated");
    return { success: true };
  } catch (error) {
    console.error("❌ Error updating profile:", error.message);
    return { success: false, error: error.message };
  }
}

// ─── ERROR HANDLING ────────────────────────────────────────────────────────

/**
 * Get user-friendly error message
 * @param {string} errorCode - Firebase error code
 * @returns {string} User-friendly message
 */
export function getErrorMessage(errorCode) {
  const errorMessages = {
    'auth/email-already-in-use': 'Email already registered. Please login instead.',
    'auth/invalid-email': 'Invalid email address.',
    'auth/weak-password': 'Password should be at least 6 characters.',
    'auth/user-not-found': 'Email not found. Please register first.',
    'auth/wrong-password': 'Incorrect password. Please try again.',
    'auth/too-many-requests': 'Too many login attempts. Please try again later.',
    'auth/account-exists-with-different-credential': 'Account exists with different sign-in method.',
    'auth/popup-closed-by-user': 'Google sign-in was cancelled.',
    'auth/network-request-failed': 'Network error. Please check your connection.'
  };
  
  return errorMessages[errorCode] || 'An error occurred. Please try again.';
}

// ─── VALIDATION ────────────────────────────────────────────────────────────

/**
 * Validate email format and domain
 * @param {string} email - Email to validate
 * @returns {object} Validation result
 */
export function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  
  if (!emailRegex.test(email)) {
    return { valid: false, error: 'Invalid email format' };
  }
  
  if (!email.endsWith('@newhorizonindia.edu')) {
    return { valid: false, error: 'Only @newhorizonindia.edu emails allowed' };
  }
  
  return { valid: true };
}

/**
 * Validate password
 * @param {string} password - Password to validate
 * @returns {object} Validation result
 */
export function validatePassword(password) {
  if (password.length < 6) {
    return { valid: false, error: 'Password must be at least 6 characters' };
  }
  
  return { valid: true };
}

/**
 * Validate username
 * @param {string} username - Username to validate
 * @returns {object} Validation result
 */
export function validateUsername(username) {
  const usernameRegex = /^[a-zA-Z0-9_]+$/;
  
  if (!usernameRegex.test(username)) {
    return { valid: false, error: 'Username can only contain letters, numbers, and underscores' };
  }
  
  if (username.length < 3) {
    return { valid: false, error: 'Username must be at least 3 characters' };
  }
  
  return { valid: true };
}
