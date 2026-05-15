// Firebase Authentication Module - Google Sign-In/Sign-Up
import { 
  signInWithPopup,
  GoogleAuthProvider,
  onAuthStateChanged,
  signOut
} from "https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js";
import { 
  collection, 
  doc, 
  setDoc, 
  getDoc,
  query,
  where,
  getDocs
} from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";

console.log("🔄 Loading Firebase Auth module...");

// Wait for Firebase to be ready
async function waitForFirebase(maxAttempts = 50) {
  for (let i = 0; i < maxAttempts; i++) {
    if (window.firebaseAuth && window.firebaseDb) {
      console.log(`✅ Firebase ready after ${i} attempts`);
      return true;
    }
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  console.error("❌ Firebase failed to initialize after 5 seconds");
  return false;
}

// Google Sign-In/Sign-Up
async function signInWithGoogle() {
  try {
    console.log("🔐 Google Sign-In initiated...");
    
    if (!await waitForFirebase()) {
      throw new Error("Firebase not initialized");
    }

    const provider = new GoogleAuthProvider();
    const userCredential = await signInWithPopup(window.firebaseAuth, provider);
    const user = userCredential.user;
    console.log("✅ Google Sign-In successful:", user.email);

    // Check if user exists in Firestore
    const userDoc = await getDoc(doc(window.firebaseDb, 'users', user.uid));
    
    if (!userDoc.exists()) {
      // New user - create document
      const colors = ['#6c63ff','#ff6584','#43d9ad','#f7c948','#ff8c42','#4ecdc4','#a29bfe','#fd79a8'];
      const color = colors[Math.floor(Math.random() * colors.length)];
      const username = user.email.split('@')[0];

      const userData = {
        uid: user.uid,
        email: user.email.toLowerCase(),
        full_name: user.displayName || username,
        username: username,
        avatar_color: color,
        bio: '',
        is_blacklisted: false,
        provider: 'google',
        photoURL: user.photoURL || '',
        created_at: new Date(),
        updated_at: new Date(),
        profile_complete: false,
        quiz_completed: false
      };

      await setDoc(doc(window.firebaseDb, 'users', user.uid), userData);
      console.log("✅ New user created in Firestore");
    } else {
      // Existing user - update last login
      await setDoc(doc(window.firebaseDb, 'users', user.uid), {
        updated_at: new Date()
      }, { merge: true });
      console.log("✅ User updated in Firestore");
    }

    // Send to backend to create session
    const response = await fetch('/api/firebase_auth', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        uid: user.uid,
        email: user.email,
        displayName: user.displayName || user.email.split('@')[0],
        photoURL: user.photoURL || '',
        provider: 'google'
      })
    });

    const result = await response.json();
    
    if (!response.ok) {
      const errorMsg = result.error || response.statusText || 'Unknown error';
      throw new Error(`Backend error: ${errorMsg}`);
    }

    console.log("✅ Google auth successful:", result.message);
    
    // Redirect to dashboard
    window.location.href = '/dashboard';
    return { success: true, user: user, message: result.message };

  } catch (error) {
    console.error("❌ Google Sign-In failed:", error.message);
    alert('Sign-in failed: ' + error.message);
    return { success: false, error: error.message };
  }
}

// Logout
async function logout() {
  try {
    console.log("🔐 Logout initiated...");
    
    if (!await waitForFirebase()) {
      throw new Error("Firebase not initialized");
    }

    await signOut(window.firebaseAuth);
    console.log("✅ User logged out");
    return { success: true };

  } catch (error) {
    console.error("❌ Logout failed:", error.message);
    return { success: false, error: error.message };
  }
}

// Monitor auth state
function monitorAuthState(callback) {
  if (!window.firebaseAuth) {
    console.error("❌ Firebase Auth not initialized");
    return;
  }

  onAuthStateChanged(window.firebaseAuth, async (user) => {
    if (user) {
      console.log("✅ User is signed in:", user.uid);
      const userDoc = await getDoc(doc(window.firebaseDb, 'users', user.uid));
      callback({ authenticated: true, user: user, userData: userDoc.data() });
    } else {
      console.log("❌ User is signed out");
      callback({ authenticated: false, user: null });
    }
  });
}

// Export functions
window.firebaseAuthModule = {
  signInWithGoogle,
  logout,
  monitorAuthState,
  waitForFirebase
};

export {
  signInWithGoogle,
  logout,
  monitorAuthState,
  waitForFirebase
};

console.log("✅ Firebase Auth module loaded");
