<!DOCTYPE html>
<html lang="en">
<body>

<h1>Expense Tracker API</h1>

<p>A RESTful API built with <strong>Django REST Framework</strong> to manage expenses and categories. The API allows users to create expenses, view top categories, and track spending efficiently.</p>

<h2>Features</h2>
<ul>
    <li>Create, read, and manage <strong>expense categories</strong></li>
    <li>Add expenses with <strong>amount, description, category, and date</strong></li>
    <li>Track <strong>top 3 categories by total expense</strong></li>
    <li>User authentication with <strong>DRF token/JWT</strong></li>
    <li>Supports <strong>reporting and analytics</strong></li>
</ul>

<h2>Tech Stack</h2>
<ul>
    <li><strong>Backend:</strong> Django 5.2, Django REST Framework</li>
    <li><strong>Database:</strong> PostgreSQL / SQLite</li>
    <li><strong>Authentication:</strong> Django REST Framework IsAuthenticated</li>
    <li><strong>Python Version:</strong> 3.8+</li>
    <li><strong>Virtual Environment:</strong> venv</li>
</ul>

<h2>Installation</h2>
<pre><code># Clone the repository
git clone https://github.com/VishalNeosoft24/expense-tracker.git
cd expense-tracker

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver
</code></pre>

<p>Server will start at <code>http://127.0.0.1:8000/</code></p>

<h2>API Endpoints</h2>

<h3>1. Add Expense</h3>
<p><code>POST /expenses/api/add-expense/</code></p>
<pre><code>{
    "category": 2,
    "amount": 500.00,
    "description": "Lunch with team",
    "expense_date": "2025-09-01",
    "created_by": 1
}
</code></pre>

<h3>2. Top 3 Categories</h3>
<p><code>GET /reports/api/top-three-cat/</code></p>
<pre><code>{
  "top_categories": [
    {"id": 2, "name": "Food", "max_limit": 2000, "total_amount": 1500.00},
    {"id": 1, "name": "Travel", "max_limit": 5000, "total_amount": 800.00},
    {"id": 3, "name": "Shopping", "max_limit": 3000, "total_amount": 500.00}
  ]
}
</code></pre>

<h2>Models Overview</h2>

<h3>Category</h3>
<ul>
    <li><strong>name:</strong> Name of the category</li>
    <li><strong>max_limit:</strong> Optional maximum spending limit</li>
    <li><strong>created_at, updated_at:</strong> Timestamps</li>
</ul>

<h3>Expense</h3>
<ul>
    <li><strong>category:</strong> ForeignKey to Category</li>
    <li><strong>amount:</strong> Expense amount</li>
    <li><strong>description:</strong> Optional text</li>
    <li><strong>expense_date:</strong> Date of expense</li>
    <li><strong>created_by:</strong> User who added the expense</li>
    <li><strong>created_at, updated_at:</strong> Timestamps</li>
</ul>

<h2>Notes</h2>
<ul>
    <li>Ensure <strong>user authentication</strong> is set for endpoints requiring <code>IsAuthenticated</code>.</li>
    <li>Decimal fields are used for amounts to avoid floating-point precision errors.</li>
    <li>Recommended to use <strong>PostgreSQL</strong> for production deployments.</li>
</ul>

<h2>Future Improvements</h2>
<ul>
    <li>JWT authentication</li>
    <li>Expense filtering by date range and category</li>
    <li>Monthly and yearly reports</li>
    <li>Frontend integration with React or Vue</li>
</ul>

<h2>🐍 API Documentation</h2>
<p>Interactive API documentation is available via:</p>

<ul>
  <li>Swagger UI: <a href="http://127.0.0.1:8000/swagger/" target="_blank">http://127.0.0.1:8000/swagger/</a></li>
  <li>Redoc: <a href="http://127.0.0.1:8000/redoc/" target="_blank">http://127.0.0.1:8000/redoc/</a></li>
</ul>

<p>Both allow you to view endpoints, send requests, and test APIs interactively.</p>

</body>
</html>
