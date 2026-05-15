# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3, hashlib, json, random
from datetime import datetime
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'univibe_secret_2024'
DB_PATH = 'univibe.db'

QUESTIONS = [
    {"id":1,"text":"What is your favourite sport to watch?","icon":"🏆","type":"dropdown","options":["Cricket","Football","Basketball","Tennis","Badminton","Kabaddi","Chess","Table Tennis","Volleyball","Swimming","Athletics","Hockey","Baseball","Rugby","F1 Racing"]},
    {"id":2,"text":"Which sport do you love playing yourself?","icon":"⚽","type":"dropdown","options":["Cricket","Football","Basketball","Badminton","Table Tennis","Tennis","Volleyball","Chess","Kabaddi","Running","Swimming","Gym / Fitness","Cycling","Hockey","I prefer watching"]},
    {"id":3,"text":"What type of projects excite you the most?","icon":"💻","type":"dropdown","options":["Web Development","Mobile Apps","AI / ML","Data Science","Cybersecurity","Game Development","IoT / Hardware","Blockchain / Web3","Cloud Computing","UI/UX Design","Open Source Contributions","Research & Publications","Social Impact Projects","Startup / Entrepreneurship","Robotics"]},
    {"id":4,"text":"Which tech stack / language do you prefer?","icon":"⚙️","type":"dropdown","options":["Python","JavaScript / TypeScript","Java","C / C++","Kotlin / Android","Swift / iOS","Go","Rust","PHP","Ruby on Rails","React / Next.js","Flutter / Dart","No preference – I learn what's needed","SQL / Databases","Shell / DevOps"]},
    {"id":5,"text":"What's your go-to music genre?","icon":"🎵","type":"dropdown","options":["Bollywood / Hindi","Pop","Hip-Hop / Rap","Rock / Metal","Classical / Instrumental","Electronic / EDM","Jazz / Blues","Lo-Fi / Chill","K-Pop","Indie / Alternative","Devotional / Spiritual","Ghazal / Sufi","Country","R&B / Soul","I don't listen to music"]},
    {"id":6,"text":"What kind of movies / series do you binge-watch?","icon":"🎬","type":"dropdown","options":["Action / Thriller","Sci-Fi / Fantasy","Comedy / Rom-Com","Horror / Mystery","Documentary","Anime","Drama / Slice-of-Life","Crime / Detective","Superhero","Historical / Period","Bollywood Masala","Korean Drama","Reality / Game Shows","Stand-up Comedy","I barely watch"]},
    {"id":7,"text":"How do you study best?","icon":"📚","type":"dropdown","options":["Alone in silence","With background music","In a study group","In a café or open space","Late nights only","Early mornings","With YouTube / video lectures","Pomodoro technique","Spaced repetition / flashcards","Reading textbooks","Teaching others to learn","Practice problems only","Mind maps & diagrams","Voice notes / recordings","I figure it out before exams"]},
    {"id":8,"text":"What do you usually do in your free time?","icon":"🎮","type":"dropdown","options":["Gaming","Reading / Books","Social Media Scrolling","Gym / Workout","Cooking / Baking","Drawing / Art","Photography / Video Editing","Listening to Podcasts","Hanging out with friends","Watching content","Coding side projects","Writing / Journaling","Volunteering / Social work","Music / Instruments","Sleeping honestly"]},
    {"id":9,"text":"What campus activity would you most likely join?","icon":"🏫","type":"dropdown","options":["Technical Club (Coding/Robotics)","Sports Team","Cultural / Dance / Drama Club","Music Band or Choir","Entrepreneurship / Startup Cell","NSS / NCC / Social Service","Debating / MUN","Photography / Media Club","Literary / Quizzing Club","Student Government","Research / Seminar Group","Gaming / Esports Team","Fine Arts / Design Club","Language / International Club","I prefer no clubs — solo path"]},
    {"id":10,"text":"Where do you see yourself in 5 years?","icon":"🚀","type":"dropdown","options":["Software Engineer at a top tech company","Founder / Running my own startup","Data Scientist / ML Engineer","Product Manager","Government / Civil Services","Pursuing a Master's / PhD","Working abroad / Global opportunities","Full Stack Developer / Freelancer","Investment / Finance / FinTech","Creative professional (Design, Media, Content)","Cybersecurity Expert","Researcher / Professor","Healthcare / BioTech / Med-Tech","Social Entrepreneur / NGO work","I'm still figuring it out"]},
    {"id":11,"text":"Which best describes your personality?","icon":"🧠","type":"dropdown","options":["The Logical Thinker","The Creative Dreamer","The Leader","The Empath / Listener","The Problem-Solver","The Social Butterfly","The Introvert Powerhouse","The Overachiever","The Laid-Back Chill Person","The Curious Explorer","The Rebel / Contrarian","The Planner / Organizer","The Spontaneous One","The Philosopher","The Mentor / Guide"]},
    {"id":12,"text":"What's your favourite food vibe?","icon":"🍕","type":"dropdown","options":["Biryani all day","Pizza / Pasta Italian feels","South Indian (Dosa, Idli, Sambar)","Street food (Chaat, Pani Puri)","Chinese / Asian Fusion","North Indian (Dal, Sabji, Roti)","Burgers / Fast Food","Healthy / Salads / Juices","Desserts & Sweets only","Seafood","Continental / Western","Vegan / Plant-based","I eat anything and everything","Home-cooked food only","Instant noodles & hostel food"]},
    {"id":13,"text":"Your ideal travel destination?","icon":"✈️","type":"dropdown","options":["Mountains / Trekking","Beach / Coastal","City Tour / Urban Exploration","Spiritual / Temple tours","Forest / Wildlife Safari","Historical / Archaeological sites","International / Europe Dream","Road Trips with friends","Backpacking on a budget","Adventure Sports destination","Cultural / Festival travel","Desert landscapes","Island hopping","Food tourism","I prefer staying home"]},
    {"id":14,"text":"How would your friends describe your social style?","icon":"🤝","type":"dropdown","options":["Life of the party — always hyper","Friendly but takes time to open up","Deep conversations only — no small talk","Loyal ride-or-die to a close circle","Makes friends everywhere instantly","Quiet but helpful when needed","The planner — always organizing hangouts","The comedian — keeps everyone laughing","The advice-giver / agony uncle or aunt","Loves online friends more than IRL","Super reliable — never cancels","Always late but worth it","Motivates everyone around them","Low-key mysterious","Just vibing — no labels needed"]},
    {"id":15,"text":"What matters most to you in life right now?","icon":"💫","type":"dropdown","options":["Career Growth & Success","Meaningful Friendships","Learning & Personal Growth","Financial Independence","Creative Expression","Making a Social Impact","Family & Relationships","Health & Well-being","Adventure & New Experiences","Academic Excellence","Fame / Recognition / Influence","Inner peace & Mental Health","Building something of my own","Travel & Freedom","Just surviving this semester"]}
]

