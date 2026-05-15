// Firebase Configuration - Modular SDK
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut, setPersistence, browserLocalPersistence } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-analytics.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCDwaBMoEJvJO1NBS-uUzsMTirSSGz8Mcc",
  authDomain: "univibe-c85c6.firebaseapp.com",
  projectId: "univibe-c85c6",
  storageBucket: "univibe-c85c6.firebasestorage.app",
  messagingSenderId: "631710741538",
  appId: "1:631710741538:web:49b43d32353d97bcc3467b",
  measurementId: "G-1CXWWSRM61"
};

console.log("🔄 Firebase Config loading...");
console.log("📄 Current hostname:", window.location.hostname);

// Initialize Firebase
const app = initializeApp(firebaseConfig);
console.log("✅ Firebase app initialized");

// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);
console.log("✅ Firebase Auth initialized");

// Set persistence to LOCAL for development
try {
  setPersistence(auth, browserLocalPersistence)
    .then(() => console.log("✅ Firebase persistence set to LOCAL"))
    .catch(err => console.warn("⚠️ Persistence error:", err));
} catch (e) {
  console.warn("⚠️ Could not set persistence:", e);
}

// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(app);
console.log("✅ Firestore initialized");

// Initialize Analytics
try {
  const analytics = getAnalytics(app);
  console.log("✅ Firebase Analytics initialized");
  window.firebaseAnalytics = analytics;
} catch (e) {
  console.warn("⚠️ Analytics initialization warning:", e);
}

// Export for use in other scripts
window.firebaseApp = app;
window.firebaseAuth = auth;
window.firebaseDb = db;

console.log("✅ Firebase Config loaded successfully!");
console.log("📄 Project ID:", firebaseConfig.projectId);
console.log("📄 Auth Domain:", firebaseConfig.authDomain);
