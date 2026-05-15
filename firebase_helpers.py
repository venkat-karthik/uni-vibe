# Firebase Helpers for UniVibe
# Handles Firestore operations and user management

from firebase_admin import firestore, auth
from datetime import datetime
import json

db = firestore.client()

# ─── FIRESTORE COLLECTIONS ────────────────────────────────────────────────

def init_firestore_collections():
    """Initialize Firestore collections structure"""
    try:
        # Create collections with initial documents
        collections = [
            'users',
            'quiz_answers',
            'connections',
            'messages',
            'reviews',
            'notifications',
            'blacklist'
        ]
        
        for collection in collections:
            # Check if collection exists by trying to get a document
            try:
                docs = db.collection(collection).limit(1).stream()
                list(docs)  # Force evaluation
            except:
                # Collection doesn't exist, create it with a placeholder
                db.collection(collection).document('_placeholder').set({
                    'created_at': datetime.now(),
                    'placeholder': True
                })
                # Delete placeholder
                db.collection(collection).document('_placeholder').delete()
        
        print("✅ Firestore collections initialized")
        return True
    except Exception as e:
        print(f"❌ Error initializing Firestore: {e}")
        return False

# ─── USER MANAGEMENT ──────────────────────────────────────────────────────

def create_user_in_firestore(uid, email, full_name, username, bio="", avatar_color="#6c63ff"):
    """Create user document in Firestore"""
    try:
        user_data = {
            'uid': uid,
            'email': email,
            'full_name': full_name,
            'username': username,
            'bio': bio,
            'avatar_color': avatar_color,
            'is_blacklisted': False,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            'profile_complete': False,
            'quiz_completed': False
        }
        
        db.collection('users').document(uid).set(user_data)
        print(f"✅ User created in Firestore: {uid}")
        return True
    except Exception as e:
        print(f"❌ Error creating user: {e}")
        return False

def get_user_from_firestore(uid):
    """Get user document from Firestore"""
    try:
        doc = db.collection('users').document(uid).get()
        if doc.exists:
            return doc.to_dict()
        return None
    except Exception as e:
        print(f"❌ Error getting user: {e}")
        return None

def update_user_in_firestore(uid, data):
    """Update user document in Firestore"""
    try:
        data['updated_at'] = datetime.now()
        db.collection('users').document(uid).update(data)
        print(f"✅ User updated in Firestore: {uid}")
        return True
    except Exception as e:
        print(f"❌ Error updating user: {e}")
        return False

# ─── QUIZ ANSWERS ─────────────────────────────────────────────────────────

def save_quiz_answers(uid, answers):
    """Save quiz answers to Firestore"""
    try:
        quiz_data = {
            'uid': uid,
            'answers': answers,
            'submitted_at': datetime.now(),
            'updated_at': datetime.now()
        }
        
        # Check if user already has quiz answers
        existing = db.collection('quiz_answers').where('uid', '==', uid).limit(1).stream()
        existing_docs = list(existing)
        
        if existing_docs:
            # Update existing
            existing_docs[0].reference.update(quiz_data)
        else:
            # Create new
            db.collection('quiz_answers').add(quiz_data)
        
        # Update user profile
        update_user_in_firestore(uid, {'quiz_completed': True})
        print(f"✅ Quiz answers saved for user: {uid}")
        return True
    except Exception as e:
        print(f"❌ Error saving quiz answers: {e}")
        return False

def get_quiz_answers(uid):
    """Get quiz answers from Firestore"""
    try:
        docs = db.collection('quiz_answers').where('uid', '==', uid).limit(1).stream()
        for doc in docs:
            return doc.to_dict()
        return None
    except Exception as e:
        print(f"❌ Error getting quiz answers: {e}")
        return None

# ─── CONNECTIONS ──────────────────────────────────────────────────────────

def create_connection(sender_uid, receiver_uid):
    """Create connection request"""
    try:
        connection_data = {
            'sender_uid': sender_uid,
            'receiver_uid': receiver_uid,
            'status': 'pending',
            'created_at': datetime.now()
        }
        
        db.collection('connections').add(connection_data)
        print(f"✅ Connection created: {sender_uid} -> {receiver_uid}")
        return True
    except Exception as e:
        print(f"❌ Error creating connection: {e}")
        return False