# ─── DATABASE ─────────────────────────────────────────────────────────────────
def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=10.0)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute('PRAGMA journal_mode=WAL')
    except sqlite3.OperationalError:
        pass
    return conn

def init_db():
    conn = sqlite3.connect(DB_PATH, timeout=10.0)
    try:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                full_name TEXT,
                bio TEXT,
                avatar_color TEXT,
                is_blacklisted INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS quiz_answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                answers TEXT NOT NULL,
                submitted_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
            CREATE TABLE IF NOT EXISTS connections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender_id INTEGER NOT NULL,
                receiver_id INTEGER NOT NULL,
                status TEXT DEFAULT 'pending',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(sender_id, receiver_id)
            );
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reviewer_id INTEGER NOT NULL,
                reviewed_id INTEGER NOT NULL,
                rating INTEGER NOT NULL,
                comment TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS blacklist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                reason TEXT,
                bad_review_count INTEGER DEFAULT 0,
                blacklisted_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id)
            );
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender_id INTEGER NOT NULL,
                receiver_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                is_read INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                from_user_id INTEGER,
                type TEXT NOT NULL,
                message TEXT NOT NULL,
                is_read INTEGER DEFAULT 0,
                link TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS cookie_consent (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE NOT NULL,
                accepted_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()
    finally:
        conn.close()

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def add_notification(user_id, from_user_id, ntype, message, link=''):
    conn = get_db()
    try:
        conn.execute('INSERT INTO notifications (user_id, from_user_id, type, message, link) VALUES (?,?,?,?,?)',
                     (user_id, from_user_id, ntype, message, link))
        conn.commit()
    finally:
        conn.close()

def get_unread_count(user_id):
    conn = get_db()
    try:
        row = conn.execute('SELECT COUNT(*) as c FROM notifications WHERE user_id=? AND is_read=0', (user_id,)).fetchone()
        return row['c'] if row else 0
    finally:
        conn.close()

def check_and_blacklist(reviewed_id):
    """Auto-blacklist user if they get 3+ bad reviews (rating <= 2)."""
    conn = get_db()
    try:
        row = conn.execute(
            'SELECT COUNT(*) as c FROM reviews WHERE reviewed_id=? AND rating <= 2', (reviewed_id,)
        ).fetchone()
        bad_count = row['c'] if row else 0
        if bad_count >= 3:
            conn.execute('''INSERT INTO blacklist (user_id, reason, bad_review_count)
                            VALUES (?,?,?)
                            ON CONFLICT(user_id) DO UPDATE SET
                            bad_review_count=excluded.bad_review_count,
                            reason=excluded.reason''',
                         (reviewed_id, f'Auto-blacklisted: {bad_count} bad reviews received', bad_count))
            conn.execute('UPDATE users SET is_blacklisted=1 WHERE id=?', (reviewed_id,))
            conn.commit()
            return True
        conn.commit()
        return False
    finally:
        conn.close()

def are_connected(uid1, uid2):
    conn = get_db()
    try:
        row = conn.execute(
            '''SELECT id FROM connections
               WHERE ((sender_id=? AND receiver_id=?) OR (sender_id=? AND receiver_id=?))
               AND status="accepted"''',
            (uid1, uid2, uid2, uid1)
        ).fetchone()
        return row is not None
    finally:
        conn.close()

def has_cookie_consent(user_id):
    conn = get_db()
    try:
        row = conn.execute('SELECT id FROM cookie_consent WHERE user_id=?', (user_id,)).fetchone()
        return row is not None
    finally:
        conn.close()

# ─── COSINE SIMILARITY ENGINE ─────────────────────────────────────────────────
def build_option_index(questions):
    index = {}
    pos = 0
    for q in questions:
        for opt in q['options']:
            index[(str(q['id']), opt)] = pos
            pos += 1
    return index, pos

OPTION_INDEX, VECTOR_SIZE = build_option_index(QUESTIONS)

def answers_to_vector(answers):
    vec = np.zeros(VECTOR_SIZE)
    for qid, val in answers.items():
        key = (str(qid), val)
        if key in OPTION_INDEX:
            vec[OPTION_INDEX[key]] = 1.0
    return vec

def compute_cosine_score(a1, a2):
    v1 = answers_to_vector(a1).reshape(1, -1)
    v2 = answers_to_vector(a2).reshape(1, -1)
    score = cosine_similarity(v1, v2)[0][0]
    return round(float(score) * 100, 1)

def get_top_matches(user_id, user_answers):
    conn = get_db()
    try:
        rows = conn.execute(
            'SELECT qa.user_id, qa.answers, u.username, u.full_name, u.bio, u.avatar_color, u.is_blacklisted '
            'FROM quiz_answers qa JOIN users u ON qa.user_id = u.id '
            'WHERE qa.user_id != ? AND u.is_blacklisted = 0', (user_id,)
        ).fetchall()
    finally:
        conn.close()
    results = []
    for row in rows:
        try:
            other_answers = json.loads(row['answers'])
        except (json.JSONDecodeError, KeyError):
            continue
        score = compute_cosine_score(user_answers, other_answers)
        common = []
        for q in QUESTIONS:
            qid = str(q['id'])
            if qid in user_answers and qid in other_answers and user_answers[qid] == other_answers[qid]:
                common.append({'q': q['icon'] + ' ' + q['text'].split('?')[0].split('do you')[0].strip(), 'val': user_answers[qid]})
        results.append({
            'user_id': row['user_id'], 'username': row['username'],
            'full_name': row['full_name'] or row['username'],
            'bio': row['bio'] or 'No bio yet',
            'avatar_color': row['avatar_color'] or '#6c63ff',
            'score': score, 'common': common[:5]
        })
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:5]

