"""
Security configuration for EscaMap application.
"""
import os
from datetime import timedelta

class SecurityConfig:
    """Security configuration settings."""
    
    # SECURITY: Secret key for session management
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(32))
    
    # SECURITY: Session configuration
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=1)
    
    # SECURITY: Rate limiting configuration
    RATELIMIT_STORAGE_URL = 'memory://'
    RATELIMIT_DEFAULT = "100 per hour"
    
    # SECURITY: File upload restrictions
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'csv'}
    
    # SECURITY: Logging configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'app.log')
    
    # SECURITY: Application configuration
    TESTING = False
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    @staticmethod
    def allowed_file(filename):
        """Check if file extension is allowed."""
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in SecurityConfig.ALLOWED_EXTENSIONS