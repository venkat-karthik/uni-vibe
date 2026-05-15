// Firebase Configuration - Modular SDK
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-analytics.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyA1WDAtr4k3DThLBx4oc3M392h6bri1Jf0",
  authDomain: "unvb-6e1a0.firebaseapp.com",
  projectId: "unvb-6e1a0",
  storageBucket: "unvb-6e1a0.firebasestorage.app",
  messagingSenderId: "133181278048",
  appId: "1:133181278048:web:706ce5a2d40be2b5f6c005",
  measurementId: "G-41ZSP04VR7"
};

console.log("🔄 Firebase Config loading...");

// Initialize Firebase
const app = initializeApp(firebaseConfig);
console.log("✅ Firebase app initialized");

// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);
console.log("✅ Firebase Auth initialized");

// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(app);
console.log("✅ Firestore initialized");

// Initialize Analytics
const analytics = getAnalytics(app);
console.log("✅ Firebase Analytics initialized");

// Set persistence to LOCAL
auth.setPersistence = () => {
  console.log("✅ Firebase persistence set to LOCAL");
};

// Export for use in other scripts
window.firebaseApp = app;
window.firebaseAuth = auth;
window.firebaseDb = db;
window.firebaseAnalytics = analytics;

console.log("✅ Firebase Config loaded successfully!");
console.log("📄 Project ID:", firebaseConfig.projectId);
console.log("📄 Auth Domain:", firebaseConfig.authDomain);