# ─── MAIN ROUTES ──────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return '<h1 style="color:red;">Server is working!</h1>'

@app.route('/register', methods=['GET', 'POST'])
def register():
    flash('Registration is currently disabled.', 'info')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    flash('Login is currently disabled.', 'info')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    uid = session['user_id']
    conn = get_db()
    try:
        has_quiz = conn.execute('SELECT id FROM quiz_answers WHERE user_id=?', (uid,)).fetchone()
        # Pending connection requests for this user
        pending = conn.execute(
            '''SELECT c.id, c.sender_id, u.full_name, u.username, u.avatar_color
               FROM connections c JOIN users u ON c.sender_id=u.id
               WHERE c.receiver_id=? AND c.status="pending"''', (uid,)
        ).fetchall()
        # Accepted connections
        connections = conn.execute(
            '''SELECT u.id, u.full_name, u.username, u.avatar_color
               FROM connections c
               JOIN users u ON (CASE WHEN c.sender_id=? THEN c.receiver_id ELSE c.sender_id END)=u.id
               WHERE (c.sender_id=? OR c.receiver_id=?) AND c.status="accepted"''',
            (uid, uid, uid)
        ).fetchall()
    finally:
        conn.close()
    unread = get_unread_count(uid)
    cookie_accepted = has_cookie_consent(uid)
    return render_template('dashboard.html', has_quiz=has_quiz, pending=pending,
                           connections=connections, unread=unread, cookie_accepted=cookie_accepted)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        answers = {str(q['id']): request.form.get(f'q{q["id"]}', '') for q in QUESTIONS}
        conn = get_db()
        try:
            existing = conn.execute('SELECT id FROM quiz_answers WHERE user_id=?', (session['user_id'],)).fetchone()
            if existing:
                conn.execute('UPDATE quiz_answers SET answers=?, submitted_at=? WHERE user_id=?',
                             (json.dumps(answers), datetime.now().isoformat(), session['user_id']))
            else:
                conn.execute('INSERT INTO quiz_answers (user_id, answers) VALUES (?,?)',
                             (session['user_id'], json.dumps(answers)))
            conn.commit()
        finally:
            conn.close()
        return redirect(url_for('results'))
    return render_template('quiz.html', questions=QUESTIONS)

