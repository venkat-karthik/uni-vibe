// Firebase Authentication Helper for UniVibe
// This script handles Firebase authentication with New Horizon India email validation

const ALLOWED_EMAIL_DOMAIN = "newhorizonindia.edu";

/**
 * Validate if email belongs to New Horizon India organization
 */
function isValidOrganizationEmail(email) {
  return email.toLowerCase().endsWith(`@${ALLOWED_EMAIL_DOMAIN}`);
}

/**
 * Sign up with Firebase
 */
async function firebaseSignUp(email, password, fullName, username) {
  try {
    // Validate email domain
    if (!isValidOrganizationEmail(email)) {
      throw new Error(`Only ${ALLOWED_EMAIL_DOMAIN} emails are allowed!`);
    }

    // Create user with Firebase
    const userCredential = await window.firebaseAuth.createUserWithEmailAndPassword(email, password);
    const user = userCredential.user;

    // Update user profile
    await user.updateProfile({
      displayName: fullName
    });

    console.log("Firebase signup successful:", user.uid);
    return { success: true, user: user, uid: user.uid };
  } catch (error) {
    console.error("Firebase signup error:", error.message);
    return { success: false, error: error.message };
  }
}

/**
 * Sign in with Firebase
 */
async function firebaseSignIn(email, password) {
  try {
    // Validate email domain
    if (!isValidOrganizationEmail(email)) {
      throw new Error(`Only ${ALLOWED_EMAIL_DOMAIN} emails are allowed!`);
    }

    const userCredential = await window.firebaseAuth.signInWithEmailAndPassword(email, password);
    const user = userCredential.user;

    console.log("Firebase signin successful:", user.uid);
    return { success: true, user: user, uid: user.uid };
  } catch (error) {
    console.error("Firebase signin error:", error.message);
    return { success: false, error: error.message };
  }
}

/**
 * Sign out from Firebase
 */
async function firebaseSignOut() {
  try {
    await window.firebaseAuth.signOut();
    console.log("Firebase signout successful");
    return { success: true };
  } catch (error) {
    console.error("Firebase signout error:", error.message);
    return { success: false, error: error.message };
  }
}

/**
 * Get current Firebase user
 */
function getCurrentFirebaseUser() {
  return window.firebaseAuth.currentUser;
}

/**
 * Listen to authentication state changes
 */
function onAuthStateChanged(callback) {
  window.firebaseAuth.onAuthStateChanged(callback);
}

// Export functions globally
window.firebaseAuthHelpers = {
  isValidOrganizationEmail,
  firebaseSignUp,
  firebaseSignIn,
  firebaseSignOut,
  getCurrentFirebaseUser,
  onAuthStateChanged
};

console.log("Firebase Auth Helper loaded!");
