responce = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Email Directory</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }
        .department {
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h2 {
            color: #007bff;
            margin-top: 0;
        }
        .email-list {
            list-style: none;
            padding: 0;
        }
        .email-list li {
            padding: 10px;
            border-bottom: 1px solid #eee;
            display: flex;
            align-items: center;
        }
        .email-list li:last-child {
            border-bottom: none;
        }
        .email-icon {
            margin-right: 10px;
            color: #007bff;
            font-weight: bold;
        }
        .email-address {
            color: #0066cc;
            text-decoration: none;
            font-family: monospace;
            font-size: 16px;
        }
        .email-address:hover {
            text-decoration: underline;
            color: #004499;
        }
        .role {
            color: #666;
            margin-left: 10px;
            font-size: 14px;
        }
        footer {
            text-align: center;
            margin-top: 30px;
            color: #666;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>📧 Company Email Directory</h1>
    
    <div class="department">
        <h2>🏢 Executive Team</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:ceo@example.com" class="email-address">ceo@example.com</a>
                <span class="role">- Chief Executive Officer</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:cto@example.com" class="email-address">cto@example.com</a>
                <span class="role">- Chief Technology Officer</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:cfo@example.com" class="email-address">cfo@example.com</a>
                <span class="role">- Chief Financial Officer</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>💻 Technical Support</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:support@example.com" class="email-address">support@example.com</a>
                <span class="role">- General Technical Support</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:bugs@example.com" class="email-address">bugs@example.com</a>
                <span class="role">- Report Bugs</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:ithelpdesk@example.com" class="email-address">ithelpdesk@example.com</a>
                <span class="role">- IT Help Desk</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>🤝 Customer Service</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:info@example.com" class="email-address">info@example.com</a>
                <span class="role">- General Information</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:help@example.com" class="email-address">help@example.com</a>
                <span class="role">- Customer Assistance</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:feedback@example.com" class="email-address">feedback@example.com</a>
                <span class="role">- Send Feedback</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:complaints@example.com" class="email-address">complaints@example.com</a>
                <span class="role">- Complaints Department</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>📞 Other Departments</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:sales@example.com" class="email-address">sales@example.com</a>
                <span class="role">- Sales Team</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:marketing@example.com" class="email-address">marketing@example.com</a>
                <span class="role">- Marketing Department</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:hr@example.com" class="email-address">hr@example.com</a>
                <span class="role">- Human Resources</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:press@example.com" class="email-address">press@example.com</a>
                <span class="role">- Media & Press Inquiries</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:careers@example.com" class="email-address">careers@example.com</a>
                <span class="role">- Job Applications</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>🌍 Regional Offices</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:us@example.com" class="email-address">us@example.com</a>
                <span class="role">- North America</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:europe@example.com" class="email-address">europe@example.com</a>
                <span class="role">- Europe</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:asia@example.com" class="email-address">asia@example.com</a>
                <span class="role">- Asia Pacific</span>
            </li>
        </ul>
    </div>

    <footer>
        <p>Click on any email address to send a message | For testing purposes only - replace "example.com" with your domain</p>
    </footer>
   <h1>📧 Company Email Directory</h1>
    
    <div class="department">
        <h2>🏢 Executive Team</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:ceo@example.com" class="email-address">ceo@example.com</a>
                <span class="role">- Chief Executive Officer</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:cto@example.com" class="email-address">cto@example.com</a>
                <span class="role">- Chief Technology Officer</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:cfo@example.com" class="email-address">cfo@example.com</a>
                <span class="role">- Chief Financial Officer</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>💻 Technical Support</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:support@example.com" class="email-address">support@example.com</a>
                <span class="role">- General Technical Support</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:bugs@example.com" class="email-address">bugs@example.com</a>
                <span class="role">- Report Bugs</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:ithelpdesk@example.com" class="email-address">ithelpdesk@example.com</a>
                <span class="role">- IT Help Desk</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>🤝 Customer Service</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:info@example.com" class="email-address">info@example.com</a>
                <span class="role">- General Information</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:Kalidmume2@gmail.com" class="email-address">help@example.com</a>
                <span class="role">- Customer Assistance</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:feedback@example.com" class="email-address">feedback@example.com</a>
                <span class="role">- Send Feedback</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:complaints@example.com" class="email-address">complaints@example.com</a>
                <span class="role">- Complaints Department</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>📞 Other Departments</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:sales@example.com" class="email-address">sales@example.com</a>
                <span class="role">- Sales Team</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:marketing@example.com" class="email-address">marketing@example.com</a>
                <span class="role">- Marketing Department</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:hr@example.com" class="email-address">hr@example.com</a>
                <span class="role">- Human Resources</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:press@example.com" class="email-address">press@example.com</a>
                <span class="role">- Media & Press Inquiries</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:careers@example.com" class="email-address">careers@example.com</a>
                <span class="role">- Job Applications</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>🌍 Regional Offices</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:us@example.com" class="email-address">us@example.com</a>
                <span class="role">- North America</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:europe@example.com" class="email-address">europe@example.com</a>
                <span class="role">- Europe</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:asia@example.com" class="email-address">asia@example.com</a>
                <span class="role">- Asia Pacific</span>
            </li>
        </ul>
    </div>

    <footer>
        <p>Click on any email address to send a message | For testing purposes only - replace "example.com" with your domain</p>
    </footer>
   <h1>📧 Company Email Directory</h1>
    
    <div class="department">
        <h2>🏢 Executive Team</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:ceo@example.com" class="email-address">ceo@example.com</a>
                <span class="role">- Chief Executive Officer</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:cto@example.com" class="email-address">cto@example.com</a>
                <span class="role">- Chief Technology Officer</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:cfo@example.com" class="email-address">cfo@example.com</a>
                <span class="role">- Chief Financial Officer</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>💻 Technical Support</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:support@example.com" class="email-address">support@example.com</a>
                <span class="role">- General Technical Support</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:bugs@example.com" class="email-address">bugs@example.com</a>
                <span class="role">- Report Bugs</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:ithelpdesk@example.com" class="email-address">ithelpdesk@example.com</a>
                <span class="role">- IT Help Desk</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>🤝 Customer Service</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:info@example.com" class="email-address">info@example.com</a>
                <span class="role">- General Information</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:help@example.com" class="email-address">help@example.com</a>
                <span class="role">- Customer Assistance</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:feedback@example.com" class="email-address">feedback@example.com</a>
                <span class="role">- Send Feedback</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:complaints@example.com" class="email-address">complaints@example.com</a>
                <span class="role">- Complaints Department</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>📞 Other Departments</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:sales@example.com" class="email-address">sales@example.com</a>
                <span class="role">- Sales Team</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:marketing@example.com" class="email-address">marketing@example.com</a>
                <span class="role">- Marketing Department</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:hr@example.com" class="email-address">hr@example.com</a>
                <span class="role">- Human Resources</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:press@example.com" class="email-address">press@example.com</a>
                <span class="role">- Media & Press Inquiries</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:careers@example.com" class="email-address">careers@example.com</a>
                <span class="role">- Job Applications</span>
            </li>
        </ul>
    </div>

    <div class="department">
        <h2>🌍 Regional Offices</h2>
        <ul class="email-list">
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:us@example.com" class="email-address">us@example.com</a>
                <span class="role">- North America</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:europe@example.com" class="email-address">europe@example.com</a>
                <span class="role">- Europe</span>
            </li>
            <li>
                <span class="email-icon">📨</span>
                <a href="mailto:asia@example.com" class="email-address">asia@example.com</a>
                <span class="role">- Asia Pacific</span>
            </li>
        </ul>
    </div>

    <footer>
        <p>Click on any email address to send a message | For testing purposes only - replace "example.com" with your domain</p>
    </footer>
</body>
</html>"""