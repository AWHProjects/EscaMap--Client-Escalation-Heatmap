from flask import Flask, render_template
from markupsafe import escape
from data_processing import load_and_prepare_data
from heatmap import create_heatmap, create_region_heatmap, create_client_heatmap
import os
import logging
from markupsafe import Markup
from functools import wraps

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# SECURITY: Configure Flask security settings
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(32))
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# SECURITY: Add security headers to all responses
@app.after_request
def add_security_headers(response):
    """Add comprehensive security headers to all responses."""
    # Content Security Policy - prevents XSS attacks
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; "
        "style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; "
        "font-src 'self' https://cdnjs.cloudflare.com; "
        "img-src 'self' data:; "
        "connect-src 'self'; "
        "frame-ancestors 'none';"
    )
    
    # HTTP Strict Transport Security - enforces HTTPS
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    
    # Prevent clickjacking attacks
    response.headers['X-Frame-Options'] = 'DENY'
    
    # Prevent MIME type sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # XSS Protection (legacy browsers)
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # Referrer Policy for privacy
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    
    # Remove server information disclosure
    response.headers.pop('Server', None)
    
    return response

@app.route('/')
def home():
    """Main route that displays the escalation heatmap dashboard."""
    try:
        # Load and prepare the data
        df = load_and_prepare_data()
        
        # Create multiple heatmaps for comprehensive view
        create_heatmap(df)  # Main product vs month heatmap
        create_region_heatmap(df)  # Region vs severity heatmap
        create_client_heatmap(df)  # Client vs product heatmap
        
        # Get some basic stats for the template
        total_escalations = len(df)
        high_severity_count = len(df[df['Severity'] == 'High'])
        unique_clients = df['Client'].nunique()
        
        stats = {
            'total_escalations': total_escalations,
            'high_severity_count': high_severity_count,
            'unique_clients': unique_clients,
            'severity_percentage': round((high_severity_count / total_escalations) * 100, 1) if total_escalations > 0 else 0
        }
        
        return render_template('index.html', stats=stats)
    
    except Exception as e:
        # SECURITY: Log error details securely without exposing to user
        logging.error(f"Error in home route: {str(e)}")
        return "An error occurred while loading the dashboard. Please try again later.", 500

@app.route('/data')
def data_view():
    """Route to view raw data in table format."""
    try:
        df = load_and_prepare_data()
        # Convert DataFrame to HTML table with proper escaping
        table_html = df[['Client', 'Region', 'Product', 'Severity', 'Date', 'SeverityScore']].to_html(
            classes='table table-striped',
            table_id='data-table',
            escape=True  # SECURITY: Enable HTML escaping to prevent XSS
        )
        return render_template('data.html', table=table_html)
    except Exception as e:
        # SECURITY: Log error details securely without exposing to user
        logging.error(f"Error in data_view route: {str(e)}")
        return "An error occurred while loading the data view. Please try again later.", 500

if __name__ == '__main__':
    # Configure secure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )
    
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    # SECURITY: Remove debug mode and restrict host for production
    # Use environment variables for configuration
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.getenv('FLASK_HOST', '127.0.0.1')  # Default to localhost only
    port = int(os.getenv('FLASK_PORT', '5000'))
    
    app.run(debug=debug_mode, host=host, port=port)