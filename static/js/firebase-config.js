// Firebase Configuration for UniVibe
// Using CDN script tags instead of ES modules

console.log("🔄 Firebase Config loading...");

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCc9soowCRi8W7hGZqL_RViQwallIPutp4",
  authDomain: "unvibe-54ae1.firebaseapp.com",
  projectId: "unvibe-54ae1",
  storageBucket: "unvibe-54ae1.firebasestorage.app",
  messagingSenderId: "91608029769",
  appId: "1:91608029769:web:18544d40309fbd82a63d98",
  measurementId: "G-Z8MKB0PL4M"
};

// Initialize Firebase when ready
function initializeFirebase() {
  try {
    // Check if Firebase SDK is loaded
    if (typeof firebase === 'undefined') {
      console.warn("⚠️ Firebase SDK not loaded yet, retrying...");
      setTimeout(initializeFirebase, 100);
      return false;
    }

    // Check if already initialized
    if (firebase.apps.length > 0) {
      console.log("✅ Firebase already initialized");
      window.firebaseAuth = firebase.auth();
      window.firebaseDb = firebase.firestore();
      return true;
    }

    console.log("🔄 Initializing Firebase...");
    
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    
    // Get Auth instance
    window.firebaseAuth = firebase.auth();
    window.firebaseDb = firebase.firestore();
    
    // Initialize Analytics
    try {
      firebase.analytics();
    } catch (e) {
      console.warn("⚠️ Analytics initialization warning:", e.message);
    }
    
    console.log("✅ Firebase initialized successfully!");
    console.log("✅ window.firebaseAuth:", window.firebaseAuth ? "Available" : "Not available");
    console.log("✅ window.firebaseDb:", window.firebaseDb ? "Available" : "Not available");
    
    return true;
  } catch (error) {
    console.error("❌ Firebase initialization error:", error);
    console.error("Error message:", error.message);
    console.error("Error code:", error.code);
    return false;
  }
}

// Wait for Firebase SDK to load - use multiple strategies
console.log("🔄 Setting up Firebase initialization...");

// Strategy 1: Wait for DOM to be ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', function() {
    console.log("📄 DOM loaded, initializing Firebase...");
    initializeFirebase();
  });
} else {
  console.log("📄 DOM already loaded, initializing Firebase...");
  initializeFirebase();
}

// Strategy 2: Also try immediately in case scripts are already loaded
setTimeout(function() {
  if (!window.firebaseAuth) {
    console.log("🔄 Retrying Firebase initialization...");
    initializeFirebase();
  }
}, 500);

// Strategy 3: Final retry after 1 second
setTimeout(function() {
  if (!window.firebaseAuth) {
    console.log("🔄 Final retry for Firebase initialization...");
    initializeFirebase();
  }
}, 1000);
