# 📊 EscaMap: Client Escalation Heatmap

> **A secure, professional-grade Flask web application that transforms client data into meaningful escalation visualizations for Technical Account Managers and Product Managers.**

![EscaMap Dashboard](https://img.shields.io/badge/Status-Production%20Ready-brightgreen) ![Security](https://img.shields.io/badge/Security-Audited-blue) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Flask](https://img.shields.io/badge/Flask-2.3+-green)

## 🎯 **Overview**

EscaMap enables Technical Account Managers and Product Managers to quickly visualize client escalation patterns, pinpoint areas of friction, and proactively manage customer relationships. The application demonstrates proactive, data-driven client management with minimal friction - a highly valued skill in customer success and product management roles.

### **Key Features**
- 📈 **Interactive Heatmap Visualizations** - Multiple view types (Product Timeline, Regional Analysis, Client Overview)
- 🔒 **Enterprise-Grade Security** - Comprehensive security audit with OWASP compliance
- 📊 **Smart Data Processing** - Transforms raw CSV data into meaningful business insights
- 🎨 **Professional UI/UX** - Modern, responsive design with smooth animations
- ⚡ **Real-time Analytics** - Live statistics and dynamic data visualization
- 🛡️ **Rate Limiting & Protection** - Built-in DoS protection and security headers

## 🏗️ **Architecture**

```
EscaMap/
├── 📁 data/                          # Data storage
│   └── escalations_dummy_data.csv    # Sample client data (100+ records)
├── 📁 src/                           # Core application logic
│   ├── app.py                        # Flask web application with security
│   ├── data_processing.py            # Secure data transformation engine
│   └── heatmap.py                    # Visualization generation
├── 📁 templates/                     # HTML templates
│   ├── index.html                    # Main dashboard
│   └── data.html                     # Raw data view
├── 📁 static/                        # Static assets & generated images
│   └── style.css                     # Professional styling
├── 📄 config.py                      # Security configuration
├── 📄 SECURITY.md                    # Security audit documentation
├── 📄 requirements.txt               # Python dependencies
└── 📄 README.md                      # This file
```

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning)

### **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AWHProjects/EscaMap--Client-Escalation-Heatmap.git
   cd EscaMap--Client-Escalation-Heatmap
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables (Optional)**
   ```bash
   # For production deployment
   export SECRET_KEY="your-secret-key-here"
   export FLASK_DEBUG=False
   export FLASK_HOST=127.0.0.1
   export FLASK_PORT=5000
   ```

4. **Run the Application**
   ```bash
   python src/app.py
   ```

5. **Access the Dashboard**
   Open your browser and navigate to: `http://localhost:5000`

## 📊 **How It Works**

### **Data Processing Pipeline**

1. **Data Ingestion** - Reads CSV files with client information (name, phone, email, numberrange)
2. **Smart Transformation** - Converts raw data into escalation analytics:
   - **Region Assignment**: Based on email domains (hotmail→North America, yahoo→Asia, etc.)
   - **Product Categorization**: Based on client name patterns (Analytics, API, Dashboard, Reporting)
   - **Severity Mapping**: numberrange values → Low/Medium/High severity levels
   - **Date Generation**: Creates realistic escalation timelines

3. **Visualization Generation** - Creates multiple heatmap types:
   - **Product Timeline**: Escalation patterns over time
   - **Regional Analysis**: Geographic distribution by severity
   - **Client Overview**: Individual client escalation matrix

### **Security Features**

- ✅ **XSS Prevention**: HTML escaping and input sanitization
- ✅ **Path Traversal Protection**: File access validation
- ✅ **Rate Limiting**: DoS protection (200/day, 50/hour)
- ✅ **Security Headers**: CSP, HSTS, X-Frame-Options, etc.
- ✅ **Secure Error Handling**: No information disclosure
- ✅ **Input Validation**: Comprehensive data sanitization

## 🎨 **User Interface**

### **Dashboard Features**
- **Statistics Cards**: Total escalations, high severity count, unique clients, severity percentage
- **Interactive Tabs**: Switch between different visualization types
- **Responsive Design**: Works on desktop and mobile devices
- **Professional Styling**: Modern gradient backgrounds with glassmorphism effects

### **Navigation**
- **Main Dashboard** (`/`) - Interactive heatmap visualizations
- **Raw Data View** (`/data`) - Detailed data table with secure rendering
- **Smooth Transitions** - Professional animations and hover effects

## 🔧 **Configuration**

