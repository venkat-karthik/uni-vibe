#!/bin/bash

# UniVibe Google OAuth Setup Script

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         UniVibe Google OAuth Setup                             ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

echo "📋 STEP 1: Get Your Google Client ID"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Go to: https://console.cloud.google.com/"
echo "2. Create a new project or select existing"
echo "3. Enable Google+ API"
echo "4. Create OAuth 2.0 credentials (Web application)"
echo "5. Add authorized redirect URIs:"
echo "   - http://localhost:5000"
echo "   - http://localhost:5000/enter"
echo "   - http://127.0.0.1:5000"
echo "6. Copy your Client ID"
echo ""

read -p "Enter your Google Client ID: " CLIENT_ID

if [ -z "$CLIENT_ID" ]; then
    echo "❌ Client ID cannot be empty"
    exit 1
fi

echo ""
echo "✅ Setting environment variable..."
export GOOGLE_CLIENT_ID="$CLIENT_ID"

echo ""
echo "📝 To make this permanent, add to your shell profile:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "For bash (~/.bashrc or ~/.bash_profile):"
echo "  export GOOGLE_CLIENT_ID=\"$CLIENT_ID\""
echo ""
echo "For zsh (~/.zshrc):"
echo "  export GOOGLE_CLIENT_ID=\"$CLIENT_ID\""
echo ""

echo "🚀 Starting Flask server..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Server will start on http://localhost:5000"
echo "Test Google Sign-In at http://localhost:5000/enter"
echo ""

python3 app.py
