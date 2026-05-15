// Firebase Web SDK Initialization
// This file initializes Firebase and sets up authentication

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-analytics.js";

// Firebase Configuration
const firebaseConfig = {
  apiKey: "AIzaSyCDwaBMoEJvJO1NBS-uUzsMTirSSGz8Mcc",
  authDomain: "univibe-c85c6.firebaseapp.com",
  projectId: "univibe-c85c6",
  storageBucket: "univibe-c85c6.firebasestorage.app",
  messagingSenderId: "631710741538",
  appId: "1:631710741538:web:49b43d32353d97bcc3467b",
  measurementId: "G-1CXWWSRM61"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
console.log("✅ Firebase initialized");

// Initialize Firebase Authentication
const auth = getAuth(app);
console.log("✅ Firebase Auth initialized");

// Initialize Firestore
const db = getFirestore(app);
console.log("✅ Firestore initialized");

// Initialize Analytics
const analytics = getAnalytics(app);
console.log("✅ Firebase Analytics initialized");

// Google Auth Provider
const googleProvider = new GoogleAuthProvider();
googleProvider.addScope('profile');
googleProvider.addScope('email');

// Export for use in other files
export { 
  app, 
  auth, 
  db, 
  analytics,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  GoogleAuthProvider,
  signInWithPopup,
  googleProvider
};
