// Firebase Authentication Enhanced
console.log("🔄 Loading Firebase Auth Enhanced module...");

window.firebaseAuthEnhanced = {
  waitForFirebase: async function(maxAttempts = 100) {
    let attempts = 0;
    while (attempts < maxAttempts) {
      if (window.firebaseAuth && window.firebaseDb) {
        console.log("✅ Firebase ready after " + attempts + " attempts");
        return true;
      }
      await new Promise(resolve => setTimeout(resolve, 100));
      attempts++;
    }
    console.error("❌ Firebase not initialized after " + maxAttempts + " attempts");
    return false;
  },

  signInWithGoogle: async function() {
    try {
      console.log("🔐 Google Sign-In initiated...");
      const isReady = await this.waitForFirebase();
      if (!isReady) {
        console.error("❌ Firebase not initialized");
        return { success: false, error: "Firebase not initialized. Please refresh the page." };
      }

      if (!window.firebaseAuth) {
        console.error("❌ Firebase Auth not available");
        return { success: false, error: "Firebase Auth not available" };
      }

      console.log("✅ Firebase Auth available, creating provider...");
      const provider = new firebase.auth.GoogleAuthProvider();
      provider.setCustomParameters({ hd: 'newhorizonindia.edu' });

      console.log("🔄 Opening Google Sign-In popup...");
      const result = await window.firebaseAuth.signInWithPopup(provider);
      const user = result.user;

      console.log("✅ Google Sign-In successful:", user.email);

      if (!user.email.endsWith('@newhorizonindia.edu')) {
        console.warn("⚠️ Invalid email domain:", user.email);
        await window.firebaseAuth.signOut();
        return { success: false, error: "Only @newhorizonindia.edu emails are allowed" };
      }

      console.log("🔄 Sending user data to backend...");
      const response = await fetch('/api/firebase_auth', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          uid: user.uid,
          email: user.email,
          displayName: user.displayName,
          photoURL: user.photoURL,
          provider: 'google'
        })
      });

      if (response.ok) {
        const data = await response.json();
        console.log("✅ Backend response:", data);
        return { success: true, user: user };
      } else {
        const error = await response.json();
        console.error("❌ Backend error:", error);
        return { success: false, error: error.message || "Backend error" };
      }
    } catch (error) {
      console.error("❌ Google Sign-In Error:", error);
      return { success: false, error: error.message || "Google sign-in failed" };
    }
  },

  signInWithEmail: async function(email, password) {
    try {
      console.log("🔐 Email Sign-In initiated...");
      const isReady = await this.waitForFirebase();
      if (!isReady) return { success: false, error: "Firebase not initialized" };
      if (!window.firebaseAuth) return { success: false, error: "Firebase not initialized" };
      if (!email.endsWith('@newhorizonindia.edu')) {
        return { success: false, error: "Only @newhorizonindia.edu emails are allowed" };
      }

      const result = await window.firebaseAuth.signInWithEmailAndPassword(email, password);
      const user = result.user;
      console.log("✅ Email Sign-In successful:", user.email);

      const response = await fetch('/api/firebase_auth', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          uid: user.uid,
          email: user.email,
          displayName: user.displayName,
          photoURL: user.photoURL,
          provider: 'email'
        })
      });

      if (response.ok) return { success: true, user: user };
      else {
        const error = await response.json();
        return { success: false, error: error.message || "Backend error" };
      }
    } catch (error) {
      console.error("❌ Email Sign-In Error:", error);
      return { success: false, error: error.message || "Sign-in failed" };
    }
  },

  signUpWithEmail: async function(email, password, displayName) {
    try {
      console.log("🔐 Email Sign-Up initiated...");
      const isReady = await this.waitForFirebase();
      if (!isReady) return { success: false, error: "Firebase not initialized" };
      if (!window.firebaseAuth) return { success: false, error: "Firebase not initialized" };
      if (!email.endsWith('@newhorizonindia.edu')) {
        return { success: false, error: "Only @newhorizonindia.edu emails are allowed" };
      }

      const result = await window.firebaseAuth.createUserWithEmailAndPassword(email, password);
      const user = result.user;
      await user.updateProfile({ displayName: displayName });
      console.log("✅ Email Sign-Up successful:", user.email);

      const response = await fetch('/api/firebase_auth', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          uid: user.uid,
          email: user.email,
          displayName: displayName,
          photoURL: user.photoURL,
          provider: 'email'
        })
      });

      if (response.ok) return { success: true, user: user };
      else {
        const error = await response.json();
        return { success: false, error: error.message || "Backend error" };
      }
    } catch (error) {
      console.error("❌ Email Sign-Up Error:", error);
      return { success: false, error: error.message || "Sign-up failed" };
    }
  },

  signOut: async function() {
    try {
      if (window.firebaseAuth) {
        await window.firebaseAuth.signOut();
        console.log("✅ Sign-out successful");
        return { success: true };
      }
      return { success: false, error: "Firebase not initialized" };
    } catch (error) {
      console.error("❌ Sign-Out Error:", error);
      return { success: false, error: error.message };
    }
  },

  getCurrentUser: function() {
    return window.firebaseAuth ? window.firebaseAuth.currentUser : null;
  },

  onAuthStateChanged: function(callback) {
    if (window.firebaseAuth) {
      return window.firebaseAuth.onAuthStateChanged(callback);
    }
  }
};

console.log("✅ Firebase Auth Enhanced module loaded");
