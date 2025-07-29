import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import logging

def validate_filepath(filepath):
    """
    SECURITY: Validate and sanitize file path to prevent path traversal attacks.
    Only allow access to files in the data directory.
    """
    # Normalize the path to resolve any .. or . components
    normalized_path = os.path.normpath(filepath)
    
    # Get the absolute path
    abs_path = os.path.abspath(normalized_path)
    
    # Define allowed directory (data directory)
    allowed_dir = os.path.abspath('data')
    
    # Check if the file is within the allowed directory
    if not abs_path.startswith(allowed_dir):
        raise ValueError("Access denied: File path outside allowed directory")
    
    # Check if file exists
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Additional check for file extension (only allow CSV files)
    if not abs_path.lower().endswith('.csv'):
        raise ValueError("Access denied: Only CSV files are allowed")
    
    return abs_path

def load_and_prepare_data(filepath='data/escalations_dummy_data.csv'):
    """
    Load and prepare escalation data for heatmap visualization.
    Adapts the provided data format to create meaningful escalation patterns.
    """
    try:
        # SECURITY: Validate file path to prevent path traversal
        safe_filepath = validate_filepath(filepath)
        df = pd.read_csv(safe_filepath, sep='\t')
        
        # SECURITY: Validate required columns exist
        required_columns = ['name', 'email', 'numberrange']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        # SECURITY: Validate data types and ranges
        if not pd.api.types.is_numeric_dtype(df['numberrange']):
            raise ValueError("numberrange column must be numeric")
        
        # SECURITY: Sanitize numberrange values (ensure they're within expected range)
        df['numberrange'] = df['numberrange'].clip(0, 10)
        
    except Exception as e:
        logging.error(f"Error loading data from {filepath}: {str(e)}")
        raise
    
    # Create synthetic escalation data based on the numberrange
    # Higher numberrange values indicate more severe escalations
    df['Severity'] = df['numberrange'].apply(lambda x: 
        'High' if x >= 7 else 'Medium' if x >= 5 else 'Low')
    
    # Create synthetic regions based on email domains
    def assign_region(email):
        try:
            # SECURITY: Validate email format and sanitize input
            if not isinstance(email, str) or '@' not in email:
                return 'Unknown'
            
            # SECURITY: Escape and validate email to prevent injection
            email = str(email).strip().lower()
            if len(email) > 254:  # RFC 5321 limit
                return 'Unknown'
            
            domain = email.split('@')[1] if '@' in email else ''
            if 'hotmail' in domain or 'aol' in domain:
                return 'North America'
            elif 'yahoo' in domain:
                return 'Asia'
            elif 'google' in domain:
                return 'Europe'
            else:
                return 'South America'
        except Exception:
            return 'Unknown'
    
    df['Region'] = df['email'].apply(assign_region)
    
    # Create synthetic products based on name patterns
    def assign_product(name):
        try:
            # SECURITY: Validate and sanitize name input
            if not isinstance(name, str):
                return 'Unknown'
            
            # SECURITY: Sanitize name to prevent injection attacks
            name = str(name).strip()
            if len(name) > 100:  # Reasonable limit for names
                name = name[:100]
            
            if not name:
                return 'Unknown'
            
            first_name = name.split()[0].lower() if name.split() else ''
            if first_name.startswith(('a', 'b', 'c', 'd', 'e')):
                return 'Analytics'
            elif first_name.startswith(('f', 'g', 'h', 'i', 'j')):
                return 'API'
            elif first_name.startswith(('k', 'l', 'm', 'n', 'o')):
                return 'Dashboard'
            else:
                return 'Reporting'
        except Exception:
            return 'Unknown'
    
    df['Product'] = df['name'].apply(assign_product)
    
    # Create synthetic dates based on numberrange (recent dates for higher severity)
    base_date = datetime.now() - timedelta(days=30)
    df['Date'] = df['numberrange'].apply(lambda x: 
        base_date + timedelta(days=np.random.randint(0, 30-x*2)))
    
    # Create month column for grouping
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    
    # Create severity score mapping
    severity_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    df['SeverityScore'] = df['Severity'].map(severity_mapping)
    
    # Rename 'name' to 'Client' for consistency
    df['Client'] = df['name']
    
    return df