@app.route('/results')
def results():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    uid = session['user_id']
    conn = get_db()
    try:
        row = conn.execute('SELECT answers FROM quiz_answers WHERE user_id=?', (uid,)).fetchone()
    finally:
        conn.close()
    if not row:
        flash('Please complete the quiz first!', 'warning')
        return redirect(url_for('quiz'))
    user_answers = json.loads(row['answers'])
    matches = get_top_matches(uid, user_answers)
    # Get connection statuses for each match
    conn = get_db()
    try:
        for m in matches:
            c = conn.execute(
                '''SELECT status FROM connections
                   WHERE (sender_id=? AND receiver_id=?) OR (sender_id=? AND receiver_id=?)''',
                (uid, m['user_id'], m['user_id'], uid)
            ).fetchone()
            m['conn_status'] = c['status'] if c else None
            m['conn_direction'] = None
            if c:
                d = conn.execute('SELECT sender_id FROM connections WHERE (sender_id=? AND receiver_id=?) OR (sender_id=? AND receiver_id=?)',
                                 (uid, m['user_id'], m['user_id'], uid)).fetchone()
                m['conn_direction'] = 'sent' if d and d['sender_id'] == uid else 'received'
    finally:
        conn.close()
    unread = get_unread_count(uid)
    return render_template('results.html', matches=matches, user_answers=user_answers,
                           questions=QUESTIONS, unread=unread)

