import os
import shutil

def setup_static_files():
    """Set up static files and directories"""
    # Get the app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(app_dir, "app", "static")
    
    # Create static directory structure
    os.makedirs(os.path.join(static_dir, "css"), exist_ok=True)
    os.makedirs(os.path.join(static_dir, "js"), exist_ok=True)
    
    # CSS content
    css_content = """/* Base styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

/* Layout */
.container-fluid {
    min-height: 100vh;
}

/* Sidebar */
.sidebar {
    min-height: 100vh;
    background-color: #f8f9fa;
    padding: 20px;
    border-right: 1px solid #dee2e6;
}

.nav-link {
    color: #333;
    padding: 8px 16px;
    margin: 4px 0;
    border-radius: 4px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.nav-link:hover {
    background-color: #e9ecef;
    text-decoration: none;
}

.nav-link.active {
    background-color: #0d6efd;
    color: white;
}

/* Content area */
.content {
    padding: 20px;
}

/* Forms */
.form-group {
    margin-bottom: 1rem;
}

.form-control {
    border-radius: 4px;
    border: 1px solid #ced4da;
}

textarea.form-control {
    min-height: 150px;
}

/* Buttons */
.btn-primary {
    background-color: #0d6efd;
    border-color: #0d6efd;
}

.btn-primary:hover {
    background-color: #0b5ed7;
    border-color: #0a58ca;
}

/* Cards */
.card {
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
}

.card-header {
    background-color: #f8f9fa;
    border-bottom: 1px solid #dee2e6;
}

/* Alerts */
.alert {
    border-radius: 4px;
    margin-bottom: 1rem;
}

/* Icons */
.bi {
    margin-right: 0.5rem;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .sidebar {
        min-height: auto;
    }
}"""

    # JavaScript content
    js_content = """// Form submission handling
document.addEventListener('DOMContentLoaded', function() {
    const complaintForm = document.getElementById('complaintForm');
    if (complaintForm) {
        complaintForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            
            try {
                const response = await fetch('/api/complaints', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                if (result.success) {
                    window.location.href = `/complaints/${result.complaint_id}/report`;
                } else {
                    alert('Failed to submit complaint. Please try again.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while submitting the complaint.');
            }
        });
    }

    // File input handling
    const fileInput = document.querySelector('input[type="file"]');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const fileName = e.target.files[0]?.name || 'No file chosen';
            const fileLabel = document.querySelector('.custom-file-label');
            if (fileLabel) {
                fileLabel.textContent = fileName;
            }
        });
    }

    // Active navigation highlighting
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});"""

    # Write files
    with open(os.path.join(static_dir, "css", "styles.css"), "w") as f:
        f.write(css_content)
    
    with open(os.path.join(static_dir, "js", "main.js"), "w") as f:
        f.write(js_content)

    print("Static files have been set up successfully!")

if __name__ == "__main__":
    setup_static_files()