def get_connections(uid):
    """Get all connections for a user"""
    try:
        docs = db.collection('connections').where('uid', '==', uid).stream()
        connections = []
        for doc in docs:
            connections.append(doc.to_dict())
        return connections
    except Exception as e:
        print(f"❌ Error getting connections: {e}")
        return []

# ─── MESSAGES ──────────────────────────────────────────────────────────────

def send_message(sender_uid, receiver_uid, content):
    """Send message between users"""
    try:
        message_data = {
            'sender_uid': sender_uid,
            'receiver_uid': receiver_uid,
            'content': content,
            'is_read': False,
            'created_at': datetime.now()
        }
        
        db.collection('messages').add(message_data)
        print(f"✅ Message sent: {sender_uid} -> {receiver_uid}")
        return True
    except Exception as e:
        print(f"❌ Error sending message: {e}")
        return False

def get_messages(uid1, uid2):
    """Get messages between two users"""
    try:
        docs = db.collection('messages').where(
            'sender_uid', '==', uid1
        ).where('receiver_uid', '==', uid2).stream()
        
        messages = []
        for doc in docs:
            messages.append(doc.to_dict())
        
        return sorted(messages, key=lambda x: x['created_at'])
    except Exception as e:
        print(f"❌ Error getting messages: {e}")
        return []

# ─── REVIEWS ──────────────────────────────────────────────────────────────

def submit_review(reviewer_uid, reviewed_uid, rating, comment=""):
    """Submit review for a user"""
    try:
        review_data = {
            'reviewer_uid': reviewer_uid,
            'reviewed_uid': reviewed_uid,
            'rating': rating,
            'comment': comment,
            'created_at': datetime.now()
        }
        
        db.collection('reviews').add(review_data)
        print(f"✅ Review submitted: {reviewer_uid} -> {reviewed_uid}")
        return True
    except Exception as e:
        print(f"❌ Error submitting review: {e}")
        return False

def get_reviews(uid):
    """Get all reviews for a user"""
    try:
        docs = db.collection('reviews').where('reviewed_uid', '==', uid).stream()
        reviews = []
        for doc in docs:
            reviews.append(doc.to_dict())
        return reviews
    except Exception as e:
        print(f"❌ Error getting reviews: {e}")
        return []

# ─── NOTIFICATIONS ────────────────────────────────────────────────────────

def create_notification(user_uid, from_user_uid, ntype, message, link=""):
    """Create notification for user"""
    try:
        notification_data = {
            'user_uid': user_uid,
            'from_user_uid': from_user_uid,
            'type': ntype,
            'message': message,
            'link': link,
            'is_read': False,
            'created_at': datetime.now()
        }
        
        db.collection('notifications').add(notification_data)
        print(f"✅ Notification created for user: {user_uid}")
        return True
    except Exception as e:
        print(f"❌ Error creating notification: {e}")
        return False

def get_notifications(uid):
    """Get all notifications for a user"""
    try:
        docs = db.collection('notifications').where('user_uid', '==', uid).stream()
        notifications = []
        for doc in docs:
            notifications.append(doc.to_dict())
        return sorted(notifications, key=lambda x: x['created_at'], reverse=True)
    except Exception as e:
        print(f"❌ Error getting notifications: {e}")
        return []

# ─── BLACKLIST ────────────────────────────────────────────────────────────

def blacklist_user(uid, reason=""):
    """Blacklist a user"""
    try:
        blacklist_data = {
            'uid': uid,
            'reason': reason,
            'blacklisted_at': datetime.now()
        }
        
        db.collection('blacklist').add(blacklist_data)
        update_user_in_firestore(uid, {'is_blacklisted': True})
        print(f"✅ User blacklisted: {uid}")
        return True
    except Exception as e:
        print(f"❌ Error blacklisting user: {e}")
        return False

def is_user_blacklisted(uid):
    """Check if user is blacklisted"""
    try:
        docs = db.collection('blacklist').where('uid', '==', uid).limit(1).stream()
        return len(list(docs)) > 0
    except Exception as e:
        print(f"❌ Error checking blacklist: {e}")
        return False