@app.route('/profile/<int:uid>')
def profile(uid):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    me = session['user_id']
    conn = get_db()
    try:
        user = conn.execute('SELECT * FROM users WHERE id=?', (uid,)).fetchone()
        quiz_row = conn.execute('SELECT answers FROM quiz_answers WHERE user_id=?', (uid,)).fetchone()
        reviews = conn.execute(
            '''SELECT r.*, u.full_name, u.username, u.avatar_color
               FROM reviews r JOIN users u ON r.reviewer_id=u.id
               WHERE r.reviewed_id=? ORDER BY r.created_at DESC''', (uid,)
        ).fetchall()
        avg_rating = conn.execute('SELECT AVG(rating) as avg FROM reviews WHERE reviewed_id=?', (uid,)).fetchone()
        already_reviewed = conn.execute('SELECT id FROM reviews WHERE reviewer_id=? AND reviewed_id=?', (me, uid)).fetchone()
        conn_row = conn.execute(
            '''SELECT status, sender_id FROM connections
               WHERE (sender_id=? AND receiver_id=?) OR (sender_id=? AND receiver_id=?)''',
            (me, uid, uid, me)
        ).fetchone()
        is_blacklisted_row = conn.execute('SELECT id FROM blacklist WHERE user_id=?', (uid,)).fetchone()
    finally:
        conn.close()
    if not user:
        flash('User not found', 'danger')
        return redirect(url_for('dashboard'))
    answers = json.loads(quiz_row['answers']) if quiz_row else {}
    answer_map = {q['text']: {'icon': q['icon'], 'val': answers[str(q['id'])]}
                  for q in QUESTIONS if str(q['id']) in answers}
    connected = are_connected(me, uid)
    conn_status = conn_row['status'] if conn_row else None
    conn_direction = None
    if conn_row:
        conn_direction = 'sent' if conn_row['sender_id'] == me else 'received'
    unread = get_unread_count(me)
    avg = round(avg_rating['avg'], 1) if avg_rating and avg_rating['avg'] else None
    return render_template('profile.html', profile_user=user, answer_map=answer_map,
                           reviews=reviews, avg_rating=avg, already_reviewed=already_reviewed,
                           connected=connected, conn_status=conn_status, conn_direction=conn_direction,
                           is_blacklisted=is_blacklisted_row is not None,
                           unread=unread, cookie_accepted=has_cookie_consent(me))

# ─── CONNECTION ROUTES ─────────────────────────────────────────────────────────
@app.route('/connect/<int:uid>', methods=['POST'])
def connect(uid):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    me = session['user_id']
    if me == uid:
        flash('You cannot connect with yourself!', 'warning')
        return redirect(url_for('profile', uid=uid))
    conn = get_db()
    try:
        existing = conn.execute(
            'SELECT id FROM connections WHERE (sender_id=? AND receiver_id=?) OR (sender_id=? AND receiver_id=?)',
            (me, uid, uid, me)
        ).fetchone()
        if not existing:
            conn.execute('INSERT INTO connections (sender_id, receiver_id, status) VALUES (?,?,?)', (me, uid, 'pending'))
            conn.commit()
            # Get sender name for notification
            sender = conn.execute('SELECT full_name, username FROM users WHERE id=?', (me,)).fetchone()
            name = sender['full_name'] or sender['username']
            add_notification(uid, me, 'connection_request',
                             f'{name} sent you a connection request!',
                             url_for('dashboard'))
            flash('Connection request sent!', 'success')
        else:
            flash('Connection request already exists.', 'info')
    finally:
        conn.close()
    return redirect(url_for('profile', uid=uid))