### **Environment Variables**
```bash
# Security Configuration
SECRET_KEY=your-secret-key-here          # Flask session security
FLASK_DEBUG=False                        # Production mode
FLASK_HOST=127.0.0.1                     # Bind address
FLASK_PORT=5000                          # Port number
LOG_LEVEL=INFO                           # Logging level
LOG_FILE=app.log                         # Log file location
```

### **Data Format**
Your CSV file should follow this format:
```csv
name,phone,email,numberrange
John Doe,1-555-123-4567,john@example.com,7
Jane Smith,1-555-987-6543,jane@company.org,3
```

**Field Descriptions:**
- `name`: Client name (used for product categorization)
- `phone`: Contact phone number
- `email`: Email address (used for region assignment)
- `numberrange`: Numeric value 0-10 (converted to severity levels)

## 🛡️ **Security**

EscaMap has undergone a comprehensive security audit. All critical and high-priority vulnerabilities have been resolved:

### **Security Measures**
- **Input Validation**: All user inputs are validated and sanitized
- **Output Encoding**: HTML escaping prevents XSS attacks
- **Path Security**: File access is restricted to allowed directories
- **Rate Limiting**: Prevents abuse and DoS attacks
- **Security Headers**: Comprehensive protective headers
- **Error Handling**: Secure error messages without information disclosure

### **Compliance**
- ✅ **OWASP Top 10** compliance
- ✅ **Industry standard** security headers
- ✅ **Production-ready** security configuration

For detailed security information, see [`SECURITY.md`](SECURITY.md).

## 📈 **Use Cases**

### **For Technical Account Managers**
- **Client Health Monitoring**: Identify clients with recurring escalations
- **Proactive Outreach**: Spot patterns before they become critical
- **Resource Allocation**: Focus support efforts on high-risk areas
- **Executive Reporting**: Professional visualizations for stakeholder updates

### **For Product Managers**
- **Product Quality Insights**: Identify which products generate most escalations
- **Regional Analysis**: Understand geographic patterns in customer issues
- **Priority Setting**: Data-driven decision making for product improvements
- **Customer Success**: Improve overall customer satisfaction metrics

## 🚀 **Deployment**

### **Local Development**
```bash
# Development mode with debug enabled
export FLASK_DEBUG=True
python src/app.py
```

### **Production Deployment**
```bash
# Production configuration
export SECRET_KEY="your-production-secret-key"
export FLASK_DEBUG=False
export FLASK_HOST=0.0.0.0  # Only if needed for external access
python src/app.py
```

### **Docker Deployment** (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "src/app.py"]
```

## 🔍 **Troubleshooting**

### **Common Issues**

1. **Import Errors**
   ```bash
   # Ensure all dependencies are installed
   pip install -r requirements.txt
   ```

2. **Port Already in Use**
   ```bash
   # Change the port
   export FLASK_PORT=8000
   python src/app.py
   ```

3. **Permission Errors**
   ```bash
   # Ensure proper file permissions
   chmod +x src/app.py
   ```

4. **Data Loading Issues**
   - Verify CSV file format matches expected structure
   - Check file permissions in `data/` directory
   - Review logs in `app.log` for detailed error information

## 📝 **Development**

### **Adding New Data Sources**
1. Update `src/data_processing.py` with new data format handling
2. Modify validation rules in `validate_filepath()` function
3. Test with new data format

### **Customizing Visualizations**
1. Edit `src/heatmap.py` to modify chart appearance
2. Update color schemes, sizing, or chart types
3. Add new visualization functions as needed

### **Extending Security**
1. Review `config.py` for additional security settings
2. Update rate limiting rules in `src/app.py`
3. Add new security headers as needed

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 **Professional Value**

**EscaMap demonstrates:**
- **Full-Stack Development**: Python backend with modern frontend
- **Data Visualization**: Professional charts using matplotlib/seaborn
- **Security Best Practices**: Enterprise-grade security implementation
- **UI/UX Design**: Modern, responsive interface design
- **Problem Solving**: Converting raw data into actionable business insights

Perfect for showcasing technical skills to potential employers in Technical Account Management and Product Management roles.

---

## 📞 **Support**

For questions, issues, or contributions:
- 📧 **Email**: [your-email@example.com]
- 🐛 **Issues**: [GitHub Issues](https://github.com/AWHProjects/EscaMap--Client-Escalation-Heatmap/issues)
- 📖 **Documentation**: [Security Guide](SECURITY.md)

---

**Built with ❤️ for proactive customer success management**
