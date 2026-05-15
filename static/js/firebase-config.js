// Firebase Configuration - Firestore Only
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";

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

// Initialize Firebase
const app = initializeApp(firebaseConfig);
console.log("✅ Firebase app initialized");

// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(app);
console.log("✅ Firestore initialized");

// Export for use in other scripts
window.firebaseApp = app;
window.firebaseDb = db;

console.log("✅ Firebase Config loaded successfully!");
console.log("📄 Project ID:", firebaseConfig.projectId);