@app.route('/connection/respond/<int:conn_id>/<action>')
def respond_connection(conn_id, action):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    me = session['user_id']
    conn = get_db()
    try:
        c = conn.execute('SELECT * FROM connections WHERE id=? AND receiver_id=?', (conn_id, me)).fetchone()
        if c:
            if action == 'accept':
                conn.execute('UPDATE connections SET status="accepted" WHERE id=?', (conn_id,))
                conn.commit()
                me_info = conn.execute('SELECT full_name, username FROM users WHERE id=?', (me,)).fetchone()
                name = me_info['full_name'] or me_info['username']
                add_notification(c['sender_id'], me, 'connection_accepted',
                                 f'{name} accepted your connection request! You can now chat.',
                                 url_for('chat', uid=me))
                flash('Connection accepted! You can now chat.', 'success')
            elif action == 'reject':
                conn.execute('DELETE FROM connections WHERE id=?', (conn_id,))
                conn.commit()
                flash('Connection request declined.', 'info')
    finally:
        conn.close()
    return redirect(url_for('dashboard'))

# ─── REVIEW ROUTES ─────────────────────────────────────────────────────────────
@app.route('/review/<int:uid>', methods=['POST'])
def submit_review(uid):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    me = session['user_id']
    if me == uid:
        flash('You cannot review yourself!', 'warning')
        return redirect(url_for('profile', uid=uid))
    if not are_connected(me, uid):
        flash('You can only review people you are connected with.', 'warning')
        return redirect(url_for('profile', uid=uid))
    rating = int(request.form.get('rating', 3))
    comment = request.form.get('comment', '').strip()
    conn = get_db()
    try:
        already = conn.execute('SELECT id FROM reviews WHERE reviewer_id=? AND reviewed_id=?', (me, uid)).fetchone()
        if already:
            flash('You have already reviewed this person.', 'warning')
        else:
            conn.execute('INSERT INTO reviews (reviewer_id, reviewed_id, rating, comment) VALUES (?,?,?,?)',
                         (me, uid, rating, comment))
            conn.commit()
            # Notify the reviewed person
            me_info = conn.execute('SELECT full_name, username FROM users WHERE id=?', (me,)).fetchone()
            name = me_info['full_name'] or me_info['username']
            stars = '⭐' * rating
            add_notification(uid, me, 'review',
                             f'{name} gave you a {stars} review!',
                             url_for('profile', uid=uid))
            # Check for auto-blacklist
            blacklisted = check_and_blacklist(uid)
            if blacklisted:
                add_notification(uid, None, 'blacklist',
                                 'Your account has been suspended due to 3 or more bad reviews.',
                                 url_for('dashboard'))
            flash('Review submitted successfully!', 'success')
    finally:
        conn.close()
    return redirect(url_for('profile', uid=uid))

# ─── CHAT ROUTES ───────────────────────────────────────────────────────────────
@app.route('/chat/<int:uid>')
def chat(uid):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    me = session['user_id']
    # Must have cookie consent to chat
    if not has_cookie_consent(me):
        flash('You must accept cookies to use the chat feature.', 'warning')
        return redirect(url_for('profile', uid=uid))
    if not are_connected(me, uid):
        flash('You can only chat with connected people.', 'warning')
        return redirect(url_for('profile', uid=uid))
    conn = get_db()
    try:
        other_user = conn.execute('SELECT * FROM users WHERE id=?', (uid,)).fetchone()
        messages = conn.execute(
            '''SELECT m.*, u.full_name, u.username, u.avatar_color
               FROM messages m JOIN users u ON m.sender_id=u.id
               WHERE (m.sender_id=? AND m.receiver_id=?) OR (m.sender_id=? AND m.receiver_id=?)
               ORDER BY m.created_at ASC''',
            (me, uid, uid, me)
        ).fetchall()
        # Mark messages as read
        conn.execute('UPDATE messages SET is_read=1 WHERE receiver_id=? AND sender_id=?', (me, uid))
        conn.commit()
    finally:
        conn.close()
    unread = get_unread_count(me)
    return render_template('chat.html', other_user=other_user, messages=messages, unread=unread)

