// Firebase Initialization - Clean Start
console.log("🔄 Firebase initialization starting...");

const firebaseConfig = {
  apiKey: "AIzaSyCc9soowCRi8W7hGZqL_RViQwallIPutp4",
  authDomain: "unvibe-54ae1.firebaseapp.com",
  projectId: "unvibe-54ae1",
  storageBucket: "unvibe-54ae1.firebasestorage.app",
  messagingSenderId: "91608029769",
  appId: "1:91608029769:web:18544d40309fbd82a63d98",
  measurementId: "G-Z8MKB0PL4M"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Get references
window.auth = firebase.auth();
window.db = firebase.firestore();

console.log("✅ Firebase initialized successfully");
