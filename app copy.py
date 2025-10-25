from flask import Flask, render_template_string, redirect, url_for, request, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Login Template
LOGIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dotsh - Sign In</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .login-container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
            overflow: hidden;
            max-width: 1000px;
            width: 100%;
            display: flex;
            min-height: 600px;
        }

        .login-left {
            flex: 1;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 60px 40px;
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .logo {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
            letter-spacing: -1px;
        }

        .logo-dot {
            color: #ffd700;
        }

        .tagline {
            font-size: 18px;
            opacity: 0.9;
            margin-bottom: 40px;
            line-height: 1.6;
        }

        .features {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .feature-item {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .feature-icon {
            width: 40px;
            height: 40px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .feature-icon svg {
            width: 20px;
            height: 20px;
            stroke: white;
        }

        .login-right {
            flex: 1;
            padding: 60px 50px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .login-header {
            margin-bottom: 40px;
        }

        .login-header h2 {
            font-size: 32px;
            color: #2d3748;
            margin-bottom: 10px;
        }

        .login-header p {
            color: #718096;
            font-size: 14px;
        }

        .form-group {
            margin-bottom: 24px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #4a5568;
            font-size: 14px;
            font-weight: 500;
        }

        .form-group input {
            width: 100%;
            padding: 14px 16px;
            border: 2px solid #e2e8f0;
            border-radius: 8px;
            font-size: 15px;
            transition: all 0.3s;
            outline: none;
        }

        .form-group input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        .btn {
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 16px;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }

        .btn-sso {
            background: white;
            color: #2d3748;
            border: 2px solid #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .btn-sso:hover {
            background: #f7fafc;
            border-color: #cbd5e0;
        }

        .btn-sso svg {
            width: 20px;
            height: 20px;
            stroke: currentColor;
        }

        .divider {
            display: flex;
            align-items: center;
            margin: 24px 0;
            color: #a0aec0;
            font-size: 14px;
        }

        .divider::before,
        .divider::after {
            content: '';
            flex: 1;
            height: 1px;
            background: #e2e8f0;
        }

        .divider::before {
            margin-right: 16px;
        }

        .divider::after {
            margin-left: 16px;
        }

        .forgot-password {
            text-align: right;
            margin-top: -16px;
            margin-bottom: 24px;
        }

        .forgot-password a {
            color: #667eea;
            text-decoration: none;
            font-size: 14px;
        }

        .forgot-password a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            .login-container {
                flex-direction: column;
            }

            .login-left {
                padding: 40px 30px;
            }

            .login-right {
                padding: 40px 30px;
            }
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-left">
            <div class="logo">
                dotsh<span class="logo-dot">.</span>
            </div>
            <p class="tagline">
                Real-time monitoring and analytics platform for modern infrastructure
            </p>
            <div class="features">
                <div class="feature-item">
                    <div class="feature-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                    <div>
                        <strong>Real-time Metrics</strong><br>
                        <small style="opacity: 0.8;">Monitor your systems in real-time</small>
                    </div>
                </div>
                <div class="feature-item">
                    <div class="feature-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M13.73 21a2 2 0 0 1-3.46 0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                    <div>
                        <strong>Smart Alerts</strong><br>
                        <small style="opacity: 0.8;">Get notified of critical issues</small>
                    </div>
                </div>
                <div class="feature-item">
                    <div class="feature-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="12" cy="12" r="10" stroke-width="2"/>
                            <polyline points="12 6 12 12 16 14" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                    <div>
                        <strong>High Performance</strong><br>
                        <small style="opacity: 0.8;">Optimized for speed and scale</small>
                    </div>
                </div>
            </div>
        </div>

        <div class="login-right">
            <div class="login-header">
                <h2>Sign in to Dotsh</h2>
                <p>Access your monitoring dashboard</p>
            </div>

            <button class="btn btn-sso" onclick="handleSSOLogin()">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M2 17L12 22L22 17" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M2 12L12 17L22 12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                Sign in with SSO
            </button>

            <div class="divider">or continue with email</div>

            <form action="/login" method="POST">
                <div class="form-group">
                    <label for="email">Email address</label>
                    <input type="email" id="email" name="email" placeholder="name@company.com" required>
                </div>

                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" placeholder="Enter your password" required>
                </div>

                <div class="forgot-password">
                    <a href="#" onclick="handleForgotPassword(event)">Forgot password?</a>
                </div>

                <button type="submit" class="btn btn-primary">Sign in</button>
            </form>
        </div>
    </div>

    <script>
        function handleSSOLogin() {
            alert('SSO login initiated. Redirecting to SSO provider...');
            window.location.href = '/home?sso=true';
        }

        function handleForgotPassword(event) {
            event.preventDefault();
            alert('Password reset link would be sent to your email.');
        }
    </script>
</body>
</html>
"""

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dotsh - Monitoring Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #f5f7fa;
            min-height: 100vh;
        }

        .dashboard {
            display: flex;
            height: 100vh;
        }

        /* Sidebar */
        .sidebar {
            width: 80px;
            background: white;
            border-right: 1px solid #e2e8f0;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px 0;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
        }

        .logo {
            font-size: 28px;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 40px;
            cursor: pointer;
        }

        .logo-dot {
            color: #ffd700;
        }

        .nav-menu {
            display: flex;
            flex-direction: column;
            gap: 10px;
            width: 100%;
            padding: 0 15px;
        }

        .nav-item {
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
            background: #f7fafc;
        }

        .nav-item:hover {
            background: #e2e8f0;
            transform: translateX(5px);
        }

        .nav-item.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .nav-item svg {
            width: 24px;
            height: 24px;
        }

        .nav-item:not(.active) svg {
            stroke: #4a5568;
        }

        .nav-item.active svg {
            stroke: white;
        }

        .nav-item .tooltip {
            position: absolute;
            left: 70px;
            background: #2d3748;
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 14px;
            white-space: nowrap;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s;
            z-index: 10;
        }

        .nav-item:hover .tooltip {
            opacity: 1;
        }

        /* Main Content */
        .main-content {
            flex: 1;
            overflow-y: auto;
            padding: 30px 40px;
        }

        .header {
            margin-bottom: 30px;
        }

        .header h1 {
            font-size: 32px;
            color: #2d3748;
            margin-bottom: 8px;
        }

        .header p {
            color: #718096;
            font-size: 16px;
        }

        /* Dashboard Cards */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 24px;
            margin-bottom: 30px;
        }

        .card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            transition: all 0.3s;
        }

        .card:hover {
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
        }

        .card-icon {
            width: 48px;
            height: 48px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card-icon.purple {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .card-icon.green {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        }

        .card-icon.orange {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }

        .card-icon.blue {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        }

        .card-icon svg {
            width: 24px;
            height: 24px;
            stroke: white;
        }

        .card-title {
            font-size: 14px;
            color: #718096;
            font-weight: 500;
        }

        .card-value {
            font-size: 32px;
            font-weight: bold;
            color: #2d3748;
            margin-bottom: 8px;
        }

        .card-change {
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .card-change.positive {
            color: #38a169;
        }

        .card-change.negative {
            color: #e53e3e;
        }

        /* Content Section */
        .content-section {
            background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            margin-bottom: 24px;
        }

        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 16px;
            border-bottom: 2px solid #f7fafc;
        }

        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #2d3748;
        }

        /* Table */
        .table-container {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            text-align: left;
            padding: 12px;
            background: #f7fafc;
            color: #4a5568;
            font-weight: 600;
            font-size: 14px;
            border-bottom: 2px solid #e2e8f0;
        }

        td {
            padding: 16px 12px;
            border-bottom: 1px solid #e2e8f0;
            color: #2d3748;
        }

        tr:hover {
            background: #f7fafc;
        }

        .status-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
        }

        .status-badge.online {
            background: #c6f6d5;
            color: #22543d;
        }

        .status-badge.warning {
            background: #feebc8;
            color: #7c2d12;
        }

        .status-badge.offline {
            background: #fed7d7;
            color: #742a2a;
        }

        /* Progress Bar */
        .progress-bar {
            width: 100%;
            height: 8px;
            background: #e2e8f0;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 8px;
        }

        .progress-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s;
        }

        .progress-fill.low {
            background: #38a169;
        }

        .progress-fill.medium {
            background: #ed8936;
        }

        .progress-fill.high {
            background: #e53e3e;
        }

        /* Hidden class for page switching */
        .page {
            display: none;
        }

        .page.active {
            display: block;
        }

        .server-details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-bottom: 20px;
        }

        .detail-item {
            padding: 16px;
            background: #f7fafc;
            border-radius: 8px;
        }

        .detail-label {
            font-size: 12px;
            color: #718096;
            margin-bottom: 4px;
        }

        .detail-value {
            font-size: 18px;
            font-weight: 600;
            color: #2d3748;
        }
    </style>
</head>
<body>
    <div class="dashboard">
        <!-- Sidebar -->
        <div class="sidebar">
            <div class="logo" onclick="showPage('overview')">
                dotsh<span class="logo-dot">.</span>
            </div>
            
            <div class="nav-menu">
                <div class="nav-item active" onclick="showPage('overview')" data-page="overview">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="3" y="3" width="7" height="7" rx="1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <rect x="14" y="3" width="7" height="7" rx="1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <rect x="14" y="14" width="7" height="7" rx="1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <rect x="3" y="14" width="7" height="7" rx="1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span class="tooltip">Overview</span>
                </div>
                <div class="nav-item" onclick="showPage('capacity')" data-page="capacity">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="2" y="3" width="20" height="5" rx="1" stroke-width="2"/>
                        <rect x="2" y="10" width="20" height="5" rx="1" stroke-width="2"/>
                        <rect x="2" y="17" width="20" height="5" rx="1" stroke-width="2"/>
                    </svg>
                    <span class="tooltip">Server Capacity</span>
                </div>
                <div class="nav-item" onclick="showPage('projects')" data-page="projects">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span class="tooltip">Project Servers</span>
                </div>
                <div class="nav-item" onclick="showPage('alerts')" data-page="alerts">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M13.73 21a2 2 0 0 1-3.46 0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span class="tooltip">Alerts</span>
                </div>
                <div class="nav-item" onclick="showPage('settings')" data-page="settings">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="12" cy="12" r="3" stroke-width="2"/>
                        <path d="M12 1v6m0 6v6m9.66-9.66l-5.66 5.66M12 12 6.34 6.34M23 12h-6m-6 0H1m20.66 9.66l-5.66-5.66M12 12l-5.66 5.66" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                    <span class="tooltip">Settings</span>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <div class="main-content">
            <!-- Overview Page -->
            <div class="page active" id="overview">
                <div class="header">
                    <h1>Overview Dashboard</h1>
                    <p>Monitor your infrastructure in real-time</p>
                </div>

                <div class="cards-grid">
                    <div class="card">
                        <div class="card-header">
                            <div class="card-icon purple">
                                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect x="2" y="3" width="20" height="14" rx="2" stroke-width="2"/>
                                    <line x1="8" y1="21" x2="16" y2="21" stroke-width="2" stroke-linecap="round"/>
                                    <line x1="12" y1="17" x2="12" y2="21" stroke-width="2"/>
                                </svg>
                            </div>
                            <div class="card-title">Total Servers</div>
                        </div>
                        <div class="card-value">24</div>
                        <div class="card-change positive">↑ 2 from last week</div>
                    </div>

                    <div class="card">
                        <div class="card-header">
                            <div class="card-icon green">
                                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <polyline points="22 4 12 14.01 9 11.01" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="card-title">Active Projects</div>
                        </div>
                        <div class="card-value">12</div>
                        <div class="card-change positive">↑ 3 from last month</div>
                    </div>

                    <div class="card">
                        <div class="card-header">
                            <div class="card-icon orange">
                                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <circle cx="12" cy="12" r="10" stroke-width="2"/>
                                    <line x1="12" y1="8" x2="12" y2="12" stroke-width="2" stroke-linecap="round"/>
                                    <line x1="12" y1="16" x2="12.01" y2="16" stroke-width="2" stroke-linecap="round"/>
                                </svg>
                            </div>
                            <div class="card-title">Alerts</div>
                        </div>
                        <div class="card-value">3</div>
                        <div class="card-change negative">↑ 1 from yesterday</div>
                    </div>

                    <div class="card">
                        <div class="card-header">
                            <div class="card-icon blue">
                                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="card-title">Avg. CPU Usage</div>
                        </div>
                        <div class="card-value">67%</div>
                        <div class="card-change positive">↓ 5% from last hour</div>
                    </div>
                </div>

                <div class="content-section">
                    <div class="section-header">
                        <h2 class="section-title">Recent Server Activity</h2>
                    </div>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Server Name</th>
                                    <th>Status</th>
                                    <th>CPU</th>
                                    <th>Memory</th>
                                    <th>Uptime</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for server in servers %}
                                <tr>
                                    <td><strong>{{ server.name }}</strong></td>
                                    <td><span class="status-badge {{ server.status }}">{{ server.status|capitalize }}</span></td>
                                    <td>{{ server.cpu }}%</td>
                                    <td>{{ server.memory }}%</td>
                                    <td>{{ server.uptime }}</td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Server Capacity Page -->
            <div class="page" id="capacity">
                <div class="header">
                    <h1>Server Capacity</h1>
                    <p>Monitor resource utilization across all servers</p>
                </div>

                <div class="content-section">
                    <div class="section-header">
                        <h2 class="section-title">Storage Capacity</h2>
                    </div>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Server Name</th>
                                    <th>Total Storage</th>
                                    <th>Used</th>
                                    <th>Available</th>
                                    <th>Usage</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for capacity in storage_capacity %}
                                <tr>
                                    <td><strong>{{ capacity.name }}</strong></td>
                                    <td>{{ capacity.total }}</td>
                                    <td>{{ capacity.used }}</td>
                                    <td>{{ capacity.available }}</td>
                                    <td>
                                        {{ capacity.percentage }}%
                                        <div class="progress-bar">
                                            <div class="progress-fill {{ capacity.level }}" style="width: {{ capacity.percentage }}%"></div>
                                        </div>
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="content-section">
                    <div class="section-header">
                        <h2 class="section-title">CPU & Memory Capacity</h2>
                    </div>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Server Name</th>
                                    <th>CPU Cores</th>
                                    <th>CPU Usage</th>
                                    <th>Total RAM</th>
                                    <th>RAM Usage</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for cpu in cpu_capacity %}
                                <tr>
                                    <td><strong>{{ cpu.name }}</strong></td>
                                    <td>{{ cpu.cores }} Cores</td>
                                    <td>
                                        {{ cpu.cpu_usage }}%
                                        <div class="progress-bar">
                                            <div class="progress-fill {{ cpu.cpu_level }}" style="width: {{ cpu.cpu_usage }}%"></div>
                                        </div>
                                    </td>
                                    <td>{{ cpu.ram }}</td>
                                    <td>
                                        {{ cpu.ram_usage }}%
                                        <div class="progress-bar">
                                            <div class="progress-fill {{ cpu.ram_level }}" style="width: {{ cpu.ram_usage }}%"></div>
                                        </div>
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Project Server Details Page -->
            <div class="page" id="projects">
                <div class="header">
                    <h1>Project Server Details</h1>
                    <p>Detailed information about project-specific servers</p>
                </div>

                {% for project in projects %}
                <div class="content-section">
                    <div class="section-header">
                        <h2 class="section-title">{{ project.name }}</h2>
                    </div>
                    <div class="server-details">
                        <div class="detail-item">
                            <div class="detail-label">Server Name</div>
                            <div class="detail-value">{{ project.server_name }}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">IP Address</div>
                            <div class="detail-value">{{ project.ip }}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Environment</div>
                            <div class="detail-value">{{ project.environment }}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Region</div>
                            <div class="detail-value">{{ project.region }}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">OS</div>
                            <div class="detail-value">{{ project.os }}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Status</div>
                            <div class="detail-value"><span class="status-badge {{ project.status }}">{{ project.status|capitalize }}</span></div>
                        </div>
                    </div>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Service</th>
                                    <th>Port</th>
                                    <th>Status</th>
                                    <th>Response Time</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for service in project.services %}
                                <tr>
                                    <td>{{ service.name }}</td>
                                    <td>{{ service.port }}</td>
                                    <td><span class="status-badge {{ service.status }}">{{ service.status_text }}</span></td>
                                    <td>{{ service.response_time }}</td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
                {% endfor %}
            </div>

            <!-- Alerts Page -->
            <div class="page" id="alerts">
                <div class="header">
                    <h1>Alerts & Notifications</h1>
                    <p>Monitor system alerts and warnings</p>
                </div>

                <div class="content-section">
                    <div class="section-header">
                        <h2 class="section-title">Active Alerts</h2>
                    </div>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Time</th>
                                    <th>Server</th>
                                    <th>Type</th>
                                    <th>Message</th>
                                    <th>Severity</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for alert in alerts %}
                                <tr>
                                    <td>{{ alert.time }}</td>
                                    <td>{{ alert.server }}</td>
                                    <td>{{ alert.type }}</td>
                                    <td>{{ alert.message }}</td>
                                    <td><span class="status-badge {{ alert.severity }}">{{ alert.severity|capitalize }}</span></td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Settings Page -->
            <div class="page" id="settings">
                <div class="header">
                    <h1>Settings</h1>
                    <p>Configure your monitoring preferences</p>
                </div>

                <div class="content-section">
                    <div class="section-header">
                        <h2 class="section-title">Notification Settings</h2>
                    </div>
                    <p style="color: #718096;">Configure your alert preferences and notification channels here.</p>
                </div>

                <div class="content-section">
                    <div class="section-header">
                        <h2 class="section-title">Account Settings</h2>
                    </div>
                    <p style="color: #718096;">Manage your account details and security settings.</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        function showPage(pageId) {
            // Hide all pages
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });
            
            // Show selected page
            document.getElementById(pageId).classList.add('active');
            
            // Update nav items
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            
            // Add active class to clicked nav item
            document.querySelector(`[data-page="${pageId}"]`).classList.add('active');
        }
    </script>
</body>
</html>
"""

# Sample data
servers = [
    {'name': 'prod-web-01', 'status': 'online', 'cpu': 45, 'memory': 62, 'uptime': '23 days'},
    {'name': 'prod-db-01', 'status': 'online', 'cpu': 78, 'memory': 84, 'uptime': '45 days'},
    {'name': 'dev-api-02', 'status': 'warning', 'cpu': 91, 'memory': 88, 'uptime': '12 days'},
    {'name': 'staging-web-01', 'status': 'online', 'cpu': 34, 'memory': 56, 'uptime': '8 days'},
]

storage_capacity = [
    {'name': 'prod-web-01', 'total': '500 GB', 'used': '345 GB', 'available': '155 GB', 'percentage': 69, 'level': 'medium'},
    {'name': 'prod-db-01', 'total': '2 TB', 'used': '1.8 TB', 'available': '200 GB', 'percentage': 90, 'level': 'high'},
    {'name': 'dev-api-02', 'total': '250 GB', 'used': '89 GB', 'available': '161 GB', 'percentage': 36, 'level': 'low'},
    {'name': 'staging-web-01', 'total': '500 GB', 'used': '198 GB', 'available': '302 GB', 'percentage': 40, 'level': 'low'},
    {'name': 'prod-cache-01', 'total': '1 TB', 'used': '756 GB', 'available': '244 GB', 'percentage': 76, 'level': 'medium'},
]

cpu_capacity = [
    {'name': 'prod-web-01', 'cores': 8, 'cpu_usage': 45, 'cpu_level': 'low', 'ram': '32 GB', 'ram_usage': 62, 'ram_level': 'medium'},
    {'name': 'prod-db-01', 'cores': 16, 'cpu_usage': 78, 'cpu_level': 'medium', 'ram': '64 GB', 'ram_usage': 84, 'ram_level': 'high'},
    {'name': 'dev-api-02', 'cores': 4, 'cpu_usage': 91, 'cpu_level': 'high', 'ram': '16 GB', 'ram_usage': 88, 'ram_level': 'high'},
]

projects = [
    {
        'name': 'E-Commerce Platform',
        'server_name': 'prod-web-01',
        'ip': '192.168.1.101',
        'environment': 'Production',
        'region': 'US-East',
        'os': 'Ubuntu 22.04',
        'status': 'online',
        'services': [
            {'name': 'Nginx Web Server', 'port': '80, 443', 'status': 'online', 'status_text': 'Running', 'response_time': '45ms'},
            {'name': 'Node.js API', 'port': '3000', 'status': 'online', 'status_text': 'Running', 'response_time': '128ms'},
            {'name': 'Redis Cache', 'port': '6379', 'status': 'online', 'status_text': 'Running', 'response_time': '12ms'},
        ]
    },
    {
        'name': 'Analytics Platform',
        'server_name': 'prod-db-01',
        'ip': '192.168.1.102',
        'environment': 'Production',
        'region': 'US-West',
        'os': 'CentOS 8',
        'status': 'online',
        'services': [
            {'name': 'PostgreSQL Database', 'port': '5432', 'status': 'online', 'status_text': 'Running', 'response_time': '67ms'},
            {'name': 'Elasticsearch', 'port': '9200', 'status': 'online', 'status_text': 'Running', 'response_time': '234ms'},
            {'name': 'Kibana', 'port': '5601', 'status': 'online', 'status_text': 'Running', 'response_time': '156ms'},
        ]
    },
    {
        'name': 'Development API',
        'server_name': 'dev-api-02',
        'ip': '192.168.1.203',
        'environment': 'Development',
        'region': 'EU-Central',
        'os': 'Ubuntu 20.04',
        'status': 'warning',
        'services': [
            {'name': 'Express.js API', 'port': '4000', 'status': 'online', 'status_text': 'Running', 'response_time': '345ms'},
            {'name': 'MongoDB', 'port': '27017', 'status': 'warning', 'status_text': 'High Load', 'response_time': '567ms'},
            {'name': 'Docker Engine', 'port': '2375', 'status': 'online', 'status_text': 'Running', 'response_time': '89ms'},
        ]
    },
]

alerts = [
    {'time': '10:45 AM', 'server': 'dev-api-02', 'type': 'CPU', 'message': 'CPU usage exceeded 90%', 'severity': 'warning'},
    {'time': '09:23 AM', 'server': 'prod-db-01', 'type': 'Storage', 'message': 'Disk space above 85%', 'severity': 'warning'},
    {'time': '08:15 AM', 'server': 'prod-cache-01', 'type': 'Memory', 'message': 'Memory usage critical', 'severity': 'offline'},
]

@app.route('/')
def login():
    return render_template_string(
        LOGIN_TEMPLATE
    )

@app.route('/home')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        servers=servers,
        storage_capacity=storage_capacity,
        cpu_capacity=cpu_capacity,
        projects=projects,
        alerts=alerts
    )

@app.route('/api/servers')
def get_servers():
    return {'servers': servers}

@app.route('/api/capacity')
def get_capacity():
    return {
        'storage': storage_capacity,
        'cpu': cpu_capacity
    }

@app.route('/api/projects')
def get_projects():
    return {'projects': projects}

@app.route('/api/alerts')
def get_alerts():
    return {'alerts': alerts}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)