@app.route('/api/send_message', methods=['POST'])
def send_message():
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    me = session['user_id']
    if not has_cookie_consent(me):
        return jsonify({'error': 'Cookie consent required'}), 403
    data = request.get_json()
    receiver_id = data.get('receiver_id')
    content = data.get('content', '').strip()
    if not content or not receiver_id:
        return jsonify({'error': 'Missing fields'}), 400
    if not are_connected(me, int(receiver_id)):
        return jsonify({'error': 'Not connected'}), 403
    conn = get_db()
    try:
        conn.execute('INSERT INTO messages (sender_id, receiver_id, content) VALUES (?,?,?)',
                     (me, receiver_id, content))
        conn.commit()
        me_info = conn.execute('SELECT full_name, username FROM users WHERE id=?', (me,)).fetchone()
        name = me_info['full_name'] or me_info['username']
        add_notification(receiver_id, me, 'message',
                         f'{name} sent you a message: "{content[:40]}..."' if len(content) > 40 else f'{name}: {content}',
                         url_for('chat', uid=me))
        return jsonify({'success': True, 'time': datetime.now().strftime('%H:%M')})
    finally:
        conn.close()

@app.route('/api/get_messages/<int:uid>')
def get_messages(uid):
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    me = session['user_id']
    conn = get_db()
    try:
        messages = conn.execute(
            '''SELECT m.id, m.sender_id, m.content, m.created_at, u.full_name, u.avatar_color
               FROM messages m JOIN users u ON m.sender_id=u.id
               WHERE (m.sender_id=? AND m.receiver_id=?) OR (m.sender_id=? AND m.receiver_id=?)
               ORDER BY m.created_at ASC''',
            (me, uid, uid, me)
        ).fetchall()
        conn.execute('UPDATE messages SET is_read=1 WHERE receiver_id=? AND sender_id=?', (me, uid))
        conn.commit()
        return jsonify([{'id': r['id'], 'sender_id': r['sender_id'], 'content': r['content'],
                         'time': r['created_at'][11:16], 'name': r['full_name'],
                         'avatar_color': r['avatar_color'], 'is_me': r['sender_id'] == me}
                        for r in messages])
    finally:
        conn.close()

# ─── NOTIFICATIONS ─────────────────────────────────────────────────────────────
@app.route('/notifications')
def notifications():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    uid = session['user_id']
    conn = get_db()
    try:
        notifs = conn.execute(
            '''SELECT n.*, u.full_name, u.username, u.avatar_color
               FROM notifications n
               LEFT JOIN users u ON n.from_user_id=u.id
               WHERE n.user_id=? ORDER BY n.created_at DESC LIMIT 50''', (uid,)
        ).fetchall()
        conn.execute('UPDATE notifications SET is_read=1 WHERE user_id=?', (uid,))
        conn.commit()
    finally:
        conn.close()
    return render_template('notifications.html', notifs=notifs)

@app.route('/api/notifications/count')
def notif_count():
    if 'user_id' not in session:
        return jsonify({'count': 0})
    return jsonify({'count': get_unread_count(session['user_id'])})

# ─── COOKIE CONSENT ────────────────────────────────────────────────────────────
@app.route('/api/cookie_consent', methods=['POST'])
def cookie_consent():
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    uid = session['user_id']
    conn = get_db()
    try:
        conn.execute('INSERT OR IGNORE INTO cookie_consent (user_id) VALUES (?)', (uid,))
        conn.commit()
        return jsonify({'success': True})
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()
    print("Starting UniVibe on http://localhost:5000")
    app.run(debug=True, use_reloader=False, port=5000, host='127.0.0.1')

