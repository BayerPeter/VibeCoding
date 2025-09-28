import os

def check_paths():
    # Get the absolute path of the app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"App directory: {app_dir}")

    # Check static directory
    static_dir = os.path.join(app_dir, "app", "static")
    print(f"\nStatic directory: {static_dir}")
    print(f"Static directory exists: {os.path.exists(static_dir)}")

    # Check CSS directory and file
    css_dir = os.path.join(static_dir, "css")
    css_file = os.path.join(css_dir, "styles.css")
    print(f"\nCSS directory: {css_dir}")
    print(f"CSS directory exists: {os.path.exists(css_dir)}")
    print(f"CSS file: {css_file}")
    print(f"CSS file exists: {os.path.exists(css_file)}")

    # Check JS directory and file
    js_dir = os.path.join(static_dir, "js")
    js_file = os.path.join(js_dir, "main.js")
    print(f"\nJS directory: {js_dir}")
    print(f"JS directory exists: {os.path.exists(js_dir)}")
    print(f"JS file: {js_file}")
    print(f"JS file exists: {os.path.exists(js_file)}")

    # If files don't exist, try to create them
    if not os.path.exists(css_dir):
        os.makedirs(css_dir)
        print(f"\nCreated CSS directory: {css_dir}")

    if not os.path.exists(js_dir):
        os.makedirs(js_dir)
        print(f"\nCreated JS directory: {js_dir}")

    # Copy files if they don't exist
    if not os.path.exists(css_file):
        with open(css_file, 'w') as f:
            f.write("""/* Base styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}
""")
        print(f"\nCreated CSS file: {css_file}")

    if not os.path.exists(js_file):
        with open(js_file, 'w') as f:
            f.write("""// Main JavaScript file
document.addEventListener('DOMContentLoaded', function() {
    console.log('Application initialized');
});
""")
        print(f"\nCreated JS file: {js_file}")

if __name__ == "__main__":
    check_paths()
